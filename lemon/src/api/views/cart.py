
from rest_framework import status, serializers, generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.response import Response

from ..models import Cart

from ..serializers import CartSerializer

#-------------------------
# API:
#
# /api/cart/menu-items - Customer - GET    - Returns current items in the cart for the current user token
# /api/cart/menu-items - Customer - POST   - Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items
# /api/cart/menu-items - Customer - DELETE - Deletes all menu items created by the current user token
#-------------------------
@permission_classes([IsAuthenticated])
class CartsView(generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post', 'delete']

    # fix UnorderedObjectListWarning
    queryset = Cart.objects.get_queryset()
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    # override for get & post
    def get_queryset(self):
        user = self.request.user

        # 'order_by' - fixes UnorderedObjectListWarning
        return Cart.objects.all().filter(user=user).order_by('id')

    def delete(self, request, *args, **kwargs):

        # delete all object in the cart for current user
        self.get_queryset().delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
