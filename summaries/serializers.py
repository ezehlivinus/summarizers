from dataclasses import fields
from numpy import source
from rest_framework import serializers

from . models import DataModel

class DataModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = DataModel
    fields = ['id', 'content', 'created_at', 'updated_at']
    
class ImportNewDataSerializer(serializers.Serializer):
  data_url = serializers.CharField(max_length=400)
   
  def create(self, validated_data):
    source = validated_data.get('source')
    content = validated_data.get(content)
    
    data_model = DataModel(content=content, source=source)
    data_model.save()
    
    return data_model
    