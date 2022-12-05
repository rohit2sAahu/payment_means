from django.db import models
from django.db.models.aggregates import Max, Min
from django.forms.widgets import Widget


class Coffee(models.Model):
    name=models.CharField(max_length=100)
    amount=models.CharField(max_length=500)
    payment_id=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)
    
    
    
    



