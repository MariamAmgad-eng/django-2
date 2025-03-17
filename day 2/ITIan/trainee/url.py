from django.urls import path
from . import views

urlpatterns = [
    path('trainee-list/', views.trainee_list, name='trainee_list'),
    path('add-trainee/', views.add_trainee, name='add_trainee'),
    path('update-trainee/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete-trainee/<int:id>/', views.delete_trainee, name='delete_trainee'),
]
