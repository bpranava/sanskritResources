from django.db import models

# Create your models here.

class Resource(models.Model):
    resourceName = models.CharField(max_length=200)
    numberOfChapters = models.IntegerField(default=0)

    def __str__(self):
        return self.resourceName

class Chapter(models.Model):
    resourceId = models.ForeignKey(Resource, on_delete=models.CASCADE)
    chapterName = models.CharField(max_length=200)
    numberOfVerses = models.IntegerField(default=0)

    def __str__(self):
        return self.chapterName

class Content(models.Model):
    resourceId = models.ForeignKey(Resource, on_delete=models.CASCADE)
    chapterId = models.ForeignKey(Chapter, on_delete= models.CASCADE)
    sanskritContent = models.CharField(max_length=500)
    translations = models.CharField(max_length=500)

    def __str__(self):
        return self.sanskritContent
    

