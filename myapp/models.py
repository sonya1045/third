from django.db import models
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    published_date =  models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, name='posts', on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title
    
    def publisher_recently(self):
        return self.published_date > timezone.now() - timedelta(days=7)
    
    
