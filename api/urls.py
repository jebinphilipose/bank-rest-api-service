from django.urls import path
from .views import BranchDetailView, BankBranchesView

urlpatterns = [
    path('branch/<slug:ifsc>/', BranchDetailView.as_view(), name="branch-detail-api"),
    path('bank/<slug:bank>/city/<slug:city>/', BankBranchesView.as_view(), name="bank-branches-api"),
]
