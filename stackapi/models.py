from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.


class Stack(models.Model):
  slack_name = models.CharField(max_length=200)
  current_day = models.DateField(default=date.today)
  utc_time = models.DateTimeField(default=timezone.now)
  track = models.CharField(max_length=200)

  def __str__(self):
    return self.slack_name
  
  @property
  def github_file_url(self):
    return "https://github.com/timmyades3/HNG_TASK_1/blob/master/stackapi/views.py"
  @property
  def github_repo_url(self):
    return "https://github.com/timmyades3/HNG_TASK_1"
  @property
  def status_code(self):
    return 200