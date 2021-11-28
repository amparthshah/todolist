from django.urls import path
from .views import*
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import  PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('change-password/', PasswordsChangeView.as_view(), name='change-password'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'ToDoApp/reset_password.html'), name='reset_password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(template_name = 'ToDoApp/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name = 'ToDoApp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name = 'ToDoApp/password_reset_complete.html'), name='password_reset_complete'),


    path('',TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('create-task/',TaskCreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),

]
