from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_visitor/', views.add_visitor, name='add_visitor'),
    path('manage_visitors/', views.manage_visitors, name='manage_visitors'),
    path('edit_visitor/<int:visitor_id>/', views.edit_visitor, name='edit_visitor'),
]