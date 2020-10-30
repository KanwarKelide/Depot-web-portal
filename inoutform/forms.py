from django import forms
from .models import arrival
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
class ContactForm(forms.Form):

    #Date =
    Depot                    = forms.CharField()
    Shift                    = forms.ChoiceField(choices=[('1st', '1st'), ('2nd', '2nd')])
    Service_no               = forms.ChoiceField(choices=[('a', 'a'), ('b', 'b')])
    Route_no                 = forms.ChoiceField(choices=[('a', 'a'), ('b', 'b')])
    Scheduled_departure_time = forms.CharField()
    Actual_departure_time    = forms.CharField()
    Odometer_start_reading   = forms.CharField()
    SOC_at_departure         = forms.CharField()
    Driver_id                = forms.ChoiceField(choices=[('1', '1'), ('2', '2')])
    Vehicle_id               = forms.ChoiceField(choices=[('EX1', 'EX1'), ('EX2', 'EX2')])



class SnippetForm(forms.ModelForm):
    class Meta:
        model = arrival
        fields = ('Shift','Vehicle_id','Service_no', 'Route_no','Driver_id', 'Scheduled_departure_time', 'Actual_departure_time', 'Odometer_start_reading', 'SOC_at_departure')
        #__all__

class PersonForm(forms.ModelForm):

    class Meta:
        model = arrival
        fields = '__all__'
