from django.contrib import admin 
from django.urls import path 
from .views import index,  MenuItemsView, BookingViewSet, SingleBookingView
from rest_framework.authtoken.views import obtain_auth_token

  
urlpatterns = [ 
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-view'),
    path('menu/<int:pk>/', MenuItemsView.as_view()),
    path('booking/', BookingViewSet.as_view()),
    path('booking/<int:pk>/', SingleBookingView.as_view()),
    path('api-token-auth/', obtain_auth_token)

   
]