from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from datetime import date
import calendar
from django.db.models import Q
from django.forms import modelformset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import StockSerializer

class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)


def index(request):
    return render(request,'index.html')

#record member
def add_member(request):
    all_members = CustomUser.objects.all()
    if request.method=="POST":
        fname=request.POST.get('first_name')
        lname = request.POST.get('last_name')
        form=MemberForm(request.POST, request.FILES,)
        print(form)
        if form.is_valid():
            for i in all_members:
                if(i.first_name == fname and i.last_name == lname):
                    return HttpResponse('Member With those Names Already Exists')
            form.save()
            messages.success(request, f'Member has been successfully added to the system')
            return redirect('add-member')
    form=MemberForm()
    context={'form':form, 'all_members':all_members}
    return render(request,'add_member.html',context)

#edit member
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

#delete Member
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

#add new cycle
def add_cycle(request):
    if request.method=="POST":
        form=CyclesForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cycle has been successfully added to the system')
            return redirect('add-cycle')
    else:
        form=CyclesForm()
        all_cycle=Cycle.objects.all()
        context = {'all_cycle':all_cycle, 'form': form}
        return render(request,'add_cycle.html',context)

#deleting cycle
def delete_cycle(request, pk):
    item= get_object_or_404(Cycles, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Cycle successfully deleted!")
        return redirect("add-cycle")

#editting cycle
def edit_cycle(request, pk):
    item = get_object_or_404(Cycle, pk=pk)
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
    all_cycle=Cycle.objects.all()
    today = date.today()
    for i in all_cycle:
        end_cycle = i.cycle_period_end
        if(today >= end_cycle):
            i.is_active ='False'
            i.save()
            return redirect('cycle-list')
        return redirect('cycle-list')   

#list of cycles          
def cycle_list(request):
    all_cycle=Cycle.objects.all()
    context = {
    'all_cycle':all_cycle
    }
    return render(request,'cycle_list.html', context)


#record member attendance
def make_attendence(request):
    if request.method == 'POST':
        todate = request.POST.get('date')
        tostate = request.POST.getlist('status')
        for i in tostate:
            status_id = i
            member_id=CustomUser.objects.filter(id=status_id)
            for j in member_id:
                tostatus='Present'
                tofullname = str(j.first_name )+ " " + str(j.last_name)
                Attendance.objects.create(date=todate, status=tostatus, full_name=tofullname)
        return redirect('attendence-history')
    all_members = CustomUser.objects.all()
    context={'all_members':all_members}
    return render(request,'make_attendance.html',context)

#attendance history
def attendence_history(request):
    today = datetime.now()
    years=today.year
    a_month=today.month
    a_day=today.day
    if request.method == 'POST':
        years = request.POST['attendance_year']
        a_month = request.POST['attendance_month']
        # a_day = request.POST['attendance_day']
        all_attendance = Attendance.objects.filter(date__month=a_month, date__year=years)
        mth=int(a_month)
        month=calendar.month_name[mth]
        context = {'all_attendance': all_attendance,'a_day':a_day,'a_month':a_month, 'years': years,'today': today,'month': month}
        return render(request, "view_attendance.html", context)
    mth=int(a_month)
    month=calendar.month_name[mth]
    context = {'years': years, 'month':month,'a_month':a_month}
    return render(request, "view_attendance.html", context)

#record member savings
def make_saving(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST or None, request.FILES or None)
        print(form.errors)
        if form.is_valid:
            form.save()
            return redirect('make-saving')
    current_cycle = Cycle.objects.filter(is_active=True)
    for i in current_cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
    all_savings = Saving.objects.filter(date__range=(startdate, enddate)).order_by('-date')
    form =SavingsForm()
    cycle = Cycle.objects.get(is_active=True)
    context={'form':form, 'all_savings':all_savings,'cycle':cycle}         
    return render(request,'make_saving.html', context)

#list of all member savings
def savings_list(request):    
    try: 
        all_members=CustomUser.objects.all()
        current_cycle=Cycle.objects.get(is_active=True)
        cycles = Cycle.objects.filter(is_active=True)
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

 #savings for a single member       
def view_savings(request,pk):
    get_member = CustomUser.objects.get(id=pk)
    get_all_members=CustomUser.objects.all()
    current_cycle=Cycle.objects.get(is_active=True) 
    cycles = Cycle.objects.filter(is_active=True)
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
    
def give_loan(request):
    context={}
    if request.method == 'POST':
        form = LoanForm(request.POST, request.FILES)
        if form.is_valid:
            print(form.errors)
            loan = form.save(commit=False)
            loan.save() 
            return redirect('loan-list')
    current_cycle=Cycle.objects.get(is_active=True)
    context['current_cycle']=current_cycle
    if current_cycle:
        rates=Cycle.objects.all()
        for i in rates:
            rate=i.rate
            context['rate']=rate
    form = LoanForm()
    context['form']=form
    all_members=CustomUser.objects.all()
    context['all_members']=all_members
    
    return render(request,'loan_application.html', context)
def edit_loan(request, pk):
    item = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        form = EditLoanForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Loan Details have been updated')
            return redirect('loan-list')
    else:
        form = EditLoanForm(instance=item)
        rate = item.interest_rate
        date = item.date
        period = item.loan_period
        amount = item.amount
        context={'form':form, 'amount':amount, 'rate':rate, 'date':date, 'period':period}
        return render(request, 'edit_loan.html', context)
#deleting cycle
def delete_loan(request, pk):
    item= get_object_or_404(Loan, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Loan successfully deleted!")
        return redirect("loan-list")

def list_loans(request):
    current_cycle = Cycle.objects.filter(is_active=True)
    for i in current_cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
    loan_list = Loan.objects.filter(date__range=(startdate, enddate))
    context={'loan_list':loan_list}
    return render(request, 'list_loans.html', context)

def pay_loan(request, pk):
    items = get_object_or_404(Loan,pk=pk)
    if request.method == "POST":
        form = PayingLoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan-list')
    else:
        form = LoanForm(instance=items)
        name=(items.name)
        loan_id=(items.id)
        context={'form':form, 'name':name, 'loan_id':loan_id}
        return render(request,'pay_loan.html',context)

#view single loan repayments        
def view_loan_repaymnets(request, pk):
    context = {}
    al=CustomUser.objects.all()
    get_loan_id=PayingLoan.objects.filter(loan_id=pk)
    sum_repayments = get_loan_id.aggregate(totals=models.Sum("amount"))
    total_amount = sum_repayments["totals"]
    loan_list = Loan.objects.all()
    paginator = Paginator(loan_list, 10)  # 10 loanees on each page
    page = request.GET.get('page')
    try:
        members_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        members_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        members_list = paginator.page(paginator.num_pages)
    context['page'] = page
    context['members_list'] = members_list
    context['get_loan_id'] = get_loan_id
    context['total_amount'] = total_amount
    for i in al:
        if(i.first_name !=None and i.last_name !=None):
            nam = i.first_name + " " + i.last_name
            for k in get_loan_id:
                name = k.name
                if (name == nam):
                    get_loan = Loan.objects.get(id=k.loan_id)
                    loaned_amount = get_loan.amount
                    context['loaned_amount'] = loaned_amount
                    context['name']=name
    return render(request, 'view_loan_repaymnets.html', context)

#add new lookup
def add_lookup(request):
    if request.method == "POST":
        form=LookupForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'look up has been successfully added to the system')
            return redirect('add-lookup')
            
    else:
        form=LookupForm()
        all_lookups=LookUp.objects.all()
        context = {'form': form, 'all_lookups':all_lookups}
        return render(request,'add_lookup.html',context)

#add new lookup Details
def add_lookup_details(request):
    if request.method=="POST":
        form=LookupDetailsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'look up details has been successfully added to the system')
            return redirect('add-lookup-details')
    else:
        form=LookupDetailsForm()
        all_lookups_details=LookupDetail.objects.all()
        context = {'form': form, 'all_lookups_details':all_lookups_details}
        return render(request,'add_lookup_details.html',context)        

#list of cycles          
def list_lookup_details(request):
    all_lookups_details=LookupDetail.objects.all()
    context = {
    'all_lookups_details':all_lookups_details
    }
    return render(request,'list_lookup_details.html', context)        

def record_social_fund(request):
    if request.method == 'POST':
        todate = request.POST.get('date')
        tostate = request.POST.getlist('status')
        for i in tostate:
            status_id = i
            member_id = CustomUser.objects.filter(id=status_id)
            for j in member_id:
                toAmount = 1000
                tofullname = str(j.first_name) + " " + str(j.last_name)
                SocialFund.objects.create(date=todate, social_fund=toAmount, full_name=tofullname)
        return redirect('social-fund-list')
    all_members = CustomUser.objects.all()
    context={'all_members':all_members}
    return render(request,'record_social_fund.html',context)

def social_fund_list(request):
    current_cycle = Cycle.objects.get(is_active=True)
    all_members = CustomUser.objects.all()
    context = {'all_members': all_members, 'current_cycle': current_cycle}
    return render(request, 'social_fund_list.html', context)

 

#display social fund contrbution routine
def social_fund_routine(request, pk):
    get_member = CustomUser.objects.get(id=pk)
    name=(get_member.first_name + " " + get_member.last_name)
    get_all_members = CustomUser.objects.all()
    current_cycle = Cycle.objects.get(is_active=True)

    cycles = Cycle.objects.filter(is_active=True)
    for i in cycles:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end  

    get_contributions = SocialFund.objects.filter(full_name=name, date__range=(startdate, enddate))
    all_contributions = get_contributions.aggregate(totals=models.Sum("social_fund"))
    total_amount = all_contributions["totals"]

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
    context = {'current_cycle': current_cycle, 'total_amount': total_amount,
                'get_contributions': get_contributions, 'get_member': get_member, 'page': page, 'members_list': members_list}
    return render(request, 'social_funds_routine.html', context)
