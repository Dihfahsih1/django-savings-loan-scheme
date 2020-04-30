from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import date
import calendar
from django.forms import modelformset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage




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

#archive the saving at exactly the end    
def archiving_cycle(request):
    all_cycle=SavingCycle.objects.all()
    today = date.today()
    for i in all_cycle:
        end_cycle = i.cycle_period_end
        if(today >= end_cycle):
            i.is_active ='False'
            i.save()
            return redirect('cycle-list')
        return redirect('cycle-list')   
          
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
    current_cycle=SavingCycle.objects.get(is_active=True)
    all_savings=Saving.objects.filter(cycle=current_cycle)
    form =SavingsForm()        
    context={'cycle':cycle,'form':form, 'all_savings':all_savings}         
    return render(request,'make_saving.html', context)


def savings_list(request):    
    try: 
        all_members=CustomUser.objects.all()
        current_cycle=SavingCycle.objects.get(is_active=True)
        cycles = SavingCycle.objects.filter(is_active=True)
        for i in cycles:
            startdate= i.cycle_period_start
            enddate= i.cycle_period_end
            all_savings =Saving.objects.filter(date__range=(startdate, enddate)).aggregate(totals=models.Sum("amount"))
            total_amount = all_savings["totals"]
            context={'total_amount':total_amount,'current_cycle':current_cycle, 'all_members':all_members}
            return render(request,'savings_list.html',context)
    except:
        all_members=CustomUser.objects.all()
        context={'all_members':all_members}
        return render(request,'savings_list.html',context)
def view_savings(request,pk):
    get_member = CustomUser.objects.get(id=pk)
    get_all_members=CustomUser.objects.all()
    current_cycle=SavingCycle.objects.get(is_active=True) 
    cycles = SavingCycle.objects.filter(is_active=True)
    for i in cycles:
        startdate= i.cycle_period_start
        enddate= i.cycle_period_end 
    get_savings = Saving.objects.filter(name=pk, date__range=(startdate, enddate))
    all_savings =get_savings.aggregate(totals=models.Sum("amount"))
    total_amount = all_savings["totals"]

    paginator = Paginator(get_all_members, 10)  # 10 members on each page
    page = request.GET.get('page')
    try:
        members_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        members_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        members_list = paginator.page(paginator.num_pages) 
    context={'current_cycle':current_cycle,'total_amount':total_amount,'get_savings':get_savings, 'get_member':get_member, 'page':page, 'members_list': members_list}
    return render (request, 'view_savings.html', context)

def edit_saving(request, pk):
    item = get_object_or_404(Saving, pk=pk)
    if request.method == "POST":
        form = SavingsForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Saving has been updated')
            return redirect('make-saving')
    else:
        form = SavingsForm(instance=item)
        context={'form':form}
        return render(request, 'edit_saving.html', context)
def social_fund(request):
    return render(request,'social_fund.html')
