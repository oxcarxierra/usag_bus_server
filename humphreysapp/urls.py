from django.urls import path
from humphreysapp import views

app_name='humphreysapp'

urlpatterns = [
    path('bus_stop/', views.bus_stop_list),
    path('bus_line/', views.bus_line_list),
    path('bus_line/<str:line>/', views.bus_line_detail),
    path('bus_stop/<str:stop_id>/<str:weekend>', views.bus_stop_detail),
    # path('bus_stop/<string:camp>', StopSchedule.as_view()),
]