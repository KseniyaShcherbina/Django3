from django.db import models

class Task(models.Model):
    title = models.CharField("Название",max_length=50)
    task = models.TextField("Описание")
    clock = models.FloatField("Время на задание")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Задача"
        verbose_name_plural = "Задачи"

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural = "Отзывы"