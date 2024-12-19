from django.db import models



class Type(models.Model):

    class Meta:
        
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    name = models.CharField(verbose_name='Название', max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
    
    
class Category(models.Model):

    class Meta:
        
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(verbose_name='Название', max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'
    

class Brand(models.Model):

    class Meta:
        
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    name = models.CharField(verbose_name='Название', max_length=100)

    def __str__(self):
        return f'{self.name}'
    
class Size(models.Model):

    class Meta:
        
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    name = models.CharField(verbose_name='Размер', max_length=100)

    def __str__(self):
        return f'{self.name}'
    

    

class Shops(models.Model):
    class Meta:
        
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    
    
    name = models.CharField(verbose_name='Название',max_length=100 )
    articul = models.CharField(verbose_name='Артикул',max_length=100 )
    price = models.CharField(verbose_name='Цена',max_length=100 )
    size = models.ManyToManyField('shop.Size', related_name='shop',verbose_name='Размер') 
    season = models.CharField(verbose_name='Сезон',max_length=100 )
    brand =  models.ForeignKey('shop.Brand', on_delete=models.CASCADE, related_name='shop', null=True, verbose_name='Бренд')    

    type = models.ForeignKey('shop.Type', on_delete=models.CASCADE, related_name='shop', null=True, verbose_name='Тип')
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE, related_name='shop', null=True, verbose_name='Категории')
    image = models.ImageField(verbose_name='Изображение', upload_to='assets/png/',null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    views = models.PositiveIntegerField( verbose_name= 'Просмотры', default=0)
    date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name='Дата изменении', auto_now=True)
    sale = models.BooleanField( verbose_name='Скидки', default= True)


    def __str__(self):
        return self.name

# Create your models here.
