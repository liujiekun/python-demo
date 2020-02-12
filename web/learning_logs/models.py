from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
  owner = models.ForeignKey(User, models.SET('liu'))
  text=models.CharField(max_length=200)
  date_add = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.text

class Entry(models.Model):
  topic = models.ForeignKey(Topic,models.SET('liu'))
  text = models.TextField()
  date_add = models.DateTimeField(auto_now_add=True)
  class Meta:
    verbose_name_plural = 'entries'
  def __str__(self):
    if (len(self.text) > 50):
      return str(self.text)[:50] + "..."
    else:
      return self.text
