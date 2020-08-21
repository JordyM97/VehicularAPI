from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('user_detail/<int:pk>/', views.UserDetail.as_view()),
    path('user_create/', views.UserCreate.as_view()),
    path('user_update/<int:pk>/', views.UserUpdate.as_view()),
    path('user_delete/<int:pk>/', views.UserDelete.as_view()),
]