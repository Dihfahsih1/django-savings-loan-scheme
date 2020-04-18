from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from datetime import datetime, timedelta
import calendar

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

def make_attendence(request):
    if request.method=="POST":
        form=AttendanceForm(request.POST, request.FILES,)
        if form.is_valid():
            form.save()
            messages.success(request, f'Members Attendance For Today has been Made')
            return redirect('make-attendence')
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
