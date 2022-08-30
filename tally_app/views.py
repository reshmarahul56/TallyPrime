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

def create_centre(request):
    return render(request,'create_centre.html')




def primary(request,pk):
    cost=CostCategory.objects.get(id=pk)
    return render(request, 'primarycost.html',{'i':cost})


def costcat(request):
    cost=CostCategory.objects.all()
    context={'cost':cost,}

    return render(request, 'costcat.html',context)


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

def costcentr(request):
    centr=Costcentr.objects.all()
    context={'centr':centr,}

    return render(request, 'costcentr.html',context)
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

def currency(request):
    obj=CreateCurrency.objects.all()
    context={'cur':obj,}
    return render(request, 'currency.html',context)

def currency_alter(request,pk):
    cur=CreateCurrency.objects.get(id=pk)
    return render(request,'currency_alter.html',{'i':cur})

def load_create_currency(request):
    return render(request,'load_create_currency.html')

def create_currency(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        fname = request.POST['fname']
        if len(symbol) <= 0:
            print('XX')
            return JsonResponse({
                'status': 00
            })
        elif len(fname) <= 0:
            print('XXX')
            return JsonResponse({
                'status': 00
            })
        else:
            pass

        iso_code = request.POST['iso_code']
        n_deci_placs = request.POST['n_deci_placs']
        smt_millon = request.POST['smt_millon']
        symbol_to_amount = request.POST['symbol_to_amount']
        space_bt_sy = request.POST['space_bt_sy']
        amount_after_decimal = request.POST['amount_after_decimal']
        amount_in_words = request.POST['amount_in_words']

        mdl_obj = CreateCurrency(
            symbol=symbol,
            formal_name=fname,
            ISO_code=iso_code,
            decimal_places=n_deci_placs,
            show_in_millions=smt_millon,
            suffix_to_amount=symbol_to_amount,
            space_symbol_amount=space_bt_sy,
            word_after_decimal=amount_after_decimal,
            decimal_no_in_words = amount_in_words,
        )
        mdl_obj.save()
        return redirect('load_create_currency')

def save_currency_data(request):
    if request.method == 'POST':
        sl = request.POST['slno']
        cname = request.POST['curname']
        stdr = request.POST['stdr']
        lvr = request.POST['lvr']
        sr = request.POST['sr']
        lvr2 = request.POST['lvr2']
        sr2 = request.POST['sr2']
        
        obj = CurrencyAlter(
            slno = sl,
            currencys= cname,
            stdrate = stdr,
            lastvrate = lvr,
            specirate = sr,
            lastvrate2 = lvr2,
            specirate2 = sr2,
            
            
           
        )
        
        obj.save()
        grp = CreateCurrency.objects.all()
        obj1 = CurrencyAlter.objects.all()
        context = {'grp':grp ,'obj':obj1}
        return redirect('load_rates_of_exchange',context)

def update_currency(request,pk):
    if request.method=='POST':
        cur =CreateCurrency.objects.get(id=pk)
        cur.symbol = request.POST.get('symbol')
        cur.formal_name = request.POST.get('fname')
        cur.ISO_code = request.POST.get('iso_code')
        cur.decimal_places = request.POST.get('n_deci_placs')
        cur.show_in_millions = request.POST.get('smt_millon')
        cur.suffix_to_amount = request.POST.get('symbol_to_amount')
        cur.space_symbol_amount = request.POST.get('space_bt_sy')
        cur.word_after_decimal = request.POST.get('amount_after_decimal')
        cur.decimal_no_in_words = request.POST.get('amount_in_words')
        
        cur.save()
        return redirect('currency')
    return render(request, 'currency_alter.html',)