from rest_framework import serializers

from .models import book_store


class book_store_serializers(serializers.ModelSerializer):
    class Meta:
        model = book_store
        fields = '__all__'
        # exclude = ('added_by')
