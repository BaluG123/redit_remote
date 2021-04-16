from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.
class CustomaManager(models.Manager):
    def get_query(self):
        return super().get_query().filter(status="publish")

class Post(models.Model):
    STATUS_CHOICES=(('publish','Publish'),('deraft','Draft'))
    name=models.CharField(max_length=46)
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    video=models.FileField(null=True,blank=True,upload_to='videos/')
    caption=models.CharField(max_length=256)
    title=models.SlugField(max_length=256,unique_for_date="publish")
    publish=models.DateTimeField(default=timezone.now)
    uploaded=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()
    objects=CustomaManager()

    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.title])    
