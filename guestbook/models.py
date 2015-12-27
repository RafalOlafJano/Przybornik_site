from django.db import models

# Create your models here.
class GBook(models.Model):
    pierwsze_imie = models.CharField(max_length=8)
    drugie_imie = models.CharField(max_length=8)
    nazwisko = models.CharField(max_length=12)
    zawod = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    text = models.TextField()

    class Meta:
        db_table = "guestbook"

    def __str__(self):
		
        return self.title
