import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.views import CreateAPICustomView
from restaurant.models import Order
from payment.serializers import PaymentWriteSerializer
from payment.models import Payment
class PaymentIntentView(CreateAPICustomView):
    serializer_class = PaymentWriteSerializer
    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        order = request.data.get('order')

        try:
            order = Order.objects.get(id=order)
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_price),
                currency='usd',
            )
            # Create a Payment object in your database
            Payment.objects.create(
                order=order,
                amount=order.total_price,
                payment_intent_id=intent.id
            )
            return Response({'clientSecret': intent.client_secret})
        except stripe.error.CardError as e:
            return Response({'error': str(e)}, status=status.HTTP_403_FORBIDDEN)
