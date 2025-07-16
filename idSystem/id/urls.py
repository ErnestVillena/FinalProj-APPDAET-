from django.urls import path
from .views import IdList

app_name = 'id'

urlpatterns = [
    path('id_list/', IdList.as_view(), name="idlist"),
]