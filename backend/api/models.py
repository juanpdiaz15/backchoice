from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class BackEndFramework(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    """def get_dimension_score(self, dimension):
        evaluations = Evaluation.objects.filter(framework=self)
        metric_scores = []
        for evaluation in evaluations:
            if evaluation.metric.dimension == dimension:
                metric_scores.append(evaluation.score)
        if metric_scores:
            return sum(metric_scores) / len(metric_scores)
        else:
            return 0"""
    
    def __str__(self):
        return self.name

class Dimension(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    weight = models.FloatField(null=True)
    
    def __str__(self):
        return self.name

class Metric(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    score = models.FloatField()
    comentario = models.TextField()
    framework = models.ForeignKey(BackEndFramework, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)

class MeasurementScale(models.Model):
    SCALE_CHOICES = (
        (0, '0'),
        (0.5, '0.5'),
        (1, '1'),
    )
    metric = models.OneToOneField(Metric, on_delete=models.CASCADE, null=True)
    scale = models.FloatField(
        choices=SCALE_CHOICES,
        validators=[MinValueValidator(0), MaxValueValidator(0.5)]
    )
    framework = models.ForeignKey(BackEndFramework, on_delete=models.CASCADE, null=True)
    
    

