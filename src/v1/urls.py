# from rest_framework import routers
from rest_framework_nested import routers
from django.conf.urls import url, include
from .views.book import BookViewSet, BookReserveViewSet
from .views.client import ClientViewSet, ClientReserveViewSet
from .views.interest import InterestViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'client', ClientViewSet)
router.register(r'book', BookViewSet)
router.register(r'interest', InterestViewSet)

book_reserve_router = routers.NestedSimpleRouter(router, r'book', lookup='book')
book_reserve_router.register(r'reserve', BookReserveViewSet)
client_reserve_router = routers.NestedSimpleRouter(router, r'client', lookup='client')
client_reserve_router.register(r'book', ClientReserveViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(book_reserve_router.urls)),
    url(r'^', include(client_reserve_router.urls)),
]
