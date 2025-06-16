from django import forms
from myapp1.models import Car


# The Meta inner class tells Django which model to use (Car) and which fields to include.
# fields = "__all__" means include all fields from the Car model in the form.
class Car_form(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

