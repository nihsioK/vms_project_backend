from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (AuctionVehicleViewSet, FuelingRecordViewSet, MaintenanceJobViewSet, UserViewSet, VehicleViewSet, FuelRequestViewSet,
                    MaintRequestViewSet, RouteViewSet, DriverViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'fuelrequests', FuelRequestViewSet)
router.register(r'maintrequests', MaintRequestViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'auctionvehicles', AuctionVehicleViewSet)
router.register(r'maintenancejobs', MaintenanceJobViewSet)
router.register(r'fuelingrecords', FuelingRecordViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
