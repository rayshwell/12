from .models import *
from rest_framework import serializers
class GoodSerizlizer1(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方使用source=模型名.字段名
    # read_only = True 表示不能更改（只读）get能获得显示，post无法显示
    # write_only=True 表示只能修改 （get不显示，post显示）   两个不能同时为True
    category=serializers.CharField(source="category.name",write_only=True)
    class Meta:
        model=Good
        # fields="__all__"
        fields = ("id","name","desc","category")
class CategorySerizlizer1(serializers.ModelSerializer):
            """
            编写针对Category的序列化类
            本类指明了Category的序列化细节
            需要继承ModelSerializer 才可以针对模型进行序列化
            在Meta类中 model指明序列化的模型  fields 指明序列化的字段
            """
            ### goods一定要和related_name的值一致

            ##  StringRelatedField() 可以显示关联模型的 __str__ 返回值 many=True 代表多个对象
            # goods=serializers.StringRelatedField(many=True)
            ##  PrimaryKeyRelatedField()可以显示关联模型的主键 ead_only=True只读
            # goods=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
            ## HyperlinkedRelatedField()可以显示关联模型的自己资源的超级链接 view_name="模型名-detail"
            goods = serializers.HyperlinkedRelatedField(view_name="good-detail", read_only=True, many=True)

            ## 使用自定义序列化类
            # goods=CustomSerializers(many=True,read_only=True)

            # goods=GoodSerizlizer(many=True)
            class Meta:
                model = Category
                # __all__ 代表模型中的所有字段
                # fields="__all__"
                # fields指明序列化哪些字段
                fields = ("id", "name", "goods")
class CustomSerializers(serializers.RelatedField):
    """
    自定义序列化类
    """
    def to_representation(self, value):
        """
        重写字段的输出方式
        value 指序列化的模型
        """
        return str(value.id)+"-"+value.name+"--"+value.desc
class CategorySerizlizer(serializers.Serializer):
    """
    序列化类决定了模型序列化细节
    """
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多十个字",
        "min_length":"最少三个字"
    })
    def create(self, validated_data):
        # 通过重写create方法，来定义模型创建方式
        instance=Category.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        # 通过重写update方法，来定义模型的更新方法
        # instance   更改之前的实例
        # validated_data 更改的参数
        instance.name=validated_data.get("name",instance.name)
        instance.save()
        return instance
class GoodImgsSerizlizer(serializers.Serializer):
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
        instance=GoodImgs.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.img=validated_data.get("img",instance.img)
        instance.good=validated_data.get("good",instance.good)
        instance.save()
        return instance
class GoodSerizlizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=20,min_length=3,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少3个字"
    })
    # desc=
    category= CategorySerizlizer(label="分类名")
    imgs=GoodImgsSerizlizer(label="图片",many=True,read_only=True)
    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回新值
        """
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
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["user_permissions","groups"]
        def validate(self,attrs):
            from django.contrib.auth import hashers
            if attrs.get("password"):
                attrs["password"]=hashers.make_password(attrs["password"])
            return attrs
class OrderSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



