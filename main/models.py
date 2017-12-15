from django.db import models

# Create your models here.

class AuthorInfo(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return str(self.id)+' '+ self.full_name()

    def full_name(self):
        return self.first_name+' '+self.last_name


class BookInfo(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(AuthorInfo,on_delete=models.CASCADE,default='')
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()

    def __str__(self):
        return str(self.id)+' '+self.title
