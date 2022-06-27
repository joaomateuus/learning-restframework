from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('hero', viewsets.HeroViewSet)

urlpatterns = router.urls
