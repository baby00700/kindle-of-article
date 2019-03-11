from django.db import models

# Create your models here.
class Article(models.Model):
    con = models.TextField()
    def __str__(self):
        # 在Python3中使用 def __str__(self):
        return self.con
