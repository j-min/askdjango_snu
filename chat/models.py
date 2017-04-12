from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(blank=False, max_length=255, unique=True)
    device = models.CharField(blank=True, max_length=255)
    first_name = models.CharField(default='First', max_length=20)
    last_name = models.CharField(default='Last', max_length=20)

    @property
    def name(self):
        try:
            return " ".join([self.first_name, self.last_name])
        except:
            return "Unknown"
    # conversation = models.ManyToManyField('Conversation', blank=True)

    def __str__(self):
        return str(self.user_id)

    def get_conversations(self):
        conversations = []
        for conversation in self.conversation_set.all():
            conversations.append(conversation.get_queries())
        return "\n".join(conversations)

    get_conversations.short_description = 'Conversations'

        # return "\n".join(
        #     [c.conversation_id for c in self.conversation.all()])

class Response(models.Model):
    # session_id = models.ForeignKey('Session')
    body = models.TextField()
    query = models.ForeignKey('Query', null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body


class Query(models.Model):
    user = models.ForeignKey('User')
    def user_id(self):
        return self.user.user_id
    # session_id = models.ForeignKey('Session')
    body = models.TextField()
    conversation = models.ForeignKey('Conversation', null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    guessed_intent = models.ForeignKey(
        'Intent',
        blank=True,
        related_name='guessed_intent')

    correct_intent = models.ForeignKey(
        'Intent',
        blank=True,
        related_name='correct_intent')

    correctly_responded_choices = (
        (True, 'Yes'),
        (False, 'No')
    )
    correctly_responded = models.BooleanField(
        default=(guessed_intent==correct_intent),
        choices=correctly_responded_choices)

    def __str__(self):
        return self.body

    # Correct name in admin panel (Querys => Queries)
    class Meta:
        verbose_name = 'Querie'


intents = ['yesintent', 'nointent', 'letschatintent', 'chatintent']
intents = ((intent, intent) for intent in intents)

class Intent(models.Model):
    title = models.CharField(max_length=50,
                                blank=True,
                                choices=intents,
                                unique=True)
    base_response = models.TextField()

    def __str__(self):
        return self.title

# Session that consist of sequence of chats
# class Session(models.Model):
#     conversation_id = models.ForeignKey('Conversation')
#     user_id = models.ForeignKey('User')

class Conversation(models.Model):
    user = models.ForeignKey('User', null=True)
    conversation_id = models.CharField(max_length=255, unique=True)
    rating = models.IntegerField(default=5)
    # response = models.ManyToManyField('Response')

    def get_user_id(self):
        try:
            return self.user.user_id
        except AttributeError:
            return 'Unknown User'
    get_user_id.short_description = 'user_id'

    def get_user_name(self):
        try:
            return self.user.name
        except AttributeError:
            return 'Unknown User'
    get_user_name.short_description = 'username'

    def get_queries(self):
        return "\n".join(
            [q.body for q in self.query_set.all()])
    get_queries.short_description = 'queries'
    # def get_responses(self):
    #     return "\n".join(
    #         [r.body for r in self.response_set.all()])
