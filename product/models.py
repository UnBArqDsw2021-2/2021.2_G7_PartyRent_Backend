from django.db import models


class Product(models.Model):
    name = models.CharField('nome', max_length=20, unique=True)
    description = models.CharField('descrição', max_length=100, unique=True)
    weight = models.IntegerField('peso')
    active = models.BooleanField('ativo', default=True)
    price = models.DecimalField('preço', max_digits=7, decimal_places=2)
    teste = models.ImageField(upload_to='media/product_photo', blank=True, null=True)
    category = models.ForeignKey(
        'Category',
        verbose_name='categoria',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('nome', max_length=20, unique=True)
    description = models.CharField('descrição', max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    