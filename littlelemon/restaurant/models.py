from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID (key)
    title = models.CharField(max_length=255)  # Title (varchar(255))
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price (decimal(10,2))
    inventory = models.PositiveIntegerField()  # Inventory (int(5))

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = "menu"


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID (key)
    name = models.CharField(max_length=255)  # Name (varchar(255))
    no_of_guests = models.IntegerField()  # No. of guests (int(6))
    booking_date = models.DateTimeField()  # Booking Date (datetime)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "booking"