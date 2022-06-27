from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('hero', viewsets.HeroViewSet)
router.register('power', viewsets.PowerSerializer)

urlpatterns = router.urls
