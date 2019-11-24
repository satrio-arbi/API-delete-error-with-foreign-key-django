from django.db import models

# Create your models here.


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_code = models.CharField(max_length=3)
    location_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.location_code


class Organization(models.Model):
    organization_id = models.AutoField(primary_key=True)
    organization_code = models.CharField(max_length=10)
    organization_name = models.CharField(max_length=200)
    location_id = models.ForeignKey(
        Location, related_name='organization_location', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.organization_code


class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_code = models.CharField(max_length=20)
    position_name = models.CharField(max_length=50)
    organization_id = models.ForeignKey(
        Organization, related_name='Positon_on_Organization', on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.position_code
