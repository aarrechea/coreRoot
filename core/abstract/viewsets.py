""" --- Imports --- """
from rest_framework import viewsets
from rest_framework import filters


""" --- Abstract viewset --- """
class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']


