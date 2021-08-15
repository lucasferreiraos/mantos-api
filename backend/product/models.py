from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    image = models.ImageField(upload_to='shirt_images')


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name=_('Título'))
    slug = models.SlugField(max_length=50, verbose_name=_('Slug'))
    description = models.TextField(verbose_name=_('Descrição'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Preço'))
    thumbnail = models.ImageField(upload_to='thumbnails')
    images = models.ManyToManyField(Image)

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __repr__(self):
        return self.title
