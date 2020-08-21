from django.urls import path
from . import views

urlpatterns = [
    #path('users/', views.UserList.as_view()),
    #path('user_detail/<int:pk>/', views.UserDetail.as_view()),
    #path('user_create/', views.UserCreate.as_view()),
    #path('user_update/<int:pk>/', views.UserUpdate.as_view()),
    #path('user_delete/<int:pk>/', views.UserDelete.as_view()),

    path('vehicles/', views.VehicleList.as_view()),
    path('vehicle_detail/<int:pk>/', views.GetVehicle.as_view()),
    path('vehicle_create/', views.CreateVehicle.as_view()),
    path('vehicle_update/<int:pk>/', views.UpdateVehicle.as_view()),
    path('vehicle_delete/<int:pk>/', views.DeleteVehicle.as_view()),
]