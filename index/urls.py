from django.contrib import admin
from django.urls import path, include
from index.views import index, item_detail


urlpatterns = [
    path("<slug:slug>", item_detail, name="item_detail"),
]
