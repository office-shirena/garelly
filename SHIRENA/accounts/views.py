from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Profile
from plam.models import Company,Image,UserImage

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #user = request.POST['username']
            
            email=request.POST['email']
            
            key=User.objects.filter(email = email)
            length = len(key)
            #usercount = User.objects.raw('SELECT * FROM auth_user WHERE email = %s', email)
            print(str(length))
            
            if length == 0 :
                companycd = request.POST['companycode']
                key2=Company.objects.filter(companyCode = companycd)
                length2 = len(key2)
                if length2 ==0 :
                    return render(request, 'signup.html', {'form': form})
                else:                    
                    user = form.save()
                    
                    
                    
                    
                    
                    user.profile.companycode= companycd
                    login(request, user)
                    
              
                    
                    
                    #ここに写真等のユーザdataベースを作成し、保存する
                    
                    
                    
                    return redirect('home')    
            else:
                return render(request, 'signup.html', {'form': form})
            
            
            
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})