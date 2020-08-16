from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False, verbose_name='Email')
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Primeiro Nome')
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Último Nome')

    class Meta:
        verbose_name = 'Cliente'


class Request(models.Model):
    request_date = models.DateField(blank=False, null=False, verbose_name='Data do Peddo')
    client = models.ForeignKey(Client, blank=False, null=False, verbose_name='Client Relacionado', on_delete=models.PROTECT)
    status = models.CharField(default='open', max_length=6, choices=(('open', 'open'), ('closed', 'closed')), blank=False, null=False, verbose_name='Status do Pedido')
    value = models.DecimalField(max_digits=12, decimal_places=3, verbose_name='Valor do Pedido', blank=True, null=True)

    class Meta:
        verbose_name = 'Pedido'
