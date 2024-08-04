from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars, Reservation
from .forms import ReservationForm, LoginForm, UserRegistration, AvailabilityForm
from django.contrib.auth import authenticate, login, logout
from .filters import CarFilter
from django.contrib import messages
import datetime
from cart.forms import CartAddCarForm
from cart.views import cart_add


def car_list(request):
    cars = Cars.objects.all()
    form1 = AvailabilityForm()
    myFilters = CarFilter(request.GET, queryset=cars)
    cars = myFilters.qs
    return render(request, 'rsystem/list.html', {'cars': cars, 'myFilters': myFilters, 'form1': form1})


@login_required
def car_detail(request, pk):
    car_detail = get_object_or_404(Cars, id=pk)
    user_reservation_detail = Reservation.objects.filter(user=request.user)
    return render(request, 'rsystem/detail.html',
                  {'car_detail': car_detail, 'user_reservation_detail': user_reservation_detail})


@login_required
def reservation_view(request, pk):
    cars = Cars.objects.get(id=pk)
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.car_make = cars
            reservation.user = request.user
            reservation_start_date = form.cleaned_data['start_date']
            reservation_end_date = form.cleaned_data['end_date']
            if reservation_start_date and reservation_end_date < datetime.date.today():
                messages.error(request, 'Date must be a future date')
            else:
                reservation.save()
                return redirect('rsystem:car_detail', pk=pk)

    else:
        form = ReservationForm()
    return render(request, 'rsystem/reservation.html', {'form': form, 'cars': cars})


def delete_reservation(request, pk):
    reservation_delete = get_object_or_404(Reservation, id=pk)
    if request.method == 'POST':
        reservation_delete.delete()
        return redirect('rsystem:car_list')

    return render(request, 'registration/delete.html', {'reservation_delete': reservation_delete})


def check_availability(request, pk):
    car = get_object_or_404(Cars, id=pk)
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            check_date = form.cleaned_data['check_availability']
            if check_date <= datetime.date.today():
                messages.error(request, "Date must be a future date")
            else:
                reservation = car.reservation_set.all()
                for res in reservation:
                    if res.start_date <= check_date <= res.end_date:
                        messages.info(request, "Reservation not Available , choose a different date")
                        break
                else:
                    messages.success(request, 'Reservation available')
    else:
        form = AvailabilityForm()
    return render(request, 'rsystem/check_availability.html', {'form': form, 'car': car})


def logout_user(request):
    logout(request)
    return redirect('rsystem/login.html')


def registration(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'rsystem/reg_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistration()
    return render(request, 'rsystem/reg.html', {'user_form': user_form})


def search(request):
    pass

# def login_user(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#             else:
#                 messages.info(request, "Password or username incorrect!!")
#                 return redirect('login')
#     form = LoginForm()
#     return render(request, 'rsystem/login.html', {'form': form})
