from .models import cheese
from rest_framework import serializers

class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cheese
        fields= ('id','name','origin','type' )
