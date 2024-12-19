from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator

from workspace.forms import ShopForm
from shop.models import Category, Shops, Type, Brand, Size


def workspace(request):
    shop = Shops.objects.all()
    
    return render(request, 'workspace/index.html', {'shop': shop,})



def create_cross(request):
    form = ShopForm()

    if request.method == 'POST':
        form = ShopForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()

            return redirect('/workspace/')
            # image = form.cleaned_data.pop('image')
            # size = form.cleaned_data.pop('size')

            # shop = Shops.objects.create(**form.cleaned_data)

            # shop.size.add(*size)

            # if image:
            #     shop.image.save(image.name, image)

            
        
    return render(request, 'workspace/create_cross.html', {'form':form})


    #     shop = Shops.objects.create(

    #         name = request.POST.get('name'),
    #         articul = request.POST.get('articul'),
    #         price = request.POST.get('price'),
    #         season = request.POST.get('season'),
    #         description = request.POST.get('description'),            
    #         brand = Brand.objects.get(id=int(request.POST.get('brand'))),
    #         type = Type.objects.get(id=int(request.POST.get('type'))),
    #         category = Category.objects.get(id=int(request.POST.get('category')))
    #     )

           
    #     size_id=list(map(int, request.POST.getlist('size')))
    #     size = Size.objects.filter(id__in = size_id)
    #     shop.size.add(*size)

    #     image = request.FILES.get('image')
    #     if image:
    #         shop.image.save(image.name, image)

    #     shop.save()

    #     return redirect('/workspace/')


    # shop = Shops.objects.all()
    # types = Type.objects.all()
    # categories = Category.objects.all()
    # brands = Brand.objects.all()
    # sizes = Size.objects.all()
    
   
    
    # return render(request, 'workspace/create_cross.html', {'shop': shop, 'types':types, 'categories':categories, 'brands':brands, 'sizes':sizes,})


def update_cross(request, id):

    shop = get_object_or_404(Shops, id=id)
    

    if request.method == 'POST':
        form = ShopForm(data=request.POST, files=request.FILES, instance=shop)

        if form.is_valid():
            form.save()
            return redirect('/workspace/')

    else:       
        form = ShopForm(instance=shop)
    # form = ShopForm(action=ShopForm.UPDATE, initial={
    #         'name': shop.name,
    #         'articul': shop.articul,
    #         'price': shop.price,
    #         'season': shop.season,
    #         'description': shop.description,
    #         'brand': shop.brand,
    #         'type': shop.type,
    #         'category': shop.category,
    #         'size': shop.size.all(),
    #         'sale': shop.sale,
    #     })

    
            # image = form.cleaned_data.pop('image')
            # size = form.cleaned_data.pop('size')

            # shop.size.clear()
            # shop.size.add(*size)

           
            # if image is not None:
            #     shop.image.save(image.name, image)
           
            
            # shop.save()
            # Shops.objects.filter(id=id).update(**form.cleaned_data)
            
   

        # instance Заполняем форму данными объекта shop
        # initial используется для передачи стартовых значений полей формы.

    return render(request, 'workspace/update_cross.html', {'form': form, 'shop': shop})

    # if request.method =='POST':

    #     shop.name = request.POST.get('name')
    #     shop.articul = request.POST.get('articul')
    #     shop.price = request.POST.get('price')
    #     shop.season = request.POST.get('season')
    #     shop.description = request.POST.get('description')           
    #     shop.brand = Brand.objects.get(id=int(request.POST.get('brand')))
    #     shop.type = Type.objects.get(id=int(request.POST.get('type')))
    #     shop.category = Category.objects.get(id=int(request.POST.get('category')))

    #     size_id=list(map(int, request.POST.getlist('size')))
    #     size = Size.objects.filter(id__in = size_id)
    #     shop.size.clear()
    #     shop.size.add(*size)

    #     image = request.FILES.get('image')
    #     if image:
    #         shop.image.save(image.name, image)

    #     shop.save()

    #     return redirect('/workspace/')
    
    # shops = Shops.objects.all()
    # types = Type.objects.all()
    # categories = Category.objects.all()
    # brands = Brand.objects.all()
    # sizes = Size.objects.all()
    
   
    
    # return render(request, 'workspace/update_cross.html', {'shops': shops, 'types':types, 'categories':categories, 'brands':brands, 'sizes':sizes,'shop':shop,})


def delete_cross(request, id):
    shop = get_object_or_404(Shops, id=id)

    if request.method =='POST':
        shop.delete()  
        return redirect('/workspace/')
    

    

# Create your views here.