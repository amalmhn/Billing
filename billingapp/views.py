from django.db.models import Sum
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

class OrderCreate(TemplateView):
    model = Order
    form_class = OrderCreateForm
    template_name = 'billingapp/orderCreate.html'
    context = {}
    def get(self, request, *args, **kwargs):
        order = self.model.objects.last()#orm query to fetch the last entered details
        if order:
            last_billnumber = order.billnumber
            lst = int(last_billnumber.split('-')[1])+1
            billnumber = 'klyn-'+str(lst)

        else:
            billnumber='klyn-1000'
        form = self.form_class(initial={'billnumber':billnumber})
        self.context['form'] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            billnumber = form.cleaned_data.get('billnumber')
            form.save()
            return redirect('orderline',billnumber=billnumber)

class OrderLinesView(TemplateView):
    model = OrderLines
    form_class = OrderLinesForm
    template_name = 'billingapp/orderLines.html'
    context = {}
    def get(self, request, *args, **kwargs):
        billnum = kwargs.get('billnumber')
        form = self.form_class(initial={'bill_number':billnum})
        self.context['form'] = form
        items = self.model.objects.filter(bill_number__billnumber=billnum)
        self.context['items'] = items
        total = self.model.objects.filter(bill_number__billnumber=billnum).aggregate(Sum('amount'))
        self.context['total'] = total['amount__sum'] #this amount__sum is the type pf sum saved in total.U can see that in the shell
        self.context['billnum'] = billnum
        return render(request,self.template_name,self.context)
    def post(self,request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            bill_number = form.cleaned_data.get('bill_number')
            p_qty = form.cleaned_data.get('product_quantity')
            product_name = form.cleaned_data.get('product_name')
            order = Order.objects.get(billnumber=bill_number)
            product = PurchaseModel.objects.get(item__item_name=product_name)
            prdct = ItemModel.objects.get(item_name = product_name)
            amount = p_qty * product.selling_price
            orderline = self.model(bill_number=order,product_name=prdct,product_qty=p_qty,amount=amount)

            orderline.save()
            return redirect('orderline',billnumber=bill_number)

class BillGenerate(TemplateView):
    model = Order
    def get(self, request, *args, **kwargs):
        billnum=kwargs.get('billnumber')
        order = self.model.objects.get(billnumber=billnum)
        total = OrderLines.objects.filter(bill_number__billnumber=billnum).aggregate(Sum('amount'))
        total = total['amount__sum']
        order.bill_total = total
        order.save()
        print('bill saved')
        return redirect('order')
