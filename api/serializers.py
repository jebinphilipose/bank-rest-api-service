from rest_framework import serializers
from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    bank = serializers.CharField(source='bank_id.bank_name', read_only=True)

    class Meta:
        model = Branch
        fields = '__all__'
