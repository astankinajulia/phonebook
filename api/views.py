from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import (EmailSerializer, TokenObtainByEmailSerializer)

User = get_user_model()


@api_view(['POST'])
@permission_classes([AllowAny, ])
def email_auth(request):
    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def obtain_token_by_email(request):
    serializer = TokenObtainByEmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User, email=serializer.validated_data.get('email')
    )
    token = AccessToken().for_user(user)
    data = {'token': str(token)}
    return Response(data, status=status.HTTP_200_OK)
