from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import permissions

class ContactViewsList(viewsets.ReadOnlyModelViewSet):
    serializer_class = ContactSerializerList
    queryset = Contact.objects.all()

class ContactViewsPost(viewsets.ModelViewSet):
    serializer_class = ContactSerializerList
    queryset = Contact.objects.all()


class JobsViewsList(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobsSerializerList
    queryset = Jobs.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('jobcategory', 'jobtype',)
    

class JobsViewsPost(viewsets.ModelViewSet):
    serializer_class = JobsSerializerPost
    queryset = Jobs.objects.all()

class DropMailViewsList(viewsets.ModelViewSet):
    serializer_class = DropMailSerializerList
    queryset = DropMail.objects.all()

class JobCategoryViewsList(viewsets.ModelViewSet):
    serializer_class = JobCategorySerializerList
    queryset = JobCategory.objects.all()


class JobTypeViewsList(viewsets.ModelViewSet):
    serializer_class = JobTypeSerializerList
    queryset = JobType.objects.all()


#class SosialLinkViewsList(viewsets.ModelViewSet):
 #   serializer_class = SosialLinkSerializerList
  #  queryset = SosialLink.objects.all()


