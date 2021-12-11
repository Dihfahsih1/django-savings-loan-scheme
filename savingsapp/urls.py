from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from savingsapp import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^MemberAccountRegister/', views.MemberAccountRegister,
        name='MemberAccountRegister'),
    url(r'^Logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^Login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^Password-Reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
     name='password_reset'),
    url(r'^Done/Password-Reset', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^Complete/Password-Reset', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^Sacco-Account', views.sacco_account, name='sacco-account'),
    url(r'^Add-Member', views.add_member, name='add-member'), 
    url(r'^Edit-Member/(?P<pk>\d+)', views.edit_member, name='edit-member'),
    url(r'^Member-Details/(?P<pk>\d+)', views.view_member, name='view-member'),
    url(r'^Edit-Savings/(?P<pk>\d+)', views.edit_saving, name='edit-saving'),
    url(r'^Savings-delete-member/(?P<pk>\d+)', views.delete_member, name='delete-member'),
    url(r'^Member-Savings/(?P<pk>\d+)', views.view_savings, name='view-savings'),
    url(r'^All-Members', views.members_list, name='members-list'),
    url(r'^Record-Attendance', views.make_attendence, name='make-attendence'),
    url(r'^Attendance-History', views.attendence_history, name='attendence-history'),
    url(r'^Record-Savings', views.make_saving, name='make-saving'),
    url(r'^All-Savings', views.savings_list, name='savings-list'),
    
    url(r'^Record-Social-Fund', views.record_social_fund, name='record-social-fund'),
    url(r'^Social-Fund-List', views.social_fund_list, name='social-fund-list'),
    url(r'^Social-Funds-Routine/(?P<pk>\d+)', views.social_fund_routine, name='social-fund-routine'),
    url(r'^Manage-Cycles', views.add_cycle, name='add-cycle'),
    url(r'^Cycle-List', views.cycle_list, name='cycle-list'),
    url(r'^archiving-cycles', views.archiving_cycle, name='archive-cycle'),
    url(r'^Edit-Cycle/(?P<pk>\d+)', views.edit_cycle, name='edit-cycle'),
    path('activate/<str:uidb64>/<str:token>/',views.activate_email, name='activate'), 
    url(r'^Activate-Cycle/(?P<pk>\d+)', views.activate_cycle, name='activate-cycle'),
    url(r'^Savings-delete-cycle/(?P<pk>\d+)', views.delete_cycle, name='delete-cycle'),

    url(r'^Loan-Application', views.give_loan, name='give-loan'),
    url(r'^All-Loan-Repayments', views.list_loan_repayment, name='loan-list'),
    url(r'^All-Loans', views.all_loans_given, name='all-loans'),
    url(r'^Paying-Loan/(?P<pk>\d+)', views.pay_loan,name='pay-loan'),
    url(r'^Edit-Loan-Repayment/(?P<pk>\d+)', views.edit_loan_repayment, name='edit-loan-repayment'),
    url(r'^edit-loan/(?P<pk>\d+)', views.edit_loan, name='edit-loan'),
    url(r'^delete-loan-details/(?P<pk>\d+)', views.delete_loan, name='delete-loan'),
    
    url(r'^Add-Lookup', views.add_lookup, name='add-lookup'),
    url(r'^Lookup-Details', views.add_lookup_details, name='add-lookup-details'),
    url(r'^All-Look-Ups', views.list_lookup_details, name='list-lookup-details'),
    url(r'^stocks/', views.StockList.as_view()), 
    url(r'^Loan-Repayment/(?P<pk>\d+)', views.view_loan_repaymnets, name='loan-repayments'),
    ]
urlpatterns= format_suffix_patterns(urlpatterns)
