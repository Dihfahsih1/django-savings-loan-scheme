from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
import calendar
from django.forms import modelformset_factory
from itertools import islice


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

def add_lookups(request):
    if request.method=="POST":
        form=LookUpsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'lookup has been successfully added to the system')
            return redirect('add-lookups')
    else:
        form=LookUpsForm()
        all_lookups=LookUps.objects.all()
        context = {'all_lookups':all_lookups, 'form': form}
        return render(request,'add_lookups.html',context)

def delete_lookup(request, pk):
    item= get_object_or_404(LookUps, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Lookup successfully deleted!")
        return redirect("add-lookups")

def edit_lookup(request, pk):
    item = get_object_or_404(LookUps, pk=pk)
    if request.method == "POST":
        form = LookUpsForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lookup Information has been updated')
            return redirect('add-lookups')
    else:
        form = LookUpsForm(instance=item)
    return render(request, 'edit_lookup.html', {'form': form})

def lookups_list(request):
    all_lookups=LookUps.objects.all()
    context = {
    'all_lookups':all_lookups
    }
    return render(request,'lookups_list.html', context)

def add_lookups_details(request):
    if request.method=="POST":
        form=LookUpsDetailsForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'lookup detail has been successfully added to the system')
            return redirect('details')
    else:
        all_lookups=LookupsDetails.objects.all()
        form=LookUpsDetailsForm()
        context = {
        'all_lookups':all_lookups, 'form': form
        }
        return render(request,'add_lookups_details.html',context)

def lookups_list_details(request):
    all_lookups=LookupsDetails.objects.all()
    context = {
    'all_lookups':all_lookups
    }
    return render(request,'lookups_list_details.html', context)

def delete_lookup_details(request, pk):
    item= get_object_or_404(LookupsDetails, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Lookup Details successfully deleted!")
        return redirect("details")

def edit_lookup_details(request, pk):
    item = get_object_or_404(LookupsDetails, pk=pk)
    if request.method == "POST":
        form = LookUpsDetailsForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lookup Details Information has been updated')
            return redirect('details')
    else:
        form = LookUpsDetailsForm(instance=item)
    return render(request, 'edit_lookup_details.html', {'form': form})

def make_attendence(request):
    objs = CustomUser.objects.count()
    #AttendanceFormset=modelformset_factory(Attendance, form=AttendanceForm, extra=0)
    if request.method == 'POST':
        formset = AttendanceForm(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('attendence-history')
        else:
            print (formset.errors)
    else:
        formset =  AttendanceForm()
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
    return render(request,'make_saving.html')
def savings_list(request):
    return render(request,'savings_list.html')

def social_fund(request):
    return render(request,'social_fund.html')
