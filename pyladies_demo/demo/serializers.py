from .models import Inventory
from rest_framework import serializers

class InventorySerializer(serializers.HyperlinkedModelSerializer):
	#hold on url
	url = serializers.HyperlinkedIdentityField(view_name='inventory-detail')
	class Meta: 
		model = Inventory
		fields = ('url','count', 'name', 'description', 'available')

class BasicInventorySerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='basic-detail')
	class Meta: 
		model = Inventory
		fields = ('url','count', 'name', 'description', 'available')

class ManageInventorySerializer(serializers.HyperlinkedModelSerializer):
	url = serializers.HyperlinkedIdentityField(view_name='manage-detail')
	class Meta: 
		model = Inventory
		fields = ('url','count', 'name', 'description', 'price', 'cost', 'available')
