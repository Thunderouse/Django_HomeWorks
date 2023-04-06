from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = list(Phone.objects.all())
    # print('!'*50, '\n', 'type(phones)', type(phones), '\n', '!'*50)
    match request.GET.get("sort"):
        case 'name':
            phones.sort(key=lambda a: a.name)
        case "max_price":
            phones.sort(key=lambda a: a.price, reverse=True)
        case "min_price":
            phones.sort(key=lambda a: a.price)

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone[0],
    }
    return render(request, template, context)
