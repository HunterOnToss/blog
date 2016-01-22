from django.contrib import admin
from hunter_bank.models import Offer, Organization, Client, CreditApplication


class OfferAdmin(admin.ModelAdmin):
    list_display = ('offer_create', 'offer_update', 'offer_rotation_begin', 'offer_rotation_end')


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'organization_status')


class ClientAdmin(admin.ModelAdmin):
    list_filter = ['client_create']
    list_display = ('ID', 'client_create', 'client_update', 'client_name', 'client_family', 'client_otchestvo',
                    'client_birthday', 'client_phone_number', 'client_passport_number', 'client_scoring_point')


class CreditApplicationAdmin(admin.ModelAdmin):
    list_display = ('credit_application_create', 'credit_application_send', 'credit_application_client',
                    'credit_application_offer', 'credit_application_status')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(CreditApplication, CreditApplicationAdmin)
