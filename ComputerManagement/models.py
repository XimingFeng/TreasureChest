from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Computer(models.Model):
    computer_name = models.CharField(max_length=50)
    last_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True, blank=True)
    network_setting = models.ManyToManyField('NetworkSetting', through='ComputerNetworkSetting')
    system_setting = models.ManyToManyField('SystemSetting', through='ComputerSystemSetting')
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):
        return self.computer_name