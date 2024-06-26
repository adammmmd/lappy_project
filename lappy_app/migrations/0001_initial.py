# Generated by Django 5.0.3 on 2024-03-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=200)),
                ('contact_email', models.EmailField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images/customers')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('birth_date', models.DateField()),
                ('photo', models.ImageField(upload_to='images/employees')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('customer_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('order_date', models.DateField()),
                ('shipper_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('supplier_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('unit', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=15)),
                ('photo', models.ImageField(upload_to='images/products')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_email', models.EmailField(max_length=200)),
                ('review', models.TextField()),
                ('rate', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shippers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]
