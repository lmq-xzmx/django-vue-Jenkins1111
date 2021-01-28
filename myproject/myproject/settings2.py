# -*- coding: utf-8 -*-

"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$fr)!ermyhbnd*$l%91c=0h%-j^%ajx*x0g)4i1se*v9_ll9r6'

# SECURITY WARNING: don't run with debug turned on in production!
# 生产环境设置 Debug = False
Debug = False
#DEBUG = True

#ALLOWED_HOSTS = ['web']
#ALLOWED_HOSTS = ['127.0.0.1']
#ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['127.0.0.1','web','111.67.193.29','fumuxin.online']
#ALLOWED_HOSTS = ['web','111.67.193.29','fumuxin.online']
ALLOWED_HOSTS = ['111.67.193.29']
# Application definition

INSTALLED_APPS = [
    #'polls.apps.PollsConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'myapp',
    #'polls',

    #'myaccount',
    #'widget_tweaks',
    #'blog',
    #'blogeditor',
    #'taggit',
    #'xiehuimap',
    #'xiehuimapinfo',

    #富文本编辑器
    #'ckeditor',
    #'ckeditor_uploader',

    #'mdeditor',

    #'corsheaders',

    #'v1',
    #'rest_framework',
    #'rest_framework.authtoken',
    #'board',
    #'quickstart',
    #以下为django-allauth相关模块
    #'rest_framework.authtoken',
    #'movies',
    #'django_filters',
    
    'django.contrib.sites',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',

    #第三方账号相关，根据需求添加
    #'allauth.socialaccount.providers.weibo',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.baidu',

]

# app django.contrib.sites需要的设置
SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

# 基本设定：

# 在本例中我们可以让用户通过email或者用户名登录。
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_AUTHENTICATION_METHOD (="username" | "email" | "username_email")
# 指定要使用的登录方法（用户名、电子邮件地址或两者之一）

ACCOUNT_EMAIL_REQUIRED = True
# 要求用户注册时必须填写email


# 设置BACKENDS并提供用户登录验证的方法和用户登录后跳转的链接。
LOGIN_REDIRECT_URL = '/accounts/profile/'
# LOGIN_REDIRECT_URL (="/") 
# 设置登录后跳转链接，重新定向

ACCOUNT_LOGOUT_REDIRECT_URL ="/accounts/profile/"
# ACCOUNT_LOGOUT_REDIRECT_URL (="/") 
# 设置退出登录后跳转链接

# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS (=3)
# 邮件确认邮件的截止日期(天数)

# ACCOUNT_EMAIL_VERIFICATION (="optional")
# 注册中邮件验证方法:“强制（mandatory）”,“可选（optional）”或“否（none）”之一

# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN (=180)
# 邮件发送后的冷却时间(以秒为单位)

# ACCOUNT_LOGIN_ATTEMPTS_LIMIT (=5)
# 登录尝试失败的次数

# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT (=300)
# 从上次失败的登录尝试，用户被禁止尝试登录的持续时间

# ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION (=False)
# 更改为True，用户一旦确认他们的电子邮件地址，就会自动登录

# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE (=False)
# 更改或设置密码后是否自动退出

# ACCOUNT_LOGIN_ON_PASSWORD_RESET (=False)
# 更改为True，用户将在重置密码后自动登录

# ACCOUNT_SESSION_REMEMBER (=None)
# 控制会话的生命周期，可选项还有:False,True

# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE (=False)
# 用户注册时是否需要输入邮箱两遍

# ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE (=True)
# 用户注册时是否需要用户输入两遍密码

ACCOUNT_SIGNUP_FORM_CLASS = 'myaccount.forms.SignupForm'
#要告诉django-allauth使用我们自定义的登录表单



# ACCOUNT_USERNAME_BLACKLIST (=[])
# 用户不能使用的用户名列表

# ACCOUNT_UNIQUE_EMAIL (=True)
# 加强电子邮件地址的唯一性

# ACCOUNT_USERNAME_MIN_LENGTH (=1)
# 用户名允许的最小长度的整数

# SOCIALACCOUNT_AUTO_SIGNUP (=True)
# 使用从社会帐户提供者检索的字段(如用户名、邮件)来绕过注册表单


#如果model中使用了 AbstractUser
# 例如“class UserProfile(AbstractUser):”
#需要在 settings中 定义 AUTH_USER_MODEL = ".UserProfile"
#告诉django 使用 我们定义的user——model
#AUTH_USER_MODEL = "myaccount.UserProfile"



AUTHENTICATION_BACKENDS = (

    # django admin所使用的用户登录与django-allauth无关 
    'django.contrib.auth.backends.ModelBackend',
    # allauth 身份验证 
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 邮箱设定
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '86447840@qq.com' # 你的 QQ 账号和授权码
EMAIL_HOST_PASSWORD = 'psllszkqnbbjbjbg'
EMAIL_USE_TLS = True  # 这里必须是 True，否则发送不成功
EMAIL_FROM = '86447840@qq.com' # 你的 QQ 账号
DEFAULT_FROM_EMAIL = '86447840@qq.com'

# EMAIL_USE_SSL = True #表示十分采取隐式TLS安全连接

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # pip install django-cors-headers
    # python 3.5~3.8
    #'corsheaders.middleware.CorsMiddleware',


    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': ['appfront/dist'],
        'DIRS': ['appfront/dist'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

'''
# 设置数据库。这里用户名和密码必需和docker-compose.yml里mysql环境变量保持一致

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'dbuser',
        'PASSWORD': 'nongming',
        #'HOST': '127.0.0.1',
		'HOST': 'db',
        'PORT': '3306',
    }
}

 # 设置redis缓存。这里密码为redis.conf里设置的密码
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1", #这里直接使用redis别名作为host ip地址
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "nongming", # 换成你自己密码
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


CKEDITOR_UPLOAD_PATH = 'blog_uploads/'
CKEDITOR_JQUERY_URL ='https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_BROWSE_SHOW_DIRS = True
CKEDITOR_RESTRICT_BY_USER = True
CKEDITOR_RESTRICT_BY_DATE = True


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (['Source', '-',  'Preview', '-', ],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', ],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat', '-',
                     "CodeSnippet", 'Subscript', 'Superscript'],
                    ['NumberedList', 'BulletedList', '-', 'Blockquote'],
                    ['Link', 'Unlink', ],
                    ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', ],
                    ['Format', 'Font', 'FontSize', 'TextColor', 'BGColor', ],
                    ['Bold', 'Italic', 'Underline', 'Strike', ],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ),
        'extraPlugins': 'codesnippet',
        'width': 'auto',
    }
}

'''
MDEDITOR_CONFIGS = {
'default':{
    'width': '90%',  # 自定义编辑框宽度
    'heigth': 500,   # 自定义编辑框高度
    'toolbar': ["undo", "redo", "|",
                "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                "h1", "h2", "h3", "h5", "h6", "|",
                "list-ul", "list-ol", "hr", "|",
                "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                "emoji", "html-entities", "pagebreak", "goto-line", "|",
                "help", "info",
                "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
    'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
    'image_folder': 'editor',  # 图片保存文件夹名称
    'theme': 'default',  # 编辑框主题 ，dark / default
    'preview_theme': 'default',  # 预览区域主题， dark / default
    'editor_theme': 'default',  # edit区域主题，pastel-on-dark / default
    'toolbar_autofixed': True,  # 工具栏是否吸顶
    'search_replace': True,  # 是否开启查找替换
    'emoji': True,  # 是否开启表情功能
    'tex': True,  # 是否开启 tex 图表功能
    'flow_chart': True,  # 是否开启流程图功能
    'sequence': True,  # 是否开启序列图功能
    'watch': True,  # 实时预览
    'lineWrapping': False,  # 自动换行
    'lineNumbers': False  # 行号
    }
}
'''
CKEDITOR_CONFIGS = {
    # 配置名是default时，django-ckeditor默认使用这个配置
    'default': {
        # 使用简体中文
        'language':'zh-cn',
        # 编辑器的宽高请根据你的页面自行设置
        'width':'auto',
        'height':'150px',
        'image_previewText':' ',
        'tabSpaces': 4,
        'toolbar': 'Custom',
        # 添加按钮在这里
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline', 'Format', 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Blockquote', 'CodeSnippet'],
            ['Image', 'Link', 'Unlink'],
            ['Maximize']
        ],
        # 插件
        'extraPlugins': ','.join(['codesnippet','uploadimage','prism','widget','lineutils',]),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'



USE_I18N = True

USE_L10N = True

USE_TZ = False
# 保证存储到数据库中的是 UTC 时间；
# 在函数之间传递时间参数时，确保时间已经转换成 UTC 时间；


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATIC_URL = '/static/'

# Add for vuejs
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "appfront/dist/static"),
    
    #os.path.join(BASE_DIR, "static"), 
#]




#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')
MEDIA_URL = '/media/'



#设置 MEDIA_ROOT 和 MEDIA_URL，CKEDITOR_UPLOAD_PATH = 'upload/'，
#图片将上传到项目下的media/upload路径下，图片的url是 /media/upload/
#设置CKEDITOR_IMAGE_BACKEND = 'pillow', 用于生成图片缩略图，在编辑器里浏览上传的图片
CKEDITOR_UPLOAD_PATH = 'upload/'
CKEDITOR_IMAGE_BACKEND = 'pillow'


STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR,"dist/static/")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "appfront/dist/static"),
    
    #寻找静态资源文件夹的列表
)


CORS_ORIGIN_ALLOW_ALL = True
#允许携带cookie
CORS_ALLOW_CREDENTIALS = True


