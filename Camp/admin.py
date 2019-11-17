from django.contrib import admin
from .models import Campaign
# Register your models here.


class CampaignAdmin(admin.ModelAdmin):
    list_display = ['campname', 'camptype',
                    'parameters', 'candidate', 'prize']
    list_per_page = 20
    search_fields = ['campname', 'candidate']

admin.site.register(Campaign, CampaignAdmin)