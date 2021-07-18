from django.db import models

# Create your models here.


class CountryList(models.Model):
    name =  models.CharField(max_length=256)
    code = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "CountryList"


class StateList(models.Model):
    country = models.ForeignKey(CountryList, on_delete=models.CASCADE, related_name="country")
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "StateList"

class DistrictList(models.Model):

    state = models.ForeignKey(StateList, on_delete=models.CASCADE, related_name="state")
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "DistrictList"


class CityList(models.Model):
    
    distict = models.ForeignKey(DistrictList, on_delete=models.CASCADE, related_name="district")
    name = models.CharField(max_length=256)
    zip = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "CityList"

class Programming(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    programming = models.ForeignKey(Programming,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
