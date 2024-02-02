from django.contrib import admin

from common.admin import BaseModelAdmin

from payment.models import (
    Payment,
)


admin.site.register(Payment)
class PaymentAdmin(BaseModelAdmin):
    pass