from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    自定义权限，只允许对象的所有者编辑对象。
    """
    def has_object_permission(self, request, view, obj):
        # 读取权限允许任何请求，
        # 所以我们总是允许GET, HEAD或OPTIONS请求。
        if request.method in permissions.SAFE_METHODS:
            return True
        # 写权限只允许代码段的所有者使用。
        return obj.owner == request.user
