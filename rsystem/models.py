from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime


# check availability filter

class Cars(models.Model):
    make = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    car_model = models.IntegerField()
    car_description = models.TextField()
    car_rent = models.IntegerField()
    car_image = models.ImageField(upload_to='media', blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['make']

    def __str__(self):
        return self.make

    def get_absolute_url(self):
        return reverse('rsystem:car_detail', args=[self.slug])


class Reservation(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    anonymous_user = models.CharField(max_length=255, blank=True, null=True)
    car_make = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        user_info = self.user.username if self.user else self.anonymous_user
        return f"{user_info} - {self.car_make.make} Reservation "

    def clean(self):
        overlapping_reservation = Reservation.objects.filter(
            car_make=self.car_make,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date,
        ).exclude(pk=self.pk)

        if overlapping_reservation.exists():
            raise ValidationError('Reservation not Available, pick another time or car')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


