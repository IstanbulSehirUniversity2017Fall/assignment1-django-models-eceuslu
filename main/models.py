from django.db import models

# Create your models here.

class PeriodInfo(models.Model):
    title=models.CharField(max_length=50)
    start_year=models.DateField()
    end_year=models.DateField()
    is_actual=models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+' - '+self.title

    def get_is_actual(self):
        if self.is_actual:return 'Period is on going'
        else:return 'Period is over'


class AuthorInfo(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    literary_period=models.ForeignKey(PeriodInfo,on_delete=models.CASCADE,default=1)
    is_alive=models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)+' '+ self.full_name()

    def full_name(self):
        return self.first_name+' '+self.last_name

    def get_is_alive(self):
        if self.is_alive:return 'Author is alive'
        else:return 'Author is not alive'


class BookInfo(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(AuthorInfo,on_delete=models.CASCADE,default='')
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()
    is_digital=models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+self.title

    def get_is_digital(self):
        if self.is_digital:return 'Book is Soft Copy'
        else:return 'Book is Hard Copy'
