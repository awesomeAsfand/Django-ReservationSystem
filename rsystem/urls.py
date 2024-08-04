from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'rsystem'

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('detail/<int:pk>/', views.car_detail, name='car_detail'),
    path('reservation/<int:pk>/', views.reservation_view, name='reservation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('check_availability/<str:pk>', views.check_availability, name='check_availability'),
    path('delete/<int:pk>', views.delete_reservation, name='delete_reservation'),
    # path('logout_user/', views.login_user, name='logout'),
]



