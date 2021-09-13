from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Company(models.Model):
    address = models.TextField('Адрес', max_length=200)
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', max_length=200)
    employees = models.ManyToOneRel('Список сотрудников', )

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    # личный рабочий факс
    type = models.CharField('Тип')
    number = models.CharField('Номер телефона')
    employee = models.ForeignKey()


class Employee(models.Model):
    name = models.CharField('ФИО', max_length=200)
    position = models.CharField('Должность', max_length=200)
    phone_numbers = models.ForeignKey(
        PhoneNumber,
        verbose_name='Номер телефона',
        on_delete=models.CASCADE,
        related_name='employee',
        null=False,
    )

    def __str__(self):
        return self.name
