from rest_framework import routers

from .views import RestaurantViewSet, EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"restaurants", RestaurantViewSet)
router.register(r"employees", EmployeeViewSet)

urlpatterns = router.urls
