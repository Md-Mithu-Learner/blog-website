from django.urls import path
from task.views.function_base_views import function_base_task_list_api_view, function_base_task_createapi_view,function_base_task_detail_api_view,\
    function_base_task_update_api_view,func_base_task_delete,function_base_tasks,function_base_tasks_PPD,function_base_tasks_serializers,func_task_serializer_api_view
app_name = 'task'

urlpatterns = [
    path('func-task-list/', function_base_task_list_api_view, name='func_task_list'),
    path('func-task-create/', function_base_task_createapi_view, name='func_task_create'),
    path('func-task-detail/<int:task_id>/', function_base_task_detail_api_view, name='func_task_detail'),
    path('func-task-update/<int:task_id>/', function_base_task_update_api_view, name='func_task_update'),
    path('func-task-delete/<int:task_id>/', func_base_task_delete, name='func_task_delete'),
]
urlpatterns += [
    path('func-tasks/', function_base_tasks, name='function_base_tasks'),
    path('func-tasks-PPD/<int:task_id>/', function_base_tasks_PPD, name='function_base_tasks_PPD'),

]
urlpatterns += [
    path('func-tasks-serial/', function_base_tasks_serializers, name='function_task_serializer'),
    path('func-tasks-serial-api-view/<int:task_id>/', func_task_serializer_api_view, name='func_task_serializer_api_view'),
]