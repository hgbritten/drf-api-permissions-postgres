from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ClimbSerializer
from .models import Climb
from .permissions import IsAuthorOrReadOnly


class ClimbList(ListCreateAPIView):
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer


class ClimbDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Climb.objects.all()
    serializer_class = ClimbSerializer
