from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from .models import *

class AllCarsView(View):
    
    def get(self, request):
        all_cars = CarDetails.objects.all()
        context = {
            'all_cars': all_cars
        }
        return render(request, 'cars/home.html', context)

class CarDetailView(DetailView):
    model = CarDetails
    template_name = 'cars/car_details.html'
    context_object_name = 'car'


from .forms import Contact_form  # Adjust import as needed

def ContactView(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Contact_form()

    context = {'form': form}
    return render(request, 'cars/contact.html', context)