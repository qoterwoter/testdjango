from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class News(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = models.TextField("Название новости")
    description = models.TextField('Описание')
    photo = models.TextField('Ссылка на фотографию')
    date = models.DateField(("Дата публикации"), auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Новость")
        verbose_name_plural = ("Новости")

    def __str__(self):
        return str(self.title) 
class Drivers(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.TextField("Имя водителя")
    surname = models.TextField('Фамилия водителя')
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(0),MaxValueValidator(10)])
    class Meta:
        verbose_name = ("Водитель")
        verbose_name_plural = ("Водители")

    def __str__(self):
        return str(self.name + " " + self.surname) 
class DriversPhoto(models.Model):
    
    driver_id = models.ForeignKey(Drivers,related_name='photos', on_delete=models.CASCADE)
    photo_id = models.AutoField(primary_key=True)
    url = models.TextField('Ссылка на фото')

    class Meta:
        verbose_name = ("Фото водителя")
        verbose_name_plural = ("Фото водителей")

    def __str__(self):
        return str("Фото "+ str(self.driver_id.name)+"a "+ str(self.driver_id.surname)+"a")
class Cars(models.Model):
    
    id = models.AutoField(primary_key=True)
    mark = models.TextField('Марка машины')
    model = models.TextField('Модель машины')
    isValid = models.BooleanField
    class Meta:
        verbose_name = ("Машина")
        verbose_name_plural = ("Машины")

    def __str__(self):
        return self.mark + ' ' + self.model
class DriversCars(models.Model):

    id = models.AutoField(primary_key = True)
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Машина водителя")
        verbose_name_plural = ("Машины водителей")

    def __str__(self):
        return str(self.car_id.mark + ' ' + self.car_id.model + " " + self.driver_id.name + 'а '+ self.driver_id.surname + 'а')
class Clients(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField("Имя клиента")
    surname = models.TextField('Фамилия клиента')
    rating = models.IntegerField('Рейтинг', validators=[MinValueValidator(0),MaxValueValidator(10)])

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")

    def __str__(self):
        return self.name
