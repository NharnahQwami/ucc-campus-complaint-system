from django.db import models



# Create your models here.

class Complaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    status = models.CharField(max_length=100, null = True)
    faculty = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')


class CustomUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = raw_password

    def check_password(self, raw_password):
        return self.password == raw_password
    



    
