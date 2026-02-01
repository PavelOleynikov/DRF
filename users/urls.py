from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import PaymentsViewSet

app_name = "users"

router = DefaultRouter()
router.register(r"payments", PaymentsViewSet, basename="payments")

urlpatterns = [
    path('', include(router.urls)),
]
