from django.db import models

# Create your models here.

class books(models.Model):
    book_name=models.CharField(max_length=100)
    id=models.CharField(max_length=100)
    created_at=models.DateTimeField()
    preview_link=models.URLField(max_length=100)
    count=models.IntegerField()

    def __str__(self):
        return f"{self.book_name}"
