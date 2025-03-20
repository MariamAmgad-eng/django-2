from django.urls import path
from . import views

urlpatterns = [
    path('course-list/', views.course_list, name='course_list'),
    path('add-course/', views.add_course, name='add_course'),
    path('update-course/<int:id>/', views.update_course, name='update_course'),
    path('delete-course/<int:id>/', views.delete_course, name='delete_course'),
]
