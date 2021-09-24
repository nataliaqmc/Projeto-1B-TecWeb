from django.db import models

class TagData(models.Model):
    tagTitle = models.CharField(max_length=200)
    def __str__(self):
        #ID.TITULO - RETURN
        return f'{self.tagTitle}'
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tagContent = models.ForeignKey(TagData, on_delete=models.CASCADE)
    def __str__(self):
        #ID.TITULO - RETURN
        return f'{self.id}.{self.title}'

