from django.db import models
from datetime import datetime

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255, db_index=True)
    No_of_guests = models.PositiveIntegerField(default=1)
    BookingDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f'{self.Name}, table for {self.No_of_guests} on {self.BookingDate}'

class Menu(models.Model):
    Title = models.CharField(max_length=255, db_index=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    Inventory = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'