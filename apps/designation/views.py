from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AbleDesignation
from .serializers import AbleDesignationSerializer


class CreateDesignationAPIView(APIView):

    def post(self, request):
        serializer = AbleDesignationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ListDesignationAPIView(APIView):

    def get(self, request):
        designations = AbleDesignation.objects.all().order_by('-created_at')
        serializer = AbleDesignationSerializer(designations, many=True)
        return Response(serializer.data)
