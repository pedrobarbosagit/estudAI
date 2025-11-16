from django.db import models

# Create your models here.
class Activity(models.Model):
    activity_title = models.CharField(max_length=55)
    activity_description = models.CharField(max_length=1100, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_title

    