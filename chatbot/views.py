from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bussiness
from .serializers import UserInputSerializer 
from .bot import Bot  

class BotResponseView(APIView):
    serializer_class = UserInputSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user_input = serializer.validated_data.get('user_input')
        user = request.user  
        try:
            info = Bussiness.objects.get(user=user)
        except Bussiness.DoesNotExist:
            return Response({"error": 'access denied!'}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            bot = Bot(info)
            response = bot.get_response(user_input)
            return Response({"response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
