from django.urls import path
from . import views

urlpatterns = [
    path('courses/enroll/<int:pk>/', views.StudentCoursesEnrollDetailView.as_view(),
         name='student_course_enroll'),
    path('courses/billing/', views.StudentCourseBillingView.as_view(), name='course_billing'),
]
