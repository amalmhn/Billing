from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

# class CustomUserManager(BaseUserManager):
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given username, email and password.
#         """
#         if not email:
#             raise ValueError('The given username must be set')
#         email = self.normalize_email(email)
#         #username = self.model.normalize_username(username)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self,email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)


class ItemModel(models.Model):
    item_name = models.CharField(max_length=150,unique=True)

    def __str__(self):
        return self.item_name

class PurchaseModel(models.Model):
    item = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    qty_purchase = models.IntegerField(default=1)
    purchase_price = models.IntegerField(default=1)
    selling_price = models.IntegerField(default=1)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.qty_purchase+self.selling_price)

class Order(models.Model):
    billnumber = models.CharField(max_length=12,unique=True)
    bill_date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=12)
    bill_total = models.IntegerField(default=0)

    def __str__(self):
        return str(self.billnumber)

class OrderLines(models.Model):
    bill_number = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_name = models.ForeignKey(ItemModel,on_delete=models.CASCADE)
    product_qty = models.FloatField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.bill_number)

# class CustomUser(AbstractUser):
#     username = None
#     '''if u want to login via email or phone you need to customise the User model.
# That's why you inherited the AbstractUser here
# You can go inside the user and check the fields required'''
#     email = models.EmailField(('email address'), unique=True)
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email']
#     objects =  CustomUserManager()





