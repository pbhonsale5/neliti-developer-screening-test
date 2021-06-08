from django import forms


class CoordinateForm(forms.Form):
    latitude = forms.DecimalField(decimal_places=7)
    longitude = forms.DecimalField(decimal_places=7)
