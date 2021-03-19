from django.db import models
from django.utils import timezone

# Create your models here.

class articles(models.Model):
    title= models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField(blank=True , null = True , upload_to=" images/%Y/%m/%D/")
    publish_date=models.DateTimeField(default=timezone.now)
    

    def publish(self):
        self.publish_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title