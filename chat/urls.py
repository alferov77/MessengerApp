from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatGroupViewSet, MessageViewSet, UserViewSet, user_detail_view, chatgroup_detail_view

router = DefaultRouter()
router.register(r'chatgroups', ChatGroupViewSet)
router.register(r'users', UserViewSet)

message_list = MessageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
message_detail = MessageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('chatgroups/<int:chat_group_pk>/messages/', message_list, name='message-list'),
    path('chatgroups/<int:chat_group_pk>/messages/<int:pk>/', message_detail, name='message-detail'),
    path('users/<int:pk>/', user_detail_view, name='user-detail'),
    path('chatgroups/<int:pk>/', chatgroup_detail_view, name='chatgroup-detail'),
]





