import streamlit as st

# إعدادات الصفحة وتصميم الواجهة
st.set_page_config(
    page_title="المساعد الذكي للتشخيص التفريقي - نساء وتوليد",
    page_icon="🩺",
    layout="wide"
)

# تنسيق الألوان والتصميم بستايل هادئ ومهني
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4b6cb7;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #182848;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق والشعار
st.title("🩺 المساعد الذكي للتشخيص التفريقي (نساء وتوليد)")
st.markdown("---")
st.markdown("مرحباً بكِ دكتورة. هذا النظام مصمم لمساعدتكِ خطوة بخطوة في الوصول للتشخيص التفريقي السريع في الحالات الحرجة وطوارئ النساء والتوليد.")

# القائمة الجانبية للتنقل بين الأقسام
st.sidebar.header("📋 أقسام النظام")
menu = st.sidebar.selectbox(
    "اختر القسم:",
    ["التشخيص التفريقي السريع", "حسابات الحمل والعمر الحملي", "دليل الأدوية والطوارئ", "إرشادات الاستخدام"]
)

# ---------------- القسم الأول: التشخيص التفريقي السريع ----------------
if menu == "التشخيص التفريقي السريع":
    st.header("⚡ التشخيص التفريقي لحالات الطوارئ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        symptom_category = st.selectbox(
            "اختر العرض الرئيسي للمريضة:",
            ["نزيف أول الحمل (First Trimester Bleeding)", 
             "نزيف أواخر الحمل (Late Trimester Bleeding)", 
             "آلام الحوض والبطن الحادة (Acute Abdominal Pain)", 
             "ارتفاع ضغط الدم الحملي / تسمم الحمل (Hypertensive Disorders)"]
        )
    
    with col2:
        vital_signs = st.selectbox(
            "حالة العلامات الحيوية (Hemodynamic Status):",
            ["مستقرة (Stable)", "غير مستقرة / صدمة (Unstable / Shock)"]
        )

    st.markdown("### 🔍 النتائج والتشخيص التفريقي المقترح:")
    
    if symptom_category == "نزيف أول الحمل (First Trimester Bleeding)":
        st.markdown("""
        <div class="card">
        <ul>
            <li><b>التشخيص المرجح 1:</b> حمل خارج الرحم (Ectopic Pregnancy) - <i>يجب استبعاده فوراً</i>.</li>
            <li><b>التشخيص المرجح 2:</b> إجهاض منذر أو حتمي (Threatened / Inevitable Abortion).</li>
            <li><b>التشخيص المرجح 3:</b> حمل باهت أو عنقودي (Molar Pregnancy).</li>
        </ul>
        <b>الخطوات الإكلينيكية المقترحة:</b> إجراء سونار فوري (Pelvic/Transvaginal Ultrasound)، فحص هرمون الحمل الكمي (Beta-hCG)، وفحص فصيلة الدم (Blood Group & Rh).
        </div>
        """, unsafe_allow_html=True)
        
    elif symptom_category == "نزيف أواخر الحمل (Late Trimester Bleeding)":
        st.markdown("""
        <div class="card">
        <ul>
            <li><b>التشخيص المرجح 1:</b> انفكاك المشيمة المبكر (Placental Abruption).</li>
            <li><b>التشخيص المرجح 2:</b> المشيمة المتقدمة (Placenta Previa).</li>
            <li><b>التشخيص المرجح 3:</b> تمزق الرحم (Uterine Rupture - خاصة مع وجود ندبة سابقة).</li>
        </ul>
        <b>الخطوات الإكلينيكية المقترحة:</b> تجنب الفحص المهني الداخلي (Digital Vaginal Examination) حتى يتم نفي المشيمة المتقدمة بالسونار، تقييم نبض الجنين (CTG)، وتأمين وريدين وتوفير وحدات دم.
        </div>
        """, unsafe_allow_html=True)

    elif symptom_category == "آلام الحوض والبطن الحادة (Acute Abdominal Pain)":
        st.markdown("""
        <div class="card">
        <ul>
            <li><b>التشخيص المرجح 1:</b> التواء كيس المبيض (Ovarian Torsion).</li>
            <li><b>التشخيص المرجح 2:</b> التهاب الزائدة الدودية الحاد (Acute Appendicitis).</li>
            <li><b>التشخيص المرجح 3:</b> انقباضات الرحم المبكرة أو المخاض المبكر.</li>
        </ul>
        <b>الخطوات الإكلينيكية المقترحة:</b> فحص دوبلر للمبيضين بالسونار، تحليل بول، وتحليل صورة دم كاملة (CBC).
        </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("""
        <div class="card">
        <ul>
            <li><b>التشخيص المرجح 1:</b> تسمم الحمل الشديد (Severe Preeclampsia).</li>
            <li><b>التشخيص المرجح 2:</b> متلازمة هيلب (HELLP Syndrome).</li>
            <li><b>التشخيص المرجح 3:</b> تسمم الحمل المزمن المتفاقم.</li>
        </ul>
        <b>الخطوات الإكلينيكية المقترحة:</b> قياس ضغط الدم بدقة، فحص الزلال في البول (Proteinuria)، طلب تحاليل وظائف كبد وكلي وتعداد صفائح دموية (Platelets)، وبدء بروتوكول كبريتات المغنيسيوم (MgSO4) عند الحاجة.
        </div>
        """, unsafe_allow_html=True)

# ---------------- القسم الثاني: حسابات الحمل ----------------
elif menu == "حسابات الحمل والعمر الحملي":
    st.header("📅 حاسبة العمر الحملي وموعد الولادة المتوقع")
    
    import datetime
    
    col1, col2 = st.columns(2)
    with col1:
        lmp_date = st.date_input("تاريخ آخر دوره menstruation (LMP):", datetime.date.today() - datetime.timedelta(days=90))
        
    if lmp_date:
        today = datetime.date.today()
        delta = today - lmp_date
        total_days = delta.days
        weeks = total_days // 7
        days = total_days % 7
        
        edd = lmp_date + datetime.timedelta(days=280)
        
        with col2:
            st.markdown(f"""
            <div class="card">
            <h4>نتائج الحساب:</h4>
            <p><b>العمر الحملي الحالي:</b> {weeks} أسبوع و {days} أيام</p>
            <p><b>موعد الولادة المتوقع (EDD):</b> {edd.strftime('%Y-%m-%d')}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- القسم الثالث: دليل الأدوية والطوارئ ----------------
elif menu == "دليل الأدوية والطوارئ":
    st.header("💊 دليل الأدوية والجرعات السريعة")
    
    drug_search = st.text_input("ابحث عن اسم الدواء أو التصنيف العلاجي:", "")
    
    drugs_data = [
        {"name": "Magnesium Sulfate (كبريتات المغنيسيوم)", "category": "مضادات الاختلاج / تسمم الحمل", "dose": "جرعة تحميلية 4-6 جرام وريدي ببطء، ثم 1-2 جرام/ساعة مستمر."},
        {"name": "Oxytocin (أوكسيتوسين)", "category": "مقويات الرحم / تحفيز المخاض", "dose": "10-20 وحدة في محلول وريدي لتنظيم التقلصات ومنع النزيف التالي للوضع."},
        {"name": "Labetalol (لابيتالول)", "category": "خافض ضغط الدم في الحمل", "dose": "20-40 ملغ وريدي، يمكن تكرارها عند الحاجة لارتفاع الضغط الحاد."},
        {"name": "Tranexamic Acid (حمض الترانيكساميك)", "category": "موقف للنزيف", "dose": "1 جرام وريدي ببطء في حالات نزيف ما بعد الولادة (PPH)."}
    ]
    
    for drug in drugs_data:
        if drug_search.lower() in drug["name"].lower() or drug_search.lower() in drug["category"].lower() or drug_search == "":
            st.markdown(f"""
            <div class="card">
            <h4>{drug['name']}</h4>
            <p><b>التصنيف:</b> {drug['category']}</p>
            <p><b>الجرعة الإكلينيكية الشائعة:</b> {drug['dose']}</p>
            </div>
            """, unsafe_allow_html=True)

# ---------------- القسم الرابع: إرشادات الاستخدام ----------------
else:
    st.header("ℹ️ إرشادات الاستخدام")
    st.markdown("""
    <div class="card">
    <p>هذا التطبيق مصمم ليكون أداة مساعدة سريعة (Decision Support Tool) للطبيبة والكوادر الطبية في سرعة تقييم الحالات واتخاذ القرار السريري.</p>
    <p><b>ملاحظة هامة:</b> لا يُغنى هذا التطبيق عن الفحص السريري المباشر والتقدير الطبي الشخصي للحالة وفقاً للبروتوكولات المعتمدة في المستشفى.</p>
    </div>
    """, unsafe_allow_html=True)
