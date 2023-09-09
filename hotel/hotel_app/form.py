# forms.py
from django import forms

from hotel_app.models import RoomFeature


class BookingApplicationForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255)
    check_in_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    additional_services = forms.ModelMultipleChoiceField(
        queryset=RoomFeature.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
