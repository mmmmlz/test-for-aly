from django.db import models

from  django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNum
from read_statistics.models import ReadNumExoandMethod

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name
class Blog(models.Model,ReadNumExoandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_created=True)
    last_update_time = models.DateTimeField(auto_created=True)

    def  __str__(self):
        return "<Blog: %s>" % self.title
    class Meta:
        ordering = ['-created_time']
# Create your models here.




'''
class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)
    blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)
'''