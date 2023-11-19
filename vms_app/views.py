from rest_framework import viewsets
from .models import AuctionVehicle, FuelingRecord, MaintenanceJob, User, Vehicle, FuelRequest, MaintRequest, Route, Driver
from .serializers import (AuctionVehicleSerializer, FuelingRecordSerializer, MaintenanceJobSerializer, UserSerializer, VehicleSerializer, FuelRequestSerializer,
                          MaintRequestSerializer, RouteSerializer, DriverSerializer)


from .models import Route



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class FuelRequestViewSet(viewsets.ModelViewSet):
    queryset = FuelRequest.objects.all()
    serializer_class = FuelRequestSerializer

class MaintRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintRequest.objects.all()
    serializer_class = MaintRequestSerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class AuctionVehicleViewSet(viewsets.ModelViewSet):
    queryset = AuctionVehicle.objects.all()
    serializer_class = AuctionVehicleSerializer

class MaintenanceJobViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceJob.objects.all()
    serializer_class = MaintenanceJobSerializer

class FuelingRecordViewSet(viewsets.ModelViewSet):
    queryset = FuelingRecord.objects.all()
    serializer_class = FuelingRecordSerializer

