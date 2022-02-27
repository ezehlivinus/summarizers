from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from numpy import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from rest_framework import generics, views, status, viewsets

from summaries.models import DataModel
from . serializers import DataModelSerializer, ImportNewDataSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.
@api_view(['POST'])
def import_new_data(request):
  url = request.data.get('data_url')
  page = requests.get(url)
  
  data = {
    'content': page.text,
    'source': url
  }
  
  
  
  # text_list = page.text.splitlines()
  # description = '\n'.join(text_list[0:5])
  # body_and_header = text_list[5::]
  
  return Response({"message": "Hello, world!", 'data': page.text})

user_response = openapi.Response('response description', DataModelSerializer)
class DataModelView(viewsets.ViewSet):
  # serializer_class = ImportNewDataSerializer

  @swagger_auto_schema(
        request_body=ImportNewDataSerializer,
        responses={
            '201': user_response,
            '400': 'Invalid input or request',
            '200': openapi.Response('response description', DataModelSerializer)
        },
        security=[],
        operation_id='Create or Update',
        operation_description='''
        Import new data from Met Office.
        data_url is the url from Met Office after selecting region and parameters.
        example: https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/ranked/England_E_and_NE.txt
        
        Model is updated if it already exists. That is if you provide the same url again after using it previously.
        
        This would have been modelled further to include the region and parameters:
        {
          'region': 'E',
          'parameter': 'Sunshine'
          'content': '...' # is the summarised data from met office
        }
        
        ''',
    )
  def create(self, request):
    url = request.data.get('data_url')
    page = requests.get(url)
    
    if not url:
      return Response({'message': 'Please provide a url'}, status=status.HTTP_400_BAD_REQUEST)
    
    if page.status_code != 200 or page.text == '':
      return Response({"message": "Something failed"}, status=status.HTTP_400_BAD_REQUEST)
    
    data = {'content': page.text, 'source': url }
    
    serializer = DataModelSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    
    queryset = DataModel.objects.filter(source=url)

    if queryset.exists():
      serializer.update(queryset.first(), serializer.data)
      return Response(data=serializer.data, status=status.HTTP_200_OK)

    serializer.save()
    
    # text_list = page.text.splitlines()
    # description = '\n'.join(text_list[0:5])
    # body_and_header = text_list[5::]
    
    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
  
  @swagger_auto_schema(
      responses={
          '200': DataModelSerializer(many=True),
          '404': 'Not found'
      },
      security=[],
      operation_id='List',
      operation_description='List all data',
  )
  def list(self, request):
    # queryset = DataModel.objects.all()
    queryset = get_list_or_404(DataModel)
    serializer = DataModelSerializer(queryset, many=True)

    return Response(data=serializer.data)
  
  @swagger_auto_schema(
      responses={
          '200': DataModelSerializer,
          '404': 'Not found'
      },
      security=[],
      operation_id='retrieve',
      operation_description='retrieve data',
  )
  def retrieve(self, request, pk):
    queryset = get_object_or_404(DataModel, pk=pk)
    serializer = DataModelSerializer(queryset)
  
    return Response(data=serializer.data)

    
    