from django.contrib import admin
from .models import Invoice, InvoiceType

# Register your models here.


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['date', 'plate_number',
                    'invoice_number', 'invoice_type', 'price_net', 'vin']
    list_per_page = 20
    search_fields = ['plate_number', 'invoice_number']


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceType)
