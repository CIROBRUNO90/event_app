from rest_framework import routers
from business_core import views

app_name='business_app'

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet, basename='professor')
router.register(r'room', views.RoomViewSet, basename='subject')
router.register(r'event', views.EventViewSet, basename='textbook')
router.register(r'booking', views.BookingViewSet, basename='textbook')

urlpatterns = router.urls