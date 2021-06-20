from rest_framework import serializers
from .models import Nhanvien
class NhanvienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nhanvien
