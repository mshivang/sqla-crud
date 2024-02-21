from rest_framework.response import Response
from rest_framework import status, generics
from users.serializers import UserSerializer
import math
from django.contrib.auth.models import User, AnonymousUser

class Users(generics.GenericAPIView):
    # Initialize serializer class. 
    serializer_class = UserSerializer
    queryset = User.objects.all()

    '''
        Endpoint: /api/users
        Method: GET
        Description: Returns list of all users, or based on provided page, limit, search value.
    '''
    def get(self, request):
         #Authorize User
        user = self.request.user
        if type(user) == AnonymousUser:
            return Response({
            "status": "fail",
            "message": "Unauthorized"
        }, 401)

        # Get page number and limit from request query params.
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))

        # Decide range of objects to send.
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num

        # Get search sting from query params
        search_param = request.GET.get("search")

        # Get all users and their count.
        users = User.objects.all()
        total_users = users.count()

        # Filter users by search param.
        if search_param:
            users = users.filter(title__icontains=search_param)

        # Serialize data.
        serializer = self.serializer_class(users[start_num:end_num], many=True)

        #Returns response.
        return Response({
            "status": "success",
            "total": total_users,
            "page": page_num,
            "last_page": math.ceil(total_users / limit_num),
            "users": serializer.data
        })
        
class UserDetail(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    '''
        Method: get_user
        Returns: User
        Description: Returns user by id from database.
        Params: pk: primary key.
    '''
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return None

    '''
        Endpoint: /api/users/:pk
        Method: GET
        Description: Get a user from database.
    '''
    def get(self, request, pk):
         #Authorize User
        user = self.request.user
        if type(user) == AnonymousUser:
            return Response({
            "status": "fail",
            "message": "Unauthorized"
        }, 401)

        # Retrieves user from database.
        user = self.get_user(pk=pk)

        # Returns error response if user not found.
        if user == None:
            return Response({"status": "fail", "message": f"User with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        # Seriialize user data.
        serializer = self.serializer_class(user)
        return Response({"status": "success", "user": serializer.data})

    '''
        Endpoint: /api/users/:pk
        Method: DELETE
        Description: Delete a user from database.
    '''
    def delete(self, request, pk):
        #Authorize User
        user = self.request.user
        if type(user) == AnonymousUser or not user.is_superuser:
            return Response({
            "status": "fail",
            "message": "Unauthorized"
        }, 401)

        # Retrieves user from database.
        user = self.get_user(pk)

        # Returns error response if user does not exists.
        if user == None:
            return Response({"status": "fail", "message": f"User with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        # Deletes user from database.
        user.delete()

        #Returns response to client
        return Response({"status": "success", "message": f"User with Id {pk} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

