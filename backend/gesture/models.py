from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class Translate(models.Model):
    wordsEnglish = models.CharField(max_length=20, primary_key=True)
    wordsChinese = models.CharField(max_length=20)
    wordsDescription = models.CharField(max_length=100)
    wordsPath = models.CharField(max_length=100)

    class Meta:
        verbose_name = "单词信息"
        verbose_name_plural = "单词信息"


class Word(models.Model):
    username = models.CharField(max_length=20)
    wordsEnglish = models.CharField(max_length=20)
    wordsProficiency = models.IntegerField(default=0)

    class Meta:
        unique_together = ("username", "wordsEnglish")
        verbose_name = "单词熟练度信息"
        verbose_name_plural = "单词熟练度信息"
