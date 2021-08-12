from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name=_('Título'))
    slug = models.SlugField(max_length=50, verbose_name=_('Slug'))
    description = models.TextField(verbose_name=_('Descrição'))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_('Preço'))

    class Meta:
        verbose_name = _('Produto')
        verbose_name_plural = _('Produtos')

    def __repr__(self):
        return self.title
