from django.contrib import admin
from django.contrib import admin
from .models import Customer, Product, Repair, RealmeRepair, XiomiRepair, IphoneRepair, InfinixRepair, SamsungRepair, OppoRepair, TecnoRepair, RedmiRepair

# Register each model separately
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Repair)
admin.site.register(RealmeRepair)
admin.site.register(XiomiRepair)
admin.site.register(IphoneRepair)
admin.site.register(InfinixRepair)
admin.site.register(SamsungRepair)
admin.site.register(OppoRepair)
admin.site.register(TecnoRepair)
admin.site.register(RedmiRepair)


