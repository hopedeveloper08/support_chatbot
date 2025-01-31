from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from .local_settings import set_google_api_key

class Bot:
    def __init__(self, info):
        set_google_api_key()
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.1)
        
        messages = [
            f"تو یک ربات پشتیبانی برای کسب و کار {info.name} هستی. از زبان پشتیبان به سوالات کاربران پاسخ بده.",
            '.در صورتی که سوالی بی‌ربط به کسب و کار پرسیده شود، باید پیامی با عنوان "فقط مسئول جواب دادن سوالات مربوط به کسب و کار هستم" ارسال کن.',
            f'اگر پاسخی را نمیدانی کاربر را به اطلاعات "{info.support_info}" ارجاع بده.',
            "باید فقط بر اساس اطلاعات زیر به سوالات کاربران پاسخ بدی:",
            info.description,
        ]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", "\n".join(messages)),
            ("user", "{user_input}")
        ])
        
        self.bot = prompt | llm
    
    def get_response(self, user_input):
        response = self.bot.invoke({"user_input": user_input})
        return response.content