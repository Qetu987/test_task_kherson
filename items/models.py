from django.db import models

from django.utils.safestring import mark_safe

from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


"""
тут у нас модель товара
"""
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    curent_sale = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_first_carusel = models.BooleanField(default=False)
    is_second_carusel = models.BooleanField(default=False)
    is_top_item = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"slug": str(self.id)})

    @property
    def image_tag(self):
        return mark_safe('<img width="60" src="%s" />' % self.image.url)


"""
здесь хранятся наши изменения цен
"""


class History_of_price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender=Item)
def update_item_for_History(sender, instance, **kwargs):
        History_of_price.objects.create(
            item = instance,
            price = instance.curent_sale
        )