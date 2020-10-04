from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MessageForm,nyukoForm , CompanyForm
from .models import Pallets, SendPlan, Company,CompanyUser, Pallettype,Message,CompanyRelated,ZaikoTable,Image
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.db.models import Q
import datetime
from django.db.models import Max


#@login_required
#def reply_topic(request, pk, topic_pk):
#    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            post = form.save(commit=False)
#            post.topic = topic
#            post.created_by = request.user
#            post.save()
#            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
#    else:
#        form = PostForm()
#    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
#


#
#def topic_posts(request, pk, topic_pk):
#    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
#    return render(request, 'topic_posts.html', {'topic': topic})
#
#@login_required
#def board_topics(request, pk):
#    board = get_object_or_404(Board, pk=pk)
#    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
#    return render(request, 'topics.html', {'board': board, 'topics': topics})




def home(request):
    
    
    user = request.user
    companycode = user.profile.companycode
    companyname = Company.objects.get(companyCode=companycode)
    plan = SendPlan.objects.filter(Q(rcvCompanycode__iexact=companycode)).distinct()
    sendplan=SendPlan.objects.filter(Q(sndCompanycode__iexact=companycode)).distinct()    
    messages = Message.objects.filter(
        Q(sndCompanycode__iexact=companycode) | 
        Q(rcvCompanycode__iexact=companycode)
        ).distinct().order_by('sendDate').reverse()
    items = CompanyRelated.objects.filter(keycompanyCode = companycode)
    #form = MessageForm()
    params = {
            'plan' : plan,
            'sendplan' :sendplan,
            'companyname':companyname,
            #'form' : form,
            'messages': messages,
            'items':items
            }
    ####################
    ###テスト#############
    #Entry.objects.all().delete()
    
    
    cntdata = Pallets.objects.all().count()
    
    
    for num in range(cntdata):
        PLtype = Pallets.objects.values('PLtype')[num:num+1]
        PLname = Pallets.objects.values('PLname')[num:num+1]
        print(PLtype)
        print(PLname)
        #'PLvolume','sndCompanycode','rcvCompanycode','sndDate','rcvDate''
        ##ここにワークテーブルに書き込む処理を入れればいい気がする。
        
        
       
    ####################
    
    
    
    if request.method == 'POST':
        #form = MessageForm(request.POST)
        sndCompanycode = companycode
        #rcvCompanyname = form.cleaned_data['rcvCompanyname']
        #rcvCompanycode = form.cleaned_data['rcvCompanycode']
        rcvCompanycode =request.POST['rcvCompanycode']
        message = request.POST['message']
        sndCompanyname= Company.objects.values_list('companyName',flat=True).get(companyCode=sndCompanycode)
        rcvCompanyname= Company.objects.values_list('companyName',flat=True).get(companyCode=rcvCompanycode)
        userName = request.POST['updateUser']
        
        # 安全なデータを使ってオブジェクトを作成
        savedata = Message.objects.create(
                sndCompanycode=sndCompanycode,
                sndCompanyname=sndCompanyname,
                rcvCompanycode=rcvCompanycode,
                rcvCompanyname=rcvCompanyname,
                messagetext=message,
                updateUser=userName
                )
        # オブジェクトをＤＢへ保存
        savedata.save()
            

            
            
        # トップページへリダイレクトして結果を表示
        return redirect('/home')
    else:
        """
        動作順序①
        """
        # 最初にブラウザから呼び出されるときに使用するフォームクラスを指定

        return render(request, 'home.html', params)


def menu(request):
    user = request.user
    companycode = user.profile.companycode
    companyname = Company.objects.get(companyCode=companycode)
    params = {
            'companycode':companycode,
            'companyname':companyname,
            }


    return render(request, 'menu.html',params)

def company(request):
    user = request.user
    companycode = user.profile.companycode
    
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        selection = request.POST['selection']
        print(selection)
        if companycode == '0001':
            if selection == 'on':
                
                
                if form.is_valid():
                    company = form.save(commit = False)
                    company.companyCode
                    company.companyName
                    companycode = company.companyCode
                    companyname = company.companyName
                    
                    querySet = Company.objects.filter(companyCode = companycode)
                    if querySet.first() is None:
                        company.save()
                    
                    company = Company.objects.all() 
                    params2 = {
                        'companycode':companycode,
                        'companyname':companyname,
                        'company':company,
                        }
                    request.session['companycode'] = companycode        
                    request.session['companyname'] = companyname         
                    
                    # オブジェクトをＤＢへ保存
                    # トップページへリダイレクトして結果を表示
                    return render(request, 'company_related.html' ,params2)
                    #return redirect('/company_related',params2)
                        
                
    else:
        
        
        form = CompanyForm()
        """
        動作順序①
        """
        # 最初にブラウザから呼び出されるときに使用するフォームクラスを指定
    if companycode == '0001':

        params = {
            'companycode':companycode,
            'form':form,
                }
        return render(request, 'company.html',params)

    else:
        user = request.user
        companycode = user.profile.companycode
        companyname = Company.objects.get(companyCode=companycode)
        plan = SendPlan.objects.filter(Q(rcvCompanycode__iexact=companycode)).distinct()
        sendplan=SendPlan.objects.filter(Q(sndCompanycode__iexact=companycode)).distinct()    
        messages = Message.objects.filter(
                Q(sndCompanycode__iexact=companycode) | 
                Q(rcvCompanycode__iexact=companycode)
                ).distinct().order_by('sendDate').reverse()
        items = CompanyRelated.objects.filter(keycompanyCode = companycode)
    #form = MessageForm()
        params = {
                'plan' : plan,
                'sendplan' :sendplan,
                'companyname':companyname,
                #'form' : form,
                'messages': messages,
                'items':items
                }
        return render(request, 'home.html',params)

    







def company_related(request):
    
    
    if (request.method == 'POST'):
       
       
       user = request.user
       companycode = user.profile.companycode
       companyname=Company.objects.values_list('companyName',flat=True).get(companyCode=companycode)
       
       checked_list = request.POST.getlist('chkbx')
       keycompanyCode=request.session['companycode']
       keycompanyName=request.session['companyname']
       
       for i in checked_list: 
            relatedcompanyCode=Company.objects.values_list('companyCode',flat=True).get(id=i)
            relatedcompanyName=Company.objects.values_list('companyName',flat=True).get(id=i)
           #print(i + relatedcompanyName)
           ###################
        ####ここにデータベースに書き込む処理を追記！！！！！！
            savedata = CompanyRelated.objects.create(
            keycompanyCode = keycompanyCode,
            keycompanyName = keycompanyName,
            relatedcompanyCode = relatedcompanyCode,
            relatedcompanyName = relatedcompanyName        
            )
                # オブジェクトをＤＢへ保存
            savedata.save()
        
       return redirect('/company')
    else:
    
    
    
    
        company = Company.objects.all()
        #companycode=request.GET['companycode']
        params = {
            'company' : company,
            'companycode': companycode,
            'companyname':companyname,            
                }
    
        return render(request, 'company_related.html', params)


        
    
def select(request,num):
    keyid=SendPlan.objects.values_list('planNo',flat=True).get(id=num)
    PLtype=SendPlan.objects.values_list('PLtype',flat=True).get(id=num)
    PLname=SendPlan.objects.values_list('PLname',flat=True).get(id=num)
    PLvolume=SendPlan.objects.values_list('PLvolume',flat=True).get(id=num)
    sndCompanycode=SendPlan.objects.values_list('sndCompanycode',flat=True).get(id=num)
    rcvCompanycode=SendPlan.objects.values_list('rcvCompanycode',flat=True).get(id=num)
    sndCompanyName=SendPlan.objects.values_list('sndCompanyName',flat=True).get(id=num)
    rcvCompanyName=SendPlan.objects.values_list('rcvCompanyName',flat=True).get(id=num)    
    sndDate=SendPlan.objects.values_list('sndPlanDate',flat=True).get(id=num)
    rcvDate=SendPlan.objects.values_list('rcvPlanDate',flat=True).get(id=num)
    #obj=SendPlan.objects.get(id=num)    
    
    
    if (request.method=='POST'):
        
        user = request.user
        updateUser=request.user.username
        companycode = user.profile.companycode
        keyid = request.POST['keyid']
        PLname = request.POST['PLname']
        PLtype = Pallettype.objects.values_list('PLtype',flat=True).get(PLname=PLname)
        
        PLvolume =request.POST['PLvolume']
        sndCompanycode=request.POST['sndCompanycode']
        rcvCompanycode=companycode
        sndCompanyName=sndCompanyName
        rcvCompanyName=rcvCompanyName
        sndDate = request.POST['sndDate']
        rcvDate = request.POST['rcvDate']
        jidoQty= 0
        nonjidoQty = 0
                # 安全なデータを使ってオブジェクトを作成
        
        if PLtype =='1':
            jidoQty=int(request.POST['PLvolume'])
        elif PLtype =='2':
            nonjidoQty=int(request.POST['PLvolume'])
    
        savedata = Pallets.objects.create(
            keyid = keyid,
            PLtype = PLtype,
            PLname = PLname,
            PLvolume =PLvolume,
            sndCompanycode=sndCompanycode,
            rcvCompanycode=rcvCompanycode,
            sndCompanyName=sndCompanyName,
            rcvCompanyName=rcvCompanyName,
            sndDate = sndDate,
            rcvDate = rcvDate,
            updateUser=updateUser
            )
                # オブジェクトをＤＢへ保存
        savedata.save()
        
        
        
        
        querySet2 = ZaikoTable.objects.filter(companyCode = rcvCompanycode)
        if querySet2.first() is None:
            savedata3 = ZaikoTable.objects.create(
                    companyCode=rcvCompanycode, 
                    companyName = Company.objects.values_list('companyName',flat=True).get(companyCode=rcvCompanycode),
                    JidoTagPL=jidoQty,
                    NonTagPL=nonjidoQty
                    )
            savedata3.save()
        else:
            
            ny = ZaikoTable.objects.get(companyCode=rcvCompanycode)
            ny.companyCode = rcvCompanycode
            ny.companyName = Company.objects.values_list('companyName',flat=True).get(companyCode=rcvCompanycode),
            ny.JidoTagPL=int(ny.JidoTagPL) + jidoQty
            ny.NonTagPL=int(ny.NonTagPL) + nonjidoQty
            print(ny.NonTagPL)
            ny.save()
        
        querySet = ZaikoTable.objects.filter(companyCode = sndCompanycode)
        if querySet.first() is None:
            savedata2 = ZaikoTable.objects.create(
                    companyCode=sndCompanycode, 
                    companyName = Company.objects.values_list('companyName',flat=True).get(companyCode=sndCompanycode),
                    JidoTagPL=-jidoQty,
                    NonTagPL=-nonjidoQty
                    )
            savedata2.save()
        else:
            t = ZaikoTable.objects.get(companyCode=sndCompanycode)
            t.companyCode = sndCompanycode
            t.companyName = Company.objects.values_list('companyName',flat=True).get(companyCode=sndCompanycode),
            t.JidoTagPL=int(t.JidoTagPL) - jidoQty
            t.NonTagPL=int(t.NonTagPL) - nonjidoQty
            t.save()
        
        
        SendPlan.objects.get(id=num).delete()
        
        
        
        
        
        
            # トップページへリダイレクトして結果を表示
            
            
            
            
        return redirect('/home')
    #obj=[keyid,PLtype,PLname,PLvolume,sndCompanycode,rcvCompanycode,sndDate,rcvDate]
    
    sndDatedate = sndDate.strftime("%Y-%m-%d")
    rcvDatedate = rcvDate.strftime("%Y-%m-%d")
#    rcvDatedatetime = datetime.datetime.strptime(rcvDate, '%Y-%m-%d %H:%M:%S')
#    rcvDatedate = datetime.date(rcvDatedatetime.year, rcvDatedatetime.month, rcvDatedatetime.day)
#    
    params = {
            'id':num,
            'keyid' : keyid,
            'PLtype' : PLtype,
            'PLname' : PLname,
            'PLvolume' : PLvolume,
            'sndCompanycode' : sndCompanycode,
            'sndCompanyName' : sndCompanyName,
            'rcvCompanycode' : rcvCompanycode,
            'rcvCompanyName' : rcvCompanyName,
            'sndDate' : sndDatedate,
            #'sndDate' : date_value = dt.strptime(sndDate, '%Y/%m/%d %H:%M:%S'),
            'rcvDate' : rcvDatedate, 
            }
    return render(request, 'select.html', params)


def change(request,num):
    keyid=SendPlan.objects.values_list('planNo',flat=True).get(id=num)
    PLtype=SendPlan.objects.values_list('PLtype',flat=True).get(id=num)
    PLname=SendPlan.objects.values_list('PLname',flat=True).get(id=num)
    PLvolume=SendPlan.objects.values_list('PLvolume',flat=True).get(id=num)
    sndCompanycode=SendPlan.objects.values_list('sndCompanycode',flat=True).get(id=num)
    rcvCompanycode=SendPlan.objects.values_list('rcvCompanycode',flat=True).get(id=num)
    sndDate=SendPlan.objects.values_list('sndPlanDate',flat=True).get(id=num)
    rcvDate=SendPlan.objects.values_list('rcvPlanDate',flat=True).get(id=num)
    #obj=SendPlan.objects.get(id=num)    
    
    
    if (request.method=='POST'):
        
        user = request.user
        companycode = user.profile.companycode
        keyid = request.POST['keyid']
        PLname = request.POST['PLname']
        PLtype = Pallettype.objects.values_list('PLtype',flat=True).get(PLname=PLname)
        
        PLvolume =request.POST['PLvolume']
        sndCompanycode=request.POST['sndCompanycode']
        rcvCompanycode=companycode
        sndDate = request.POST['sndDate']
        rcvDate = request.POST['rcvDate']
                # 安全なデータを使ってオブジェクトを作成
                
                
        s = SendPlan.objects.filter(id=num).first()
        s.PLtype=PLtype
        s.PLname=PLname
        s.PLvolume=PLvolume
        s.save()

        return redirect('/home')
    #obj=[keyid,PLtype,PLname,PLvolume,sndCompanycode,rcvCompanycode,sndDate,rcvDate]
    
    sndDatedate = sndDate.strftime("%Y-%m-%d")
    rcvDatedate = rcvDate.strftime("%Y-%m-%d")
#    rcvDatedatetime = datetime.datetime.strptime(rcvDate, '%Y-%m-%d %H:%M:%S')
#    rcvDatedate = datetime.date(rcvDatedatetime.year, rcvDatedatetime.month, rcvDatedatetime.day)
#    
    params = {
            'id':num,
            'keyid' : keyid,
            'PLtype' : PLtype,
            'PLname' : PLname,
            'PLvolume' : PLvolume,
            'sndCompanycode' : sndCompanycode,
            'rcvCompanycode' : rcvCompanycode,
            'sndDate' : sndDatedate,
            #'sndDate' : date_value = dt.strptime(sndDate, '%Y/%m/%d %H:%M:%S'),
            'rcvDate' : rcvDatedate, 
            }
    return render(request, 'change.html', params)



def delete(request,num):
    
    Message.objects.filter(id=num).delete()
   
    return redirect('/home')


def pl_adjust(request):
    if (request.method=='POST'):
        user = request.user
        JidoPL= request.POST['JidoPL']
        NonTagPL= request.POST['NonTagPL']
        companyCode=user.profile.companycode
              
        ny = ZaikoTable.objects.get(companyCode=companyCode)
        ny.JidoTagPL=int(JidoPL)
        ny.NonTagPL=int(NonTagPL)
        ny.save()
        
        return redirect('/home')
        
    else:
        user = request.user
        companyCode = user.profile.companycode
        ny = ZaikoTable.objects.get(companyCode=companyCode)
        JidoPL=ny.JidoTagPL
        NonTagPL=ny.NonTagPL
        params = {
                 'user':user,
                 'companyCode':companyCode,
                 'JidoPL' :JidoPL,
                 'NonTagPL':NonTagPL
                }
        # 初期化時に第2引数に初期値を設定します。some_text=Text, boolean=Trueが初期値で設定されます
     
        return render(request, 'pl_adjust.html', params)

    #return render(request, 'select.html')

def pl_shipment(request):
    if (request.method=='POST'):
        planNo =request.POST['keyid']
        sndPlanDate = request.POST['sndDate']
        rcvPlanDate = request.POST['rcvDate']
        
        PLname=''
        user = request.user
        updateUser=request.user.username
        PLtype=request.POST['PLtype']
        if PLtype =='1':
            PLname ='自動倉庫PL_タグあり'
            #jidoQty=int(request.POST['PLvolume'])
        elif PLtype =='2':
            PLname ='タグなしパレット'
            #nonjidoQty=int(request.POST['PLvolume'])
        PLvolume =request.POST['PLvolume']
        sndCompanycode =user.profile.companycode
        print(sndCompanycode)
        rcvCompanycode =request.POST['rcvCompanycode']
        sndCompanyName = Company.objects.values_list('companyName',flat=True).get(companyCode=sndCompanycode)
        rcvCompanyName = Company.objects.values_list('companyName',flat=True).get(companyCode=rcvCompanycode)
        
        
        rcvFlg = 0
        
              
                
        savedata = SendPlan.objects.create(
            planNo = planNo,
            sndPlanDate = sndPlanDate,
            rcvPlanDate = rcvPlanDate,
            PLtype = PLtype,
            PLname = PLname,
            PLvolume =PLvolume,
            sndCompanycode=sndCompanycode,
            sndCompanyName=sndCompanyName,
            rcvCompanycode=rcvCompanycode,
            rcvCompanyName=rcvCompanyName,
            rcvFlg = rcvFlg,
            updateUser = updateUser
            )
                # オブジェクトをＤＢへ保存
        savedata.save()
        
  
        return redirect('/home')
        
    else:
        user = request.user
        companycode = user.profile.companycode
        sndDatedate = datetime.date.today()
        rcvDatedate = datetime.date.today()
        sndDatedate = sndDatedate.strftime("%Y-%m-%d")
        rcvDatedate = rcvDatedate.strftime("%Y-%m-%d")
        objkeyid  =SendPlan.objects.all().aggregate(Max('id')) 
        
        
        objid = int(objkeyid['id__max'])
        keyid = '{0:010d}'.format(objid+1)
        print(keyid)
        sndCompanycode=companycode
        rcvCompanycode=companycode
        print(sndCompanycode)
        sndDate = sndDatedate
        rcvDate = rcvDatedate    
        items = CompanyRelated.objects.filter(keycompanyCode = companycode)
        print(items)
        params = {
                 'keyid':keyid,
                 'items':items,
                 'sndDate' :sndDate,
                 'rcvDate':rcvDate,
                 'sndCompanycode':sndCompanycode
                }
        # 初期化時に第2引数に初期値を設定します。some_text=Text, boolean=Trueが初期値で設定されます
     
        return render(request, 'pl_shipment.html', params)




def tagpl(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'tagpl.html', context)


def nontagpl(request):
    user = request.user
    companycode = user.profile.companycode
    params = {
            'user':user,
            'companycode':companycode
            }
    return render(request, 'nontagpl.html',params)


def hyoji(request):


    user = request.user
    companycode = user.profile.companycode
    if companycode == '0001':
        d = {
                'hyou': ZaikoTable.objects.all(),
                }
        return render(request, 'hyoji.html', d)
    
    else:
        d = {
                'hyou': ZaikoTable.objects.filter(companyCode=companycode),
                }
        return render(request, 'hyoji.html', d)
    
    

def hyoji2(request):


    user = request.user
    companycode = user.profile.companycode
    if companycode == '0001':
        d = {
                'hyou2': Pallets.objects.all().order_by('rcvDate').reverse(),
                }
        return render(request, 'hyoji2.html', d)
    
    else:        
        d = {
                'hyou2': Pallets.objects.filter(Q(rcvCompanycode__exact=companycode)|Q(sndCompanycode__exact=companycode)).distinct().order_by('rcvDate').reverse(),
                }
        return render(request, 'hyoji2.html', d)

def allcompany(request):


    user = request.user
    companycode = user.profile.companycode
    if companycode == '0001':
        d = {
                'hyou3': Company.objects.all(),
                }
        return render(request, 'allcompany.html', d)
    
    else:
        user = request.user
        companycode = user.profile.companycode
        companyname = Company.objects.get(companyCode=companycode)
        plan = SendPlan.objects.filter(Q(rcvCompanycode__iexact=companycode)).distinct()
        sendplan=SendPlan.objects.filter(Q(sndCompanycode__iexact=companycode)).distinct()    
        messages = Message.objects.filter(
                Q(sndCompanycode__iexact=companycode) | 
                Q(rcvCompanycode__iexact=companycode)
                ).distinct().order_by('sendDate').reverse()
        items = CompanyRelated.objects.filter(keycompanyCode = companycode)
    #form = MessageForm()
        params = {
                'plan' : plan,
                'sendplan' :sendplan,
                'companyname':companyname,
                #'form' : form,
                'messages': messages,
                'items':items
                }
        return render(request, 'home.html',params)


    
#  Entry.objects.filter(name='Taro').order_by('pub_date').reverse()    

#PLtype = models.CharField(max_length=1)
#    PLname = models.CharField(max_length=100)
#    PLvolume =models.CharField(max_length=5)
#    sndCompanycode=models.CharField(max_length=5)
#    sndCompanyName=models.CharField(max_length=100, null=True)
#    rcvCompanycode=models.CharField(max_length=5)
#    rcvCompanyName=models.CharField(max_length=100, null=True)
#    sndDate = models.DateField()
#    rcvDate = models.DateField()
#        
        
