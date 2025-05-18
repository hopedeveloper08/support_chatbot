from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Bussiness
from .serializers import UserInputSerializer 
from .bot import model

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
        
        prompt = f"""
            شما یک دستیار هوشمند پشتیبانی مشتریان برای کسب‌وکار «{info.name}» هستید. وظیفه شما پاسخگویی به سوالات مشتریان بر اساس اطلاعات زیر است:

            **اطلاعات کسب‌وکار:**  
            {info.support_info}

            **دستورالعمل‌های پاسخ‌دهی:**  
            - پاسخ‌ها باید **دقیق، مفید و دوستانه** باشند.  
            - در صورت عدم وجود اطلاعات کافی، بگویید: «متأسفانه اطلاعاتی در این مورد ندارم. لطفاً با راه‌های ارتباطی دیگر کسب‌وکار تماس بگیرید.»  
            - از ساختارهای طولانی خودداری کنید و مستقیماً به سوال مشتری پاسخ دهید.  
            - در صورت نیاز به جزئیات بیشتر (مثلاً شماره تماس، آدرس، شرایط خاص)، فقط از اطلاعات ارائه‌شده در **اطلاعات کسب‌وکار** استفاده کنید.  

            **سوال مشتری:**  
            {user_input}

            **پاسخ شما (کوتاه و مفید):**
        """
        try:
            output = model('gemma3:1b', prompt)
            return Response({"response": output}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
