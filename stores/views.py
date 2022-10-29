from ast import Store
from itertools import product
from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import StoreItem
from stores import models
from stores.forms import StoreItemForm


def get_store_items(request: HttpRequest) -> HttpResponse:
    store_items: list[models.StoreItem] = list(models.StoreItem.objects.all())
    context = {
        "store_items": store_items,
    }
    return render(request, "store_item_list.html", context)


def create_store_item(request):
    form = StoreItemForm()
    if request.method == "Post":
        form = StoreItemForm(request.POST)
        if form. is_valid():
            form.save()
            return redirect("store-item-list")

    context = {
        "form": form,
    }
    return render(request, 'create-store-item.html', context)


def update_store_item(request, item_id):
    store_item = StoreItem.objects.get(id=item_id)
    form = StoreItemForm(instance=store_item)
    if request.method == "POST":
        form = StoreItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("store-item-list.html")
    context = {

        "form": form,
        "store_item": {
            "id": item_id,
        }
    }

    return render(request, 'edit-store-item', context)


def get_store_item(request, item_id):
    store_item = StoreItem.objects.get(id=item_id)
    context = {
        "store_item": {
            "store_item": store_item.id,
            "name": store_item.name,
            "description": store_item.description,
            "price": store_item.price,
        }
    }

    return render(request, "store_item.html", context)


def delete_view(request, item_id):
    StoreItem.objects.get(id=item_id).delete()
    return redirect(request, "store-item-list.html")
