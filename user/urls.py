from django.urls import path
from .api import views

urlpatterns = [
    path('location/', views.LocationListView.as_view(), name=None),
    path('location/create/', views.LocationCreateView.as_view(), name=None),
    path('location/<int:pk>/', views.LocationDetailView.as_view(), name=None),
    path('organization/', views.OrganizationListView.as_view(), name=None),
    path('organization/create/', views.OrganizationCreateView.as_view(), name=None),
    path('organization/<int:pk>/',
         views.OrganizationDetailView.as_view(), name=None),
    path('position/', views.PositionListView.as_view(), name=None),
    path('position/create/', views.PositionCreateView.as_view(), name=None),
    path('position/<int:pk>/', views.PositionDetailView.as_view(), name=None),
]
