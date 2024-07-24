from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('detail/<slug:car>/', views.car_detail, name='car_detail'),
    path('reservation/<int:pk>/', views.reservation_view, name='reservation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registration/', views.registration, name='registration'),
    path('check_availability/<str:pk>', views.check_availability, name='check_availability'),
    # path('login/', views.login_user,name='login'),
    # path('logout_user/', views.login_user, name='logout'),
]

