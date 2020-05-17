from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from savingsapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Add-Member', views.add_member, name='add-member'),
    path('Edit-Member/(?P<pk>\d+)', views.edit_member, name='edit-member'),
    path('Member-Details/(?P<pk>\d+)', views.view_member, name='view-member'),
    path('Edit-Savings/(?P<pk>\d+)', views.edit_saving, name='edit-saving'),
    path('Savings-delete-member/(?P<pk>\d+)', views.delete_member, name='delete-member'),
    path('Member-Savings/(?P<pk>\d+)', views.view_savings, name='view-savings'),
    path('All-Members', views.members_list, name='members-list'),
    path('Record-Attendance', views.make_attendence, name='make-attendence'),
    path('Attendance-History', views.attendence_history, name='attendence-history'),
    path('Record-Savings', views.make_saving, name='make-saving'),
    path('All-Savings', views.savings_list, name='savings-list'),
    path('Loan-Application', views.give_loan, name='give-loan'),
    path('Record-Social-Fund', views.record_social_fund, name='record-social-fund'),
    path('Social-Fund-List', views.social_fund_list, name='social-fund-list'),
    path('Social-Funds-Routine/(?P<pk>\d+)', views.social_fund_routine, name='social-fund-routine'),
    path('Add-Cycle', views.add_cycle, name='add-cycle'),
    path('Cycle-List', views.cycle_list, name='cycle-list'),
    path('archiving-cycles', views.archiving_cycle, name='archive-cycle'),
    path('Edit-Cycle/(?P<pk>\d+)', views.edit_cycle, name='edit-cycle'),
    path('Activate-Cycle/(?P<pk>\d+)', views.activate_cycle, name='activate-cycle'),
    path('Savings-delete-cycle/(?P<pk>\d+)', views.delete_cycle, name='delete-cycle'),
    path('All-Loans', views.list_loans, name='loan-list'),
    path('Paying-Loan/(?P<pk>\d+)', views.pay_loan, name='pay-loan'),
    path('edit-loan/(?P<pk>\d+)', views.edit_loan, name='edit-loan'),
    path('delete-loan-details/(?P<pk>\d+)', views.delete_loan, name='delete-loan'),
    path('Add-Lookup', views.add_lookup, name='add-lookup'),
    path('Lookup-Details', views.add_lookup_details, name='add-lookup-details'),
    path('All-Look-Ups', views.list_lookup_details, name='list-lookup-details'),
    path('stocks/', views.StockList.as_view()), 
    path('Loan-Repayment/(?P<pk>\d+)', views.view_loan_repaymnets, name='loan-repayments'),
    ]
urlpatterns= format_suffix_patterns(urlpatterns)
