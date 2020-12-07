from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('website', blank=True)
    description = models.TextField('descrição', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', verbose_name='palestrante', on_delete=models.CASCADE)
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('contato', max_length=255)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'
