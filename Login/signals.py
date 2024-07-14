from django.contrib.auth.signals import user_logged_in
from auditlog.models import LogEntry    

def log_user_login(sender, request, user, **kwargs):
    LogEntry.objects.log_action(
        user_id=user.pk,
        content_type_id=None,
        object_id=None,
        object_repr='User Login',
        action_flag=LogEntry.Action.LOGIN
    )

user_logged_in.connect(log_user_login)