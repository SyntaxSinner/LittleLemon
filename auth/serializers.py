from djoser.serializers import UserCreateSerializer, BaseCreateUserSerializer

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')

class UserDeleteSerializer(BaseCreateUserSerializer):
    class Meta(BaseCreateUserSerializer.Meta):
        fields = ('id', 'email', 'username', 'password', 'first_name', 'last_name')