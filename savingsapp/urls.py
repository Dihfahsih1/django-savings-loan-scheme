from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Savings-add-member', views.add_member, name='add-member'),
    url(r'^Savings-edit-member/(?P<pk>\d+)', views.edit_member, name='edit-member'),
    url(r'^Savings-view-member/(?P<pk>\d+)', views.view_member, name='view-member'),
    url(r'^Savings-delete-member/(?P<pk>\d+)', views.delete_member, name='delete-member'),
    url(r'^Savings-members-list', views.members_list, name='members-list'),
    url(r'^Savings-make-attendence', views.make_attendence, name='make-attendence'),
    url(r'^Savings-attendence-history', views.attendence_history, name='attendence-history'),
    url(r'^Savings-make-saving', views.make_saving, name='make-saving'),
    url(r'^Savings-savings-list', views.savings_list, name='savings-list'),
    url(r'^Savings-pay-loan', views.pay_loan, name='pay-loan'),
    url(r'^Savings-give-loan', views.give_loan, name='give-loan'),
    url(r'^Savings-social-fund', views.social_fund, name='social-fund'),
    url(r'^Savings-add-cycle', views.add_cycle, name='add-cycle'),
    url(r'^Savings-cycle-list', views.cycle_list, name='cycle-list'),
    url(r'^Savings-edit-cycle/(?P<pk>\d+)', views.edit_cycle, name='edit-cycle'),
    url(r'^Savings-delete-cycle/(?P<pk>\d+)', views.delete_cycle, name='delete-cycle'),
    ]
