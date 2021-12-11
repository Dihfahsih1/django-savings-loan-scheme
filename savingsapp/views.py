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
from django.contrib.auth.decorators import login_required
from .tokens import account_activation_token  
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_text    

class StockList(APIView):
    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

def MemberAccountRegister(request):
    members = CustomUser.objects.all()
    if request.method == 'POST':
        form = MembershipAccountForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            current_site = get_current_site(request)  
            mail_subject = 'Activate your account.'  
            message = render_to_string('acc_active_email.html', {  
                'member': member,  
                'domain': current_site.domain,  
                'uid': urlsafe_base64_encode(force_bytes(member.pk)),  
                'token': account_activation_token.make_token(member),  
                }) 
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                mail_subject, message, to=[to_email]  
            )  
            email.send()
            username = form.cleaned_data.get('username')
            context={'member':member}
            return render(request, 'activation_email_sent.html', context) 
    else:
        form = MembershipAccountForm()
        url_passed = request.path_info
        context={'form': form, 'members': members, 'url_passed':url_passed}
        return render(request, 'membershipaccount.html', context)


#activate your email address
def activate_email(request, uidb64, token):
    try:  
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        member = CustomUser.objects.get(id=uid)  
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):  
        member = None  
    if member is not None and account_activation_token.check_token(member, token): 
        member.is_active=True
        member.save()
        context={'full_name':member}
        return render(request, 'email_confirmed.html', context)  
    else:  
        return HttpResponse('Activation link is invalid!')
def index(request):
    #messages.success(request, f'Welcome to Kisajja Kikulu Savings Sacco')
    return render(request,'index.html')

#record member
@login_required
def add_member(request):
    current_cycle = Cycle.objects.get(is_active=True)
    all_members = Member.objects.filter(is_active=True)
    if request.method=="POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        form=MemberForm(request.POST, request.FILES,)
        if form.is_valid():
            for i in all_members:
                if(i.first_name == fname and i.last_name == lname):
                    return HttpResponse('Member With those Names Already Exists')
            form.save()
            messages.success(request, f'Member has been successfully added to the system')
            return redirect('add-member')
    form=MemberForm()
    context={'form':form, 'all_members':all_members, 'current_cycle':current_cycle}
    return render(request,'add_member.html',context)

#edit member
@login_required
def edit_member(request, pk):
    item = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Information has been updated')
            return redirect('members-list')
    else:
        form = MemberForm(instance=item)
        name=item.first_name +' '+ item.last_name
    context = {'form': form, 'name':name}
    return render(request, 'edit_members.html', context)

#delete Member
@login_required
def delete_member(request, pk):
    if request.method == "GET":
        item = Member.objects.get(is_active=True, id=pk)
        item.is_active='False'
        item.save()
        messages.success(request, "Member successfully deleted!")
        return redirect("members-list")

#list of members in the current cycle.
@login_required
def members_list(request):
    current_cycle = Cycle.objects.get(is_active=True)
    all_members=Member.objects.filter(is_active=True)
    context = {
        'all_members': all_members, 'current_cycle': current_cycle
    }
    return render(request,'members_list.html', context)

#view members
@login_required
def view_member(request, pk):
    current_cycle = Cycle.objects.get(is_active=True)
    member_details=Member.objects.filter(id=pk)
    context = {
        'member_details': member_details, 'current_cycle': current_cycle
    }
    return render(request,'view_member.html', context)

#add new cycle
@login_required
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
@login_required
def delete_cycle(request, pk):
    item= get_object_or_404(Cycles, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Cycle successfully deleted!")
        return redirect("add-cycle")

#editting cycle
@login_required
def edit_cycle(request, pk):
    item = get_object_or_404(Cycle, pk=pk)
    if request.method == "POST":
        form = EditCycleForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cycle Information has been updated')
            return redirect('add-cycle')
    else:
        form = EditCycleForm(instance=item)
    return render(request, 'edit_cycle.html', {'form': form})

#Activate a cycle
@login_required
def activate_cycle(request, pk):
    if request.method == "GET":
        Cycle.objects.update(is_active=False)
        Cycle.objects.filter(id=pk).update(is_active=True)
        messages.success(request, f'New Cycle has been Activated')
        return redirect('add-cycle')

#archive the saving at exactly the end 
@login_required
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
@login_required
def cycle_list(request):
    all_cycle=Cycle.objects.all()
    context = {
    'all_cycle':all_cycle
    }
    return render(request,'cycle_list.html', context)


#record member attendance
@login_required
def make_attendence(request):
    current_cycle = Cycle.objects.get(is_active=True)
    if request.method == 'POST':
        todate = request.POST.get('date')
        tostate = request.POST.getlist('status')
        for i in tostate:
            status_id = i
            member_id=Member.objects.filter(id=status_id)
            for j in member_id:
                tostatus='Present'
                tofullname = str(j.first_name )+ " " + str(j.last_name)
                Attendance.objects.create(date=todate, status=tostatus, full_name=tofullname)
        messages.success(request, f'Attendance has been succefully recorded')
        return redirect('attendence-history')
    all_members = Member.objects.all()
    context={'all_members':all_members, 'current_cycle':current_cycle}
    return render(request,'make_attendance.html',context)

#attendance history
@login_required
def attendence_history(request):
    current_cycle = Cycle.objects.get(is_active=True)
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
        context = {'current_cycle':current_cycle, 'all_attendance': all_attendance,'a_day':a_day,'a_month':a_month, 'years': years,'today': today,'month': month}
        return render(request, "view_attendance.html", context)
    mth=int(a_month)
    month=calendar.month_name[mth]
    context = {'years': years, 'month':month,'a_month':a_month, 'current_cycle':current_cycle}
    return render(request, "view_attendance.html", context)

#record member savings
@login_required
def make_saving(request):
    if request.method == 'POST':
        form = SavingsForm(request.POST or None, request.FILES or None)
        if form.is_valid:
            form.save()
            messages.success(request, f'Savings of the member has been Recorded')
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
@login_required
def savings_list(request):    
    try: 
        all_members=Member.objects.all()
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
        all_members=Member.objects.all()
        context={'all_members':all_members}
        return render(request,'savings_list.html',context)

 #savings for a single member       


@login_required
def view_savings(request,pk):
    get_member = Member.objects.get(id=pk)
    get_all_members=Member.objects.all()
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

#edit a single savings transaction
@login_required
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
        name=item.name
        context={'form':form, 'name':name}
        return render(request, 'edit_saving.html', context)

#Loan Application    
@login_required
def give_loan(request):
    context={}
    if request.method == 'POST':
        form = LoanForm(request.POST, request.FILES)
        if form.is_valid:
            loan = form.save(commit=False)
            loan.save() 
            messages.success(request, f'Member Loan Application has been recorded')
            return redirect('all-loans')
    current_cycle=Cycle.objects.get(is_active=True)
    context['current_cycle']=current_cycle
    if current_cycle:
        rates=Cycle.objects.all()
        for i in rates:
            rate=i.rate
            context['rate']=rate
    form = LoanForm()
    context['form']=form
    all_members=Member.objects.all()
    context['all_members']=all_members
    return render(request,'loan_application.html', context)

#edit loan
@login_required
def edit_loan(request, pk):
    current_cycle = Cycle.objects.get(is_active=True)
    item = get_object_or_404(Loan, pk=pk)
    name=item.name
    if request.method == "POST":
        form = EditLoanForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Loan Details have been updated')
            return redirect('all-loans')
    else:
        form = EditLoanForm(instance=item)
        rate = item.interest_rate
        date = item.date
        period = item.loan_period
        amount = item.amount
        context = {'form': form, 'amount': amount, 'rate': rate, 'name': name,
                   'date': date, 'period': period, 'current_cycle': current_cycle}
        return render(request, 'edit_loan.html', context)

#deleting cycle
@login_required
def delete_loan(request, pk):
    item= get_object_or_404(Loan, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Loan successfully deleted!")
        return redirect("loan-list")

#list of loan repayments
@login_required
def list_loan_repayment(request):
    cycle = Cycle.objects.filter(is_active=True)
    for i in cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
    loan_list = Loan.objects.filter(date__range=(startdate, enddate))
    context={'loan_list':loan_list}
    return render(request, 'loan_repayments_list.html', context)

#all loans given out
@login_required
def all_loans_given(request):
    cycle = Cycle.objects.filter(is_active=True)
    for i in cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
    loan_list = Loan.objects.filter(date__range=(startdate, enddate))
    context = {'loan_list': loan_list}
    return render(request, 'all_loans_given.html', context)

#Loan Repayments
@login_required
def pay_loan(request, pk):
    context={}
    current_cycle=Cycle.objects.get(is_active=True)
    items = get_object_or_404(Loan,pk=pk)
    if request.method == "POST":
        amount_paid = request.POST.get('amount')
        results = PayingLoan.objects.filter(loan_id=items.id).aggregate(totals=models.Sum("amount"))
        if (results['totals'])!=None:
            totalPaid = results["totals"]
        else:
            totalPaid = 0
        toTotalPaid = totalPaid + int(amount_paid)
        interest = ((items.interest_rate / 100) *items.loan_period * items.amount)
        toBalance = (items.amount + interest) - toTotalPaid
        if toBalance == 0:
            Toloan_status = 'SETTLED'
            #PayingLoan.objects.filter(loan_id=pk).update( total_paid=toTotalPaid, balance=toBalance, loan_status=Toloan_status)
            items = PayingLoan.objects.filter(loan_id=pk)
            for i in items:
                i.total_paid = toTotalPaid
                i.balance = toBalance
                i.loan_status = Toloan_status
                i.save()
        else:
            Toloan_status = 'RUNNING'
            items=PayingLoan.objects.filter(loan_id=pk)
            for i in items:
                i.total_paid = toTotalPaid
                i.balance = toBalance
                i.loan_status = Toloan_status
                i.save()
            # update(total_paid=toTotalPaid, balance=toBalance, loan_status=Toloan_status)
            
        context['toTotalPaid'] = toTotalPaid
        context['toBalance'] = toBalance
        form = PayingLoanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Member Loan Repayment has been recorded')
            return redirect('loan-repayments', pk=pk)
    else:
        form = LoanForm(instance=items)
        name=(items.name)
        loan_id=(items.id)
        loan_balance=Loan.objects.filter(id=pk)
        context['loan_balance'] = loan_balance
        context['form'] = form
        context['name'] = name
        context['loan_id'] = loan_id
        context['current_cycle'] = current_cycle
        return render(request,'pay_loan.html',context)


#Edit Loan Repayment 
@login_required
def edit_loan_repayment(request, pk):
    current_cycle = Cycle.objects.get(is_active=True)
    item = get_object_or_404(PayingLoan, pk=pk)
    name = item.name
    if request.method == "POST":
        form = PayingLoanForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Loan Repayment Details have been updated')
            return redirect('loan-list')
    else:
        form = PayingLoanForm(instance=item)
        name=item.name
        context = {'form': form,'current_cycle': current_cycle, 'name':name}
        return render(request, 'edit_loan_repayment.html', context)

#view single loan repayments    
@login_required
def view_loan_repaymnets(request, pk):
    context = {}
    al = Member.objects.all()
    if PayingLoan.objects.filter(loan_id=pk).exists():
        get_loan_id = PayingLoan.objects.filter(loan_id=pk).order_by('-date')
        for p in get_loan_id:
            repayment_balance=p.balance
            context['repayment_balance']=repayment_balance
        for i in al:
            if(i.first_name != None and i.last_name != None):
                nam = i.first_name + " " + i.last_name
                for k in get_loan_id:
                    name = k.name
                    get_loan = Loan.objects.get(id=k.loan_id)
                    loaned_amount = get_loan.amount
                    context['name'] = name
                    context['loaned_amount'] = loaned_amount                        
    else:
        get_loan_details = Loan.objects.get(id=pk)
        context = {'get_loan_details': get_loan_details}
        return render(request,'no_repayments_made.html', context)    
    sum_repayments = get_loan_id.aggregate(totals=models.Sum("amount"))
    total_amount = sum_repayments["totals"]
    loan_list = Loan.objects.all()
    cycle = Cycle.objects.filter(is_active=True)
    for i in cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
    loan_list = Loan.objects.filter(date__range=(startdate, enddate))
    paginator = Paginator(loan_list, 10)  #items per page
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
    return render(request, 'view_loan_repaymnets.html', context)

#add new lookup
@login_required
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
@login_required
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
@login_required        
def list_lookup_details(request):
    all_lookups_details=LookupDetail.objects.all()
    context = {
    'all_lookups_details':all_lookups_details
    }
    return render(request,'list_lookup_details.html', context)        


#RECORDING SOCIAL FUND
@login_required
def record_social_fund(request):
    current_cycle = Cycle.objects.get(is_active=True)
    if request.method == 'POST':
        todate = request.POST.get('date')
        tostate = request.POST.getlist('status')
        for i in tostate:
            status_id = i
            member_id = Member.objects.filter(id=status_id)
            for j in member_id:
                toAmount = 1000
                tofullname = str(j.first_name) + " " + str(j.last_name)
                SocialFund.objects.create(date=todate, social_fund=toAmount, full_name=tofullname)
        messages.success(request, f'Member Social Fund Contributions have been recorded')
        return redirect('social-fund-list')
    all_members = Member.objects.all()
    context={'all_members':all_members, 'current_cycle':current_cycle}
    return render(request,'record_social_fund.html',context)

#list of social funds
@login_required
def social_fund_list(request):
    current_cycle = Cycle.objects.get(is_active=True)
    all_members = Member.objects.all()
    context = {'all_members': all_members, 'current_cycle': current_cycle}
    return render(request, 'social_fund_list.html', context)


#display social fund contrbution routine
@login_required
def social_fund_routine(request, pk):
    get_member = Member.objects.get(id=pk)
    name=(get_member.first_name + " " + get_member.last_name)
    get_all_members = Member.objects.all()
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


#Total money in the sacco
def sacco_account(request):
    current_cycle = Cycle.objects.filter(is_active=True)
    for i in current_cycle:
        startdate = i.cycle_period_start
        enddate = i.cycle_period_end
        results_registration = Member.objects.filter(joining_date__range=(startdate, enddate)).aggregate(totals=models.Sum("application_fee"))
        if (results_registration["totals"])!=None:
            total_registration = results_registration["totals"]
        else:
            total_registration = 0

        results_savings = Saving.objects.filter(date__range=(startdate, enddate)).aggregate(totals=models.Sum("amount"))
        if (results_savings["totals"]) != None:
            total_savings = results_savings["totals"]
        else:
            total_savings = 0

        results_social = SocialFund.objects.filter(date__range=(startdate, enddate)).aggregate(totals=models.Sum("social_fund"))
        if (results_social["totals"]) != None:
            total_social = results_social["totals"]
        else:
            total_social = 0

        results_repayments = PayingLoan.objects.filter(date__range=(startdate, enddate)).aggregate(totals=models.Sum("amount"))
        if (results_repayments["totals"]) != None:
            total_repayments = results_repayments["totals"]
        else:
            total_repayments = 0

        results_loan_given = Loan.objects.filter(date__range=(startdate, enddate)).aggregate(totals=models.Sum("amount"))
        if (results_loan_given["totals"]) != None:
            total_loan_given = results_loan_given["totals"]
        else:
            total_loan_given = 0
        total_amount = (total_registration + total_savings + total_social + total_repayments) - total_loan_given
        context = {'total_registration': total_registration, 'total_savings': total_savings,
                    'total_social': total_social, 'total_repayments': total_repayments, 'total_loan_given': total_loan_given, 'total_amount':total_amount}   
    return render(request, 'sacco_account.html', context)
