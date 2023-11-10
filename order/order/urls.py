"""
URL configuration for order project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainpage.views as mainpage_views
import productpage.views as productpage_views
import autoregister.views as autoregister_views
import contactpage.views as contactpage_views
import shoppingcardpage.views as shopping_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage_views.mainpage, name = "main"),
    path('productpage/', productpage_views.productpage, name = "productpage"),
    path('contactpage/',contactpage_views.contactpage, name = 'contactpage' ),
    path('autoregister/', autoregister_views.view_log, name = "login"),
    path('shoppingcardpage/', shopping_views.shopping, name = "shoppingcardpage"),
    path('register/', autoregister_views.register, name='register'),
    path('productpage2/', productpage_views.productpage2, name = "clothes1"),
    path('productpage3/', productpage_views.productpage3, name = "clothes2"),
    path('productpage4/', productpage_views.productpage4, name = "shoes"),
    path('1', shopping_views.shopping1, name="1"),
    path('2', shopping_views.shopping2, name="2"),
    path('3', shopping_views.shopping3, name="3"),
    path('4', shopping_views.shopping4, name="4"),
    path('5', shopping_views.shopping5, name="5"),
    path('6', shopping_views.shopping6, name="6"),
    path('7', shopping_views.shopping7, name="7"),
    path('8', shopping_views.shopping8, name="8"),
    path('9', shopping_views.shopping9, name="9"),
    path('10', shopping_views.shopping10, name="10"),
    path('11', shopping_views.shopping11, name="11"),
    path('12', shopping_views.shopping12, name="12"),
    path('13', shopping_views.shopping13, name="13"),
    path('14', shopping_views.shopping14, name="14"),
    path('15', shopping_views.shopping15, name="15"),
    path('16', shopping_views.shopping16, name="16"),
    path('17', shopping_views.shopping17, name="17"),
    path('logout/', autoregister_views.logout2, name = 'logout')
]
    