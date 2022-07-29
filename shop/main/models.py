from django.db import models

# Create your models here.
class Owner(models.Model):
    username = models.CharField(max_length=50, verbose_name="Владелец")

    def __str__(self):
        return self.username

class Product(models.Model):
    # name
    # description
    # price
    # rating
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Стоимость товара')
    rating = models.FloatField(verbose_name='Рейтинг товара')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}: {self.description}"

