from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from manager.models import Task
from account.models import Notification


@receiver(post_save, sender=Task)
def create_profile(sender, instance, created, **kwargs):
    if created:
        # trigger notification to all consumers in the 'user-notification' group
        channel_layer = get_channel_layer()
        group_name = 'user-notifications'
        msg = f"Hey {instance.assigned_to.username}: {instance.project.manager.username} assigned  {instance.title} to  you"
        event = {
            "type": "task_created_noti",
            "text": msg,
            'employee_email': instance.assigned_to.email
        }
        Notification.objects.create(
                    user = instance.assigned_to ,
                    message = msg
                )
        async_to_sync(channel_layer.group_send)(group_name, event)
   

@receiver(pre_save, sender=Task)
def task_status_update(sender, instance, **kwargs):
    try:
        # Check if the instance is being updated
        if instance.pk:
            # Get the original instance from the database
            original_instance = Task.objects.get(pk=instance.pk)
            
            # Check if the status field is updated
            if original_instance.status != instance.status:
                # Trigger notification for status update
                channel_layer = get_channel_layer()
                group_name = 'user-notifications'
                msg=  f"{instance.assigned_to.username} was updated the status of  {instance.title} - {original_instance.status} to {instance.status}"
                event = {
                    "type": "user_joined",
                    "text":msg ,
                    'manager_eamil': instance.project.manager.email
                }
                Notification.objects.create(
                    user = instance.project.manager ,
                    message = msg
                )
                async_to_sync(channel_layer.group_send)(group_name, event)
    except Task.DoesNotExist:
        # Handle the case where the original instance is not found
        pass        