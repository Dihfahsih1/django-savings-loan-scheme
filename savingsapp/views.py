from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
import calendar
from django.forms import modelformset_factory



def index(request):
    return render(request,'index.html')

def add_member(request):
    if request.method=="POST":
        form=MemberForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member has been successfully added to the system')
            return redirect('members-list')
    else:
        form=MemberForm()
        return render(request,'add_member.html',{'form':form})

def edit_member(request, pk):
    item = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Information has been updated')
            return redirect('members-list')
    else:
        form = MemberForm(instance=item)
    return render(request, 'edit_members.html', {'form': form})

def delete_member(request, pk):
    item= get_object_or_404(CustomUser, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Member successfully deleted!")
        return redirect("members-list")

def members_list(request):
    all_members=CustomUser.objects.all()
    context = {
    'all_members':all_members
    }
    return render(request,'members_list.html', context)

def view_member(request, pk):
    member_details=CustomUser.objects.filter(id=pk)
    context = {
    'member_details':member_details
    }
    return render(request,'view_member.html', context)

def give_loan(request):
    return render(request,'loan_application.html')
def pay_loan(request):
    return render(request,'pay_loan.html')

def add_cycle(request):
    if request.method=="POST":
        form=CyclesForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cycle has been successfully added to the system')
            return redirect('add-cycle')
    else:
        form=CyclesForm()
        all_cycle=SavingCycle.objects.all()
        context = {'all_cycle':all_cycle, 'form': form}
        return render(request,'add_cycle.html',context)

def delete_cycle(request, pk):
    item= get_object_or_404(Cycles, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Cycle successfully deleted!")
        return redirect("add-cycle")

def edit_cycle(request, pk):
    item = get_object_or_404(SavingCycle, pk=pk)
    if request.method == "POST":
        form = CyclesForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cycle Information has been updated')
            return redirect('add-cycle')
    else:
        form = CyclesForm(instance=item)
    return render(request, 'edit_cycle.html', {'form': form})

def cycle_list(request):
    all_cycle=SavingCycle.objects.all()
    context = {
    'all_cycle':all_cycle
    }
    return render(request,'cycle_list.html', context)



def make_attendence(request):
    objs = CustomUser.objects.count()
    AttendanceFormset=modelformset_factory(Attendance, form=AttendanceForm, extra=0)
    if request.method == 'POST':
        formset = AttendanceFormset(request.POST, request.FILES)
        if formset.is_valid():
            print(formset)
            formset.save()
            return redirect('attendence-history')
        else:
            print (formset.errors)
    else:
        formset =  AttendanceFormset()
    all_members = CustomUser.objects.all()
    context={'formset':formset, 'all_members':all_members}
    return render(request,'make_attendance.html',context)


    # if request.method=="POST":
    #     formset=AttendanceForm(request.POST)
    #     if formset.is_valid():
    #         instances = formset.save(commit=False)
    #         instances.save()
    #         return redirect('make-attendence')
    # else:
    #     formset=AttendanceForm()
    #     all_members=CustomUser.objects.all()
    #     context={'formset':formset,'all_members':all_members}
    #     return render(request,'make_attendance.html',context)

def attendence_history(request):
    today = datetime.now()
    years=today.year
    a_month=today.month
    if request.method == 'POST':
        years = request.POST['attendance_year']
        a_month = request.POST['attendance_month']
        all_attendance = Attendance.objects.filter( date__month=a_month, date__year=years)
        mth=int(a_month)
        month=calendar.month_name[mth]
        context = {'all_attendance': all_attendance,'a_month':a_month, 'years': years,'today': today,'month': month}
        return render(request, "view_attendance.html", context)
    mth=int(a_month)
    month=calendar.month_name[mth]
    context = {'years': years, 'month':month,'a_month':a_month}
    return render(request, "view_attendance.html", context)

def make_saving(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST, request.FILES)
        if form.is_valid:
            savings = form.save(commit=False)
            savings.save() 
    cycle=SavingCycle.objects.all()
    form =SavingsForm()        
    context={'cycle':cycle,'form':form}         
    return render(request,'make_saving.html', context)
def savings_list(request):
    return render(request,'savings_list.html')

def social_fund(request):
    return render(request,'social_fund.html')
