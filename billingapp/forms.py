from django.forms import ModelForm
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
#user creation form and User model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ItemCreateForm(ModelForm):
    class Meta:
        model = ItemModel
        fields = '__all__'

    #def clean(self):

class PurchaseCreateForm(ModelForm):
    # date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = PurchaseModel
        fields = '__all__'

    #def clean(self):

class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['billnumber','customer_name','phone_number']

class OrderLinesForm(forms.Form):
    bill_number = forms.CharField()
    product_quantity = forms.IntegerField()
    product_name = PurchaseModel.objects.all().values_list('item__item_name')
    result = [(tp[0],tp[0]) for tp in product_name]
    product_name = forms.ChoiceField(choices=result)

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'password1' , 'password2' , 'first_name' , 'last_name' , 'email']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=130)

