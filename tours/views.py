from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tour
from .serializers import TourSerializer
from django.shortcuts import get_object_or_404

class TourListView(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        queryset = Tour.objects.all()
        place = self.request.query_params.get('place')
        if place:
            queryset = queryset.filter(place__icontains=place)
        # Add more filtering criteria as needed
        return queryset

class TourDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

@api_view(['GET'])
def tour_detail(request, pk):
    try:
        tour = get_object_or_404(Tour, pk=pk)
        serializer = TourSerializer(tour)
        return Response(serializer.data)
    except Tour.DoesNotExist:
        return Response(status=404)
