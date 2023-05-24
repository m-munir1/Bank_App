from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest
from bank_management.models import Account

def home(request: HttpRequest):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if Account.objects.filter(username=username).exists():
            user = Account.objects.get(username=username)
            login(request, user)
            return redirect('bank_management')
        else:
            user = Account.objects.create_user(
                username=username,
                password=password,
            )
            user.save()
            login(request, user)
            return redirect('step_1')
    
    return render(request, 'bank_management/home.html', context)

def step_1(request: HttpRequest):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        have_account = request.POST.get('have_account')
        
        if have_account is None:
            context['exception'] = "Please choose an option"
        elif have_account == "n":
            return redirect('step_2')
        else:
            if username == "":
                context['exception'] = "Please enter a name"
                
            if Account.objects.filter(username=username).exists():
                account = Account.objects.get(username=username)
                
                if have_account == "y":
                    # connexion
                    context['have_account'] = True
                    context['balance'] = account.balance
                else:
                    context['exception'] = "Sorry, this account is already registed in our database"
            else:
                context['exception'] = "Sorry, this account doesn't exist"
        
    return render(request, 'bank_management/step_1.html', context)

def step_2(request: HttpRequest):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        create_account = request.POST.get('create_account')
        
        if create_account is None:
            context['exception'] = "Please choose an option"
        elif create_account == "y":
            if username == "":
                context['exception'] = "Please enter a name"
            else:
                    return redirect('step_3')

    return render(request, 'bank_management/step_2.html', context)


def step_3(request: HttpRequest):
    context = {}
    
    if request.method == "POST":
        deposit_amount = int(request.POST.get('deposit_amount'))
        if deposit_amount:
            account = Account.objects.get(username=request.user)
            account.balance += deposit_amount
            account.save()
            context['message'] = "Money has been deposited"

    return render(request, 'bank_management/step_3.html', context)

def bank_management(request: HttpRequest):
    context = {}
    return render(request, 'bank_management/bank_management.html', context)

def deposit(request: HttpRequest):
    context = {}
    
    if request.method == "POST":
        deposit_amount = int(request.POST.get('deposit_amount'))
        if deposit_amount:
                account = Account.objects.get(username=request.user)
                account.balance += deposit_amount
                account.save()
                context['deposit_amount'] = deposit_amount
                context['balance'] = account.balance
                
    return render(request, 'bank_management/deposit.html', context)

def withdraw(request: HttpRequest):
    context = {}
    
    if request.method == "POST":
        withdraw_amount = int(request.POST.get('withdraw_amount'))
        if withdraw_amount:
                account = Account.objects.get(username=request.user)
                account.balance -= withdraw_amount
                account.save()
                context['withdraw_amount'] = withdraw_amount
                context['balance'] = account.balance
    
    return render(request, 'bank_management/withdraw.html', context)

def balance(request: HttpRequest):
    context = {}
    account = Account.objects.get(username=request.user)
    context['balance'] = account.balance
    return render(request, 'bank_management/balance.html', context)

def details(request: HttpRequest):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        account = Account.objects.get(username=request.user)
        account.username = username
        account.save()
        context['message'] = True
    return render(request, 'bank_management/details.html', context)
    
def _logout(request: HttpRequest):
    logout(request)
    return redirect('home')
    
def delete(request: HttpRequest):
    Account.objects.filter(username=request.user).delete()
    logout(request)
    return redirect('home')
