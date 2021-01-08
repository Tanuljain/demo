from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import CursorPagination
from .models import TaskModel
from .serializers import TaskModelSerializer


class Pagination(CursorPagination):
    page_size = 5
    ordering = '-updated_time'


class LCTaskAPI(ListCreateAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'desc']
    pagination_class = Pagination


class RUDTaskAPI(RetrieveUpdateDestroyAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer
