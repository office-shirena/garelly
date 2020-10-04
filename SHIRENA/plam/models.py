from django.db import models
from django.contrib.auth.models import User


#class Board(models.Model):
#    name = models.CharField(max_length=30, unique=True)
#    description = models.CharField(max_length=100)
#    def __str__(self):
#        return self.name
#    def get_posts_count(self):
#        return Post.objects.filter(topic__board=self).count()
#
#    def get_last_post(self):
#        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Image(models.Model):
    companyCode = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.companyCode + ":" + self.title


class UserImage(models.Model):
    companyCode = models.CharField(max_length=5)
    companyName = models.CharField(max_length=100)
    username = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    quantity = models.CharField(max_length=4)
    
    def __str__(self):
        return self.companyCode + '　' + self.companyName + ':' + self.username  + ':' + self.title + ':' + str(self.quantity)
        


class ZaikoTable(models.Model):
    companyCode= models.CharField(max_length=5)
    companyName=models.CharField(max_length=100)
    JidoTagPL = models.CharField(max_length=5)
    NonTagPL = models.CharField(max_length=5)
    def __str__(self):
        return self.companyCode + ':' + self.companyName + ':' + self.Jido_TagPL  + ':' + self.NonTagPL



class Pallets(models.Model): 
    keyid = models.CharField(max_length=10)
    PLtype = models.CharField(max_length=1)
    PLname = models.CharField(max_length=100)
    PLvolume =models.CharField(max_length=5)
    sndCompanycode=models.CharField(max_length=5)
    sndCompanyName=models.CharField(max_length=100, null=True)
    rcvCompanycode=models.CharField(max_length=5)
    rcvCompanyName=models.CharField(max_length=100, null=True)
    sndDate = models.DateField()
    rcvDate = models.DateField()
    updateUser=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.keyid + " " + self.PLtype + " " + self.PLname + ":" + self.PLvolume + "," + self.rcvCompanycode + "," + str(self.rcvDate) + " from " + self.sndCompanycode + "," + str(self.sndDate) + "," + str(self.updateUser)

class SendPlan(models.Model):
    planNo=models.CharField(max_length=10)
    sndPlanDate = models.DateField()
    rcvPlanDate = models.DateField()
    PLtype = models.CharField(max_length=1)
    PLname = models.CharField(max_length=100)
    PLvolume =models.CharField(max_length=5)
    sndCompanycode=models.CharField(max_length=5)
    sndCompanyName=models.CharField(max_length=100, null=True)
    rcvCompanycode=models.CharField(max_length=5)
    rcvCompanyName=models.CharField(max_length=100, null=True)
    rcvFlg = models.BooleanField()
    updateUser=models.CharField(max_length=50, null=True)
    def __str__(self):
         return self.planNo + " " + self.PLtype + " " + self.PLname + ":" + self.PLvolume + "," + self.sndCompanycode + "," + str(self.sndPlanDate) + " to " + self.rcvCompanycode + "," + str(self.rcvPlanDate) + "," + str(self.updateUser)

class Company(models.Model): 
    companyCode = models.CharField(max_length=5)
    companyName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.companyCode + ':' + self.companyName

class CompanyUser(models.Model): 
    companyCode = models.CharField(max_length=5)
    userEmail = models.EmailField(max_length=200)
    
    def __str__(self):
        return self.companyCode + ':' + self.userEmail
    

class Pallettype(models.Model):
    PLtype = models.CharField(max_length=1)
    PLname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.PLtype + ':' + self.PLname

class Message(models.Model):
    sendDate = models.DateTimeField(auto_now_add=True)
    sndCompanycode=models.CharField(max_length=5)
    sndCompanyname=models.CharField(max_length=100)
    rcvCompanycode=models.CharField(max_length=5)
    rcvCompanyname=models.CharField(max_length=100)
    messagetext=models.TextField(max_length=300)
    updateUser=models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return str(self.sendDate) + ':' + self.sndCompanycode + " to " + self.rcvCompanycode + ":" + self.messagetext + "," + str(self.updateUser)
    
class CompanyRelated(models.Model):
    keycompanyCode = models.CharField(max_length = 5)
    keycompanyName = models.CharField(max_length = 100)
    relatedcompanyCode = models.CharField(max_length = 5)
    relatedcompanyName = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.keycompanyCode) + ':' + self.keycompanyName + " related " + self.relatedcompanyCode + ":" + self.relatedcompanyName
    
    

     
    