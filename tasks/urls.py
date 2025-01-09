from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/edit/', views.profile_view, name='profile'),
    path('profile/', views.view_own_profile, name='view_own_profile'),
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_confirm_delete'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
