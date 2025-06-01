
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.listing.title}"

class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.booking.user.username} for {self.booking.listing.title}"
