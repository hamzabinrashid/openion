from authservice.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


def authenticate(password, username=None, email=None):
    if not (email or username):
        return None
    try:
        if email:
            user = User.objects.get(email=email)
        else:
            user = User.objects.get(username=username)
    except User.DoesNotExist:
        return {'details':'User Does Not Exist'}, status.HTTP_404_NOT_FOUND

    if user.check_password(password):
        tokens = get_token(user)
        return tokens, status.HTTP_200_OK

    return {'detail': 'Invalid credentials'}, status.HTTP_401_UNAUTHORIZED


def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
