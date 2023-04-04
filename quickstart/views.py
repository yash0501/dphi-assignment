from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Users, HackathonOrganizers, Hackathons, HackathonRegistry, HackathonSubmissions
from .serializers import ItemSerializer, UsersSerializer, HackathonOrganizersSerializer, HackathonsSerializer, HackathonRegistrySerializer, HackathonSubmissionsSerializer

# Create your views here.
# @api_view(['GET'])
# def get_data(request):
#     # person = {'name': "Yash Garg", 'age': 22}
#     items = Item.objects.all()
#     serializer = ItemSerializer(items, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def post_data(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['POST'])
def add_user(request):
    if Users.objects.filter(email=request.data['email']).exists():
        return Response("User already exists")
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# {
# "name":"Yash",
# "email": "abc@abc.com",
# "password":"1234"
# }

@api_view(['POST'])
def add_hackathon_organizer(request):
    if HackathonOrganizers.objects.filter(email=request.data['email']).exists():
        return Response("User already exists")
    serializer = HackathonOrganizersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def add_hackathon(request):
    if Hackathons.objects.filter(name=request.data['name']).exists():
        return Response("Hackathon already exists")
    serializer = HackathonsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_hackathons(request):
    hackathons = Hackathons.objects.all()
    serializer = HackathonsSerializer(hackathons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register_for_hackathon(request):
    if not Hackathons.objects.filter(id=request.data['hackathon']).exists():
        return Response("Hackathon does not exist")
    if HackathonRegistry.objects.filter(user=request.data['user'], hackathon=request.data['hackathon']).exists():
        return Response("User already registered")
    serializer = HackathonRegistrySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_registered_hackathons(request):
    hackathon_registry = HackathonRegistry.objects.filter(user=request.data['user'])
    serializer = HackathonRegistrySerializer(hackathon_registry, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def submit_hackathon(request):
    if not Hackathons.objects.filter(id=request.data['hackathon']).exists():
        return Response("Hackathon does not exist")
    if not HackathonRegistry.objects.filter(user=request.data['user'], hackathon=request.data['hackathon']).exists():
        return Response("User not registered")
    serializer = HackathonSubmissionsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_submissions(request):
    hackathon_submissions = HackathonSubmissions.objects.filter(user=request.data['user'])
    serializer = HackathonSubmissionsSerializer(hackathon_submissions, many=True)
    return Response(serializer.data)