from rest_framework import serializers
from payment.models import Payment

class PaymentWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = (
            'id',
            'alias',
            'order',
            'amount',
            'created_at',
        )
        read_only_fields = (
            'alias',
        )
