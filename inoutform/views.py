from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm, PersonForm
from .models import get_myp_route_strings
from .models import get_jbs_route_strings
from .models import get_myp_vehicle_strings
from .models import get_jbs_vehicle_strings
from .models import get_myp_driver_strings
from .models import get_jbs_driver_strings
from .models import get_myp_service_ab_strings
from .models import get_myp_service_aj_strings
from .models import get_jbs_service_al_strings
from .models import get_jbs_service_am_strings


#going out
def going_out(request):

    if request.method == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            Shift                    = form.cleaned_data['Shift']
            Service_no               = form.cleaned_data['Service_no']
            Route_no                 = form.cleaned_data['Route_no']
            Scheduled_departure_time = form.cleaned_data['Scheduled_departure_time']
            Actual_departure_time    = form.cleaned_data['Actual_departure_time']
            Odometer_start_reading   = form.cleaned_data['Odometer_start_reading']
            SOC_at_departure         = form.cleaned_data['SOC_at_departure']
            Driver_id                = form.cleaned_data['Driver_id']
            Vehicle_id               = form.cleaned_data['Vehicle_id']

            print (Shift, Service_no, Route_no, Scheduled_departure_time, Actual_departure_time, Odometer_start_reading, SOC_at_departure,Driver_id, Vehicle_id)


    form = ContactForm()
    return render(request, 'form.html',{'form': form})

def coming_in(request):
    if request.method == 'POST':
        form  = SnippetForm(request.POST)
        if form.is_valid():
            print ('Valid')
            form.save()

    form = SnippetForm()
    return render(request, 'form.html',{'form': form})

def personform_page(request):
    context = {}

    personform = PersonForm()
    context['personform'] = personform

    #ROUTE DATA PUSH
    myp_route_strings = get_myp_route_strings()
    jbs_route_strings = get_jbs_route_strings()

    json_myp_strings = json.dumps(myp_route_strings)
    json_jbs_strings = json.dumps(jbs_route_strings)

    context['json_myp_strings'] = json_myp_strings
    context['json_jbs_strings'] = json_jbs_strings

    #----------------------************************----------------------------

    #VEHICLE DATA PUSH
    myp_vehicle_strings = get_myp_vehicle_strings()
    jbs_vehicle_strings = get_jbs_vehicle_strings()

    json_myp_vehicle_strings = json.dumps(myp_vehicle_strings)
    json_jbs_vehicle_strings = json.dumps(jbs_vehicle_strings)

    context['json_myp_vehicle_strings'] = json_myp_vehicle_strings
    context['json_jbs_vehicle_strings'] = json_jbs_vehicle_strings

    #----------------------************************----------------------------

    #DRIVER DATA PUSH
    myp_driver_strings = get_myp_driver_strings()
    jbs_driver_strings = get_jbs_driver_strings()

    json_myp_driver_strings = json.dumps(myp_driver_strings)
    json_jbs_driver_strings = json.dumps(jbs_driver_strings)

    context['json_myp_driver_strings'] = json_myp_driver_strings
    context['json_jbs_driver_strings'] = json_jbs_driver_strings

    #----------------------************************----------------------------

    #SERVICE DATA PUSH  MIYAPUR AJ AND AB
    myp_service_ab_strings = get_myp_service_ab_strings()
    myp_service_aj_strings = get_myp_service_aj_strings()

    json_myp_service_ab_strings = json.dumps(myp_service_ab_strings)
    json_myp_service_aj_strings = json.dumps(myp_service_aj_strings)

    context['json_myp_service_ab_strings'] = json_myp_service_ab_strings
    context['json_myp_service_aj_strings'] = json_myp_service_aj_strings

    #----------------------************************----------------------------

    #SERVICE DATA PUSH JBA AM AND AL
    jbs_service_am_strings = get_jbs_service_am_strings()
    jbs_service_al_strings = get_jbs_service_al_strings()

    json_jbs_service_am_strings = json.dumps(jbs_service_am_strings)
    json_jbs_service_al_strings = json.dumps(jbs_service_al_strings)

    context['json_jbs_service_am_strings'] = json_jbs_service_am_strings
    context['json_jbs_service_al_strings'] = json_jbs_service_al_strings

    return render(request, 'form1.html', context)
