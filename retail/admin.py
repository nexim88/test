from django.contrib import admin
from .models import DIM_Role, DIM_Access, DIM_Contact_Type, DIM_Unit, DIM_GST, Contact_Info, Sales, Sales_Det, Purchase, Purchase_Det, WebTemplate, DIM_SubCategory, Inventory, Customer

# Register your models here.
admin.site.register(DIM_Role)
admin.site.register(DIM_Access)
admin.site.register(DIM_Contact_Type)
admin.site.register(DIM_Unit)
admin.site.register(DIM_GST)
admin.site.register(Contact_Info)
admin.site.register(Sales)
admin.site.register(Sales_Det)
admin.site.register(Purchase)
admin.site.register(Purchase_Det)
admin.site.register(WebTemplate)
admin.site.register(DIM_SubCategory)
admin.site.register(Inventory)
admin.site.register(Customer)
