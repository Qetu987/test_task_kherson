from django.db import models
from items.models import Item
from seller.models import User


"""
все наши продажи бегут сюда
"""
# Create your models here.
class Sale(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
