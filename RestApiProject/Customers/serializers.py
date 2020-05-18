from rest_framework import serializers
from .models import *


class PersonalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        # fields = ('FirstName', 'LastName', 'ContactNo', "DOB")
        fields = '__all__'
