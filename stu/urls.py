#coding=utf-8

from django.conf.urls import url
from stu import views

urlpatterns=[
    url(r'^$',views.index_view),
    url(r'^topay/$',views.pay_view),
    url(r'^checkPay/$',views.checkPay_view),

]