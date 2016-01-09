from django.contrib import admin
from hunter_bank.models import Offer, Organization


class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_create', 'offer_update', 'offer_rotation_begin')


class OrganizationAdminAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organization_status')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Organization, OrganizationAdminAdmin)
