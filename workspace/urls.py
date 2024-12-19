from django.urls import path

from workspace import views

urlpatterns = [
    path('create-cross/', views.create_cross, name='create_cross'),
    path('update-cross/<int:id>/', views.update_cross, name='update_cross'),   
    path('delete-cross/<int:id>/', views.delete_cross, name='delete_cross'), 
    path('', views.workspace, name='workspace'),
]