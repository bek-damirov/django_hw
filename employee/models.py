from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=25, verbose_name='Имя')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Employee(AbstractPerson):
    position = models.CharField(max_length=35, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    work_experience = models.DateField(verbose_name='Опыт работы с какого года')

    def __str__(self):
        return self.name


class Passport(models.Model):
    inn = models.CharField(max_length=16, verbose_name='ИНН паспорта')
    id_card = models.CharField(max_length=16, verbose_name='ID карта')
    worker = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.inn

    def save(self, *args, **kwargs):
        if self.inn and self.id_card:
            super().save(*args, **kwargs)
            print('ИИН и ID успешно сохранено')

    def get_gender(self):
        if self.inn[0] == '1':
            print('Male')
        elif self.inn[0] == '2':
            print('Female')


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50)
    persons = models.ManyToManyField(Employee, related_name='projects', through="Membership")

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        if self.project_name:
            super().save(*args, **kwargs)
            print('Наименование проекта сохранена')


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    data_joined = models.DateField(verbose_name='Дата присоединения')

    def __str__(self):
        return f'{self.employee.name}-{self.work_project.project_name}'

    def save(self, *args, **kwargs):
        if self.data_joined:
            super().save(*args, **kwargs)
            print('Дата присоединения сохранена')


class Client(AbstractPerson):
    address = models.CharField(max_length=55, verbose_name='Адрес')
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name


class VipClient(Client):
    vip_status_start = models.DateField(verbose_name='Дата присоединения')
    domination_amount = models.IntegerField(verbose_name='Сумма пожертвования')

    def __repr__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.vip_status_start and self.domination_amount:
            super().save(*args, **kwargs)
            print('Дата присоединения и сумма пожертвования сохранена')
