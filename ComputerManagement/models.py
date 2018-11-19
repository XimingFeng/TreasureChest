from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from Root import models as RootModels

class Computer(models.Model):
    computer_name = models.CharField(max_length=50)
    last_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(RootModels.Location,on_delete=models.CASCADE, null=True, blank=True)
    network_setting = models.ManyToManyField(RootModels.NetworkSetting, through='ComputerNetworkSetting')
    system_setting = models.ManyToManyField(RootModels.SystemSetting, through='ComputerSystemSetting')
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)
    def __str__(self):
        return self.computer_name

class ComputerNetworkSetting(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    network_setting = models.ForeignKey(RootModels.NetworkSetting, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)

class ComputerSystemSetting(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    system_setting = models.ForeignKey(RootModels.SystemSetting, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)