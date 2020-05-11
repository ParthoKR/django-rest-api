from django.shortcuts import render, HttpResponse, render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView features"""
        