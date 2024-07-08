from django.contrib import admin
from django.urls import path ,  include
from . import views
from .views import AllTrainsListView,Bookings,TrainsDetailView,LogoutUserView,showHome
from .views import search,register_page,login_page,profile,BookingCancelDetailView, confirm_cancel,confirm_booking


urlpatterns = [
    path('', showHome, name='home'),
    path('login/',login_page,name='login'),
    
    path('register/',register_page,name='register'),
    path('search/',search,name='search'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    
    
    path('confirm_cancel/<int:pk>',confirm_cancel,name='confirm_cancel'),
    path('buy/<int:pk>',confirm_booking,name ='confirm_booking'),
    
    path('all_booked/',Bookings.as_view(),name = 'all_booked'),
    path('all/',AllTrainsListView.as_view(),name = 'all_trains'),
    path('trains/<int:pk>',TrainsDetailView.as_view(),name ='trains'),
    path('user/<slug:username>/',profile.as_view(),name='profile'),
    path('booking/<int:pk>/',BookingCancelDetailView.as_view(),name='cancel'),
    
    
    path('confirm_cancel/<int:pk>',confirm_cancel,name='confirm_cancel'),
    path('buy/<int:pk>',confirm_booking,name ='confirm_booking'),

    
    
    
]