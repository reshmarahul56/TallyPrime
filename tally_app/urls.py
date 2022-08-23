from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [

                path('',views.base,name='base'),
                path('index',views.index,name='index'),
                path('voucher',views.voucher,name='voucher'),
                path('vouchpage',views.vouchpage,name='vouchpage'),
                path('load_create_vouchertyp',views.load_create_vouchertyp,name='load_create_vouchertyp'),
                path('create_voucher',views.create_voucher,name="create_voucher"),
                path('update_voucher/<int:pk>',views.update_voucher,name="update_voucher"),
                path('save_voucher/<int:pk>',views.save_voucher,name="save_voucher"),
                
]
