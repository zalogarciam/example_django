from django.urls import re_path
from panel import views

app_name = 'panel'
urlpatterns = [
    re_path('^$', views.home, name='home')
]