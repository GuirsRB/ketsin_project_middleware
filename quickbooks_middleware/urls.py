from django.urls import re_path, include
from rest_framework import routers

from quickbooks_middleware import views

router = routers.DefaultRouter(trailing_slash=False)
router.root_view_name = 'quickbooks_middleware'
router.register(r'', views.Order,basename="order")

urlpatterns = [
    re_path(r'^order/', include((router.urls,'quickbooks_middleware'),namespace='order')),
]