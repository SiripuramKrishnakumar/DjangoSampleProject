from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class CustomerDetails(APIView):
    def get(self, request):
        model = PersonalDetails.objects.all()
        serializer = PersonalDetailSerializer(model, many=True)
        return Response(serializer.data)



