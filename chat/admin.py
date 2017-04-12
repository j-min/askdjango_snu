from django.contrib import admin
from chat.models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'first_name', 'last_name', 'name', 'device' , 'get_conversations']
    list_editable = ['first_name', 'last_name']

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'body', 'timestamp', 'guessed_intent', 'correct_intent', 'correctly_responded']
    list_editable = ['body', 'correct_intent', 'correctly_responded']

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['body', 'query', 'timestamp']
    list_display_links=['body']

@admin.register(Intent)
class IntentAdmin(admin.ModelAdmin):
    list_display = ['title', 'base_response']
    # list_display_links=['title']
    # list_editable = ['title', 'base_response']

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ['get_user_id', 'get_user_name', 'conversation_id', 'rating', 'get_queries']# , 'get_responses']
    list_display_links = ['conversation_id']
    list_editable = ['rating']
