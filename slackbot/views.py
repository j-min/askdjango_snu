from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import requests
import json
from .models import Team
from .config import SLACK_CLIENT_ID, SLACK_CLIENT_SECRET

def index(request):
    client_id = SLACK_CLIENT_ID
    return render(request, 'slackbot/landing.html', {'client_id': client_id})

def slack_oauth(request):
    code = request.GET['code']

    params = {
        'code': code,
        'client_id': SLACK_CLIENT_ID,
        "client_secret": SLACK_CLIENT_SECRET
    }
    url = 'https://slack.com/api/oauth.access'
    json_response = requests.get(url, params)
    data = json.loads(json_response.text)
    Team.objects.get_or_create(
        name=data['team_name'],
        team_id=data['team_id'],
        bot_user_id=data['bot']['bot_user_id'],
        bot_access_token=data['bot']['bot_access_token']
    )
    return HttpResponse('Bot added to your Slack team!')
