from django.db import models


class Products(models.Model):
    specification = models.CharField(max_length=22)
    name_product = models.CharField(max_length=22)

    def __str__(self):
        return f'{self.specification} {self.name_product}'

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
