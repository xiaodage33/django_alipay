# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import random
# Create your views here.
from utils.alipay import *
import json



def index_view(request):
    return render(request,'index.html')



alipay = AliPay(appid='2016091100486702', app_notify_url='http://127.0.0.1:9999/stu/checkPay/', app_private_key_path='stu/keys/my_private_key.txt',
                 alipay_public_key_path='stu/keys/alipay_public_key.txt', return_url='http://127.0.0.1:9999/stu/checkPay/', debug=True)

#获取支付二维码界面
def pay_view(request):
    import uuid

    #获取请求参数
    m = request.POST.get('m',0)
    #随机数字订单编号
    # random_id =  random.randrange(1,1010,2)  #或者订单编号给一个随机数值也可

    #获取扫码支付请求参数  ;uuid.uuid4().hex()这个报错 str不能调用
    # params = alipay.direct_pay(subject='京东超市', out_trade_no=uuid.uuid4().hex(), total_amount=str(m))
    params = alipay.direct_pay(subject='京东超市', out_trade_no=str(uuid.uuid4()).replace("-",""), total_amount=str(m))
    print(params)
    print("=====")
    print(str(uuid.uuid4()))
        #获取扫码支付的请求地址
    url = alipay.gateway+"?"+params
    return HttpResponseRedirect(url)


#校验是否支付完成
def checkPay_view(request):
    #获取所有请求参数
    params = request.GET.dict()

    #移除并获取sign参数的值
    sign = params.pop('sign')

    #校验是否支付成功
    if alipay.verify(params,sign):
        return HttpResponse('支付成功！')
    return HttpResponse('支付失败！')