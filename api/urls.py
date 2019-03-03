from django.urls import path
from . import views
from .views import BranchDetailView, BankBranchesView

urlpatterns = [
    path('', views.index, name="index"),
    path('api/v1/branch/<slug:ifsc>/', BranchDetailView.as_view(), name="branch-detail-api"),
    path('api/v1/bank/<slug:bank>/city/<slug:city>/', BankBranchesView.as_view(), name="bank-branches-api"),
]
