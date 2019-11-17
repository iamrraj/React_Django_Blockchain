from django.contrib import admin
from .models import Contact

# Register your models here.


class ConatctAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'phone', 'email']
    list_per_page = 20
    search_fields = ['first_name', 'last_name']


admin.site.register(Contact, ConatctAdmin)
