from django.db import models

# Create your models here.
class organizationMaster(models.Model):
    Ornganization_id = models.AutoField(primary_key=True)
    Organization_name = models.CharField(max_length=50)
    Address = models.CharField(max_length=200)
    Phone_no = models.CharField(max_length=15)
    Email = models.EmailField(max_length=50)
    Status = models.CharField(max_length=10)
    Created_date = models.DateField()
class userMaster(models.Model):
    User_id = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50)
    Ornganization_id = models.ForeignKey(organizationMaster,on_delete=models.CASCADE)
    Mobile_no = models.CharField(max_length=15)
    Designation = models.CharField(max_length=25)
    Gender = models.CharField(max_length=15)
    Age = models.CharField(max_length=10)
    Role = models.CharField(max_length=25)
    Status = models.CharField(max_length=25)
class loginMaster(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Role = models.CharField(max_length=25)
class AreaMaster(models.Model):
    Area_code = models.AutoField(primary_key=True)
    Area_name = models.CharField(max_length=50)
    Status = models.CharField(max_length=20)
    Ornganization_id = models.ForeignKey(organizationMaster,on_delete=models.CASCADE)
class hospitalMaster(models.Model):
    Hospital_id = models.AutoField(primary_key=True)
    Hospital_name = models.CharField(max_length=200)
    Address = models.CharField(max_length=500)
    Status = models.CharField(max_length=20)
    Ornganization_id = models.ForeignKey(organizationMaster,on_delete=models.CASCADE)
class donorMaster(models.Model):
    Donor_id = models.AutoField(primary_key=True)
    Donor_name = models.CharField(max_length=50)
    Gender = models.CharField(max_length=15)
    DOB = models.DateField()
    Age = models.CharField(max_length=5)
    Address = models.CharField(max_length=500)
    Phone_no = models.CharField(max_length=15)
    Blood_group = models.CharField(max_length=10)
    Donated_earlier = models.BooleanField(default=False)
    Last_donation_date = models.DateField(null=True, blank=True)
    Created_date = models.DateField()
    Status = models.CharField(max_length=15)
    Captured_by = models.ForeignKey(userMaster,on_delete=models.CASCADE)
    Area = models.ForeignKey(AreaMaster,on_delete=models.CASCADE)
    Ornganization_id = models.ForeignKey(organizationMaster,on_delete=models.CASCADE)
class donationDetails(models.Model):
    Donation_id = models.AutoField(primary_key=True)
    Patient_bystander = models.CharField(max_length=50)
    Contact_no = models.CharField(max_length=15)
    Purpose = models.CharField(max_length=50)
    Donation_date = models.DateField()
    Donation_status = models.CharField(max_length=25)
    Created_date = models.DateField()
    Status = models.CharField(max_length=10)
    Ornganization_id = models.ForeignKey(organizationMaster,on_delete=models.CASCADE)
    Captured_by = models.ForeignKey(userMaster,on_delete=models.CASCADE)
    Hospital_id = models.ForeignKey(hospitalMaster,on_delete=models.CASCADE)
    Donor_id = models.ForeignKey(donorMaster,on_delete=models.CASCADE)
    
    
    
    
    
    

    
    
    
    
    
    
    
