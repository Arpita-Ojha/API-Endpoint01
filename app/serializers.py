from rest_framework import serializers
from .models import Bts

class BtsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bts
        fields = '__all__'