from django.contrib.auth.models import User
from rest_framework import serializers
from .models import BackEndFramework, Dimension, Metric, Evaluation, MeasurementScale


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class BackEndFrameworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackEndFramework
        fields = ['id', 'name', 'description']

class DimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dimension
        fields = ['id', 'name', 'description','weight']

class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ['id', 'name', 'description', 'dimension']

class EvaluationSerializer(serializers.ModelSerializer):
    framework = serializers.SlugRelatedField(slug_field='name', queryset=BackEndFramework.objects.all())
    metric = serializers.SlugRelatedField(slug_field='name', queryset=Metric.objects.all())
    dimension_name = serializers.CharField(source='Metric.dimension.name', read_only=True)

    class Meta:
        model = Evaluation
        fields = ['id', 'score', 'framework', 'metric', 'dimension_name']
        
    

class MeasurementScaleSerializer(serializers.ModelSerializer):
    framework = serializers.SlugRelatedField(slug_field='name', queryset=BackEndFramework.objects.all())
    metric = serializers.SlugRelatedField(slug_field='name', queryset=Metric.objects.all())
    class Meta:
        model = MeasurementScale
        fields = ['id', 'scale', 'metric', 'framework']