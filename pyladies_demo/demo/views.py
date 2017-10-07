# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import Http404

# DRF imports



# Create your views here.

# DRF views
from .models import Inventory
from .serializers import InventorySerializer 
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
class InventoryViewSet(viewsets.ViewSet):
	def list(self, request):
		#consider filter
		queryset = Inventory.objects.all()
		serializer = InventorySerializer(queryset, many=True, context={'request':request})
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Inventory.objects.all()
		item = get_object_or_404(queryset, pk=pk)
		serializer = InventorySerializer(item, context={'request':request})
		return Response(serializer.data)
		

from .serializers import BasicInventorySerializer
class BasicInventoryViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Inventory.objects.all().order_by('name')
	serializer_class = BasicInventorySerializer


from .serializers import ManageInventorySerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes
@permission_classes((IsAdminUser, ))
class ManageInventoryViewSet(viewsets.ModelViewSet):
	queryset = Inventory.objects.all().order_by('name')
	serializer_class = ManageInventorySerializer

	def destroy(self, request, pk=None):
		return Response({'details': 'Forbidden'}, status=403)


