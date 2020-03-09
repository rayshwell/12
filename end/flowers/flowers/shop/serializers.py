from .models import *
from rest_framework import serializers
class AdsSerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    img = serializers.ImageField()
    def create(self, validated_data):
        instance=Ads.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.img=validated_data.get("img",instance.img)
        instance.save()
        return instance
class GoodImgSerizlizer(serializers.Serializer):
    img=serializers.ImageField()
    good=serializers.CharField(source="good.name")

    def validate(self, attrs):
        try:
            g=Good.objects.get(name=attrs["good"]["name"])
            attrs["good"]=g
        except:
            raise serializers.ValidationError("输入的商品不存在")
        return attrs
    def create(self, validated_data):
        instance=GoodImg.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.img=validated_data.get("img",instance.img)
        instance.good=validated_data.get("good",instance.good)
        instance.save()
        return instance
class CategorySerizlizer1(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=10,min_length=2,error_messages={
        "max_length":"最多十个字",
        "min_length":"最少三个字"
    })

    def create(self, validated_data):
        instance=Category.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.save()
        return instance
class GoodSerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少3个字"
    })
    img = serializers.ImageField()
    category = CategorySerizlizer1(label="分类名")
    imgs=GoodImgSerizlizer(label="图片",many=True,read_only=True)
    def validate_category(self, category):
        try:
            Category.objects.get(name=category["name"])
        except:
            raise  serializers.ValidationError("输入的类名不存在")
        return category
    def validate(self, attrs):
        try:
            c=Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name=attrs["category"]["name"])
        attrs["category"]=c
        return attrs
    def create(self, validated_data):
        instance=Good.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.category=validated_data.get("category",instance.category)
        instance.save()
        return instance
class CategorySerizlizer(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=10,min_length=2,error_messages={
        "max_length":"最多十个字",
        "min_length":"最少三个字"
    })

    goods=GoodSerizlizer(many=True,read_only=True)
    def create(self, validated_data):
        instance=Category.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.name=validated_data.get("name",instance.name)
        instance.save()
        return instance
class UserRegistSerizlizer(serializers.Serializer):
    username=serializers.CharField(max_length=10,min_length=3)
    password=serializers.CharField(max_length=10,min_length=3)
    password2=serializers.CharField(max_length=10,min_length=3,write_only=True)
    def validate_password2(self,data):
        if data!=self.initial_data["password"]:
            raise serializers.ValidationError("密码不一致")
        else:
            return data
    def validate(self,attrs):
        del attrs["password2"]
        return attrs
    def create(self,validated_data):
        return User.objects.create_user(username=validated_data.get("username"),email=validated_data.get("email"),password=validated_data.get("password"))
class UserSerizlizer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["user_permissions","groups"]
        def validate(self,attrs):
            print(attrs)
            from django.contrib.auth import hashers
            if attrs.get("password"):
                attrs["password"]=hashers.make_password(attrs["password"])
            return attrs
class OrderSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



