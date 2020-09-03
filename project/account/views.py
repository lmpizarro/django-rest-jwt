from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import logging
logger = logging.getLogger(__name__)

class CreateAccount(APIView):

    def post(self, request, format=None):
        data = {'endpoint': 'CreateAccount'}
        data.update(request.data)

        logger.info('CREATE USER')
        return Response(data)


from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from account.serializers import  UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
