from django import forms

from shop.models import Brand, Category, Shops, Size, Type

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shops
        
        exclude = ('views',)


        widgets = {
            'name': forms.TextInput(attrs={'class': 'create-form', 'placeholder':'Название'}),
            'articul':forms.TextInput(attrs={'class': 'create-form', 'placeholder':'Артикул'}),
            'price': forms.TextInput( attrs={'class': 'create-form', 'placeholder':'Цена'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание', 'rows': 7}),
            'season': forms.TextInput(attrs={'class': 'create-form', 'placeholder':'Season'}),
            
            'category': forms.Select(attrs={'class': 'form-select'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'size': forms.CheckboxSelectMultiple(),
        }

    # CREATE = 'creating'
    # UPDATE= 'updating'

    # def __init__(self, action = CREATE,*args, **kwargs ):
    #     super().__init__(*args, **kwargs)

    #     self.action = action

    #     if action == self.UPDATE:
    #         self.fields['image'].required = False

    # name = forms.CharField(label='Название', max_length=100,  widget = forms.TextInput(
    #     attrs={'class': 'create-form', 'placeholder':'Название'}
    # ))
    # articul = forms.CharField(label='Артикул', max_length=100, widget = forms.TextInput(
    #     attrs={'class': 'create-form', 'placeholder':'Артикул'}
    # ))
    # price = forms.CharField(label='Цена', max_length=100, widget = forms.TextInput(
    #     attrs={'class': 'create-form', 'placeholder':'Цена'}
    # ))

    # image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class':'create-form', 'accept': 'image/*'}))

    # description = forms.CharField(label='Описание', max_length=800, widget = forms.Textarea(
    #     attrs={'class': 'create-form', 'placeholder':'Описание', 'rows':8}
    # ))
    # season = forms.CharField(label='Season', max_length=100, widget = forms.TextInput(
    #     attrs={'class': 'create-form', 'placeholder':'Season'}
    # ))

    # category = forms.ModelChoiceField(label='Категория', queryset = Category.objects.all(), widget=forms.Select(
    #     attrs={'class':'form-select'}))
    
    # type = forms.ModelChoiceField(label='Тип', queryset = Type.objects.all(), widget=forms.Select(
    #     attrs={'class':'form-select'}))
    
    # brand = forms.ModelChoiceField(label='Бренды', queryset = Brand.objects.all(), widget=forms.Select(
    #     attrs={'class':'form-select'}))
    
    # size = forms.ModelMultipleChoiceField(label = 'Размеры', queryset= Size.objects.all(), widget=forms.CheckboxSelectMultiple())

    # sale = forms.BooleanField(label='Скидки', required=False)
    