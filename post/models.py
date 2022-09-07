from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_of_followers  = models.IntegerField(default=0)
    follwings = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.IntegerField(default=0)
    # comments = models.IntegerField(default=0)
    def __str__(self):
        return self.user

    def count_likes(self):
        return self.likes.count()

    def count_comments(self):
        return self.comments.count()

    def liked_users(self):
        liked_users = self.likes.values_list('user', flat=True)
        return liked_users

    def get_comments(self):
        return self.comments.all().order_by("created_at")    


class Comment(models.Model):
    body = models.CharField(max_length=250)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)


class like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes")
    created = models.DateTimeField(auto_now_add=True)
