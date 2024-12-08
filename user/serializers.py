from rest_framework import serializers
from user.models import User
from user.validators import PasswordValidator, EmailDomainValidator


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        validators=[PasswordValidator()]
    )
    email = serializers.EmailField(
        validators=[EmailDomainValidator()]
    )

    class Meta:
        model = User
        fields = '__all__'


