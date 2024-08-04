from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime
from django.db.models import F, ExpressionWrapper, fields


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
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['start_date']

    def total_days(self):
        tdays = (self.end_date - self.start_date).days
        if tdays <= 0:
            return 1
        return (self.end_date - self.start_date).days

    def total_rent(self):
        days = self.total_days()
        rent = self.car_make.car_rent
        return days * rent

    # def get_reservation_days(self):
    #     return Reservation.objects.annotate(days=ExpressionWrapper(F('end_date') - F('start_date'), output_field=fields.DurationField()))

    def clean(self):
        overlapping_reservation = Reservation.objects.filter(
            car_make=self.car_make,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date,
        ).exclude(pk=self.pk)
        if overlapping_reservation.exists():
            raise ValidationError('Reservation not Available, pick another time or car')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

# start_date__lte=self.end_date: Returns reservations where the start date is less than or equal to the end date of the new reservation.
# This includes reservations that start on the same day as the end date of the new reservation.
# end_date__gte=self.start_date: Returns reservations where the end date is greater than or equal to the start date of the new reservation.
# This includes reservations that end on the same day as the start date of the new reservation.
