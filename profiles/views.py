from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test APT View."""

    def get(self, request, fromat=None):
        """Returns a list of APIView features"""

        an_apiview = [
            'Uses Http methods as function (get, put, post, patch, delete)',
            'It is similar to a traditional Django views',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})


