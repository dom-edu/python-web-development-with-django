from django.shortcuts import render
from .models import Trip

# Create your views here.

# things we would want to do/see in our app
# 1. see the list of trips -> def trip_list
# 2. create a new trip -> def trip_create 

# list trips
def trip_list(request):
    # query model
    trips = Trip.objects.all()
    # get pass in results for html rendering
    context = {'trips': trips}
    return render(request, 'trip_list.html', context)


def trip_create(request):
    pass
