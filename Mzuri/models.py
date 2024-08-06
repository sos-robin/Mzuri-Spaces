from django.db import models

class Buy_product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/')
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.title

