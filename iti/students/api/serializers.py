from rest_framework import serializers
from students.models import Student


class StudentSerlizer(serializers.ModelSerializer):
    track_name = serializers.StringRelatedField(source="track", read_only=True)
    class Meta:
        model = Student
        fields = ("name", "grade", "email", "track", "track_name")

        fields = '__all__'