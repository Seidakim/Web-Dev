from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Category, Producct


def products_list(request):
    products = Producct.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Producct.objects.get(id=product_id)
    except Producct.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(product.to_json())


def categories_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(category.to_json())
def category_products(request,category_id):
    try:
        products = Producct.objects.all().filter(cat_id=category_id)
        products_json = [product.to_json() for product in products]
    except Category.DoesNotExist as exception:
        return JsonResponse({'exception': str(exception)}, status=400)
    return JsonResponse(products_json, safe=False)
