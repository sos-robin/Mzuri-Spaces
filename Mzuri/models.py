from django.db import models

class Buy_product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='Mzuri_uploads/', blank=True, null=True)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        # Construct the URL for the image based on Supabase configuration
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None
