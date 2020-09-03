from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import logging
logger = logging.getLogger(__name__)



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        logger.info('HELLO VIEW ERROR CALLED')
        logger.error('HELLO VIEW INFO CALLED')
        return Response(content)
