from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.newton_school_dashboard, name='school_dashboard'),
    path('newtonschool/about/', views.newton_school_about, name='school_about'),
    path('newtonschool/courses/', views.CoursesListView.as_view(), name='courses'),
]
