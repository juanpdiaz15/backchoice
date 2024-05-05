from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, BackEndFrameworkSerializer,    DimensionSerializer,    MetricSerializer,    EvaluationSerializer,    MeasurementScaleSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import BackEndFramework, Dimension, Metric, Evaluation, MeasurementScale
# Create your views here.
class BackEndFrameworkListCreate(generics.ListCreateAPIView):
    serializer_class = BackEndFrameworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BackEndFramework.objects

class BackEndFrameworkDelete(generics.DestroyAPIView):
    serializer_class = BackEndFrameworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BackEndFramework.objects
class DimensionListCreate(generics.ListCreateAPIView):
    serializer_class = DimensionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dimension.objects.all()

class DimensionDelete(generics.DestroyAPIView):
    serializer_class = DimensionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dimension.objects.all()

class MetricListCreate(generics.ListCreateAPIView):
    serializer_class = MetricSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Metric.objects.all()

class MetricDelete(generics.DestroyAPIView):
    serializer_class = MetricSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Metric.objects.all()

class EvaluationListCreate(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated]

    """def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)"""

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('metric__dimension')

class EvaluationDelete(generics.DestroyAPIView):
    serializer_class = EvaluationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Evaluation.objects.all()

class MeasurementScaleListCreate(generics.ListCreateAPIView):
    serializer_class = MeasurementScaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MeasurementScale.objects.all()

class MeasurementScaleDelete(generics.DestroyAPIView):
    serializer_class = MeasurementScaleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MeasurementScale.objects.all()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
"""class DimensionScoreView(generics.ListAPIView):
    def get(self, request, pk):
        framework = BackEndFramework.objects.get(pk=pk)
        dimension = request.query_params.get('dimension')
        score = framework.get_dimension_score(dimension)
        return Response({'score': score})"""