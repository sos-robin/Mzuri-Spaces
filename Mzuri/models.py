from django.db import models

class Buy_product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='img/')
    description = models.TextField(max_length=100,blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"