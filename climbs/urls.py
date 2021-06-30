from django.urls import path
from .views import ClimbList, ClimbDetail

urlpatterns = [
    path("", ClimbList.as_view(), name="climb_list"),
    path("<int:pk>/", ClimbDetail.as_view(), name="climb_detail"),
]
