from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from savingsapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Savings-add-member', views.add_member, name='add-member'),
    url(r'^Savings-edit-member/(?P<pk>\d+)', views.edit_member, name='edit-member'),
    url(r'^Savings-view-member/(?P<pk>\d+)', views.view_member, name='view-member'),
    url(r'^Savings-edit-saving/(?P<pk>\d+)', views.edit_saving, name='edit-saving'),
    url(r'^Savings-delete-member/(?P<pk>\d+)', views.delete_member, name='delete-member'),
    url(r'^view-savings/(?P<pk>\d+)', views.view_savings, name='view-savings'),
    url(r'^Savings-members-list', views.members_list, name='members-list'),
    url(r'^Savings-make-attendence', views.make_attendence, name='make-attendence'),
    url(r'^Savings-attendence-history', views.attendence_history, name='attendence-history'),
    url(r'^Savings-make-saving', views.make_saving, name='make-saving'),
    url(r'^Savings-savings-list', views.savings_list, name='savings-list'),
    url(r'^Savings-pay-loan', views.pay_loan, name='pay-loan'),
    url(r'^Savings-give-loan', views.give_loan, name='give-loan'),
    url(r'^Savings-social-fund', views.record_social_fund, name='record-social-fund'),
    url(r'^Social-fund-list', views.social_fund_list, name='social-fund-list'),
    url(r'^Savings-add-cycle', views.add_cycle, name='add-cycle'),
    url(r'^Savings-cycle-list', views.cycle_list, name='cycle-list'),
    url(r'^archiving-cycles', views.archiving_cycle, name='archive-cycle'),
    url(r'^Savings-edit-cycle/(?P<pk>\d+)', views.edit_cycle, name='edit-cycle'),
    url(r'^Savings-delete-cycle/(?P<pk>\d+)', views.delete_cycle, name='delete-cycle'),
    url(r'^List-of-loans', views.list_loans, name='loan-list'),
    url(r'^Paying-Loan/(?P<pk>\d+)', views.pay_loan, name='pay-loan'),
    url(r'^edit-loan/(?P<pk>\d+)', views.edit_loan, name='edit-loan'),
    url(r'^delete-loan-details/(?P<pk>\d+)', views.delete_loan, name='delete-loan'),
    url(r'^add-lookup', views.add_lookup, name='add-lookup'),
    url(r'^details-of-lookup', views.add_lookup_details, name='add-lookup-details'),
    url(r'^look-details-list', views.list_lookup_details, name='list-lookup-details'),
    url(r'^stocks/', views.StockList.as_view()), 
    url(r'^view-loan-repayment/(?P<pk>\d+)', views.view_loan_repaymnets, name='loan-repayments'),
    ]
urlpatterns= format_suffix_patterns(urlpatterns)
