from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('email', 'password', 'first_name', 'last_name', 'qualification', 'mobile_no', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Teacher.objects.create_user(**validated_data)
        return user

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('email', 'password', 'first_name', 'last_name', 'qualification', 'mobile_no', 'address', 'interested_categories')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Student.objects.create_user(**validated_data)
        return user