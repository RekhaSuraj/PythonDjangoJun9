from django import forms
from django.core import validators


class Product(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    quantity = forms.IntegerField(required=False)
    # lname = forms.CharField(widget=forms.Textarea, required=False)
    # gender = [('Male','male'),('Female','female')]
    # Gender = forms.CharField(widget=forms.Select(choices=gender))
    # email = forms.EmailField(required=False)


    # def clean_name(self):
    #     input_fname = self.cleaned_data['name']
    #     if len(input_fname) > 10:
    #         raise forms.ValidationError("Name should contain max 10 characters")
    #
    #     if input_fname.islower():
    #         raise forms.ValidationError("First letter should be capital")

    # def clean_email(self):
    #     inputemail = self.cleaned_data['email']
    #     if inputemail[-10::] != '@gmail.com':
    #         raise forms.ValidationError('Email must and should be ends with @gmail.com')
    #     return inputemail


# Characteristics:
# Not connected to any database table. You define each form field manually.#
# Used when:
# You don’t need to save the data in a model.You’re handling temporary or computed data (e.g., a contact form or search filter).
#
# ❌ Limitations:
# No automatic DB save/load.
# You must manually handle what happens with the submitted data.

