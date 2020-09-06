from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
	path('blog/<str:pk>/', views.blog, name="detail_blog"),
    path('project/<str:pk>/', views.project, name="detail_project"),
]