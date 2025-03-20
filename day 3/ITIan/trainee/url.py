from django.urls import path
from . import views
from .views import TraineeListView, TraineeCreateView, TraineeUpdateView, TraineeDeleteView


urlpatterns = [
    path('trainee-list/', views.trainee_list, name='trainee_list'),
    path('add-trainee/', views.add_trainee, name='add_trainee'),
    path('update-trainee/<int:id>/', views.update_trainee, name='update_trainee'),
    path('delete-trainee/<int:id>/', views.delete_trainee, name='delete_trainee'),
    

    #>>>>>>>>>>>>VIEWS lab4>>>>>>>>>>>>
    path('', TraineeListView.as_view(), name='trainee_list'),
    path('add/', TraineeCreateView.as_view(), name='trainee_add'),
    path('update/<int:pk>/', TraineeUpdateView.as_view(), name='trainee_update'),
    path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='trainee_delete'),
]
