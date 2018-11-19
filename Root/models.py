from django.db import models
from datetime import datetime

class NetworkSetting(models.Model):
    is_DHCP = models.BooleanField(default=True)
    domain = models.CharField(max_length=20)
    IPv4_addr1 = models.PositiveSmallIntegerField(default=0)
    IPv4_addr2 = models.PositiveSmallIntegerField(default=0)
    IPv4_addr3 = models.PositiveSmallIntegerField(default=0)
    IPv4_addr4 = models.PositiveSmallIntegerField(default=0)
    subnet_mask1 = models.PositiveSmallIntegerField(default=255)
    subnet_mask2 = models.PositiveSmallIntegerField(default=255)
    subnet_mask3 = models.PositiveSmallIntegerField(default=255)
    subnet_mask4 = models.PositiveSmallIntegerField(default=0)
    DNS_addr1 = models.PositiveSmallIntegerField(default=0)
    DNS_addr2 = models.PositiveSmallIntegerField(default=0)
    DNS_addr3 = models.PositiveSmallIntegerField(default=0)
    DNS_addr4 = models.PositiveSmallIntegerField(default=0)
    mac_address = models.CharField(max_length=50)
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)

    def __str__(self):
        IPStatus = "DHCP IP Address: "
        if self.is_DHCP is False:
            IPStatus = "Static IP Address: "
        return IPStatus + str(self.IPv4_addr1) + "." + str(self.IPv4_addr2) \
               + "." + str(self.IPv4_addr3) + "." + str(self.IPv4_addr4) + "\n Subnet Mask:" \
               + str(self.subnet_mask1) + "." +  str(self.subnet_mask2) + "." + str(self.subnet_mask3) \
               + "." +  str(self.subnet_mask4) + "\n DNS Server " + str(self.DNS_addr1) + "." + \
               str(self.DNS_addr2) + "." + str(self.DNS_addr3) + "." + str(self.DNS_addr4) \
               + "\n Mac Address: " + self.mac_address + "\n domain: " + self.domain


class SystemSetting(models.Model):
    memory_mb = models.PositiveSmallIntegerField()
    CPU_model = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    machine_model = models.CharField(max_length=50)
    service_tag = models.CharField(max_length=50)
    serial_num = models.CharField(max_length=50)
    product_num = models.CharField(max_length=50)
    warranty_expire_date = models.DateField()
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)

class Location(models.Model):
    floor = models.SmallIntegerField(default=2)
    start_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)