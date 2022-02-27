from django.db import models

class RecentDownload(models.Model):
    LastDownload = models.FloatField(blank = False)
    created_at = models.DateTimeField(auto_now_add = True)

class ShadowClient(models.Model):
    firstname = models.CharField(max_length = 100,blank = True)
    lastname = models.CharField(max_length = 100,blank = True)
    email = models.EmailField(max_length = 100,blank = True)
    phone = models.IntegerField(blank=False)
    NationalInsuranceId = models.IntegerField(blank=True,null = True)
    is_agreed = models.BooleanField(default = False)
    is_shadow = models.BooleanField(default = True)

    def __str__(self):
        return str(self.firstname)
