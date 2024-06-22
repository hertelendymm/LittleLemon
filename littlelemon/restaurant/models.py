from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID (key)
    title = models.CharField(max_length=255)  # Title (varchar(255))
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price (decimal(10,2))
    inventory = models.PositiveIntegerField()  # Inventory (int(5))

    def __str__(self):
        return self.title 
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'

    # id = models.SmallIntegerField(max_length=5)
    # title = models.CharField(max_length=255)
    # price = 
    # inventory =  


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID (key)
    name = models.CharField(max_length=255)  # Name (varchar(255))
    no_of_guests = models.IntegerField()  # No. of guests (int(6))
    booking_date = models.DateTimeField()  # Booking Date (datetime)

    def __str__(self):
        return self.name

    # first_name = models.CharField(max_length=200)
    # reservation_date = models.DateField()
    # reservation_slot = models.SmallIntegerField(default=10)
    # name = models.CharField(max_length=200) 
    # price = models.IntegerField(null=False) 
    # menu_item_description = models.TextField(max_length=1000, default='') 