from rest_framework import serializers
from .models import Item, Users, HackathonOrganizers, Hackathons, HackathonRegistry, HackathonSubmissions

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class HackathonOrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonOrganizers
        fields = '__all__'

class HackathonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathons
        fields = '__all__'

class HackathonRegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonRegistry
        fields = '__all__'

class HackathonSubmissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HackathonSubmissions
        fields = '__all__'