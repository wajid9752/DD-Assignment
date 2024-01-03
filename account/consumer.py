from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user']
        if not self.user.is_authenticated:
            self.close()
            return
        
        self.GROUP_NAME = 'user-notifications'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME, self.channel_name
            )
    
    def user_joined(self, event):
        if self.user.email == event['manager_eamil']:
            html = get_template("main/partials/notification.html").render(
                context={"notification": event["text"]}
            )
            self.send(text_data=html)
        else:
            self.close()
            return
    def task_created_noti(self, event):
        if self.user.email == event['employee_email']:
            html = get_template("main/partials/notification.html").render(
                context={"notification": event["text"]}
            )
            self.send(text_data=html)
        else:
            self.close()
            return
