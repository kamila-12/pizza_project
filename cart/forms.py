# from django import forms
# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
# class CartAddProductForm(forms.Form):
#     quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
#     override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity', max_value=20, required=True)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


