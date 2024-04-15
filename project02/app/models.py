from django.db import models

# Create your models here.

class Category(models.Model):
    Category_id = models.IntegerField(primary_key=True)
    Category_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.Category_name
    
class Product(models.Model):
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length = 100)
    product_price = models.IntegerField()
    product_brand = models.CharField(max_length = 100)
    def __str__(self):
        return self.product_name    