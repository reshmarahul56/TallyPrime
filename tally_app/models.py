from django.db import models

# Create your models here.
class VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_naration_in_voucher =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)


class CostCategory(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    revenue=models.CharField(max_length=225)
    nonrevenue=models.CharField(max_length=225)

class Costcentr(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    emply=models.CharField(max_length=225)

class CreateCurrency(models.Model):
    symbol =models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    ISO_code=models.CharField(max_length=225)
    decimal_places= models.CharField(max_length=225,default=2)
    show_in_millions =  models.CharField(max_length=225)
    suffix_to_amount=  models.CharField(max_length=225)
    space_symbol_amount = models.CharField(max_length=225)
    word_after_decimal = models.CharField(max_length=225)
    decimal_no_in_words = models.CharField(max_length=225)

class CurrencyAlter(models.Model):
    cname= models.ForeignKey( CreateCurrency,on_delete=models.CASCADE,default=1)
    slno = models.CharField(max_length=225)
    currencys = models.CharField(max_length=225)
    stdrate =models.CharField(max_length=225)
    lastvrate =models.CharField(max_length=225)
    specirate =models.CharField(max_length=225)
    lastvrate2 =models.CharField(max_length=225)
    specirate2 =models.CharField(max_length=225)
