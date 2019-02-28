from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:random_wor>/', views.detail, name='detail')
]