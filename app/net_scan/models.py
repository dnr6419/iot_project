from django.db import models

# Create your models here.
class scan_result(models.Model):
    ip = models.CharField(max_length= 30)
    port = models.IntegerField()
    description = models.TextField()
    #cdate = models.TextField()
    cdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return [self.ip ,self.port, self.description,self.cdate]
        
class t_r(models.Model):
    ip = models.CharField(max_length= 30)
    port = models.CharField(max_length= 100)
    device = models.CharField(max_length= 30)
    cdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return [self.ip ,self.port, self.device]

class s_r(models.Model):
    setting_ip_band = models.CharField(max_length= 30)
    setting_port_band = models.CharField(max_length= 30)
    setting_option = models.CharField(max_length= 30)
    def __str__(self):
        return [self.setting_ip_band ,self.setting_port_band, self.setting_option]
    