
from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=128)

    def str(self):
        return self.fullname

class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    post_count = models.IntegerField(default=0)

    def str(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Nomi')
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sub_content = models.TextField()

    author = models.ForeignKey(Author, related_name='posts',on_delete=models.CASCADE)

    image = models.ImageField(upload_to="post/", null=True)
    published_date_time = models.DateTimeField(null=True)

    read_duration = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    instagram_link = models.CharField(max_length=128, blank=True)
    twitter_link = models.CharField(max_length=128, blank=True)


    def str(self):
        return self.title

class Comments(models.Model):
    title = models.CharField(max_length=128, verbose_name='Nomi')
    author = models.ForeignKey(Author, related_name='comments')
    content = models.TextField()