from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.CharField(max_length=50, null=True) #Default value if not entered is considered as true
    product_type=models.CharField(max_length=50, null=True)
    cost=models.IntegerField(null=True)
    popularity=models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.product_name
    
class Catogoery(models.Model):
    product_type=models.CharField(max_length=50, null=True)
    description=models.CharField(max_length=1000, null=True)
    Model=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.product_type
    
class Reviews(models.Model):
    product_name=models.CharField(max_length=50, null=True)
    product_type=models.CharField(max_length=50, null=True)
    ratings=models.IntegerField(null=True)

    def __str__(self):
        return self.product_name


