from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', login_required(ViolationList.as_view()), name="violation_list_url"),
    path('get_json/', violation_json, name='violation_json_url'),
    path('save/', login_required(ViolationSave.as_view()), name="violation_create_url"),
    path('detail/<int:id>/', login_required(ViolationDetail.as_view()), name="violation_detail_url"),
    path('update/<int:id>/', login_required(ViolationUpdate.as_view()), name="violation_update_url"),
    path('delete/<int:id>/', login_required(ViolationDelete.as_view()), name="violation_delete_url"),

    path('violation/create/', ViolationCreateView.as_view(), name="violation_create_rest_url")
]