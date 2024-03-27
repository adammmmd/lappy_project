from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

admin.site.site_header = "Admin Lappy"
admin.site.site_title = "Lappy"
admin.site.index_title = "Admin Toko"

class CustomersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'image_tag')
    list_filter = ('customer_name','contact_name', 'address', 'city', 'postal_code', 'country')
    search_fields = ('customer_name','contact_name', 'address', 'city', 'postal_code', 'country')

admin.site.register(Customers, CustomersAdmin)

class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    list_filter = ('category_name', 'description')
    search_fields = ('category_name', 'description')

admin.site.register(Categories, CategoriesAdmin)

class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date', 'image_tag', 'notes')
    list_filter = ('first_name', 'last_name', 'birth_date', 'photo', 'notes')
    search_fields = ('id', 'first_name', 'last_name', 'birth_date', 'notes')

admin.site.register(Employees, EmployeesAdmin)

class OrderDetailsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'order_id', 'product_id', 'quantity')
    list_filter = ('order_id', 'product_id', 'quantity')
    search_fields = ('order_id', 'product_id', 'quantity')

admin.site.register(OrderDetails, OrderDetailsAdmin)

class OrdersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'order_id', 'customer_id', 'employee_id', 'order_date', 'shipper_id')
    list_filter = ('order_id', 'customer_id', 'employee_id', 'order_date', 'shipper_id')
    search_fields = ('id', 'order_id', 'customer_id', 'employee_id', 'order_date', 'shipper_id')

admin.site.register(Orders, OrdersAdmin)

class ProductsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_description', 'supplier_id', 'category_id', 'unit', 'price', 'image_tag')
    list_filter = ('product_name', 'supplier_id', 'category_id', 'unit', 'price')
    search_fields = ('product_name', 'supplier_id', 'category_id', 'unit', 'price')

admin.site.register(Products, ProductsAdmin)

class ShippersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'shipper_name', 'phone')
    list_filter = ('shipper_name', 'phone')
    search_fields = ('shipper_name', 'phone')

admin.site.register(Shippers, ShippersAdmin)

class SuppliersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'phone')
    list_filter = ('supplier_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'phone')
    search_fields = ('supplier_name', 'contact_name', 'address', 'city', 'postal_code', 'country', 'phone')

admin.site.register(Suppliers, SuppliersAdmin)


class ContactsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'contact_name', 'contact_email', 'message')
    list_filter = ('contact_name', 'contact_email', 'message')
    search_fields = ('contact_name', 'contact_email', 'message')

admin.site.register(Contacts, ContactsAdmin)

class ReviewsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate', 'datetime')
    list_filter = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate',  'datetime')
    search_fields = ('id', 'product_id', 'customer_name', 'customer_email', 'review', 'rate', 'datetime')

admin.site.register(Reviews, ReviewsAdmin)

class SubscriptionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id','subscription_email')
    list_filter = ('id', 'subscription_email')
    search_fields = ('id', 'subscription_email')

admin.site.register(Subscriptions, SubscriptionsAdmin)









