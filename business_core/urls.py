from rest_framework import routers
from business_core import views

app_name='business_app'

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='customer')
router.register(r'room', views.RoomViewSet, basename='room')
router.register(r'event', views.EventViewSet, basename='event')
router.register(r'booking', views.BookingViewSet, basename='booking')

urlpatterns = router.urls