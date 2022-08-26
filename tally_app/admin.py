from django.contrib import admin

from tally_app.models import CostCategory, Costcentr, VoucherModels

# Register your models here.
admin.site.register(VoucherModels)
admin.site.register(CostCategory)
admin.site.register(Costcentr)