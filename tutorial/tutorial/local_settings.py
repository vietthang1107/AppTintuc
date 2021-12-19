DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_blogs',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'app-db',
        'PORT': '3306',
    }
}

SHOW_API_DOC = True
SWAGGER_URL = 'http://127.0.0.1:8080/api'