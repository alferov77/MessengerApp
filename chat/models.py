from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ChatGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chat_groups')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    chat_group = models.ForeignKey(ChatGroup, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'


class Profile(User):

    class Meta:
        proxy = True

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])
