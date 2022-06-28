from .models import User

from rest_framework.serializers import ModelSerializer


class NinjaSerializer(ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            grade=validated_data['grade'],
            ability=validated_data['ability'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['name', 'grade', 'ability', 'password']
