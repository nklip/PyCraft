# api/user_groups.py in lemon app
import json

from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, serializers, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.views import APIView

from ..serializers import UserSerializer

def access_denied():
    return HttpResponseForbidden("Access denied. You are not a manager")

def add_to_group(the_group, request):
    # try to find a user by pk
    userToAdd = User.objects.filter(username=request.data.get('username'))
    if not userToAdd.count():
        return HttpResponseNotFound("User not found!")
    # get the actual user
    userToAdd = userToAdd.first()
    # get the group
    group = Group.objects.get(name=the_group)
    # add the user to the group
    userToAdd.groups.add(group)
    return Response("Success. User added in the '" + the_group + "' group.", status=status.HTTP_201_CREATED)

def remove_from_group(the_group, **kwargs):
    # try to find a user by pk
    userToDelete = User.objects.filter(pk=kwargs.get('pk'))
    if not userToDelete.count():
        return HttpResponseNotFound("User not found!")
    # confirm that the user is a delivery person
    userToDelete = userToDelete.filter(groups__name__in=[the_group])
    if not userToDelete.count():
        return HttpResponseNotFound("User is not from " + the_group)
    # get the actual user
    userToDelete = userToDelete.first()
    # get the the group
    group = Group.objects.get(name=the_group)
    # remove the user from the group
    userToDelete.groups.remove(group)
    return Response("Success. User removed from the '" + the_group + "' group.", status=status.HTTP_200_OK)

#-------------------------
# API:
#
# /api/groups/manager/users                - Manager - GET    - Returns all managers
# /api/groups/manager/users                - Manager - POST   - Assigns the user in the payload to the manager group and returns 201-Created
# /api/groups/manager/users/{userId}       - Manager - DELETE - Removes this particular user from the manager group and returns 200 – Success if everything is okay. If the user is not found, returns 404 – Not found
# /api/groups/delivery-crew/users          - Manager - GET    - Returns all delivery crew
# /api/groups/delivery-crew/users          - Manager - POST   - Assigns the user in the payload to delivery crew group and returns 201-Created HTTP
# /api/groups/delivery-crew/users/{userId} - Manager - DELETE - Removes this user from the delivery group and returns 200 – Success if everything is okay. If the user is not found, returns  404 – Not found
#-------------------------
@permission_classes([IsAuthenticated])
class ManagersView(generics.CreateAPIView, generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post']
    queryset = User.objects.all().filter(groups__name__in=['Manager']).order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def get(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().get(request, *args, **kwargs)
        else:
            return access_denied()

    def post(self, request, *args, **kwargs):
        # only a manager can do it
        if (request.user.groups.filter(name='Manager')).exists():
            return add_to_group('Manager', request)
        else:
            return access_denied()

@permission_classes([IsAuthenticated])
class ManagerView(generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['delete']
    queryset = User.objects.all().filter(groups__name__in=['Manager']).order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def delete(self, request, *args, **kwargs):
        # only manager can do it
        if (request.user.groups.filter(name='Manager')).exists():
            return remove_from_group('Manager', **kwargs)
        else:
            return access_denied()

@permission_classes([IsAuthenticated])
class DeliveryCrewView(generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post']
    queryset = User.objects.all().filter(groups__name__in=['DeliveryCrew']).order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def get(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().get(request, *args, **kwargs)
        else:
            return access_denied()

    def post(self, request, *args, **kwargs):
        # only a manager can do it
        if (request.user.groups.filter(name='Manager')).exists():
            return add_to_group('DeliveryCrew', request)
        else:
            return access_denied()

@permission_classes([IsAuthenticated])
class DeliveryPersonView(generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['delete']
    queryset = User.objects.all().filter(groups__name__in=['DeliveryCrew']).order_by('id')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def delete(self, request, *args, **kwargs):
        # only manager can do it
        if (request.user.groups.filter(name='Manager')).exists():
            return remove_from_group('DeliveryCrew', **kwargs)
        else:
            return access_denied()