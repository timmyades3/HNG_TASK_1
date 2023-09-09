from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
import datetime
import pytz
# Create your views here.

@api_view(['GET'])
def stackapi(request):
  slack_name = request.GET.get('slack_name')
  track = request.GET.get('track')
  current_time = datetime.datetime.now(pytz.utc)
  time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
  day_of_week = current_time.strftime('%A')
  

  data = {
    'slack_name':f'{slack_name}',
    'current_day':f'{day_of_week}',
    'utc_time':f'{time}',
    'track':f'{track}',
    'github_file_url':'https://github.com/timmyades3/HNG_TASK_1/blob/master/stackapi/views.py',
    'github_repo_url':'https://github.com/timmyades3/HNG_TASK_1',
    'status_code':200
  }
  return Response(data)



  


  

