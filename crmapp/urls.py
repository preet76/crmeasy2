"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
from marketing.views import HomePage
from django.contrib.auth.views import login, logout
from accounts.views import AccountList ,account_cru
from accounts.urls import account_urls
from contacts.urls import contact_urls
from contacts.views import contact_cru, ContactDelete

from contacts.views import ContactDelete
from communications.urls import comm_urls

from communications.views import comm_cru
from communications.views import CommDelete

from subscribers import views




# urlpatterns = [
#
#     url(r'^$', HomePage.as_view(), name="home"),
#     url(r'^signup/$',views.subscriber_new, name='sub_new'),
#     url(r'^admin/', admin.site.urls),
#
# from  subscribers import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
     # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),
    url(r'^signup/$', views.subscriber_new, name='sub_new'),
    url(regex=r'^login/$',view=login,kwargs={'template_name': 'login.html'},name='login'),
    url(regex=r'^logout/$',view=logout,kwargs={'next_page': '/'},name='logout'),
    url(r'^account/new/$', account_cru, name='account_new'),
    url(r'^account/list/$', AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),
    url(r'^contact/new/$',contact_cru, name='contact_new'),

    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),
    url(r'^contact/(?P<pk>[\w-]+)/delete/$',ContactDelete.as_view(), name='contact_delete'),
    url(r'^comm/new/$',comm_cru, name='comm_new'),
    url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),
    url(r'^comm/(?P<pk>[\w-]+)/delete/$',CommDelete.as_view(), name='comm_delete'),


]
