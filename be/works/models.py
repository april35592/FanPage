from django.db import models

class Work(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publishing = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='works/')
    introduce = models.TextField()
    more = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title