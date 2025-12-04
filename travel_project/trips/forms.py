from django import forms 
from .models import Trip 

class TripForm(forms.ModelForm):

    start_date = forms.DateField(
        # this will add a calendar to select from
        widget=forms.DateInput(
            attrs={
            'type': 'date',
            'class':'form-control',
            'placeholder':'Select a Date'
            }
        )
    )

    end_date = forms.DateField(
        # this will add a calendar to select from
        widget=forms.DateInput(
            attrs={
            'type': 'date',
            'class':'form-control',
            'placeholder':'Select a Date'
            }
        )
    )


    class Meta:
        model = Trip
        fields = ['title',
                  'destination', 
                  'description',
                  'start_date',
                  'end_date',
                  'image']