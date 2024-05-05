from django.urls import path
from . import views

urlpatterns = [
    path('backendframeworks/', views.BackEndFrameworkListCreate.as_view(), name='backendframework-list-create'),
    path('backendframeworks/<int:pk>/', views.BackEndFrameworkDelete.as_view(), name='backendframework-delete'),
    #path('frameworks/<int:pk>/dimension-score/', views.DimensionScoreView.as_view(), name='dimension-score'),


    path('dimensions/', views.DimensionListCreate.as_view(), name='dimension-list-create'),
    path('dimensions/<int:pk>/', views.DimensionDelete.as_view(), name='dimension-delete'),

    path('metrics/', views.MetricListCreate.as_view(), name='metric-list-create'),
    path('metrics/<int:pk>/', views.MetricDelete.as_view(), name='metric-delete'),

    path('evaluations/', views.EvaluationListCreate.as_view(), name='evaluation-list-create'),
    path('evaluations/<int:pk>/', views.EvaluationDelete.as_view(), name='evaluation-delete'),

    path('measurementscales/', views.MeasurementScaleListCreate.as_view(), name='measurementscale-list-create'),
    path('measurementscales/<int:pk>/', views.MeasurementScaleDelete.as_view(), name='measurementscale-delete'),
]
