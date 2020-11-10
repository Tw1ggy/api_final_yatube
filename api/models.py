from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Group(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, verbose_name='Название группы', help_text='Название группы')


class Post(models.Model):
    text = models.TextField('Текст', help_text='Введите текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts', verbose_name='Группа', help_text='Группа')

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField('Текст', help_text='Введите текст')
    created = models.DateTimeField('Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    
    class Meta:
        unique_together = ['user', 'following']
