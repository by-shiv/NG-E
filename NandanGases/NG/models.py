from django.db import models

# Create your models here.

Category=(
   ('MD','Medical'),
   ('IN','Industrial'),
)


class Product(models.Model):
   title = models.CharField(max_length=100)
   selling_price = models.FloatField(default='')
   description = models.TextField(default='')
   category = models.CharField(choices=Category, max_length=2, default=1)
   product_image = models.ImageField(upload_to='product', default='')
   def _str_(self):
      return self.title
   