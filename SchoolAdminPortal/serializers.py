from rest_framework import serializers
from .models import Students, Courses


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        return Students.objects.create(**validated_data)


class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        return Courses.objects.create(**validated_data)