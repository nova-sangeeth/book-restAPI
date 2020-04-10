from rest_framework import routers
from api import viewsets

router = routers.DefaultRouter()
router.register(r'book_store', viewsets.book_store_viewset)
