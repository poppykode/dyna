from django.shortcuts import render,redirect
from datetime import datetime  
from datetime import timedelta  
from accounts.models import User
from django.utils import timezone
from requests.exceptions import ConnectionError
import requests
from django.contrib import messages
from django.conf import settings
import json
import time

# Create your views here.
def get_token(request):
    try:
        url=settings.PAYMENT_GATEWAY_BASE_URL +'/api/auth/oauth/token'
        headers ={
            'content-type': 'application/x-www-form-urlencoded',
        }
        payload ={
            'username':'admin',
            'password':'admin',
            'grant_type':'password'
        }
        Username = 'default-client'
        Password = 'YykMzIz1KctN5mCYvmmj'
        r = requests.post(url,data=payload,auth=(Username,Password),headers=headers)
        r1 =  json.loads(r.content)
        print(r1)
        token =''
        if 'access_token' in r1:
            token = r1['access_token']
            print(token)
        return token
    except ConnectionError as e:
        messages.error(request, 'Bad connection please try again later')
        redirect('subs:make-payment-subscribe')
   
def initiate_transaction(request):
    try:
        token = get_token(request)
        headers ={
            'authorization': "Bearer " + token,
            'key':'a7995b8d-de9c-11e8-ae41-9b18efac2229',
            'content-type': 'application/json'
        }
        url ='http://197.211.237.145:8404/v1/transaction-payments/initiate'
        r = requests.post(url,headers=headers)
        r1= json.loads(r.content)
        print(r1)
        ref_num =''
        if 'referenceNumber' in r1:
            ref_num =r1['referenceNumber']
        return ref_num
    except ConnectionError as e:
            messages.error(request, 'Bad connection please try again later')
            redirect('subs:make-payment-subscribe')

def check_payment_status(request):
    try:
        time.sleep(30)
        ref_num =initiate_transaction(request)
        token = get_token(request)
        url = 'http://197.211.237.145:8404/v1/transaction-payments/check-status/' + ref_num
        headers ={
            'authorization': "Bearer " + token,
            'key':'a7995b8d-de9c-11e8-ae41-9b18efac2229',
            'content-type': 'application/json'
        }
        r =requests.get(url,headers=headers)
        r1 = json.loads(r.content)
        print ('---->>>>>>>>>>>>>>>>Payment status')
        print(r1)
        if 'transactionStatus' in r1:
            sub = timezone.now() + timedelta(days=30) 
            print ('---->>>>>>>>>>>>>>>>')
            print (datetime.now())
            print(sub)
            print('---->>>>>>>>>>>>>>>>')
            user = User.objects.get(id=request.user.id)
            user.sub_expiration_date=sub
            user.save()
            status= r1['transactionStatus']
            messages.success(request, 'subscription success.' + status)
            
            return redirect('subs:make-payment-subscribe')
        elif 'error' in r1:
            messages.error(request, 'subscription unsuccessful please try again later.')           
            return redirect('subs:make-payment-subscribe')



    except ConnectionError as e:
        messages.error(request, 'Bad connection please try again later')
        redirect('subs:make-payment-subscribe')

def subscription(request):
    token = get_token(request)
    key = initiate_transaction(request)

    payment_method = request.POST.get('paymentmethod')
    phone_number = request.POST.get('phonenumber')
    amount = request.POST.get('amount')
    email = request.POST.get('email')   

    url = 'http://197.211.237.145:8404/v1/transaction-payments/process'
    headers ={
            'authorization': "Bearer " + token,
            'key':'a7995b8d-de9c-11e8-ae41-9b18efac2229',
            'content-type': 'application/json'
        }
    payload = {               
        "amount": amount,
        "referenceNumber" : "1863ba70-3926-11e9-82ba-81fdc02a72ce",
        "currencyCode": "USD",
        "customerEmail": email,
        "merchantResultUrl": "http://mysite.com",
        "paymentMethodId": 1,
        "paymentMethodRequiredFields": {
             "customerPhoneNumber": phone_number,
        }
    }
    r = requests.post(url,data=json.dumps(payload),headers=headers)
    check_payment_status(request)

   
    # sub = timezone.now() + timedelta(days=30) 
    # print ('---->>>>>>>>>>>>>>>>')
    # print (datetime.now())
    # print(sub)
    # print('---->>>>>>>>>>>>>>>>')
    # user = User.objects.get(id=request.user.id)
    # user.sub_expiration_date=sub
    # user.save()
    return render(request,'subscriptions/subcribe.html')

def subscription_view(request):
    template_name = 'subscriptions/subcribe.html'
    return render(request,template_name)

    




