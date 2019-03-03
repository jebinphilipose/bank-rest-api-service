from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Branch
from .serializers import BranchSerializer


# Create your views here.
class DetailBranchView(generics.RetrieveAPIView):
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
