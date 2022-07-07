from django.db import models
from accounts.models import User


class Post(models.Model):
    content = models.TextField(null=False, blank=False, verbose_name='Content')
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='post')
    created_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'posts'

    @property
    def likes(self):
        return self.post_like.count()


class PostLike(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='post_like')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='post_like')
    created_at = models.DateField(auto_now=True)
