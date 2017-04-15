from rest_framework import serializers
from .models import DIM_GST

class DIM_GSTSerializer(serializers.ModelSerializer):
	class Meta:
		model=DIM_GST