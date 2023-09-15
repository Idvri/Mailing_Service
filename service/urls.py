from django.urls import path

from service.views import DashboardView, CreateMailingView, ListMailingView, UpdateMailingView, DeleteMailingView, \
    DetailMailingView, CreateClientView, ListClientView, DeleteClientView

app_name = 'service'

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('create_mailing/', CreateMailingView.as_view(), name='create_mailing'),
    path('list_mailing/', ListMailingView.as_view(), name='list_mailing'),
    path('update_mailing/<int:pk>/', UpdateMailingView.as_view(), name='update_mailing'),
    path('delete_mailing/<int:pk>/', DeleteMailingView.as_view(), name='delete_mailing'),
    path('detail_mailing/<int:pk>/', DetailMailingView.as_view(), name='detail_mailing'),
    path('create_client/', CreateClientView.as_view(), name='create_client'),
    path('clients_list/', ListClientView.as_view(), name='clients_list'),
    path('delete_client/<int:pk>/', DeleteClientView.as_view(), name='delete_client'),
]
