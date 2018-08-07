from restaurants.models import Restaurant
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    RestaurantListSerializer,
    RestaurantDetailSerializer,
    RestaurantCreateUpdateSerializer,
)

class ArticleCreateView(CreateAPIView):
    serializer_class = ArticleCreateSerializer

class RestaurantListView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer


class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


# Complete Me
class RestaurantCreateView():


class RestaurantUpdateView(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'


class RestaurantDeleteView(DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'restaurant_id'

class UpdateView(RetrieveUpdateAPIView):
    queryset = ModelName.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'