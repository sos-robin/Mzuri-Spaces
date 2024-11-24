from django.db import models

class BuyProduct(models.Model):
    title = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(BuyProduct, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return f"Image for {self.product.title}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    

