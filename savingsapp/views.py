from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.html')

def add_member(request):
    return render(request,'add_member.html')

def members_list(request):
    return render(request,'members_list.html')

def give_loan(request):
    return render(request,'loan_application.html')
def pay_loan(request):
    return render(request,'pay_loan.html')

def make_attendence(request):
    return render(request,'make_attendancy.html')
def attendence_history(request):
    return render(request,'view_attendancy.html')

def make_saving(request):
    return render(request,'make_saving.html')
def savings_list(request):
    return render(request,'savings_list.html')

def social_fund(request):
    return render(request,'social_fund.html')
