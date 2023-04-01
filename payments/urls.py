from django.urls import path
from . import views

urlpatterns = [
    path('config/', views.stripe_config),
    path('success/', views.PaymentSuccessView.as_view(), name='payment-success'),
    path('failed/', views.PaymentFailedView.as_view(), name='payment-failed'),

]
