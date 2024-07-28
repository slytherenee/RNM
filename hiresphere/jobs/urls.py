from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/create/', views.create_job, name='create_job'),
    path('sign-up/', views.sign_up, name='signup'),
    path('log-in/', views.log_in, name='login'),
]
