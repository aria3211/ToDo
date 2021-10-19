from django.db import models



class ToDo(models.Model):
    title = models.CharField(max_length=80)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
