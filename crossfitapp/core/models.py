from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    observation = models.TextField(blank=True, null=True)
    personal_record = models.FloatField()
    pr_date = models.DateField()
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + f" PR {self.personal_record} ({self.created_by})"