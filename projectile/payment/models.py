from django.db import models
from common.models import BaseModel

class Payment(BaseModel):
    order = models.OneToOneField("restaurant.Order", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_intent_id = models.CharField(max_length=255)
    def __str__(self):
        return f"Payment for order {self.order.id}"
