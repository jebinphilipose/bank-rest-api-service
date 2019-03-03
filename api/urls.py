from django.urls import path
from .views import DetailBranchView

urlpatterns = [
    path('branch/<slug:ifsc>/', DetailBranchView.as_view(), name="branch-detail-api"),
]
