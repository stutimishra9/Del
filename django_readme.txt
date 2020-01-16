1. create project
django-admin startproject Myproject
2.run the server
python manage.py runserver
3.create admin credentials
python manage.py createsuperuser
4.create schema(makemigrations) and execute schema on db(migrate)
python manage.py makemigrations
python manage.py migrate
5.create app
python manage.py startapp home
6.settings.py->installed apps->add 'home'
7.myproject/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),path('',include(home.urls))
]
8.home/urls.py
from .import views
9.views.py
