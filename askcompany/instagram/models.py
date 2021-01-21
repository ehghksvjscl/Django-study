from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d') # UseFillow # upload_to
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta: 
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, limit_choices_to={'is_public':True})
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)