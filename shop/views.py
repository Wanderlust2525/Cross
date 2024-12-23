from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from shop.forms import LoginForm

from django.contrib.auth.models import User

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


def login_profile(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    form = LoginForm
    message = None

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)

            # user = User.objects.filter(username=username).first()
            # if user and user.check_password(password):

            if user:
                login(request, user)
                return redirect('/workspace/')
            message = 'The user is not found or the password is incorrect.'
    return render(request, 'auth/login.html', {'form': form, 'message': message})

def logout_profile(request):
    logout(request)
    return redirect('/')

# Create your views here.
