from django.urls import path

app_name = 'main'

from .views import index

urlpatterns = [
    path('', index, name='index'),
]