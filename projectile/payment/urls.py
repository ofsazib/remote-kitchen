from django.urls import path
from .views import PaymentIntentView

urlpatterns = [
    path('', PaymentIntentView.as_view(), name='payment-create'),
]
