from django.urls import path
from .views import CreateDesignationAPIView, ListDesignationAPIView

urlpatterns = [
    path('create/', CreateDesignationAPIView.as_view(), name='create-designation'),
    path('list/', ListDesignationAPIView.as_view(), name='list-designation'),
]
