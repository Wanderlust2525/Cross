from django.shortcuts import render
from django.core.paginator import Paginator

from shop.models import Category, Shops, Type


def main(request):
    shop = Shops.objects.all()
    types = Type.objects.all()


    type_id = request.GET.get('type')
    if type_id is not None:
        shop = shop.filter(type__id = int(type_id))



    search = request.GET.get('search')

    if search is not None:
        shop = shop.filter(name__icontains=search)


    
    

    
    return render(request, 'index.html', {'shop': shop, 'types':types})



def all_product(request):
    shop = Shops.objects.all()
    types = Type.objects.all()
    
    type_id = request.GET.get('type')
    if type_id is not None:
        shop = shop.filter(type__id = int(type_id))


    search = request.GET.get('search')

    if search is not None:
        shop = shop.filter(name__icontains=search)

        

    page = request.GET.get('offset', 1)
    page_size = request.GET.get('limit', 18)

    paginator = Paginator(shop, page_size)
    
    shop = paginator.get_page(page)
    
    return render(request, 'all_product.html', {'shop': shop, 'types':types,})


def detail_shop(request, id):
    shop = Shops.objects.all()
    
    
    type_id = request.GET.get('type')
    if type_id is not None:
        shop = shop.filter(type__id = int(type_id))
    shop=Shops.objects.get(id=id)
    
    categories = Category.objects.all()
    return render(request, 'detail_shop.html', {'shop':shop, 'categories':categories})

# Create your views here.
