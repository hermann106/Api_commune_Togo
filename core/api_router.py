
from rest_framework.routers import DefaultRouter
from composition.viewsets import RegionViewSet, PrefectureViewSet, CommuneViewSet, CantonViewSet, VillageViewSet, QuartierViewSet 
from dirigeant.viewsets import LeaderViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'regions', RegionViewSet)
router.register(r'prefectures', PrefectureViewSet)
router.register(r'Communes', CommuneViewSet)
router.register(r'Cantons', CantonViewSet)
router.register(r'villages', VillageViewSet)
router.register(r'quartier', QuartierViewSet)
router.register(r'dirigeant', LeaderViewSet)