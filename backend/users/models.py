from django.db import models
from django.contrib.auth.models import AbstractUser


# User model
class User(AbstractUser):
    # Required
    username = models.TextField(max_length=20, unique=True)
    display_name = models.TextField(max_length=50)
    email = models.EmailField(unique=True, blank=False)
    private = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    posts_count = models.IntegerField(default=0)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    # Optional
    bio = models.TextField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    website_links = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.username


# Post model
class Post(models.Model):
    # Required
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    hide_likes = models.BooleanField(default=False)

    # Optional
    caption = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.caption
