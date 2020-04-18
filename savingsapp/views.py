from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def add_member(request):
    if request.method=="POST":
        form=addmemberForm(request.POST, request.FILES,)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member has been successfully added to the system')
            return redirect('members-list')
    else:
        form=addmemberForm()
        return render(request,'add_member.html',{'form':form})

def edit_member(request, pk):
    item = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = addmemberForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Information has been updated')
            return redirect('members-list')
    else:
        form = addmemberForm(instance=item)
    return render(request, 'edit_members.html', {'form': form})

def members_list(request):
    all_members=CustomUser.objects.all()
    context = {
    'all_members':all_members
    }
    return render(request,'members_list.html', context)

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
