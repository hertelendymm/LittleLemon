from django.db import models

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=255)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    inventory = models.PositiveIntegerField()  

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = "menu"


class Booking(models.Model):
    id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255) 
    no_of_guests = models.IntegerField() 
    booking_date = models.DateTimeField() 

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "booking"