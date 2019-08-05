from django.db import models


class New(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название новости')
    text = models.TextField(verbose_name='Текст новости')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
