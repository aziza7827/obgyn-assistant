import streamlit as st
from datetime import datetime, date, timedelta

# ---------------- 1. إعدادات الصفحة والتصميم العام (CSS) ----------------
st.set_page_config(
    page_title="المساعد السريري لأمراض النساء والتوليد",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصاميم والألوان الطبية الهادئة
st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        color: #1E3A8A;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        padding-bottom: 10px;
        border-bottom: 2px solid #DBEAFE;
    }
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 12px;
        border-right: 5px solid #2563EB;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .card h3 {
        color: #1E40AF;
        margin-top: 0;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- 2. القائمة الجانبية (Sidebar) مع اسم الدكتورة ----------------
st.sidebar.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🩺 المساعد السريري</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #64748B;'>مرجع طبي تخصصي للنساء والتوليد</p>", unsafe_allow_html=True)
# إضافة اسم الدكتورة بشكل مميز في الشريط الجانبي
st.sidebar.markdown("<div style='background-color: #E0F2FE; padding: 10px; border-radius: 8px; text-align: center; margin-bottom: 15px;'><b style='color: #0369A1;'>إشراف وتطوير:<br>Dr. Aziza Mohammed</b></div>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "اختر القسم المطلوب:",
    [
        "🏠 الرئيسية ونظرة عامة",
        "🧮 الحاسبات السريرية (الحمل والولادة)",
        "🧠 محرك التشخيص الذكي للأعراض",
        "🔍 التشخيص التفريقي الطارئ",
        "💊 دليل الأدوية والجرعات السريرية"
    ]
)

# ---------------- 3. صفحة الرئيسية ونظرة عامة ----------------
if menu == "🏠 الرئيسية ونظرة عامة":
    st.markdown('<div class="main-header">أهلاً بكِ دكتورة عزيزة في المساعد السريري لأمراض النساء والتوليد</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="card">
            <h3>🎯 هدف التطبيق</h3>
            <p>توفير مرجع سريري سريع، منظم، ومحدث بدقة لمساعدة الطبيبة في اتخاذ القرارات السريرية، حساب تواريخ الحمل، مراجعة الجرعات الدوائية بدقة، والوصول السريع لتشخيص الحالات الإسعافية الحرجة في قسم النساء والتوليد.</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="card">
            <h3>⚙️ الأقسام المتاحة</h3>
            <p><b>1. الحاسبات السريرية:</b> لحساب عمر الحمل وموعد الولادة المتوقع بدقة.<br>
            <b>2. محرك التشخيص الذكي:</b> إدخال الأعراض والعلامات للحصول على التشخيص المحتمل فوراً.<br>
            <b>3. التشخيص التفريقي الطارئ:</b> خطوات منظمة للتعامل مع الطوارئ.<br>
            <b>4. دليل الأدوية الشامل:</b> مرجع موسع يضم الأدوية، الجرعات، ومحاذير الاستخدام أثناء الحمل.</p>
            </div>
        """, unsafe_allow_html=True)

# ---------------- 4. الحاسبات السريرية ----------------
elif menu == "🧮 الحاسبات السريرية (الحمل والولادة)":
    st.markdown('<div class="main-header">🧮 الحاسبات السريرية للحمل والولادة</div>', unsafe_allow_html=True)
    
    calc_type = st.radio("اختر نوع الحساب:", ["حساب موعد الولادة وعمر الحمل (بواسطة آخر دورة شهرية - LMP)", "حساب عمر الحمل بالموجات فوق الصوتية (Ultrasound)"])
    
    if "بواسطة آخر دورة شهرية" in calc_type:
        st.markdown("### حساب عمر الحمل وموعد الولادة بناءً على LMP")
        lmp_date = st.date_input("أدخل تاريخ أول يوم لآخر دورة شهرية (LMP):", value=date.today())
        
        if st.button("حساب النتائج"):
            today = date.today()
            delta = today - lmp_date
            total_days = delta.days
            
            if total_days < 0:
                st.error("التاريخ المدخل لآخر دورة شهرية مستقبلي! يرجى التحقق من التاريخ.")
            else:
                weeks = total_days // 7
                days = total_days % 7
                edd = lmp_date + timedelta(days=280)
                
                st.success(f"📅 **موعد الولادة المتوقع (EDD):** {edd.strftime('%Y-%m-%d')}")
                st.info(f"⏳ **عمر الحمل الحالي:** {weeks} أسبوع و {days} يوم.")

    else:
        st.markdown("### حساب عمر الحمل بواسطة السونار (US Dating)")
        us_weeks = st.number_input("الأسابيع بالسونار:", min_value=0, max_value=42, value=12)
        us_days = st.number_input("الأيام الإضافية بالسونار:", min_value=0, max_value=6, value=0)
        scan_date = st.date_input("تاريخ إجراء السونار:", value=date.today())
        
        if st.button("حساب العمر الحالي المتوقع"):
            scan_total_days = (us_weeks * 7) + us_days
            days_passed = (date.today() - scan_date).days
            current_total_days = scan_total_days + days_passed
            
            curr_w = current_total_days // 7
            curr_d = current_total_days % 7
            
            st.info(f"⏳ **عمر الحمل الحالي المتوقع اليوم:** {curr_w} أسبوع و {curr_d} يوم.")

# ---------------- 5. محرك التشخيص الذكي للأعراض ----------------
elif menu == "🧠 محرك التشخيص الذكي للأعراض":
    st.markdown('<div class="main-header">🧠 محرك التشخيص السريري الذكي للأعراض والعلامات</div>', unsafe_allow_html=True)
    st.markdown("<p style='color: #64748B;'>قومي بتحديد الأعراض والعلامات السريرية التي تظهر على المريضة ليقوم النظام بتحليلها وإعطاء التشخيص المحتمل والخطة الإسعافية مباشرة.</p>", unsafe_allow_html=True)
    
    with st.form("diagnostic_form"):
        st.subheader("حدد الأعراض والعلامات الملاحظة:")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            sym_bleeding = st.checkbox("نزيف مهبلي (Vaginal Bleeding)")
            sym_abig_pain = st.checkbox("ألم شديد في البطن أو الحوض (Severe Abdominal/Pelvic Pain)")
            sym_high_bp = st.checkbox("ارتفاع ضغط الدم (BP ≥ 140/90 mmHg)")
            sym_headache_blurry = st.checkbox("صداع شديد أو زغللة في الرؤية (Severe Headache / Blurry Vision)")
            sym_fever = st.checkbox("ارتفاع درجة الحرارة / حمى (Fever)")
        
        with col_f2:
            sym_pph = st.checkbox("نزيف غزير بعد الولادة (Postpartum Hemorrhage)")
            sym_atonic = st.checkbox("رخاوة وعدم انقباض الرحم بعد الولادة (Atonic Uterus)")
            sym_vomiting = st.checkbox("غثيان وقيء مستمر وشديد (Hyperemesis / Severe Vomiting)")
            sym_edema = st.checkbox("تورم واستمساء عام (Generalized Edema / Face & Hands)")
            sym_cervix_open = st.checkbox("عنق الرحم مفتوح أثناء النزيف (Open Cervix in Early Pregnancy)")

        submit_diagnosis = st.form_submit_button("تحليل الأعراض وإظهار التشخيص")

    if submit_diagnosis:
        st.markdown("---")
        st.subheader("📋 نتائج التشخيص التفريقي والخطوات السريرية:")
        
        matched_cases = 0
        
        if sym_bleeding and sym_abig_pain and not sym_pph:
            matched_cases += 1
            st.markdown("""
                <div class="card" style="border-right-color: #DC2626;">
                <h3 style="color: #DC2626;">🚨 تشخيص محتمل عالي الخطورة: الحمل خارج الرحم (Ectopic Pregnancy) أو إجهاض منذر/منسد</h3>
                <p><b>الأعراض المطابقة:</b> نزيف مهبلي + ألم شديد في البطن/الحوض.</p>
                <p><b>الإجراءات الطبية الفورية:</b><br>
                1. تركيب خط وريدي (IV Line) وسحب دم لفحص فصيلة الدم (Blood Group & Rh) وصورة الدم الكاملة (CBC).<br>
                2. إجراء موجات فوق صوتية فورية (Pelvic/Transvaginal US) للتأكد من وجود كيس الحمل داخل الرحم.<br>
                3. في حال تأكيد الحمل خارج الرحم والمريضة غير مستقرة: تحويل فوري للجراحة الطارئة.</p>
                </div>
            """, unsafe_allow_html=True)

        if sym_high_bp and (sym_headache_blurry or sym_edema):
            matched_cases += 1
            st.markdown("""
                <div class="card" style="border-right-color: #D97706;">
                <h3 style="color: #D97706;">⚠️ تشخيص محتمل: تسمم الحمل الشديد (Severe Preeclampsia)</h3>
                <p><b>الأعراض المطابقة:</b> ارتفاع ضغط الدم مع أعراض عصبية/بصرية أو تورم شديد.</p>
                <p><b>الإجراءات الطبية الفورية:</b><br>
                1. فحص البول للبروتين (Proteinuria) وتقييم وظائف الكلى والكبد وصفيحات الدم.<br>
                2. إعطاء خافض للضغط الإسعافي إذا كان الضغط $\\ge$ 160/110 ملم زئبق (مثل Labetalol وريدياً).<br>
                3. بدء كبريتات المغنيسيوم ($MgSO_4$) كجرعة تحميلية للوقاية من التشنجات (Eclampsia) مع مراقبة التنفس وانعكاس الرضفة.</p>
                </div>
            """, unsafe_allow_html=True)

        if sym_pph or sym_atonic:
            matched_cases += 1
            st.markdown("""
                <div class="card" style="border-right-color: #DC2626;">
                <h3 style="color: #DC2626;">🚨 حالة طوارئ توليدية: نزيف ما بعد الولادة (PPH due to Atonic Uterus)</h3>
                <p><b>الأعراض المطابقة:</b> نزيف غزير ورخاوة الرحم بعد الولادة.</p>
                <p><b>الإجراءات الطبية الفورية (قاعدة 4 Ts):</b><br>
                1. طلب المساعدة واستدعاء فريق الطوارئ، إعطاء أكسجين قناع وجه، وفتح خطين وريديين بمقاس واسع (16G/18G).<br>
                2. إجراء تدليك رحمي مستمر (Bimanual Uterine Massage).<br>
                3. إعطاء الأوكسيتوسين وريدياً/عضلياً، وميسوبروستول مستقيماً، والميثيل إرغومترين (إن لم تكن المريضة مصابة بارتفاع الضغط).</p>
                </div>
            """, unsafe_allow_html=True)

        if sym_bleeding and sym_cervix_open:
            matched_cases += 1
            st.markdown("""
                <div class="card" style="border-right-color: #2563EB;">
                <h3>🔍 تشخيص محتمل: إجهاض حتمي أو غير كامل (Inevitable / Incomplete Abortion)</h3>
                <p><b>الأعراض المطابقة:</b> نزيف مهبلي مع انفتاح عنق الرحم.</p>
                <p><b>الإجراءات الطبية الفورية:</b><br>
                1. إجراء سونار لتقييم محتويات الرحم وبقايا الحمل.<br>
                2. تحضير المريضة لتفريغ الرحم (Evacuation/Curettage أو استخدام الأدوية مثل Misoprostol حسب الحالة والعمر الحملي) وإعطاء مضاد حيوي وقائي وتحليل Rh (وإعطاء Anti-D إذا كانت الأم Rh Negative).</p>
                </div>
            """, unsafe_allow_html=True)

        if matched_cases == 0:
            st.info("الرجاء اختيار مجموعة أعراض متناسقة للحصول على التشخيص الدقيق، أو مراجعة قسم التشخيص التفريقي الطارئ للمزيد من التفاصيل.")

# ---------------- 6. التشخيص التفريقي الطارئ ----------------
elif menu == "🔍 التشخيص التفريقي الطارئ":
    st.markdown('<div class="main-header">🔍 المساعد الذكي للتشخيص التفريقي الإسعافي</div>', unsafe_allow_html=True)
    
    emergency_case = st.selectbox(
        "اختر الحالة الإسعافية أو العرض السريري:",
        [
            "نزيف النصف الأول من الحمل (First Trimester Bleeding)",
            "نزيف ما بعد الولادة (Postpartum Hemorrhage - PPH)",
            "ارتفاع ضغط الدم وتسمم الحمل الشديد (Severe Preeclampsia)"
        ]
    )
    
    if emergency_case == "نزيف النصف الأول من الحمل (First Trimester Bleeding)":
        st.markdown("""
            <div class="card">
            <h3>التشخيص التفريقي وخطوات التعامل:</h3>
            <p><b>1. الإجهاض المنذر (Threatened Abortion):</b> عنق الرحم مغلق، نبض الجنين موجود بالسونار.<br>
            <b>2. الحمل خارج الرحم (Ectopic Pregnancy):</b> ألم شديد بالحوض، اختبار حمل إيجابي مع عدم وجود كيس داخل الرحم بالسونار (تعتبر حالة طوارئ جراحية).<br>
            <b>3. الإجهاض الحتمي أو غير الكامل (Inevitable/Incomplete Abortion):</b> عنق الرحم مفتوح، نزيف مصحوب بتقلصات.<br>
            <b>4. الحمل العنقودي (Molar Pregnancy):</b> نزيف مع رحم أكبر من عمر الحمل وغياب نبض الجنين (صورة عاصفة الثلج بالسونار).</p>
            <p style="color: #DC2626;"><b>الإجراءات الأولية:</b> فحص علامات حيوية، تركيب خط وريدي (IV Line)، طلب فحص فصيلة الدم والـ Rh، وسونار حوضي/مهبلي فوري.</p>
            </div>
        """, unsafe_allow_html=True)
        
    elif emergency_case == "نزيف ما بعد الولادة (Postpartum Hemorrhage - PPH)":
        st.markdown("""
            <div class="card">
            <h3>بروتوكول التعامل الفوري مع PPH (قاعدة الـ 4 Ts):</h3>
            <p><b>1. التقييم والإنعاش السريع:</b> طلب المساعدة، استدعاء فريق الطوارئ، إعطاء أكسجين، تركيب خطين وريدين بمقاس كبير (16G أو 18G) وبدء تسريب السوائل وريدياً والمحاليل الدافئة.<br>
            <b>2. الأسباب الأربعة (4 Ts):</b><br>
               - <b>رخاوة الرحم (Tone - Atonic Uterus):</b> السبب الأهم (يمثل 70-80% من الحالات). التعامل: تدليك الرحم اليدوي، إعطاء الأوكسيتوسين، ميثيل إرغومترين (إن لم يوجد ضغط مرتفع)، والميسوبروستول.<br>
               - <b>بقايا المشيمة (Tissue):</b> التأكد من خروج المشيمة كاملة وإجراء تنظيف يدوي إن لزم الأمر.<br>
               - <b>الإصابات وتمزقات قناة الولادة (Trauma):</b> فحص دقيق لعنق الرحم والمهبل وعمل خياطة جراحية للتمزقات.<br>
               - <b>اضطرابات التجلط (Thrombin):</b> فحص وظائف التجلط، نسب الفيبرينوجين، وإعطاء مشتقات الدم عند الحاجة.</p>
            </div>
        """, unsafe_allow_html=True)
        
    elif emergency_case == "ارتفاع ضغط الدم وتسمم الحمل الشديد (Severe Preeclampsia)":
        st.markdown("""
            <div class="card">
            <h3>إدارة حالات تسمم الحمل الشديد وطوارئ الضغط:</h3>
            <p><b>1. خفض ضغط الدم الإسعافي:</b> إذا كان الضغط $\\ge$ 160/110 ملم زئبق، يُعطى اللابتالول وريدياً أو نيديبين فموياً لخفض الضغط تدريجياً وتجنب الهبوط المفاجئ الذي يضر بتروية المشيمة.<br>
            <b>2. الوقاية من التشنجات (Eclampsia):</b> إعطاء كبريتات المغنيسيوم ($MgSO_4$) كجرعة تحميلية وصيانة مع المراقبة المستمرة للتنفس وانعكاس الرضفة وإخراج البول.<br>
            <b>3. تحديد توقيت الولادة:</b> القرار النهائي هو إنهاء الحمل (الولادة) بغض النظر عن عمر الحمل إذا كانت الحالة غير مستقرة أو ظهرت علامات خطورة عصبية أو بصرية أو كبدية/كلوية.</p>
            </div>
        """, unsafe_allow_html=True)

# ---------------- 7. دليل الأدوية والجرعات السريرية ----------------
elif menu == "💊 دليل الأدوية والجرعات السريرية":
    st.markdown('<div class="main-header">💊 الدليل السريري الشامل لأدوية النساء والتوليد</div>', unsafe_allow_html=True)

    drug_category = st.selectbox(
        "اختر التصنيف الدوائي الموسع:",
        [
            "أدوية تحفيز الطلق والرحم (Uterotonics)",
            "موانع المخاض والتقلصات (Tocolytics)",
            "مخفضات ضغط الدم الآمنة في الحمل",
            "علاج تسمم الحمل وطوارئ الضغط (Magnesium Sulfate)",
            "محرضات نضج رئتي الجنين (Antenatal Corticosteroids)",
            "أدوية تثبيت الحمل والإجهاض المنذر (Progestogens)",
            "أدوية سكري الحمل (Gestational Diabetes Medications)",
            "مسكنات الألم ومضادات الالتهاب (Analgesics & NSAIDs)",
            "أدوية علاج الغثيان والقيء في الحمل (Antiemetics - موسع)",
            "المضادات الحيوية والمضادات الشاملة في الحمل (Antibiotics & Antimicrobials)",
            "أدوية علاج الالتهابات المهبلية والفطرية أثناء الحمل",
        ],
    )

    if drug_category == "أدوية تحفيز الطلق والرحم (Uterotonics)":
        st.markdown("""
            <div class="card">
            <h3>1. الأوكسيتوسين (Oxytocin - Pitocin):</h3>
            <p><b>الاستخدام:</b> تحريض الولادة، تعزيز المخاض، والوقاية والعلاج من نزيف ما بعد الولادة (PPH).</p>
            <p><b>جرعة التحريض:</b> يبدأ بـ 1-2 ملي وحدة/دقيقة وتُضاعف تدريجياً كل 30-40 دقيقة مع مراقبة الانقباضات وتخطيط قلب الجنين (CTG).</p>
            <p><b>جرعة الوقاية من PPH:</b> 10 وحدات عضلياً (IM) أو وريدياً ببطء بعد خروج الجنين مباشرة.</p>
            <p><b>جرعة علاج PPH:</b> 10-40 وحدة مخففة في محلول وريدي بتسريب مستمر.</p>
            </div>
            
            <div class="card">
            <h3>2. ميثيل إرغومترين (Methergine):</h3>
            <p><b>الاستخدام:</b> علاج نزيف ما بعد الولادة الناتج عن رخاوة الرحم (Atonic PPH).</p>
            <p><b>الجرعة:</b> 0.2 ملغ عضلياً (IM).</p>
            <p style="color: #DC2626;"><b>تحذير صارم:</b> يمنع منعاً باتاً استخدامه للمريضات اللاتي يعانين من ارتفاع ضغط الدم.</p>
            </div>
            
            <div class="card">
            <h3>3. ميسوبروستول (Misoprostol - Cytotec):</h3>
            <p><b>الاستخدام:</b> الوقاية والعلاج من PPH، وإنضاج عنق الرحم للتحريض أو إجهاض الفوات.</p>
            <p><b>جرعة الوقاية:</b> 600 ميكروغرام فموياً أو مستقيماً. <b>جرعة العلاج:</b> 800-1000 ميكروغرام مستقيماً.</p>
            </div>
            
            <div class="card">
            <h3>4. كاربوبروست (Carboprost - Hemabate):</h3>
            <p><b>الاستخدام:</b> علاج النزيف المستعصي (Refractory PPH).</p>
            <p><b>الجرعة:</b> 250 ميكروغرام عضلياً كل 15-90 دقيقة (بحد أقصى 8 جرعات).</p>
            <p style="color: #DC2626;"><b>تحذير:</b> يمنع في حالات الربو (Asthma).</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "موانع المخاض والتقلصات (Tocolytics)":
        st.markdown("""
            <div class="card">
            <h3>1. نيديبين (Nifedipine):</h3>
            <p><b>الاستخدام:</b> الخط الأول لإرخاء الرحم وإيقاف المخاض المبكر (Preterm Labor) بين الأسبوع 24 و 34.</p>
            <p><b>الجرعة:</b> 20 ملغ فموياً، تليها 10-20 ملغ كل 4-6 ساعات مع مراقبة ضغط الدم لتجنب الهبوط المفاجئ.</p>
            </div>
            
            <div class="card">
            <h3>2. أتوسيبان (Atosiban):</h3>
            <p><b>الاستخدام:</b> مضاد لمستقبلات الأوكسيتوسين (الأكثر أماناً قلبياً للأم).</p>
            <p><b>الجرعة:</b> حقنة وريدية تحميلية تليها تسريب مستمر حسب البروتوكول.</p>
            </div>

            <div class="card">
            <h3>3. إندوميثاسين (Indomethacin):</h3>
            <p><b>الاستخدام:</b> مضاد للبروستاجلاندين يُستخدم بشرط أن يكون الحمل <b>قبل الأسبوع 32</b>.</p>
            <p style="color: #DC2626;"><b>تحذير:</b> يمنع بعد الأسبوع 32 لتجنب انغلاق القناة الشريانية للجنين وقلة السائل الأمنيوسي.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "مخفضات ضغط الدم الآمنة في الحمل":
        st.markdown("""
            <div class="card">
            <h3>1. لابتالول (Labetalol):</h3>
            <p><b>الاستخدام:</b> علاج ارتفاع ضغط الدم المزمن أو الشديد وتسمم الحمل.</p>
            <p><b>الجرعة الفموية:</b> 100-200 ملغ فموياً 2-3 مرات يومياً. <b>جرعة الطوارئ الوريدية:</b> 20 ملغ ببطء وتُكرر عند الحاجة.</p>
            </div>
            
            <div class="card">
            <h3>2. ميثيل دوبا (Methyldopa):</h3>
            <p><b>الاستخدام:</b> الخط الأقدم والأكثر أماناً لارتفاع الضغط المزمن.</p>
            <p><b>الجرعة:</b> 250 إلى 500 ملغ فموياً مرتين إلى ثلاث مرات يومياً.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "علاج تسمم الحمل وطوارئ الضغط (Magnesium Sulfate)":
        st.markdown("""
            <div class="card">
            <h3>كبريتات المغنيسيوم (Magnesium Sulfate):</h3>
            <p><b>الاستخدام:</b> الوقاية والعلاج من نوبات الصرع الحملي (Eclampsia).</p>
            <p><b>جرعة التحميل (Loading Dose):</b> 4 إلى 6 غرام وريدياً ببطء خلال 15-20 دقيقة.</p>
            <p><b>جرعة الصيانة (Maintenance Dose):</b> 1 إلى 2 غرام في الساعة تسريب وريدي مستمر.</p>
            <p style="color: #DC2626;"><b>ملاحظات أمان حرجة:</b> متابعة معدل التنفس ($\\ge$ 12)، ردود الفعل العصبية، وإخراج البول. يجب توفر <b>غلوكونات الكالسيوم (Calcium Gluconate 10%)</b> كإسعاف فوري للتسمم.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "محرضات نضج رئتي الجنين (Antenatal Corticosteroids)":
        st.markdown("""
            <div class="card">
            <h3>1. بيتاميثازون (Betamethasone):</h3>
            <p><b>الاستخدام:</b> لتحفيز نضج رئتي الجنين بين الأسبوع 24 و 34.</p>
            <p><b>الجرعة:</b> 12 ملغ عضلياً (IM) تُعطى مرتان بينهما 24 ساعة (إجمالي 24 ملغ).</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "أدوية تثبيت الحمل والإجهاض المنذر (Progestogens)":
        st.markdown("""
            <div class="card">
            <h3>1. بروجسترون ميكرونايزد (Micronized Progesterone - Utrogestan):</h3>
            <p><b>الاستخدام:</b> دعم الحمل والوقاية من الإجهاض المتكرر والمنذر.</p>
            <p><b>الجرعة:</b> 200 إلى 400 ملغ يومياً (يفضل الاستخدام المهبلي لتقليل الدوخة).</p>
            </div>
            
            <div class="card">
            <h3>2. ديدروجسترون (Dydrogesterone - Duphaston):</h3>
            <p><b>الجرعة:</b> 10 إلى 20 ملغ مرتين يومياً.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "أدوية سكري الحمل (Gestational Diabetes Medications)":
        st.markdown("""
            <div class="card">
            <h3>1. الإنسولين (Insulin - المعيار الذهبي والآمن تماماً):</h3>
            <p><b>الاستخدام:</b> السيطرة على سكر الحمل عند عدم كفاية الحمية الغذائية (يتضمن إنسولين قاعدي وسريع المفعول).</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "مسكنات الألم ومضادات الالتهاب (Analgesics & NSAIDs)":
        st.markdown("""
            <div class="card">
            <h3>1. باراسيتامول (Paracetamol / Panadol):</h3>
            <p><b>الاستخدام:</b> المسكن والخافض للحرارة <b>الأكثر أماناً</b> طوال الحمل. الجرعة: 500 ملغ إلى 1 غرام كل 6 ساعات.</p>
            </div>
            <div class="card">
            <h3>2. مضادات الالتهاب غير الستيرويدية (NSAIDs مثل Ibuprofen):</h3>
            <p style="color: #DC2626;"><b>تحذير صارم:</b> تمنع منعاً باتاً في <b>الثلث الثالث من الحمل</b> لتجنب انغلاق القناة الشريانية للجنين وفشل الكلى.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "أدوية علاج الغثيان والقيء في الحمل (Antiemetics - موسع)":
        st.markdown("""
            <div class="card">
            <h3>1. بيريدوكسين + دوكسيلامين (Pyridoxine / Doxylamine - Diclectin):</h3>
            <p><b>الاستخدام:</b> الخط الأول الآمن تماماً (Category A) للغثيان الصباحي.</p>
            </div>
            <div class="card">
            <h3>2. ميتوكلوبراميد (Metoclopramide) & أوندانسيترون (Ondansetron):</h3>
            <p><b>الاستخدام:</b> للحالات المعتدلة إلى الشديدة من القيء المفرط الحملي (Hyperemesis Gravidarum).</p>
            <p><b>الجرعة لأوندانسيترون:</b> 4-8 ملغ فموياً أو وريدياً عند الحاجة.</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "المضادات الحيوية والمضادات الشاملة في الحمل (Antibiotics & Antimicrobials)":
        st.markdown("""
            <div class="card">
            <h3>المجموعات الآمنة (FDA Category B & A):</h3>
            <ul>
                <li><b>البنسلينات ومشتقاتها:</b> مثل Amoxicillin و Augmentin.</li>
                <li><b>السيفالوسبورينات:</b> مثل Ceftriaxone و Cefalexin.</li>
                <li><b>الماكروليدات:</b> مثل Azithromycin (بديل لحساسية البنسلين).</li>
            </ul>
            <p style="color: #DC2626;"><b>ممنوعات قطعية:</b> يُمنع تماماً التتراسيكلين، الفلوروكينولون (مثل Ciprofloxacin)، والأمينوغليكوزيدات (إلا للضرورة القصوى).</p>
            </div>
        """, unsafe_allow_html=True)

    elif drug_category == "أدوية علاج الالتهابات المهبلية والفطرية أثناء الحمل":
        st.markdown("""
            <div class="card">
            <h3>1. مضادات الفطريات موضعياً (Clotrimazole / Miconazole):</h3>
            <p><b>الاستخدام:</b> العلاج الآمن لالتهابات المهبل الفطرية (كريم أو تحاميل مهبلية لمدة 7 أيام).</p>
            </div>
            <div class="card">
            <h3>2. ميترونيدازول (Metronidazole - Flagyl):</h3>
            <p><b>الاستخدام:</b> علاج التهاب المهبل البكتيري (500 ملغ فموياً مرتين يومياً لمدة 7 أيام).</p>
            </div>
        """, unsafe_allow_html=True)
