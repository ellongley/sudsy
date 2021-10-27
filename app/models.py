from django.db import models

# Create your models here.

class Claims(models.Model):
    date_val = models.DateField()
    calendar_year = models.DateField()
    calendar_month = models.DateField()
    calendar_day = models.DateField()
    day_of_week = models.DateField()
    is_weekday = models.IntegerField()
    is_workday = models.IntegerField()
    is_holiday = models.IntegerField()
    dim_claim_id = models.IntegerField()
    bin = models.IntegerField()
    drug = models.CharField(max_length=1)
    reject_code = models.CharField(max_length=1)
    pharmacy_claim_approved = models.IntegerField()
    dim_pa_id = models.IntegerField()
    correct_diagnosis = models.IntegerField()
    tried_and_failed = models.IntegerField()
    contraindication = models.IntegerField()
    pa_approved = models.IntegerField()
    dim_date_id = models.IntegerField()
