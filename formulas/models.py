from django.db import models
class Formula(models.Model):
    user_input = models.CharField(max_length=255)


    def __str__(self):
        return self.user_input
# Create your models here.
