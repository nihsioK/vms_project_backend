from rest_framework import viewsets
from .models import AuctionVehicle, FuelingRecord, MaintenanceJob, User, Vehicle, FuelRequest, MaintRequest, Route, Driver
from .serializers import (AuctionVehicleSerializer, FuelingRecordSerializer, MaintenanceJobSerializer, UserSerializer, VehicleSerializer, FuelRequestSerializer,
                          MaintRequestSerializer, RouteSerializer, DriverSerializer)


from .models import Route
from rest_framework.permissions import IsAuthenticated
from .permissions import IsDriver


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_context(self):
        context = super(UserViewSet, self).get_serializer_context()
        context.update({"request": self.request})
        return context

class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class FuelRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FuelRequest.objects.all()
    serializer_class = FuelRequestSerializer

class MaintRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MaintRequest.objects.all()
    serializer_class = MaintRequestSerializer


class DriverViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class AuctionVehicleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = AuctionVehicle.objects.all()
    serializer_class = AuctionVehicleSerializer

class MaintenanceJobViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MaintenanceJob.objects.all()
    serializer_class = MaintenanceJobSerializer

class FuelingRecordViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FuelingRecord.objects.all()
    serializer_class = FuelingRecordSerializer

