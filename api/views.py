from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Branch, Bank
from .serializers import BranchSerializer


# Create your views here.
class BranchDetailView(generics.RetrieveAPIView):
    """
    GET branch/<ifsc>/
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self, request, *args, **kwargs):
        try:
            branch = self.queryset.get(ifsc=kwargs["ifsc"])
            return Response(BranchSerializer(branch).data)
        except Branch.DoesNotExist:
            return Response(
                data={
                    "message": "Branch with IFSC({}) does not exist".format(kwargs["ifsc"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BankBranchesView(generics.ListAPIView):
    """
    GET bank/<bank-name>/city/<city>
    """
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def get(self, request, *args, **kwargs):
        try:
            bn = kwargs["bank"].replace("-", " ")
            cty = kwargs["city"]
            try:
                bank = Bank.objects.get(bank_name__icontains=bn)
            except Bank.DoesNotExist:
                return Response(
                    data={
                        "message": "Bank({}) does not exist".format(bn)
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            branches = self.queryset.filter(bank_id=bank.pk, city__icontains=cty)
            print(branches.first().ifsc)
            return Response(BranchSerializer(branches, many=True).data)
        except AttributeError:
            return Response(
                data={
                    "message": "No Branch exist for that City({})".format(cty)
                },
                status=status.HTTP_404_NOT_FOUND
            )
