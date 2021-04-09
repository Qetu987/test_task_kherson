from django.db import models

from django.utils.safestring import mark_safe

from django.urls import reverse


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=150)
    desc = models.TextField(max_length=300)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    curent_sale = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_first_carusel = models.BooleanField(default=False)
    is_second_carusel = models.BooleanField(default=False)
    is_top_item = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_detail', kwargs={'slug': self.title })

    @property
    def image_tag(self):
        return mark_safe('<img width="60" src="%s" />' % self.image.url)