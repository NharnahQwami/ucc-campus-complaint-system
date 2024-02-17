from django.urls import path
from .views import submit_complaint
from . import views


urlpatterns  = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('complaint/', views.complaint, name='complaint'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('staff/', views.staff, name='staff'),
    path('logout/', views.logout, name='logout'), 
    path('resolve_complaint/<int:complaint_id>/', views.resolve_complaint, name='resolve_complaint'),
    path('help/', views.help_view, name='help'),
    path('about/', views.about_view, name='about'),
    path('report/', views.report_issue_view, name='report'),
    path('submit_complaint/', submit_complaint, name='submit_complaint'),
    path('success_page/', views.success_page, name='success_page'),

]

