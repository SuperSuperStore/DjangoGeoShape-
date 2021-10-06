# We'll use a different serializer and keep our main UserSerializer
# purely for the purposes of sending back populated users for profiles, etc.
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
# TODO from sprints.serializers import PopulatedSprintSerializer


User = get_user_model()

class PopulatedUserSerializer(ModelSerializer):
    pass

    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'dark_mode', 'created_sprints', 'city')