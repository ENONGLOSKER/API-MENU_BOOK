from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    PAYMENT_METHODS = [
        ('transfer', 'Transfer'),
        ('cash', 'Cash'),
    ]

    menu_items = models.ManyToManyField(Menu)
    user_name = models.CharField(max_length=255)
    table_number = models.PositiveIntegerField()
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    payment_proof = models.ImageField(upload_to='payment_proofs/', blank=True, null=True)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user_name} at table {self.table_number}'
    
    @property
    def total_price(self):
        return sum(item.price for item in self.menu_items.all())