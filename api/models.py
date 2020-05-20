from django.db import models

# Create your models here.
class Client(models.Model):
    """
    Table for the clients
    """
    id = models.AutoField(primary_key = True)
    document = models.IntegerField()
    first_name = models.CharField('First Name', max_length = 50)
    last_name = models.CharField('Last Name', max_length = 50)
    email = models.EmailField(max_lengt = 50)


class Product(models.Model):
    """
    Table for products
    """
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length = 50)
    description = models.CharField('Description', max_length = 200)


class Bill(models.Model):
    """
    Table for Bills
    """
    id = models.AutoField(primary_key = True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField('Company Name', max_length = 150)
    nit = models.IntegerField()
    code = models.IntegerField()


class Bill_Products(models.Model):
    """
    Table for bills with products
    """
    id = models.AutoField(primary_key = True)
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

