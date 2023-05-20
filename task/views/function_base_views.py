from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task.serializers import TaskSerializers
from task.models import Task
import copy
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['GET'])
def function_base_task_list_api_view(request, *args, **kwargs):
    try:
        task_queryset = Task.objects.all()
        # task_status = request.GET.get('status', None)
        # if task_status:
        #     task_queryset=Task.objects.filter(status=task_status)
        if request.GET.get('status', None):
            task_queryset = Task.objects.filter(status=request.GET['status'])
        response = []
        for task in task_queryset:
            task_obj = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'created_at': task.created_at,
                'modified_at': task.modified_at,
                'status': task.status,
                'assignee': task.assignee.id,

            }
            response.append(task_obj)
        return Response(response, status=status.HTTP_200_OK)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def function_base_task_createapi_view(request, *args, **kwargs):
    try:
        title = request.data.get('title', None)
        description = request.data.get('description', None)
        assignee = request.data.get('assignee', None)
        Task.objects.create(title=title, description=description, assignee_id=assignee)
        return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message': 'server error!!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def function_base_task_detail_api_view(request,task_id, *args, **kwargs):
    try:
        task_obj = Task.objects.get(id=task_id)
        task_detaill = {
                'id': task_obj.id,
                'title': task_obj.title,
                'description': task_obj.description,
                'created_at': task_obj.created_at,
                'modified_at': task_obj.modified_at,
                'status': task_obj.status,
                'assignee': task_obj.assignee.id,

            }
        return Response(task_detaill, status=status.HTTP_200_OK)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT', 'PATCH'])
def function_base_task_update_api_view(request,task_id,  *args, **kwargs):
    try:
        task_obj= Task.objects.get(id=task_id)
        if request.data.get('title', None):
            task_obj.title = request.data['title']
        if request.data.get('description', None):
            task_obj.description = request.data['description']
        if request.data.get('assignee', None):
            task_obj.assignee_id = request.data['assignee']
        task_obj.save()
        return Response({'message': 'updated'}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message': 'server error!!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def func_base_task_delete(request,task_id, *args, **kwargs):
    try:
        Task.objects.filter(id=task_id).update(status='deleted')
        return Response({'message': 'deleted'}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','POST'])
def function_base_tasks(request, *args, **kwargs):
    try:

        if request.method == 'GET':
            task_queryset = Task.objects.all()
            if request.GET.get('status', None):
                task_queryset = Task.objects.filter(status=request.GET['status'])
            response = []
            for task in task_queryset:
                task_obj = {
                    'id': task.id,
                    'title': task.title,
                    'description': task.description,
                    'created_at': task.created_at,
                    'modified_at': task.modified_at,
                    'status': task.status,
                    'assignee': task.assignee.id,

                }
                response.append(task_obj)
            return Response(response, status=status.HTTP_200_OK)
        else:
            title = request.data.get('title', None)
            description = request.data.get('description', None)
            assignee = request.data.get('assignee', None)
            Task.objects.create(title=title, description=description, assignee_id=assignee)
            return Response({'message': 'created'}, status=status.HTTP_201_CREATED)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT','PATCH','DELETE'])
def function_base_tasks_PPD(request,task_id, *args, **kwargs):
    try:
        if request.method == 'PUT':
            task_obj = Task.objects.get(id=task_id)
            if request.data.get('title', None):
                task_obj.title = request.data['title']
            if request.data.get('description', None):
                task_obj.description = request.data['description']
            if request.data.get('assignee', None):
                task_obj.assignee_id = request.data['assignee']
            task_obj.save()
            return Response({'message': 'updated'}, status=status.HTTP_201_CREATED)
        elif request.method == 'PATCH':
            task_obj = Task.objects.get(id=task_id)
            if request.data.get('title', None):
                task_obj.title = request.data['title']
            if request.data.get('description', None):
                task_obj.description = request.data['description']
            if request.data.get('assignee', None):
                task_obj.assignee_id = request.data['assignee']
            task_obj.save()
            return Response({'message': 'updated'}, status=status.HTTP_201_CREATED)
        else:
            Task.objects.filter(id=task_id).update(status='deleted')
            return Response({'message': 'deleted'}, status=status.HTTP_201_CREATED)

    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#-------------------------serializers-------------------------------------------------------

@api_view(['GET','POST'])
def function_base_tasks_serializers(request, *args, **kwargs):
    try:

        if request.method == 'GET':
            task_queryset = Task.objects.all()
            if request.GET.get('status', None):
                task_queryset = Task.objects.filter(status=request.GET['status'])
            response = TaskSerializers(task_queryset, many=True)

            return Response(response.data, status=status.HTTP_200_OK)
        else:
            task_serialzer = TaskSerializers(data=request.data)
            if task_serialzer.is_valid():
                task_serialzer.save()
                return Response(task_serialzer.data, status=status.HTTP_201_CREATED)
            return Response(task_serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        print(f"Error:{ex}")
    return Response({'message':"server error!!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','PUT','PATCH'])
def func_task_serializer_api_view(request,  task_id, *args, **kwargs):
    try:
        task_obj = Task.objects.filter(id=task_id).first()
        if request.method == 'GET':
            response = TaskSerializers(instance=task_obj)
            return Response(response.data, status=status.HTTP_200_OK)
        else:
            copy_request = copy.deepcopy(request.data)
            if request.data.get(['assignee', None]):
                copy_request['assignee'] = User.objects.filter(id=request.data['assignee']).first()
            serializer = TaskSerializers(instance=task_obj, data=request.data)

            if serializer.is_valid():
                serializer.update(instance=task_obj, validated_data=copy_request)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as ex:
        print(f'error-->{ex}')
    return Response({'message': 'server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

