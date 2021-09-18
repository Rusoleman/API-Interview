from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from django.shortcuts import render
from .forms import NameForm

from users.models import User
from users.serializers import UserSerializer


def get_users(request):
    users = User.objects.all()

    name_field = request.POST.get('name_user')
    age_field = request.POST.get('age_user')
    happy_checkbox = request.POST.get('happy', False)
    healthy_checkbox = request.POST.get('healthy', False)
    busy_checkbox = request.POST.get('busy', False)

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return Response(status=status.HTTP_200_OK)

    if name_field != '' and name_field is not None:
        users = users.filter(name__contains=name_field)
    elif age_field != '' and age_field is not None:
        users = users.filter(age__contains=age_field)

    if happy_checkbox == 'True':
        users = users.filter(happy=happy_checkbox)
    else:
        users = users.filter(happy=False)

    if healthy_checkbox == 'True':
        users = users.filter(healthy=healthy_checkbox)
    else:
        users = users.filter(healthy=False)

    if busy_checkbox == 'True':
        users = users.filter(busy=busy_checkbox)
    else:
        users = users.filter(busy=False)

    context = {
        "users": users
    }

    return render(request, 'users/index.html', context)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


