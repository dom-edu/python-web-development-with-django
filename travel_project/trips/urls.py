from django.urls import path, include
from . import views 


# mapped the view to the url trip_list
urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('new', views.trip_create, name="trip_create"),
]
