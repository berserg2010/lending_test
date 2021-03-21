from django.db import models
from django.contrib.auth import get_user_model


class Customer(models.Model):
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='телефон')

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='учётная запись')

    def get_email(self):
        return self.user.email
    get_email.short_description = 'Эл. почта'

    def __str__(self):
        return self.user.username
