from django.shortcuts import render
from django.contrib import messages
from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def voucher(request):
    vch=VoucherModels.objects.all()
    context={'vch':vch,}
    return render(request, 'voucher.html',context)

def vouchpage(request):
    return render(request, 'vouchpage.html')



def load_create_vouchertyp(request):
    return render(request,'load_create_vouchertyp.html')



def create_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
         
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if VoucherModels.objects.filter(voucher_name=Vname).exists():
                messages.info(request,'This Name is already taken...!')
                return render(request, 'load_create_vouchertyp')
        
        mdl = VoucherModels(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            prvnt_duplictes =prvtdp,
            
            allow_naration_in_voucher=allow_naration_in_vou,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        mdl.save()
        messages.info(request,'VOUCHER CREATED SUCCESSFULLY')
        return redirect('load_create_vouchertyp')

    return render(request, 'load_create_vouchertyp')

def update_voucher(request,pk):
    vch=VoucherModels.objects.get(id=pk)
    return render(request,'update_voucher.html',{'i':vch})


def save_voucher(request,pk):
    if request.method=='POST':
        vch =VoucherModels.objects.get(id=pk)
        vch.voucher_name = request.POST.get('nam')
        vch.alias = request.POST.get('alias')
        vch.voucher_type = request.POST.get('vtype')
        vch.abbreviation = request.POST.get('abbre')
        vch.active_this_voucher_type = request.POST.get('avtyp')
        vch.method_voucher_numbering = request.POST.get('meth_vou_num')
        vch.use_effective_date = request.POST.get('uefftdate')
        
        vch.allow_naration_in_voucher = request.POST.get('allow_naration_in_vou')
        vch.provide_naration = request.POST.get('providenr')
        vch.print_voucher = request.POST.get('print')
        
        vch.save()
        return redirect('voucher')
    return render(request, 'update_voucher.html',)

def costcat(request):
    cost=CostCategory.objects.all()
    context={'cost':cost,}

    return render(request, 'costcat.html',context)

def costcentr(request):
    centr=Costcentr.objects.all()
    context={'centr':centr,}

    return render(request, 'costcentr.html',context)

def primary(request,pk):
    cost=CostCategory.objects.get(id=pk)
    return render(request, 'primarycost.html',{'i':cost})

def update_cost(request,pk):
    if request.method=='POST':
        cost =CostCategory.objects.get(id=pk)
        cost.name = request.POST.get('a')
        cost.alias = request.POST.get('b')
        cost.revenue = request.POST.get('c')
        cost.nonrevenue = request.POST.get('d')
        
        
        cost.save()
        return redirect('costcat')
    return render(request, 'primarycost.html',)


def centr(request,pk):
    centr=Costcentr.objects.get(id=pk)
    return render(request, 'update_costcentr.html',{'i':centr})


def update_centr(request,pk):
    if request.method=='POST':
        centr =Costcentr.objects.get(id=pk)
        centr.name = request.POST.get('name')
        centr.alias = request.POST.get('alias')
        centr.under = request.POST.get('under')
        centr.emply = request.POST.get('emply')
        
        
        centr.save()
        return redirect('costcentr')
    return render(request, 'update_costcentr.html',)