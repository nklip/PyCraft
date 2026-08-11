# api/menu_items.py in lemon app
from django.http import HttpResponseForbidden

from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


from ..models import Meal
from ..serializers import MealSerializer

# Create your API here.

#-----------------------------
# Function-based views
#-----------------------------
# @api_view(['GET'])
# def meals(request):
#     meals = Meal.objects.all().values();
#     return Response(
#         meals,
#         status=status.HTTP_200_OK
#     )
def access_denied():
    return HttpResponseForbidden("Access denied. You are not a manager")

#-----------------------------
# API:
#
# /api/menu-items - Customer, Delivery crew - GET                      - Lists all menu items. Return a 200 – Ok HTTP status code
# /api/menu-items - Customer, Delivery crew - POST, PUT, PATCH, DELETE - Denies access and returns 403 – Unauthorized HTTP status code
# /api/menu-items - Manager                 - GET                      - Lists all menu items
# /api/menu-items - Manager                 - POST                     - Creates a new menu item and returns 201 - Created
# /api/menu-items/{menuItem} - Customer, Delivery crew - GET                 - Lists single menu item
# /api/menu-items/{menuItem} - Customer, Delivery crew - PUT, PATCH, DELETE  - Returns 403 - Unauthorized
# /api/menu-items/{menuItem} - Manager                 - GET                 - Lists single menu item
# /api/menu-items/{menuItem} - Manager                 - PUT, PATCH          - Updates single menu item
# /api/menu-items/{menuItem} - Manager                 - DELETE              - Deletes menu item
#-----------------------------

@permission_classes([IsAuthenticated])
class MealsView(generics.CreateAPIView, generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'put', 'post', 'patch', 'delete']
    # fix UnorderedObjectListWarning
    queryset = Meal.objects.get_queryset().order_by('id', 'price')
    serializer_class = MealSerializer
    # specifies used authentication classes
    authentication_classes = [TokenAuthentication, SessionAuthentication,]
    # searching
    search_fields = ['name', 'desc']
    # ordering
    ordering_fields = ['id', 'price']

    def put(self, request, *args, **kwargs):
        return access_denied()

    def post(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return self.create(request, *args, **kwargs)
        else:
            return access_denied()

    def patch(self, request, *args, **kwargs):
        return access_denied()

    def delete(self, request, *args, **kwargs):
        return access_denied()

@permission_classes([IsAuthenticated])
class MealView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'put', 'patch', 'delete']
    # fix UnorderedObjectListWarning
    queryset = Meal.objects.get_queryset().order_by('id', 'price')
    serializer_class = MealSerializer
    # specifies used authentication classes
    authentication_classes = [TokenAuthentication, SessionAuthentication,]
    # searching
    search_fields = ['name', 'desc']
    # ordering
    ordering_fields = ['id', 'price']

    def put(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().put(request, *args, **kwargs)
        else:
            return access_denied()

    def patch(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().patch(request, *args, **kwargs)
        else:
            return access_denied()

    def delete(self, request, *args, **kwargs):
        if (request.user.groups.filter(name='Manager')).exists():
            return super().delete(request, *args, **kwargs)
        else:
            return access_denied()
    # def get(self, request, pk):
    #     try:
    #         item = Meal.objects.get(pk=pk);
    #     except Meal.DoesNotExist:
    #         print("Meal object doesn't exist for pk = {}".format(pk))
    #         item = ""
    #     serializer = MealSerializer(item, many=False)
    #     return Response(
    #         {"meal": serializer.data },
    #         status=status.HTTP_200_OK
    #     )