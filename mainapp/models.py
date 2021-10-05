from django.db import models


class Advert(models.Model):
    # валидация полей (не больше 3 ссылок на фото, описание не больше 1000 символов, название не больше 200 символов)
    date = models.DateTimeField('Дата создания', auto_now=True)
    title = models.CharField('Название обьявления', max_length=200)
    description = models.CharField('Описание', max_length=1000)
    img = models.URLField('Изображение', max_length=200, unique=True)
    additional_img = models.URLField('Доп изображение 1', max_length=200, blank=True, null=True)
    additional_img_2 = models.URLField('Доп изображение 2', max_length=200, blank=True, null=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'



