"""
Django settings for drfend project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'iq@jcnk807dz0qdwpa3=#$$57)q20-pe^f1uc5u$bt=v8=uvwk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'rest_framework',
    # 'rest_framework_jwt',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    # 跨域
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'drfend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drfend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIAFILES_DIRS = [os.path.join(BASE_DIR,'media')]
# 此处可以对 Django rest_framework 重新配置
REST_FRAMEWORK = {
    # Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',
    #默认权限配置 ，每一个http方法都可以有对应的权限配置
    # 'DEFAULT_PERMISSION_CLASS':[
    #    ' rest_framework.permissions.AllowAny'
    # ],
    #全局认证，优先级高于视图类的
    'DEFAULT_AUTHENTICATION_CLASS':[
        # 使用rest_framework_simplejwt认证 不用在数据库里增加一张表
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        # 只能使用https协议，在服务器数据库中增加一张表，增加服务器开销
        'rest_framework.authentication.TokenAuthentication',

        # 首先使用Session认证，如果失败，会进行Basic认证 从上往下开始
        # Cookie与Session Cookie是存储在浏览器上的非敏感数据 在header中携带X-CSRFToken和相应的值 值可以在浏览器登陆用户之后找cookie复制
        # Session是存储在服务器上的敏感数据 但是Session离不开Cookie 因为session的sessionid存储在浏览器中
        # 发起请求时，需要在cookie中携带sessionid和csrftoken
        # 用户不能退出，在服务器数据库中增加一张表，增加服务器开销
        'rest_framework.authentication.SessionAuthentication',

        # 将请求中携带的类似于Basic YWRtaW46MTIzNDU2  进行解码获取对应的用户 获取成功就认证成功 失败，就认证失败
        # 发起请求时，可以将用户名密码 进行编码 写入Authentication 再发起请求
        # 每次都需要用户名和密码
        'rest_framework.authentication.BasicAuthentication',
    ],
    # # 配置全局的频次限制类 防止爬虫
    # 'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle','rest_framework.throttling.UserRateThrottle',],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'user': '100/day',
    #     'anon': '100/day',
    # },
    # 全局配置分页
    'DEFAULT_PAGINATION_CLASS':'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 2,
    # 全局过滤
    'DEFAULT_FILTER_CLASS':['django_filters.rest_framework.DjangoFilterBackend'],
}
AUTH_USER_MODEL='shop.User'

# 自定义认证类  应用名.文件名.认证类名
AUTHENTICATION_BACKENDS=['shop.authbackend.MyLoginBackend']

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True

# DRF提供了分页pagination 建立在django的基础上进行的封装
# from django.core.paginator import Paginator,Page
# 分页    paginator（将列表分成多个页）  page（每个页）

