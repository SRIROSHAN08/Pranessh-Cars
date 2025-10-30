from django.db import models

class CarDetails(models.Model):
    
    vehicle = models.CharField(max_length=250,null=True,blank=True)
    fuel_type = models.CharField(max_length=250,null=True,blank=True)
    model = models.CharField(max_length=250,null= True,blank= True)
    owner = models.CharField(max_length=250,null=True,blank=True)
    gear = models.CharField(max_length=250,null=True,blank=True)
    seats = models.CharField(max_length=250,null=True,blank=True)
    color = models.CharField(max_length=250,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    km = models.IntegerField(null=True,blank=True)
    description = models.TextField(default='Vehicle descriptions here')
    insurance = models.CharField(max_length=250,null= True,blank=True)
    picture1 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture2 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture3 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture4 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture5 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture6 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture7 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture8 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture9 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture10 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture11 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture12 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture13 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture14 = models.ImageField(null=True,blank=True,upload_to='images/')
    picture15 = models.ImageField(null=True,blank=True,upload_to='images/')


@property
def pictures(self):
    return [self.picture1, self.picture2, self.picture3, self.picture4, self.picture5]


class Contact(models.Model):
    
    name = models.CharField(max_length=250,null= True,blank=True)
    phn_no =models.CharField(max_length=250,null= True,blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"