from django.shortcuts import redirect, get_object_or_404

from shop.models import Shops


def login_required(url = '/login/'):
    def decorator(func):
        def inner_func(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect(url)
            return func(request, *args, **kwargs )
        return inner_func
    return decorator


def is_owner(func):
    def inner_func(request, *args, **kwargs):
        user = request.user
        shop = get_object_or_404(Shops, id=kwargs.get('id'))

        if shop.author != user:
            return redirect ('/workspace/')
        return func (request, *args, **kwargs)
    return inner_func