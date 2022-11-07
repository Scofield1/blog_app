from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    body = RichTextField(null=True)
    image = models.ImageField(upload_to='posts/blog_img', null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update', 'created']

    def __str__(self):
        return self.title


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(default='media/profile_pic.svg', upload_to='profile')

    def __str__(self):
        return self.user.username


class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogModel, on_delete=models.CharField)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]


class NewsFeedModel(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email









