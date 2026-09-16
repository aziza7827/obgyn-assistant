import datetime
from datetime import timedelta
import streamlit as st

# إعدادات صفحة التطبيق
st.set_page_title_config = st.set_page_config(
    page_title="المساعد الطبي الشامل - نساء وتوليد",
    page_icon="🩺",
    layout="wide",
)

# تصميم وتنسيق بصري احترافي للواجهة
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        text-align: right;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: right;
        margin-bottom: 25px;
    }
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #3B82F6;
        margin-bottom: 15px;
        text-align: right;
    }
    .alert-card {
        background-color: #FEF2F2;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #EF4444;
        margin-bottom: 15px;
        text-align: right;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# القائمة الجانبية الاحترافية
st.sidebar.markdown(
    "<h2 style='text-align: right;'>📋 أقسام النظام</h2>", unsafe_allow_html=True
)
menu = st.sidebar.selectbox(
    "اختر القسم:",
    [
        "🏠 الرئيسية",
        "🚨 طوارئ النساء والتوليد (تشخيص تفريقي)",
        "🧮 حاسبات الحمل والولادة",
        "💊 دليل الأدوية والجرعات السريرية",
        "📋 بروتوكولات الطوارئ (PPH & Pre-eclampsia)",
    ],
)

# ---------------- 1. الصفحة الرئيسية ----------------
if menu == "🏠 الرئيسية":
  st.markdown(
      '<div class="main-header">🩺 المساعد الذكي الشامل (نساء وتوليد)</div>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<div class="sub-header">نظام مرجعي وسريري متقدم مصمم لدعم الطبيبات في اتخاذ القرارات الطبية الحرجة والسريعة.</div>',
      unsafe_allow_html=True,
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    st.info("🚨 **التشخيص الطارئ**\n\nتقييم فوري للحالات الحرجة والنزيف.")
  with col2:
    st.success("🧮 **حاسبات الحمل**\n\nحساب أسابيع الحمل والولادة بدقة.")
  with col3:
    st.warning("💊 **دليل الأدوية**\n\nالجرعات وتصنيفات الأمان السريرية.")

  st.write("---")
  st.markdown(
      "### 💡 مرحباً بكِ دكتورة. استخدمي القائمة الجانبية للتنقل بين أقسام التطبيق المختلفة."
  )

# ---------------- 2. طوارئ النساء والتوليد ----------------
elif menu == "🚨 طوارئ النساء والتوليد (تشخيص تفريقي)":
  st.markdown(
      '<div class="main-header">🚨 طوارئ النساء والتوليد والتشخيص التفريقي</div>',
      unsafe_allow_html=True,
  )

  emergency_type = st.selectbox(
      "اختر العرض السريري الرئيسي للمريضة:",
      [
          "نزيف أول الحمل (First Trimester Bleeding)",
          "آلام البطن الحادة في الحمل (Acute Abdomen)",
          "ارتفاع ضغط الدم وتسمم الحمل (Pre-eclampsia/Eclampsia)",
          "نزيف ما بعد الولادة (Postpartum Hemorrhage)",
      ],
  )

  if emergency_type == "نزيف أول الحمل (First Trimester Bleeding)":
    st.markdown(
        """
        <div class="alert-card">
        <h3>🔍 التشخيصات التفريقية المحتملة:</h3>
        <ul>
            <li><b>الإجهاض المنذر (Threatened Abortion):</b> عمر الحمل متوافق، العنق مغلق، نبض الجنين موجود.</li>
            <li><b>الحمل خارج الرحم (Ectopic Pregnancy):</b> ألم حاد، نزيف خفيف، اختبار قحفي إيجابي مع عدم رؤية كيس داخل الرحم بالسونار.</li>
            <li><b>الإجهاض الحتمي أو غير الكامل (Inevitable/Incomplete Abortion):</b> عنق الرحم مفتوح، نزيف مصحوب بقطع نسيجية.</li>
            <li><b>الحمل العنقودي (Molar Pregnancy):</b> رحم أكبر من عمر الحمل، غثيان شديد، مظهر "عاصفة الثلج" بالسونار.</li>
        </ul>
        <h3>⚡ خطوات التدخل العاجل:</h3>
        <ol>
            <li>تقييم العلامات الحيوية فوراً (استبعاد الصدمة النزفية).</li>
            <li>طلب تحليل (Blood Group & Rh, CBC, Quantitative hCG).</li>
            <li>إجراء تصوير تلفزيوني (Pelvic Ultrasound).</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

  elif emergency_type == (
      "ارتفاع ضغط الدم وتسمم الحمل (Pre-eclampsia/Eclampsia)"
  ):
    st.markdown(
        """
        <div class="alert-card">
        <h3>🔍 التشخيصات والتقييم السريري:</h3>
        <ul>
            <li><b>تسمم الحمل بدون علامات خطورة:</b> ضغط ≥ 140/90 مع وجود بروتين في البول (Proteinuria).</li>
            <li><b>تسمم الحمل بعلامات خطورة (Severe Features):</b> ضغط ≥ 160/110، صداع شديد، زغللة في العين، ألم الشرسوف، نقص صفائح الدم.</li>
            <li><b>الإرجاج (Eclampsia):</b> حدوث نشنات تشنجية (Seizures) مع علامات تسمم الحمل.</li>
        </ul>
        <h3>⚡ الخطوات الإسعافية:</h3>
        <ol>
            <li>البدء الفوري بمحلول كبريتات المغنيسيوم (MgSO4) للوقاية من التشنجات.</li>
            <li>خفض الضغط الحاد بأدوية آمنة (Labetalol أو Nifedipine).</li>
            <li>تقييم وضع الجنين وتحديد توقيت التوليد.</li>
        </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    st.info(
        "جاري استعراض البروتوكول السريري لهذه الحالة وتحديث خوارزميات التدخل"
        " السريع..."
    )

# ---------------- 3. حاسبات الحمل والولادة ----------------
elif menu == "🧮 حاسبات الحمل والولادة":
  st.markdown(
      '<div class="main-header">🧮 الحاسبة السريرية للحمل والولادة</div>',
      unsafe_allow_html=True,
  )

  calc_mode = st.radio(
      "اختر طريقة الحساب:",
      ["تاريخ آخر دورة شهرية (LMP)", "تقدير عمر الحمل بالأسابيع الحالية"],
  )

  if calc_mode == "تاريخ آخر دورة شهرية (LMP)":
    lmp_date = st.date_input(
        "أدخل تاريخ أول يوم من آخر دورة شهرية (LMP):",
        datetime.date.today() - timedelta(weeks=12),
    )

    if st.button("احسب التفاصيل السريرية"):
      today = datetime.date.today()
      gestational_days = (today - lmp_date).days
      weeks = gestational_days // 7
      days = gestational_days % 7

      edd = lmp_date + timedelta(days=280)

      st.markdown(
          f"""
            <div class="card">
            <h3>📊 النتائج السريرية:</h3>
            <p><b>عمر الحمل الحالي:</b> {weeks} أسبوع و {days} أيام.</p>
            <p><b>تاريخ الولادة المتوقع (EDD):</b> {edd.strftime('%Y-%m-%d')}</p>
            <p><b>الثلث الحالي من الحمل:</b> {'الثلث الأول' if weeks <= 13 else ('الثلث الثاني' if weeks <= 27 else 'الثلث الثالث')}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

# ---------------- 4. دليل الأدوية والجرعات ----------------
elif menu == "💊 دليل الأدوية والجرعات السريرية":
  st.markdown(
      '<div class="main-header">💊 دليل أدوية النساء والتوليد والجرعات</div>',
      unsafe_allow_html=True,
  )

  drug_category = st.selectbox(
      "تصنيف الأدوية:",
      [
          "أدوية تحفيز الطلق والرحم (Uterotonics)",
          "مخفضات ضغط الدم الآمنة في الحمل",
          "المضادات الحيوية الآمنة في الحمل",
      ],
  )

  if drug_category == "أدوية تحفيز الطلق والرحم (Uterotonics)":
    st.markdown(
        """
        <div class="card">
        <h3>1. الأوكسيتوسين (Oxytocin):</h3>
        <p><b>الاستخدام:</b> تحريض الولادة، الوقاية والعلاج من نزيف ما بعد الولادة (PPH).</p>
        <p><b>الجرعة للتحريض:</b> 1 مิลلي وحدة/دقيقة وتُضاعف كل 30 دقيقة حسب الاستجابة.</p>
        <p><b>الجرعة للوقاية من PPH:</b> 10 وحدات عضلياً (IM) أو وريدياً ببطء بعد خروج الجنين.</p>
        </div>
        <div class="card">
        <h3>2. ميثيل إرغometrine (Methergine):</h3>
        <p><b>الاستخدام:</b> علاج نزيف ما بعد الولادة الناتج عن رخاوة الرحم (Atonic PPH).</p>
        <p><b>الجرعة:</b> 0.2 ملغ عضلياً (IM). <b>تحذير صارم:</b> يمنع منعاً باتاً استخدامه للمريضات اللاتي يعانين من ارتفاع ضغط الدم.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------- 5. بروتوكولات الطوارئ ----------------
elif menu == "📋 بروتوكولات الطوارئ (PPH & Pre-eclampsia)":
  st.markdown(
      '<div class="main-header">📋 قوائم التدقيق وبروتوكولات الطوارئ</div>',
      unsafe_allow_html=True,
  )
  st.markdown(
      """
    <div class="alert-card">
    <h3>🚨 بروتوكول التعامل الفوري مع نزيف ما بعد الولادة (PPH Checklist)</h3>
    <ol>
        <li><b>استدعاء المساعدة الطبية:</b> إبلاغ أخصائي التوليد، طبيب التخدير، وفريق التمريض فوراً.</li>
        <li><b>تدليك الرحم (Uterine Massage):</b> إجراء تدليك خارجي مستمر لتحفيز انقباض الرحم.</li>
        <li><b>الأدوية القابضة للرحم (Uterotonics):</b> إعطاء Oxytocin و Misoprostol و Methergine (مع مراعاة موانع الاستعمال).</li>
        <li><b>الوصول الوريدي (IV Access):</b> تركيب كانولا واسعة الحجم وبدء المحاليل الوريدية الدافئة.</li>
        <li><b>تقدير كمية النزيف:</b> قياس الدم المفقود بدقة ومراقبة العلامات الحيوية كل 5 دقائق.</li>
    </ol>
    </div>
    """,
      unsafe_allow_html=True,
  )
