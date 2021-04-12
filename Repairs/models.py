from django.db import models

class Vendor(models.Model):
    # VendorId = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Assets(models.Model):
    # assetId = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    Value = models.IntegerField()

    def __str__(self):
        return self.description

class Delivery(models.Model):
    # deliveryId = models.IntegerField(primary_key=True)
    transDate = models.DateField('Date Dispatched')
    staff = models.CharField(max_length=200)
    toLocation=models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
    

class AssetTrans(models.Model):
    delivery=models.ForeignKey(Delivery, on_delete=models.CASCADE)
    assetId= models.ForeignKey(Assets, on_delete=models.CASCADE)
    qty = models.IntegerField(null=True, blank=True)
    transDate = models.DateField('Date Dispatched')
    shipped = models.BooleanField(default=False)
    received = models.BooleanField(default=False)


    


         



