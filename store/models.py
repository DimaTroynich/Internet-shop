from django.db import models


# Create Model Category main entity
# One to many relationship
class Category(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    image = models.ImageField(default="catalog_pics/default.jpg", upload_to='catalog_pics/')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    # Name display in table
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Категории'
        verbose_name_plural = 'Категория'


# Create Model Catalog
# One to many relationship
class Catalog(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(default="catalog_pics/default.jpg", upload_to='catalog_pics/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category')

    # Name display in table
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


# Create Model Product
class Product(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')
    slug = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, db_index=True, verbose_name='Описание')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменен')
    image = models.ImageField(default="catalog_pics/default.jpg", upload_to='catalog_pics/')

    # Name display in table
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)



