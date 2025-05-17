# تكامل Google Gemini API مع مشروع WloredAI

import os
import google.generativeai as genai
from dotenv import load_dotenv

# محاولة تحميل المفتاح من ملف .env إذا كان موجودًا
load_dotenv()

# الحصول على مفتاح API من متغير البيئة أو استخدام القيمة المباشرة للتطوير فقط
# في الإنتاج، يجب استخدام متغيرات البيئة أو خدمات إدارة الأسرار
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyBZNv2DVmsWf5VcOIXY8lRzALRdlHOvRc8")

# تهيئة مكتبة Gemini
genai.configure(api_key=GEMINI_API_KEY)

class GeminiAIService:
    """فئة خدمة الذكاء الاصطناعي باستخدام Google Gemini API"""
    
    def __init__(self):
        # تهيئة النماذج المختلفة للاستخدامات المتنوعة
        self.general_model = genai.GenerativeModel('gemini-1.5-pro')
        self.flash_model = genai.GenerativeModel('gemini-1.5-flash')
    
    async def deep_search(self, query):
        """تنفيذ بحث عميق باستخدام Gemini"""
        try:
            prompt = f"""
            قم بإجراء بحث عميق حول الموضوع التالي:
            {query}
            
            يرجى تقديم:
            1. ملخص شامل للموضوع
            2. النقاط الرئيسية والحقائق المهمة
            3. وجهات نظر مختلفة حول الموضوع
            4. مصادر موثوقة للمزيد من المعلومات
            """
            
            response = self.general_model.generate_content(prompt)
            return {
                "status": "success",
                "results": response.text,
                "query": query
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "query": query
            }
    
    async def strategic_thinking(self, scenario):
        """تنفيذ تفكير استراتيجي باستخدام Gemini"""
        try:
            prompt = f"""
            قم بتحليل السيناريو التالي من منظور استراتيجي:
            {scenario}
            
            يرجى تقديم:
            1. تحليل SWOT (نقاط القوة، الضعف، الفرص، التهديدات)
            2. خيارات استراتيجية محتملة
            3. توصيات للخطوات التالية
            4. مخاطر محتملة وكيفية التخفيف منها
            """
            
            response = self.general_model.generate_content(prompt)
            return {
                "status": "success",
                "results": response.text,
                "scenario": scenario
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "scenario": scenario
            }
    
    async def content_generator(self, topic, content_type="article"):
        """توليد محتوى (مقالات، تقارير، شعر) باستخدام Gemini"""
        try:
            content_prompts = {
                "article": f"""
                اكتب مقالة شاملة ومفصلة حول الموضوع التالي:
                {topic}
                
                يجب أن تتضمن المقالة:
                - مقدمة جذابة
                - محتوى غني بالمعلومات مقسم إلى أقسام منطقية
                - خاتمة تلخص النقاط الرئيسية
                - أسلوب كتابة سلس وجذاب
                """,
                
                "report": f"""
                قم بإعداد تقرير تحليلي مفصل حول:
                {topic}
                
                يجب أن يتضمن التقرير:
                - ملخص تنفيذي
                - خلفية ومعلومات أساسية
                - تحليل البيانات والاتجاهات
                - استنتاجات وتوصيات
                - مراجع ومصادر
                """,
                
                "poetry": f"""
                اكتب قصيدة أدبية راقية حول:
                {topic}
                
                يجب أن تكون القصيدة:
                - غنية بالصور البلاغية والاستعارات
                - ذات إيقاع وقافية مناسبة
                - تعبر عن عمق المشاعر والأفكار
                - تحمل رسالة أو معنى عميق
                """
            }
            
            prompt = content_prompts.get(content_type, content_prompts["article"])
            response = self.general_model.generate_content(prompt)
            
            return {
                "status": "success",
                "results": response.text,
                "topic": topic,
                "content_type": content_type
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "topic": topic,
                "content_type": content_type
            }

# إنشاء نسخة واحدة من الخدمة للاستخدام في التطبيق
gemini_service = GeminiAIService()
