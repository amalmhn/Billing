from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView
# Create your views here.

class ItemCreate(TemplateView):
    model = ItemModel
    form_class = ItemCreateForm
    template_name = 'billingapp/itemCreate.html'
    context={}
    def get(self, request, *args, **kwargs):
        form = self.form_class
        item = self.model.objects.all()
        self.context['form'] = form
        self.context['item'] = item
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item')
        else:
            return render(request,self.template_name,self.context)


class PurchaseCreate(TemplateView):
    model = PurchaseModel
    form_class = PurchaseCreateForm
    template_name = 'billingapp/purchaseCreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        purchase = self.model.objects.all()
        self.context['form'] = self.form_class
        self.context['purchase'] = purchase
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase')
        else:
            return render(request,self.template_name,self.context)

class PurchaseView(TemplateView):
    model = PurchaseModel
    template_name = 'billingapp/purchaseView.html'
    context = {}
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        purchase = self.model.objects.filter(id=id)
        self.context['purchase'] = purchase
        return render(request,self.template_name,self.context)

class PurchaseEdit(TemplateView):
    model = PurchaseModel
    form_class = PurchaseCreateForm
    template_name = 'billingapp/purchaseEdit.html'
    context = {}
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        purchase = self.get_object(id)
        form = self.form_class(instance=purchase)
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        purchase = self.get_object(id)
        form = self.form_class(request.POST,instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase')
        else:
            return render(request,self.template_name,self.context)

class PurchaseDelete(TemplateView):
    model = PurchaseModel
    def get_object(self,id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        purchase = self.get_object(id)
        purchase.delete()
        return redirect('purchase')