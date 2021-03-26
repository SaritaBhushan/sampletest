from django.db import models

from django.db.models.fields import TimeField, BooleanField, DateField, DateTimeField, DecimalField, TextField, FloatField, IntegerField
import datetime

# from django.contrib.auth.models import User

class User(models.Model):
    name = TextField(max_length=255, null=False)
    userid = TextField(max_length=255, null=False)
    dob = DateField(null=True, blank=True)

    # Integration information
    status = BooleanField(default=True)

    # Time Stamp information
    created = DateTimeField(auto_now=True)
    updated = DateTimeField(auto_now_add=True)

class UserAddress(models.Model):
    user =  models.ForeignKey(User, to_field='id', related_name='user_addresses', on_delete=models.CASCADE,)
    address = TextField(max_length=255, null=False)

    # Time Stamp information
    created = DateTimeField(auto_now=True)
    updated = DateTimeField(auto_now_add=True)

class UserRemark(models.Model):
    # remark = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE) #,  to_field='id',related_name='user_remark', unique_key = True, on_delete = models.CASCADE)
    # user = models.ForeignKey(User, to_field='id', primary_key = True, on_delete=models.CASCADE)
    userremark = TextField(max_length=255, null=False)

    # Time Stamp information
    created = DateTimeField(auto_now=True)
    updated = DateTimeField(auto_now_add=True)
