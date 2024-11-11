from rest_framework.permissions import BasePermission
from rest_framework import permissions

class IsIndividual(BasePermission):
    def has_permission(self,request,view):
        return  request.user and request.user.role == "individual"
        #return  request.user.is_superuser or request.user.role == "individual"
    
class IsJointLeader(BasePermission):
    def has_permission(self,request,view):
        return  request.user and request.user.role == "joint leader" or request.user.is_superuser

class IsSupervisor(BasePermission):
    def has_permission(self,request,view):
        return  request.user and request.user.role == "supervisor" 

    

