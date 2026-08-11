from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from ..models import Booking

from ..serializers import BookingSerializer

#-------------------------
# API:
#
# /api/bookings - Customer - GET    - Returns bookings.
# /api/bookings - Customer - POST   - Adds a new booking.
#-------------------------
@permission_classes([IsAuthenticated])
class BookingsView(generics.CreateAPIView, generics.ListAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'post']

    # fix UnorderedObjectListWarning
    queryset = Booking.objects.get_queryset().order_by('reservation_date', 'reservation_time', 'id')
    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]
    ordering_fields = ['reservation_date', 'reservation_time']

#-------------------------
# API:
#
# /api/bookings/1 - Customer - GET    - Returns a single booking.
# /api/bookings/1 - Customer - DELETE - Deletes a single booking.
#-------------------------
@permission_classes([IsAuthenticated])
class BookingView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # limit HTTP methods
    http_method_names = ['get', 'delete']

    serializer_class = BookingSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication,]

    def get_queryset(self):
        return Booking.objects.all().filter(pk=self.kwargs['pk'])

