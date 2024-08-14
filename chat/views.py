from rest_framework import viewsets
from .models import ChatGroup, Message
from .serializers import ChatGroupSerializer, MessageSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ChatGroupViewSet(viewsets.ModelViewSet):
    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.members.add(self.request.user)
        instance.save()

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        chat_group_pk = self.kwargs.get('chat_group_pk')
        if chat_group_pk is not None:
            queryset = queryset.filter(chat_group__pk=chat_group_pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, chat_group_id=self.kwargs['chat_group_pk'])

@login_required
def home_view(request):
    return render(request, 'index.html')

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})

@login_required
def users_view(request):
    users = User.objects.all()
    for user in users:
        print(reverse('user-detail', kwargs={'pk': user.pk}))
    return render(request, 'users.html', {'users': users})


@login_required
def chatgroups_view(request):
    chatgroups = ChatGroup.objects.all()
    return render(request, 'chatgroups.html', {'chatgroups': chatgroups})

@login_required
def user_detail_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

@login_required
def chatgroup_detail_view(request, pk):
    chatgroup = get_object_or_404(ChatGroup, pk=pk)
    return render(request, 'chatgroup_detail.html', {'chatgroup': chatgroup})




