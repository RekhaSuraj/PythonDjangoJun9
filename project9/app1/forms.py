from django import forms


class Product(forms.Form):
    name = forms.CharField()
    quantity = forms.IntegerField()

# Characteristics:
# Not connected to any database table. You define each form field manually.#
# Used when:
# You don’t need to save the data in a model.You’re handling temporary or computed data (e.g., a contact form or search filter).
#
# ❌ Limitations:
# No automatic DB save/load.
# You must manually handle what happens with the submitted data.

