from flask import Flask, render_template, jsonify, request
import sys
import os
import asyncio
from dotenv import load_dotenv

# إضافة مسار المشروع إلى مسارات النظام
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# استيراد خدمة Search1API
from services.search1api_service import search1_service

# تحميل متغيرات البيئة
load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')

# --- WloredAI Configuration & Class --- # 
OWNERSHIP_SIGNATURE = "عبدالعزيز | Wlored v1.0 | 2025"

class WloredAI:
    def __init__(self):
        # 🔐 متطلبات الأمان الأساسية (مفاهيمية)
        self.تشفير_مستوى_عسكري = True
        self.نظام_منع_اختراق = "أحدث إصدار من Cloudflare Zero Trust (مفهومي)"
        # NVIDIA_AI_Shield=True (مفهومي، سيتم بحث كيفية تطبيقه)
        
        # 💡 نواة الذكاء الاصطناعي (مفاهيمية)
        self.محرك_التفكير_العميق = "Search1API - deepseek-r1-70b-online"
        self.نافذة_السياق = 131072  # رمز

    def بناء_الواجهة_cfg(self):
        return {
            "اللون_الرئيسي": "#4A2FBD",
            "النسق": "داكن/فاتح تلقائي",
            "المكونات": [
                "شريط بحث ذكي",
                "لوحة تحكم قابلة للتخصيص",
                "نظام إشعارات متقدم"
            ]
        }

    def تفعيل_الميزات_cfg(self):
        return {
            "البحث_العميق": {
                "الوصف": "بحث شامل باستخدام Search1API",
                "المحددات": "حسب حدود استخدام Search1API"
            },
            "التفكير_الاستراتيجي": {
                "المستويات": ["مبتدئ", "متوسط", "خبير"],
                "الوظيفة": "تحليل المشكلات متعددة الأبعاد باستخدام Search1API"
            },
            "منشئ_المحتوى": {
                "النماذج": ["مقالات", "تقارير", "شعر"],
                "اللغات": ["العربية", "الإنجليزية", "الفرنسية"]
            }
        }

    # --- تنفيذ الميزات باستخدام خدمة Search1API --- #
    async def perform_deep_search(self, query):
        """تنفيذ بحث عميق باستخدام Search1API"""
        result = await search1_service.deep_search(query)
        return result
    
    async def perform_strategic_thinking(self, problem, level='مبتدئ'):
        """تنفيذ تفكير استراتيجي باستخدام Search1API"""
        scenario = f"المشكلة: {problem}\nالمستوى: {level}"
        result = await search1_service.strategic_thinking(scenario)
        return result
    
    async def create_content(self, content_type, topic, language='العربية'):
        """إنشاء محتوى باستخدام Search1API"""
        topic_with_lang = f"{topic} (باللغة {language})"
        result = await search1_service.content_generator(topic_with_lang, content_type)
        return result

# إنشاء نسخة من WloredAI
wlored_ai = WloredAI()

# --- المسارات --- #
@app.route('/')
def home():
    return render_template('index.html', 
                           site_title="WloredAI - نظامك الشخصي الذكي", 
                           signature=OWNERSHIP_SIGNATURE)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', 
                           site_title="سياسة الخصوصية - WloredAI", 
                           signature=OWNERSHIP_SIGNATURE)

# --- مسارات API للميزات --- #
@app.route('/api/deep_search', methods=['POST', 'GET'])
def api_deep_search():
    query = request.args.get('query', 'موضوع افتراضي للبحث')
    
    # استخدام asyncio لتشغيل الدالة غير المتزامنة
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(wlored_ai.perform_deep_search(query))
    loop.close()
    
    return jsonify(results)

@app.route('/api/strategic_thinking', methods=['POST', 'GET'])
def api_strategic_thinking():
    problem = request.args.get('problem', 'مشكلة افتراضية للتحليل')
    level = request.args.get('level', 'مبتدئ')
    
    # استخدام asyncio لتشغيل الدالة غير المتزامنة
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    analysis = loop.run_until_complete(wlored_ai.perform_strategic_thinking(problem, level))
    loop.close()
    
    return jsonify(analysis)

@app.route('/api/create_content', methods=['POST', 'GET'])
def api_create_content():
    content_type = request.args.get('type', 'article')
    topic = request.args.get('topic', 'موضوع افتراضي للمحتوى')
    language = request.args.get('language', 'العربية')
    
    # استخدام asyncio لتشغيل الدالة غير المتزامنة
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    content = loop.run_until_complete(wlored_ai.create_content(content_type, topic, language))
    loop.close()
    
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
