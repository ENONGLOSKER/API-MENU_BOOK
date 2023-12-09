from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name