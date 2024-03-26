from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Customers (models.Model):
    customer_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.photo.url))
    image_tag.short_description = 'Image'

class Categories (models.Model):
    category_name = models.CharField(max_length=200)
    description = models.TextField()

class Employees (models.Model):
    last_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    notes = models.TextField()

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.photo.url))
    image_tag.short_description = 'Image'

class OrderDetails (models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

class Orders (models.Model):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    employee_id = models.IntegerField()
    order_date = models.DateField()
    shipper_id = models.IntegerField()

class Products (models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    supplier_id = models.IntegerField()
    category_id = models.CharField(max_length=20)
    unit = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=3)
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />'%(self.photo.url))
    image_tag.short_description = 'Image'

class Shippers (models.Model):
    shipper_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

class Suppliers (models.Model):
    supplier_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

class Contacts (models.Model):
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    message = models.TextField()

class Carts (models.Model):
    coupon = models.CharField(max_length=20)
    
class Reviews (models.Model):
    product_id = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField(max_length=200)
    review = models.TextField()
    rate = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)


