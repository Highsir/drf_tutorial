from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from snippets.views import SnippetViewSet, UserViewSet, api_root

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes= [renderers.StaticHTMLRenderer])
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#
# ])


# urlpatterns = [
#     path('snippets/', views.SnippetList.as_view()),
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
#     path('users/', views.UserList.as_view()),
#     path('', views.api_root),
#     path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

"""
因为我们使用的是ViewSet类而不是View类，所以我们实际上不需要自己设计 URL conf。Router可以使用类自动处理将资源连接到视图和 url 的约定。
我们需要做的就是向路由器注册适当的视图集，然后让它完成其余的工作。
"""
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename='user')
urlpatterns = [path('', include(router.urls))]

urlpatterns += [path('api-auth/', include('rest_framework.urls')),]
