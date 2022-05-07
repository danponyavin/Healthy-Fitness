from django import forms
from django.forms import NumberInput

from water_tracker.models import Water_tracker



class WaterForm(forms.ModelForm):
    number_of_glasses = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-input', 'placeholder': 'Количество стаканов'}))
    class Meta:
        model = Water_tracker
        fields = ('number_of_glasses',)
