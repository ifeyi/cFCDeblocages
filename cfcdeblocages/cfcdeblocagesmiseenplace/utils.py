from django.contrib.auth.models import User

def deblocage_authenticate(email, password):

    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None