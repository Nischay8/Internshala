from django.db.models import fields
from django.db.models.base import Model
from .models import Student
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'