from django.urls import path

from rate import views

app_name = 'rate'

urlpatterns = [
    path('list/', views.RateList.as_view(), name='list'),
    path('edit/<int:pk>/', views.UpdateRate.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteRate.as_view(), name='delete'),
    path('latest-rates/', views.LatestRatesView.as_view(), name='latest-rates'),
    path('download-csv/', views.RateDownloadCSV.as_view(), name='download-csv'),
    path('download-xlsx/', views.RateDownloadXLSX.as_view(), name='download-xlsx'),

    path('rates/', views.RateListCreateView.as_view(), name='rates'),
    path('rates/<int:pk>/', views.RateReadUpdateDeleteView.as_view(), name='rate'),
]
