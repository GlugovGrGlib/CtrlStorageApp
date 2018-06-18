# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ctrls', views.show_ctrls, name='show_ctrls'),
    url(r'^elements', views.show_elements, name='show_elements'),
    url(r'^bom', views.show_bom, name='show_bom'),
    url(r'^orders', views.show_orders, name='show_orders'),
    url(r'^suppliers', views.show_suppliers, name='show_suppliers'),
    url(r'^clients', views.show_clients, name='show_clients '),
    url(r'^purchases', views.show_purchases, name='show_purchases'),
    url(r'^consumptions', views.show_consumptions, name='show_consumptions'),
    url(r'^stock', views.show_stock, name='show_stock'),
    url(r'^add_ctrl', views.NewCtrl.as_view(), name='add_ctrl'),
    url(r'^add_element', views.NewElement.as_view(), name='add_element'),
    url(r'^add_bom', views.NewBom.as_view(), name='add_bom'),
    url(r'^add_order', views.NewOrder.as_view(), name='add_order'),
    url(r'^add_suppiler', views.NewSupplier.as_view(), name='add_suppiler'),
    url(r'^add_customer', views.NewCustomer.as_view(), name='add_client'),
    url(r'^add_purchase', views.NewPurchase.as_view(), name='add_purchase'),
    url(r'^add_consumption', views.NewConsumption.as_view(), name='add_consumption'),
]
