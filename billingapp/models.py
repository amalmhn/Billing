from django.db import models

# Create your models here.

class ItemModel(models.Model):
    item_name = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.item_name

class PurchaseModel(models.Model):
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty_purchase = models.IntegerField(default=1)
    purchase_price = models.IntegerField(default=1)
    selling_price = models.IntegerField(default=1)
    date = models.DateField()

    def __str__(self):
        return self.item