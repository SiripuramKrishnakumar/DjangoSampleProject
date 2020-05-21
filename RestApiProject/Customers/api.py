from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class CustomerDetails(APIView):
    def get(self, request):
        model = PersonalDetails.objects.all()
        serializer = PersonalDetailSerializer(model, many=True)
        return Response(serializer.data)


class CreateCustomer(APIView):
    def get(self, request, customerId):
        try:
            model = PersonalDetails.objects.get(id=customerId)
            serializer = PersonalDetailSerializer(model)
            if serializer.data is not None:
                return Response(serializer.data)
            else:
                return Response("NOt Found", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("Record Not Found", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, customerId):
        try:
            serializer = PersonalDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("Enter Valid details", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response("Invalid input", status=status.HTTP_400_BAD_REQUEST)


class UpdateCustomer(APIView):
    def get(self, request, customerId):
        try:
            model = PersonalDetails.objects.get(id=customerId)
            serializer = PersonalDetailSerializer(model)
            if serializer.data is not None:
                return Response(serializer.data)
            else:
                return Response("NOt Found", status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"Record Not Found ; {e.__str__()}", status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, customerId):
        try:
            model = PersonalDetails.objects.get(id=customerId)
            serializer = PersonalDetailSerializer(model, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(f"Error :{e.__str__()}", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customerId):
        try:
            model = PersonalDetails.objects.get(id=customerId)
            model.delete()
            return Response("Record deleted", status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(f"Error: {e.__str__()}", status=status.HTTP_400_BAD_REQUEST)
