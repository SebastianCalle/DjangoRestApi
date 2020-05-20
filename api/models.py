from django.db import models


class Client(models.Model):
    """
    Table for the clients
    """
    document = models.IntegerField()
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name


class Product(models.Model):
    """
    Table for products
    """
    name = models.CharField('Name', max_length=50)
    description = models.CharField('Description', max_length=200)


class Bill(models.Model):
    """
    Table for Bills
    """
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField('Company Name', max_length=150)
    nit = models.IntegerField()
    code = models.IntegerField()


class BillProducts(models.Model):
    """
    Table for bills with products
    """
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

