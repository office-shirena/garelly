from django.contrib import admin
from .models import Pallets,SendPlan,Company,CompanyUser,Pallettype,Message,ZaikoTable,Image,CompanyRelated,UserImage

admin.site.register(Pallets)
admin.site.register(SendPlan)
admin.site.register(Company)
admin.site.register(CompanyUser)
admin.site.register(Pallettype)
admin.site.register(Message)
admin.site.register(ZaikoTable)
admin.site.register(Image)
admin.site.register(CompanyRelated)
admin.site.register(UserImage)
#Register your models here.
