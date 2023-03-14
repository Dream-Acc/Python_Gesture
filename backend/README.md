# backend

> powererd by django

## 0. 运行环境配置

1. python3.9
2. 需要安装以下依赖
   ```
   Django==4.1.2
    django-cors-headers==3.13.0
    PyMySQL==1.0.2
    djangorestframework==3.14.0
    mediapipe==0.9.0.1
    torch==1.13.1
    django-simpleui==2022.7.29
   ```

   > pip install -r requirements.txt
   >

## 1. 项目搭建

> django-admin startproject backend

## 2. 运行步骤

1. 进入backend目录
   > cd backend
   >
2. 运行项目
   > python manage.py runserver
   >

## 3. 项目结构

```
│  manage.py
│  project.txt
│  README.md
│  requiments.txt
│  
├─backend  // 项目总配置
│  │  asgi.py
│  │  settings.py // 项目配置
│  │  urls.py // 路由配置(一级路由)
│  │  wsgi.py
│  │  __init__.py
│  │  
│  └─__pycache__
│          ...
│          
├─gesture
│  │  admin.py
│  │  apps.py
│  │  models.py // 公用数据库模型
│  │  tests.py
│  │  urls.py // 路由配置(二级路由)
│  │  views.py // 接口逻辑
│  │  __init__.py
│  │  
│  ├─migrations // 数据库迁移文件
│  │ ...
│  │      
│  └─model // 手语识别模型
│      │  main.py
│      │  model.py
│      │  __init__.py
│      │  
│      ├─checkpoints
│      │      model_39.pth // 训练后的模型
│      │      
│      └─tools // 绘图对应工具包
│              draw_bounding_rect.py
│              draw_landmarks.py
│              draw_rect_text.py
│              landmark_handle.py
│              
└─test
    ...    
...
...
```

## 4. 全局配置

1. 跨域配置
   - 引入django-cors-headers包
   - 在settings.py中配置

     - INSTALLED_APPS中添加corsheaders
     - MIDDLEWARE中添加corsheaders.middleware.CorsMiddleware
     - 添加以下配置

     ```python
     CORS_ORIGIN_ALLOW_ALL = True
     CORS_ALLOW_CREDENTIALS = True
     CORS_ALLOW_HEADERS = ('*')
     CORS_ALLOW_METHODS = ('*')
     ```
2. csrf验证配置
   - 开发阶段暂时关闭csrf验证
   - 全局关闭:
     注释掉settings.py中的MIDDLEWARE中的'csrf.middleware.CsrfViewMiddleware'
   - 局部关闭:
     在views.py中引入@csrf_exempt注解
     ```python
     from django.views.decorators.csrf import csrf_exempt
     @csrf_exempt
     def func(request):
         pass
     ```
3. 数据库配置
   ```python
   DATABASES = {
     'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'database',
       'USER': 'root', # 账号
       'PASSWORD': 'password', # 密码
       'HOST': '127.0.0.1', # HOST
       'POST': 3306, # 端口
     }
   }
   ```

## 5. 项目规范

1. 新建模块
   - 进入backend目录
   - 新建模块
     > python manage.py startapp module_name
     >
   - settings.py中INSTALLED_APPS中添加模块
   - 在module_name目录下新建urls.py文件
   - 在backend目录下的urls.py中添加模块路由
     ```python
     from django.urls import path, include
     urlpatterns = [
         path('module_name/', include('module_name.urls')),
     ]
     ```
2. 新建接口
   - 在module_name目录下的views.py中添加接口
   - 在module_name目录下的urls.py中添加接口路由
     ```python
     from django.urls import path
     from . import views
     urlpatterns = [
         path('func/', views.func),
     ]
     ```
3. 数据库操作
   - 在module_name目录下的models.py中添加数据库模型
   - 在module_name目录下的views.py中添加数据库操作
   - 建立模型后需要迁移数据库
     > python manage.py makemigrations
     > python manage.py migrate
     >
4. 命名规范
