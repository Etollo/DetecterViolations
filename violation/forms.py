from django import forms
from .models import Violation


class ViolationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ViolationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Violation
        fields = ['image', 'time', 'place', 'is_active', 'description']

        widgets = {
            'image': forms.ImageField(),
            'time': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'place': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
