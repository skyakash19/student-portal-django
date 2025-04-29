from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup_view
from registration import views
from registration.views import delete_student
from .views import edit_student
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # Public Pages
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('browse_courses/', views.browse_courses, name='browse_courses'),  # Fixed typo here
    path('my-courses/', views.my_courses, name='my_courses'),
    path('enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),

    # User Profile
    path('profile/', views.profile, name='profile'),
    path('course-stats/', views.course_stats, name='course_stats'),

    # Password Management
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Authentication
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout'),
    path('export/excel/', views.export_students_excel, name='export_students_excel'),
    path('export/pdf/', views.export_students_pdf, name='export_students_pdf'),
    # Admin / Staff Features
    path('students/', views.student_list, name='student_list'),
    path('add-course/', views.add_course, name='add_course'),
    path('courses/edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('course-stats/', views.course_stats, name='course_stats'),
    path('student/delete/<int:student_id>/', delete_student, name='delete_student'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('students/export/<int:student_id>/pdf/', views.export_single_student_pdf, name='export_single_student_pdf'),
    path('students/export/<int:student_id>/excel/', views.export_single_student_excel, name='export_single_student_excel'),
    # Course Management
    path('unenroll/request/<int:course_id>/', views.request_unenroll_course, name='request_unenroll_course'),

    path('request-unenroll/<int:course_id>/', views.request_unenroll_course, name='request_unenroll_course'),
    path('admin/unenroll-requests/', views.manage_unenroll_requests, name='manage_unenroll_requests'),
path('admin/unenroll-requests/<int:req_id>/approve/', views.approve_unenroll_request, name='approve_unenroll'),
path('admin/unenroll-requests/<int:req_id>/deny/', views.deny_unenroll_request, name='deny_unenroll'),


]
