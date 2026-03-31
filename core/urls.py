from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance/delete/<int:pk>/', views.delete_attendance, name='delete_attendance'),
    path('results/', views.result_list, name='result_list'),
    path('my-attendance/', views.student_attendance, name='student_attendance'),
    path('my-results/', views.student_results, name='student_results'),
    path('my-fees/', views.student_fees, name='student_fees'),
]
