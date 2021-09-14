from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Company(models.Model):
    address = models.TextField('Адрес', max_length=200)
    name = models.CharField('Название', max_length=200, unique=True, )
    description = models.TextField('Описание', max_length=200)
    # поле список сотрудников

    def __str__(self):
        return self.name


class Employee(models.Model):
    # Внутри одной организации не может быть сотрудников с одинаковыми ФИО,
    # но они могут быть в разных организациях.
    name = models.CharField('ФИО', max_length=200)
    position = models.CharField('Должность', max_length=200)
    company = models.ForeignKey(
        Company,
        verbose_name='Компания',
        on_delete=models.CASCADE,
        related_name='employee',
        null=False,
    )

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    PERSONAL = 'personal'
    WORK = 'work'
    FAX = 'fax'

    TYPES = [
        (PERSONAL, 'personal'),
        (WORK, 'work'),
        (FAX, 'fax'),
    ]

    type = models.CharField(
        'Тип',
        choices=TYPES,
        default=PERSONAL,
        max_length=20,
    )
    # Номера телефонов отображаются в формате +79161234567.
    # Нужно учесть, что номера телефонов могут быть с разными кодами страны.
    number = models.CharField(
        'Номер телефона',
        max_length=30,
    )
    employee = models.ForeignKey(
        Employee,
        verbose_name='Сотрудник',
        on_delete=models.CASCADE,
        related_name='phone',
        null=False,
    )
    # Рабочие телефоны могу быть одинаковыми для нескольких сотрудников,
    # но личные — нет.


class User(AbstractUser):
    email = models.EmailField(
        'Email',
        unique=True,
    )

    class Meta:
        ordering = ['-id']
