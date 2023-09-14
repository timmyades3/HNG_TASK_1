from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            'id',
            'name', 
            ]
    def validate_field(self, value):
        if not isinstance(value, str):
            raise serializers.ValidationError("Field should be a string.")
        return value