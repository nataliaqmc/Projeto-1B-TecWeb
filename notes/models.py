from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.CharField(max_length=200)
    def __str__(self):
        #ID.TITULO - RETURN
        return f'{self.id}.{self.title}'