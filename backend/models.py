from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class EmployeeRecord(models.Model):
    employee_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class RecordClassification(models.Model):
    classification = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.classification

class HRRecord(models.Model):
    employee = models.ForeignKey(EmployeeRecord, on_delete=models.CASCADE)
    classification = models.ForeignKey(RecordClassification, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class AuditLog(models.Model):
    action = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)

class RetentionSchedule(models.Model):
    record_classification = models.ForeignKey(RecordClassification, on_delete=models.CASCADE)
    retention_period_in_years = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.record_classification} - {self.retention_period_in_years} years'