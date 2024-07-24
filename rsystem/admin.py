from django.contrib import admin
from .models import Cars, Reservation


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['variant', 'category_slug']
#     prepopulated_fields = {'category_slug': ('variant',)}


@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ['make', 'slug', 'car_model', 'car_rent']
    list_editable = ['car_model', 'car_rent', ]
    prepopulated_fields = {'slug': ('make',)}


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['car_make', 'start_date', 'end_date']


