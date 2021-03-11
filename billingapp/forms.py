from django.forms import ModelForm
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django import forms

class ItemCreateForm(ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'

    #def clean(self):

class PurchaseCreateForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = PurchaseModel
        fields = '__all__'

    #def clean(self):
