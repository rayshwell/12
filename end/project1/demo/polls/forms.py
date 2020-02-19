from django import forms
from .models import User
class LoginForm(forms.Form):
    """
    定义一个登陆表单用于生成html登陆表单
    """
    username=forms.CharField(max_length=150,label="用户名",help_text="最大150")
    password=forms.CharField(min_length=3,max_length=11,widget=forms.PasswordInput,label="密码")


class RegistForm(forms.ModelForm):
    """
    定义一个注册表单用于生成html表单
    """
    password2=forms.CharField(widget=forms.PasswordInput,label="再次输入")
    class Meta:
        model=User
        fields=["username","password"]
        widgets={"password":forms.PasswordInput}