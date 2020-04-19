from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
import calendar

def index(request):
    return render(request,'index.html')

def add_member(request):
    if request.method=="POST":
        form=MemberForm(request.POST, request.FILES,)
        print(form)
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
            return redirect('lookups-details-list')
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
    item= get_object_or_404(LookUpsDetails, id=pk)
    if request.method == "GET":
        item.delete()
        messages.success(request, "Lookup Details successfully deleted!")
        return redirect("lookups-details-list")

def edit_lookup_details(request, pk):
    item = get_object_or_404(LookUpsDetails, pk=pk)
    if request.method == "POST":
        form = LookUpsDetailsForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lookup Details Information has been updated')
            return redirect('lookups-details-list')
    else:
        form = LookUpsDetailsForm(instance=item)
    return render(request, 'edit_lookup.html', {'form': form})

def make_attendence(request):
    if request.method=="POST":
        form=AttendanceForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Members Attendance For Today has been Made')
            return redirect('attendence-history')
    else:
        form=AttendanceForm()
        all_members=CustomUser.objects.all()
        context={'form':form, 'all_members':all_members}
        return render(request,'make_attendance.html',context)

def attendence_history(request):
    today = datetime.now()
    years=today.year
    if request.method == 'POST':
        a_year = request.POST['attendance_year']
        a_month = request.POST['attendance_month']
        all_attendance = Attendance.objects.filter( date__month=a_month, date__year=a_year)
        mth=int(a_month)
        month=calendar.month_name[mth]
        context = {'all_attendance': all_attendance,'years': years,'today': today,
                  'a_year':a_year,'a_month': a_month}
        return render(request, "view_attendance.html", context)
    context = {'years': years}
    return render(request, "view_attendance.html", context)

def make_saving(request):
    return render(request,'make_saving.html')
def savings_list(request):
    return render(request,'savings_list.html')

def social_fund(request):
    return render(request,'social_fund.html')
