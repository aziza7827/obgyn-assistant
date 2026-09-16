import datetime
import streamlit as st

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="المساعد الذكي لعيادة النساء والولادة - Dr. Aziza",
    page_icon="🩺",
    layout="wide",
)

# تخصيص الألوان والتصميم (CSS Custom Styling)
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #4A90E2;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# القائمة الجانبية: اسم الطبيبة واختيار اللغة
st.sidebar.markdown("### 👩‍⚕️ **Dr. aziza mohmmed**")
st.sidebar.markdown("---")

lang = st.sidebar.selectbox("🌐 Choose Language / اختر اللغة", ["العربية", "English"])

if lang == "العربية":
  title_text = "🩺 المساعد الذكي المتقدم لعيادة النساء والولادة"
  subtitle_text = (
      "--- \n نظام إكلينيكي متكامل ومبسط لإدارة الحسابات، الأدوية، والطوارئ الطبية."
  )
  menu_label = "اختر القسم المطلوب:"
  menu_options = [
      "1. التشخيص التفريقي للحالات الطارئة",
      "2. التشخيص السريع عبر الأعراض والعلامات",
      "3. حسابات وتتبع مراحل الحمل",
      "4. دليل الأدوية والمثبتات الشامل",
      "5. الفحوصات المخبرية والأشعة التلفزيونية",
  ]
else:
  title_text = "🩺 Advanced OB/GYN Clinical Assistant"
  subtitle_text = (
      "--- \n Comprehensive clinical system for calculations, medications, and"
      " emergency management."
  )
  menu_label = "Select Section:"
  menu_options = [
      "1. Emergency Differential Diagnosis",
      "2. Symptom-Based Quick Diagnosis",
      "3. Pregnancy Calculations & Tracking",
      "4. Comprehensive Medication & Progesterone Guide",
      "5. Labs & Ultrasound Guide",
  ]

st.title(title_text)
st.markdown(subtitle_text)

menu = st.sidebar.selectbox(menu_label, menu_options)

# ==========================================
# 1. التشخيص التفريقي للحالات الطارئة
# ==========================================
if (menu == "1. التشخيص التفريقي للحالات الطارئة") or (
    menu == "1. Emergency Differential Diagnosis"
):
  if lang == "العربية":
    st.header("🚨 التشخيص التفريقي الشامل للحالات الطارئة")
    emergency_type = st.selectbox(
        "اختر الحالة الطارئة للتقييم:",
        [
            "النزيف في الثلث الأول من الحمل (First Trimester Bleeding)",
            "آلام البطن الحادة وحالات البطن الجراحي (Acute Abdomen)",
            (
                "ارتفاع ضغط الدم الخطير وتسمم الحمل (Severe Preeclampsia &"
                " Eclampsia)"
            ),
            "النزيف التالي للولادة (Postpartum Hemorrhage - PPH)",
        ],
    )
    if (
        emergency_type
        == "النزيف في الثلث الأول من الحمل (First Trimester Bleeding)"
    ):
      st.markdown("""
            <div class="card">
            <h3>📌 تقييم النزيف المبكر:</h3>
            <ol>
                <li><b>التقييم الحيوي:</b> فحص ضغط الدم والنبض لاستبعاد الصدمة (Hypovolemic Shock).</li>
                <li><b>الأسباب الرئيسية:</b>
                    <ul>
                        <li><b>الحمل خارج الرحم (Ectopic Pregnancy):</b> طوارئ قصوى (ألم شديد، نزيف بني، عدم رؤية حمل داخل الرحم بالسونار).</li>
                        <li><b>الإجهاض بجميع أنواعه:</b> منذر (Threatened)، غير مكتمل (Inevitable/Incomplete)، أو مفقود (Missed).</li>
                        <li><b>الحمل العنقودي (Molar Pregnancy):</b> ارتفاع شديد في Beta-hCG وصورة ثلجية بالسونار.</li>
                    </ul>
                </li>
                <li><b>الفحوصات العاجلة:</b> Transvaginal US, Beta-hCG (quantitative), CBC, Blood Group & Rh (مع ضرورة إعطاء Anti-D لو الأم Rh Negative).</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
    elif (
        emergency_type
        == "آلام البطن الحادة وحالات البطن الجراحي (Acute Abdomen)"
    ):
      st.markdown("""
            <div class="card">
            <h3>📌 تقييم آلام البطن الحادة:</h3>
            <ul>
                <li><b>أسباب توليدية/نسائية:</b> انفتال كيس المبيض (Ovarian Torsion - ألم مفاجئ وشديد مع غثيان)، تمزق حمل خارج الرحم، التهاب بطانة الرحم الحاد.</li>
                <li><b>أسباب جراحية مرافقة:</b> التهاب الزائدة الدودية الحاد (Appendicitis - قد ينزاح موضع الألم قليلاً مع تقدم الحمل)، انسداد الأمعاء، حصوات المرارة أو الكلى.</li>
                <li><b>الإجراءات:</b> فحص سريري دقيق لتحديد مكان الألم، أشعة دوبلر للتأكد من تروية المبيض، تحليل بول وصورة دم (CBC).</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif (
        emergency_type
        == "ارتفاع ضغط الدم الخطير وتسمم الحمل (Severe Preeclampsia & Eclampsia)"
    ):
      st.markdown("""
            <div class="card">
            <h3>📌 تسمم الحمل الشديد (Severe Features):</h3>
            <ul>
                <li><b>العلامات السريرية المحذرة:</b> ضغط الدم ≥ 160/110 مم زئبق، صداع مستمر، زغللة في الرؤية، ألم حاد في الجزء العلوي الأيمن من البطن (Right Upper Quadrant pain).</li>
                <li><b>المخاطر:</b> انفصال المشيمة المبكر، النزيف الدماغي، الفشل الكلوي، أو حدوث تشنجات (Eclampsia).</li>
                <li><b>التصرف السريع:</b> إعطاء خافضات الضغط (Labetalol / Nifedipine)، كبريتات المغنيسيوم (MgSO4) لمنع التشنجات، وتقييم وضع الجنين فوراً والتحويل لمركز متخصص.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif emergency_type == "النزيف التالي للولادة (Postpartum Hemorrhage - PPH)":
      st.markdown("""
            <div class="card">
            <h3>📌 تدبير النزيف التالي للولادة (قواعد الـ 4 Ts):</h3>
            <ul>
                <li><b>1. Atony (رخاوة الرحم - السبب الأكبر):</b> تدليك الرحم (Bimanual massage)، إعطاء الأوكسيتوسين (Oxytocin)، ميسوبروستول (Misoprostol)، أو ميثيل إرجومترين.</li>
                <li><b>2. Trauma (التمزقات والجروح):</b> فحص قناة الولادة وعنق الرحم وخياطة الجروح بدقة.</li>
                <li><b>3. Tissue (بقايا المشيمة):</b> التأكد من خروج المشيمة كاملة وإزالة أي بقايا داخل الرحم.</li>
                <li><b>4. Thrombin (مشاكل التجلط):</b> فحص معاملات التجلط وإعطاء منشطات التخثر عند اللزوم.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
  else:
    # النسخة الإنجليزية للطوارئ
    st.header("🚨 Comprehensive Emergency Differential Diagnosis")
    emergency_type = st.selectbox(
        "Select Emergency Condition:",
        [
            "First Trimester Bleeding",
            "Acute Abdomen & Surgical Conditions",
            "Severe Preeclampsia & Eclampsia",
            "Postpartum Hemorrhage (PPH)",
        ],
    )
    if emergency_type == "First Trimester Bleeding":
      st.markdown("""
            <div class="card">
            <h3>📌 First Trimester Bleeding Assessment:</h3>
            <ol>
                <li><b>Hemodynamic Stability:</b> Check BP and pulse to rule out shock.</li>
                <li><b>Main Causes:</b> Ectopic Pregnancy, Spontaneous Abortion (Threatened, Inevitable, Incomplete), Molar Pregnancy.</li>
                <li><b>Urgent Labs & Imaging:</b> TVS ultrasound, quantitative Beta-hCG, CBC, Blood Group & Rh (Administer Anti-D if Rh negative).</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
    elif emergency_type == "Acute Abdomen & Surgical Conditions":
      st.markdown("""
            <div class="card">
            <h3>📌 Acute Abdomen Evaluation:</h3>
            <ul>
                <li><b>GYN Causes:</b> Ovarian torsion, ruptured ectopic pregnancy, PID.</li>
                <li><b>Surgical Causes:</b> Acute appendicitis, renal colic, cholecystitis.</li>
                <li><b>Action:</b> Detailed physical examination, Doppler ultrasound, urinalysis, and CBC.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif emergency_type == "Severe Preeclampsia & Eclampsia":
      st.markdown("""
            <div class="card">
            <h3>📌 Severe Preeclampsia Management:</h3>
            <ul>
                <li><b>Warning Signs:</b> BP ≥ 160/110 mmHg, severe headache, visual changes, RUQ abdominal pain.</li>
                <li><b>Immediate Actions:</b> Antihypertensives (Labetalol/Nifedipine), Magnesium Sulfate (MgSO4) for seizure prophylaxis, fetal monitoring, and urgent referral.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif emergency_type == "Postpartum Hemorrhage (PPH)":
      st.markdown("""
            <div class="card">
            <h3>📌 PPH Management (The 4 Ts):</h3>
            <ul>
                <li><b>Tone:</b> Uterine massage, Oxytocin, Misoprostol.</li>
                <li><b>Trauma:</b> Inspect and repair lacerations.</li>
                <li><b>Tissue:</b> Evacuate retained placental products.</li>
                <li><b>Thrombin:</b> Correct coagulopathy.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# 2. التشخيص السريع عبر الأعراض والعلامات
# ==========================================
elif (menu == "2. التشخيص السريع عبر الأعراض والعلامات") or (
    menu == "2. Symptom-Based Quick Diagnosis"
):
  if lang == "العربية":
    st.header("⚡ القسم التفاعلي: التشخيص السريع عبر الأعراض والعلامات")
    st.markdown(
        "اختر الأعراض الظاهرة على المريضة للحصول على التشخيص التفريقي المقترح"
        " والإجراء الأولي فوراً:"
    )

    col1, col2 = st.columns(2)
    with col1:
      sym_bleeding = st.checkbox("نزيف مهدّد أو نازف (Vaginal Bleeding)")
      sym_pain = st.checkbox("ألم حاد في أسفل البطن (Lower Abdominal Pain)")
      sym_fever = st.checkbox("ارتفاع درجات الحرارة / حمى (Fever)")
    with col2:
      sym_bp = st.checkbox("ارتفاع ضغط الدم (High BP / Edema)")
      sym_vomit = st.checkbox("غثيان وقيء مستمر (Severe Nausea/Vomiting)")
      sym_discharge = st.checkbox(
          "إفرازات مهعضية غير طبيعية / حكة (Abnormal Discharge)"
      )

    st.markdown("---")
    st.subheader("📋 النتيجة التشخيصية المقترحة:")

    if sym_bleeding and sym_pain:
      st.error(
          "⚠️ **احتمالية عالية:** حمل خارج الرحم (Ectopic Pregnancy) أو إجهاض"
          " منذر/غير مكتمل. *الإجراء الفوري:* أشعة تلفزيونية مهبلية وتحليل هرمون"
          " الحمل الكمي."
      )
    elif sym_bp:
      st.warning(
          "⚠️ **احتمالية عالية:** اضطرابات ضغط الدم المرتبطة بالحمل أو تسمم الحمل"
          " (Gestational Hypertension / Preeclampsia). *الإجراء الفوري:* قياس"
          " زلال البول وفحص وظائف الكلى."
      )
    elif sym_fever and sym_pain:
      st.warning(
          "⚠️ **احتمالية عالية:** التهاب الحوض (PID) أو التهاب المسالك البولية"
          " الحاد / التهاب الزائدة الدودية. *الإجراء الفوري:* تحليل بول (Urinalysis)"
          " وصورة دم كاملة (CBC)."
      )
    elif sym_vomit:
      st.info(
          "💡 **احتمالية عالية:** قيء الحمل المفرط (Hyperemesis Gravidarum)."
          " *الإجراء الفوري:* تقييم الجفاف، صرف محاليل وفيتامين B6 ومضادات"
          " للقيء آمنة."
      )
    elif sym_discharge:
      st.info(
          "💡 **احتمالية عالية:** التهابات مهبلية فطرية أو بكتيرية (Candidiasis"
          " / BV). *الإجراء الفوري:* فحص إكلينيكي وصرف مضادات فطرية موضعية آمنة."
      )
    else:
      st.success(
          "✅ يرجى تحديد الأعراض أعلاه لعرض التحليل التشخيصي المباشر."
      )
  else:
    st.header("⚡ Interactive Section: Symptom-Based Quick Diagnosis")
    st.markdown(
        "Select the patient's symptoms to instantly view the suggested"
        " differential diagnosis and initial action:"
    )

    col1, col2 = st.columns(2)
    with col1:
      sym_bleeding = st.checkbox("Vaginal Bleeding")
      sym_pain = st.checkbox("Severe Lower Abdominal Pain")
      sym_fever = st.checkbox("Fever / Elevated Temperature")
    with col2:
      sym_bp = st.checkbox("High Blood Pressure / Edema")
      sym_vomit = st.checkbox("Severe Nausea & Vomiting")
      sym_discharge = st.checkbox("Abnormal Vaginal Discharge / Itching")

    st.markdown("---")
    st.subheader("📋 Suggested Diagnostic Outcome:")

    if sym_bleeding and sym_pain:
      st.error(
          "⚠️ **High Probability:** Ectopic Pregnancy or Threatened/Incomplete"
          " Abortion. *Immediate Action:* Transvaginal ultrasound and"
          " quantitative Beta-hCG."
      )
    elif sym_bp:
      st.warning(
          "⚠️ **High Probability:** Gestational Hypertension or Preeclampsia."
          " *Immediate Action:* Urinalysis for protein and renal function tests."
      )
    elif sym_fever and sym_pain:
      st.warning(
          "⚠️ **High Probability:** PID, Acute UTI, or Appendicitis."
          " *Immediate Action:* Urinalysis and CBC."
      )
    elif sym_vomit:
      st.info(
          "💡 **High Probability:** Hyperemesis Gravidarum. *Immediate Action:*"
          " Assess hydration, prescribe safe antiemetics and Vitamin B6."
      )
    elif sym_discharge:
      st.info(
          "💡 **High Probability:** Vaginal Candidiasis or Bacterial Vaginosis."
          " *Immediate Action:* Clinical exam and safe topical antifungals."
      )
    else:
      st.success("✅ Please select symptoms above to view diagnostic analysis.")


# ==========================================
# 3. حسابات وتتبع مراحل الحمل
# ==========================================
elif (menu == "3. حسابات وتتبع مراحل الحمل") or (
    menu == "3. Pregnancy Calculations & Tracking"
):
  if lang == "العربية":
    st.header("📅 حسابات وتتبع مراحل الحمل (Pregnancy Calculator & Timeline)")

    col1, col2 = st.columns(2)
    with col1:
      lmp_date = st.date_input(
          "تاريخ آخر دورة شهرية (LMP):",
          value=datetime.date.today() - datetime.timedelta(days=70),
      )
    today = datetime.date.today()
    delta = today - lmp_date
    weeks = delta.days // 7
    days = delta.days % 7
    try:
      edd = lmp_date + datetime.timedelta(days=280)
    except:
      edd = "غير محدد"

    with col2:
      st.markdown(
          f"""
            <div style="background-color: #EBF3FB; padding: 15px; border-radius: 8px;">
                <h4 style="margin: 0; color: #1E3A8A;">📌 النتائج الحسابية:</h4>
                <p style="margin: 5px 0 0 0; font-size: 16px;">عمر الحمل: <b>{weeks} أسبوع و {days} أيام</b></p>
                <p style="margin: 5px 0 0 0; font-size: 16px;">موعد الولادة المتوقع (EDD): <b>{edd}</b></p>
            </div>
            """,
          unsafe_allow_html=True,
      )

    st.markdown("---")
    st.subheader("📋 الجدول الزمني لفترات الحمل والفحوصات المرتبطة:")
    st.markdown("""
        <div class="card">
        <ul>
            <li><b>الثلث الأول (First Trimester - من الأسبوع 0 إلى 13):</b>
                <ul>
                    <li>التركيز على دعم الحمل، إعطاء حمض الفوليك، وعمل سونار مبكر لتأكيد نبض الجنين وتحديد عمر الحمل بدقة.</li>
                </ul>
            </li>
            <br>
            <li><b>الثلث الثاني (Second Trimester - من الأسبوع 14 إلى 27):</b>
                <ul>
                    <li>إجراء مسح التشوهات التفصيلي (Anomaly Scan) بين الأسبوع 18-22.</li>
                    <li>بدء مكملات الحديد والكالسيوم ومتابعة نمو الجنين وحركة الحنين.</li>
                </ul>
            </li>
            <br>
            <li><b>الثلث الثالث (Third Trimester - من الأسبوع 28 إلى 40):</b>
                <ul>
                    <li>متابعة أسبوعية لضغط الدم والزلال، قياس مؤشر السائل الأمنيوسي (AFI)، ومراقبة علامات المخاض.</li>
                </ul>
            </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
  else:
    st.header("📅 Pregnancy Calculations & Timeline")
    col1, col2 = st.columns(2)
    with col1:
      lmp_date = st.date_input(
          "Last Menstrual Period (LMP):",
          value=datetime.date.today() - datetime.timedelta(days=70),
      )
    today = datetime.date.today()
    delta = today - lmp_date
    weeks = delta.days // 7
    days = delta.days % 7
    try:
      edd = lmp_date + datetime.timedelta(days=280)
    except:
      edd = "N/A"

    with col2:
      st.markdown(
          f"""
            <div style="background-color: #EBF3FB; padding: 15px; border-radius: 8px;">
                <h4 style="margin: 0; color: #1E3A8A;">📌 Calculation Results:</h4>
                <p style="margin: 5px 0 0 0; font-size: 16px;">Gestational Age: <b>{weeks} weeks & {days} days</b></p>
                <p style="margin: 5px 0 0 0; font-size: 16px;">Estimated Due Date (EDD): <b>{edd}</b></p>
            </div>
            """,
          unsafe_allow_html=True,
      )

    st.markdown("---")
    st.subheader("📋 Pregnancy Timeline & Milestone Schedule:")
    st.markdown("""
        <div class="card">
        <ul>
            <li><b>First Trimester (Weeks 0–13):</b> Focus on pregnancy support, Folic Acid, and early viability scan.</li>
            <br>
            <li><b>Second Trimester (Weeks 14–27):</b> Detailed Anomaly Scan (Weeks 18–22), iron/calcium initiation.</li>
            <br>
            <li><b>Third Trimester (Weeks 28–40):</b> Weekly BP/protein checks, AFI assessment, and labor signs monitoring.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# 4. دليل الأدوية والمثبتات الشامل
# ==========================================
elif (menu == "4. دليل الأدوية والمثبتات الشامل") or (
    menu == "4. Comprehensive Medication & Progesterone Guide"
):
  if lang == "العربية":
    st.header("💊 دليل الأدوية التخصصية ومثبتات الحمل الشامل")
    drug_sec = st.selectbox(
        "اختر تصنيف الأدوية:",
        [
            "مبتثات ومنشطات الحمل (Progesterone & Support)",
            "المضادات الحيوية ومضادات الالتهابات الآمنة",
            "أدوية الغثيان واضطرابات الجهاز الهضمي",
            "الفيتامينات والمكملات الغذائية الأساسية",
            "أدوية الولادة وتنظيم المخاض (Uterotonics & Tocolytics)",
        ],
    )

    if drug_sec == "مبتثات ومنشطات الحمل (Progesterone & Support)":
      st.markdown("""
            <div class="card">
            <h3>🛡️ مثبتات الحمل (Progesterone Preparations):</h3>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="background-color: #f1f5f9; border-bottom: 1px solid #cbd5e1;">
                    <th style="padding: 10px; text-align: right;">اسم الدواء (Drug Name)</th>
                    <th style="padding: 10px; text-align: right;">الجرعة وطريقة الاستخدام (Dose & Route)</th>
                    <th style="padding: 10px; text-align: right;">الاستخدام السريري (Clinical Indication)</th>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><b>Dydrogesterone (Duphaston)</b></td>
                    <td style="padding: 10px;">10 ملغ (1-3 مرات يومياً حسب الحالة) عن طريق الفم.</td>
                    <td style="padding: 10px;">الوقاية وعلاج الإجهاض المنذر وتثبيت الحمل.</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><b>Progesterone Vaginal Suppositories/Capsules</b> (Cyclogest / Utrogestan)</td>
                    <td style="padding: 10px;">100 إلى 400 ملغ مرتين يومياً (مهبلي أو شرجي).</td>
                    <td style="padding: 10px;">تثبيت الحمل، حالات أطفال الأنابيب، وقاية النساء اللاتي لديهن تاريخ ولادة مبكرة.</td>
                </tr>
                <tr>
                    <td style="padding: 10px;"><b>Hydroxyprogesterone Caproate (Proluton Depot)</b></td>
                    <td style="padding: 10px;">250 - 500 ملغ حقن عضلي (IM) أسبوعياً.</td>
                    <td style="padding: 10px;">الوقاية من الإجهاض المتكرر والولادة المبكرة.</td>
                </tr>
            </table>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "المضادات الحيوية ومضادات الالتهابات الآمنة":
      st.markdown("""
            <div class="card">
            <h3>💊 المضادات الحيوية الآمنة أثناء الحمل (Category B غالباً):</h3>
            <ul>
                <li><b>البنسلينات (Penicillins):</b> مثل Amoxicillin, Ampicillin, Augmentin (آمنة تماماً ولا تشكل خطراً على الجنين).</li>
                <li><b>السيفالوسبورينات (Cephalosporins):</b> مثل Cefixime, Cefuroxime, Ceftriaxone (ممتازة لعلاج التهابات البول والصدر).</li>
                <li><b>الماكروليدات (Macrolides):</b> مثل Azithromycin, Erythromycin (بديل ممتاز لمن لديهم حساسية بنسلين).</li>
                <li><b>مضادات الفطريات المهبلية:</b> Clotrimazole (تحاميل أو كريم موضعي آمن في الثلث الثاني والثالث).</li>
                <li><span style="color: red;"><b>⚠️ تحذير صارم:</b></span> تجنب تماماً استخدام التتراسيكلين (Tetracyclines)، الفلوروكوينولون (Fluoroquinolones)، والأبراميسين لتأثيرها الضار على عظام وأسنان الجنين.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "أدوية الغثيان واضطرابات الجهاز الهضمي":
      st.markdown("""
            <div class="card">
            <h3>🤢 أدوية الغثيان والقيء الآمنة:</h3>
            <ul>
                <li><b>Pyridoxine (فيتامين B6):</b> الجرعة الأولى الأساسية (10-25 ملغ 3 مرات يومياً).</li>
                <li><b>Doxylamine + Pyridoxine (مثل Diclectin):</b> تركيبة معتمدة وآمنة جداً (Category A) للغثيان الصباحي المستمر.</li>
                <li><b>Metoclopramide / Ondansetron:</b> تُستخدم بحذر تحت الإشراف الطبي للحالات الشديدة (Hyperemesis Gravidarum).</li>
                <li><b>مضادات الحموضة (Antacids):</b> مثل Maalox أو Gaviscon (آمنة لارتجاع المريء وحرقة المعدة).</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "الفيتامينات والمكملات الغذائية الأساسية":
      st.markdown("""
            <div class="card">
            <h3>🥗 الفيتامينات والمكملات الأساسية:</h3>
            <ul>
                <li><b>حمض الفوليك (Folic Acid):</b> 400 ميكروغرام يومياً (قبل الحمل وحتى أسبوع 12 لمنع تشوهات الأنبوب العصبي).</li>
                <li><b>مكملات الحديد (Iron Supplements):</b> تبدأ غالباً من الأسبوع 14 لمنع فقر الدم (Anemia) مثل Ferrous Sulfate أو Ferrous Bisglycinate.</li>
                <li><b>الكالسيوم وفيتامين د (Calcium & Vit D):</b> لدعم العظام والوقاية من تسمم الحمل المرتبط بنقص الكالسيوم.</li>
                <li><b>أوميغا 3 (Omega-3 / DHA):</b> لتطوير الدماغ والجهاز العصبي للجنين.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "أدوية الولادة وتنظيم المخاض (Uterotonics & Tocolytics)":
      st.markdown("""
            <div class="card">
            <h3>⚡ أدوية الرحم والمخاض:</h3>
            <ul>
                <li><b>1. مقبضات ومنظمات الرحم (Uterotonics):</b>
                    <ul>
                        <li><b>Oxytocin (Syntocinon):</b> لتحفيز الطلق أو الوقاية/علاج النزيف التالي للولادة.</li>
                        <li><b>Misoprostol (Cytotec):</b> لنضج عنق الرحم أو علاج PPH (يُستخدم بحذر شديد).</li>
                        <li><b>Methylergometrine:</b> مقبض قوي للرحم (يُمنع منعاً باتاً في وجود ارتفاع ضغط الدم).</li>
                    </ul>
                </li>
                <li><b>2. مثبطات المخاض المبكر (Tocolytics):</b>
                    <ul>
                        <li><b>Nifedipine:</b> مرخي عضلات الرحم المفضل لإيقاف الولادة المبكرة.</li>
                        <li><b>Atosiban / Magnesium Sulfate:</b> لحماية الجهاز العصبي للجنين وتأخير المخاض المبكر.</li>
                    </ul>
                </li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
  else:
    # النسخة الإنجليزية للأدوية
    st.header("💊 Comprehensive Medication & Progesterone Guide")
    drug_sec = st.selectbox(
        "Select Medication Category:",
        [
            "Progesterone & Pregnancy Support",
            "Safe Antibiotics & Anti-inflammatories",
            "Nausea & GI Medications",
            "Essential Vitamins & Supplements",
            "Labor & Uterine Medications (Uterotonics & Tocolytics)",
        ],
    )
    if drug_sec == "Progesterone & Pregnancy Support":
      st.markdown("""
            <div class="card">
            <h3>🛡️ Progesterone Support:</h3>
            <table style="width:100%; border-collapse: collapse;">
                <tr style="background-color: #f1f5f9; border-bottom: 1px solid #cbd5e1;">
                    <th style="padding: 10px; text-align: left;">Drug Name</th>
                    <th style="padding: 10px; text-align: left;">Dose & Route</th>
                    <th style="padding: 10px; text-align: left;">Clinical Indication</th>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><b>Dydrogesterone (Duphaston)</b></td>
                    <td style="padding: 10px;">10 mg (1-3 times daily) oral.</td>
                    <td style="padding: 10px;">Threatened abortion and pregnancy support.</td>
                </tr>
                <tr style="border-bottom: 1px solid #e2e8f0;">
                    <td style="padding: 10px;"><b>Progesterone Vaginal Suppositories</b> (Cyclogest / Utrogestan)</td>
                    <td style="padding: 10px;">100–400 mg twice daily (vaginal/rectal).</td>
                    <td style="padding: 10px;">Luteal phase support, IVF, preterm labor prevention.</td>
                </tr>
                <tr>
                    <td style="padding: 10px;"><b>Hydroxyprogesterone Caproate (Proluton)</b></td>
                    <td style="padding: 10px;">250–500 mg IM weekly.</td>
                    <td style="padding: 10px;">Prevention of recurrent miscarriage and preterm delivery.</td>
                </tr>
            </table>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "Safe Antibiotics & Anti-inflammatories":
      st.markdown("""
            <div class="card">
            <h3>💊 Safe Pregnancy Antibiotics (Category B):</h3>
            <ul>
                <li><b>Penicillins:</b> Amoxicillin, Ampicillin, Augmentin (Safest profile).</li>
                <li><b>Cephalosporins:</b> Cefixime, Cefuroxime, Ceftriaxone.</li>
                <li><b>Macrolides:</b> Azithromycin, Erythromycin.</li>
                <li><b>Vaginal Antifungals:</b> Clotrimazole (Safe in 2nd/3rd trimesters).</li>
                <li><span style="color: red;"><b>⚠️ Warning:</b></span> Avoid Tetracyclines and Fluoroquinolones.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "Nausea & GI Medications":
      st.markdown("""
            <div class="card">
            <h3>🤢 Safe Nausea Treatments:</h3>
            <ul>
                <li><b>Pyridoxine (Vit B6):</b> First-line standard dose.</li>
                <li><b>Doxylamine + Pyridoxine:</b> Approved combination (Category A).</li>
                <li><b>Metoclopramide / Ondansetron:</b> For severe cases (Hyperemesis).</li>
                <li><b>Antacids:</b> Maalox or Gaviscon for heartburn.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "Essential Vitamins & Supplements":
      st.markdown("""
            <div class="card">
            <h3>🥗 Essential Supplements:</h3>
            <ul>
                <li><b>Folic Acid:</b> 400 mcg daily in the first trimester.</li>
                <li><b>Iron Supplements:</b> Started at week 14 to prevent anemia.</li>
                <li><b>Calcium & Vitamin D:</b> Bone health and preeclampsia reduction.</li>
                <li><b>Omega-3 / DHA:</b> Fetal brain and eye development.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    elif drug_sec == "Labor & Uterine Medications (Uterotonics & Tocolytics)":
      st.markdown("""
            <div class="card">
            <h3>⚡ Uterine & Labor Medications:</h3>
            <ul>
                <li><b>1. Uterotonics:</b> Oxytocin, Misoprostol, Methylergometrine (contraindicated in hypertension).</li>
                <li><b>2. Tocolytics:</b> Nifedipine, Atosiban, Magnesium Sulfate.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)


# ==========================================
# 5. الفحوصات المخبرية والأشعة التلفزيونية
# ==========================================
elif (menu == "4. الفحوصات المخبرية والأشعة التلفزيونية") or (
    menu == "5. Labs & Ultrasound Guide"
):
  if lang == "العربية":
    st.header("🔬 الفحوصات المخبرية والأشعة التلفزيونية")
    tab1, tab2 = st.tabs(["🧪 التحاليل المخبرية الأساسية", "📡 جدول الأشعة التلفزيونية"])
    with tab1:
      st.markdown("""
            <div class="card">
            <h3>🧪 التحاليل المخبرية الضرورية للحامل:</h3>
            <ol>
                <li><b>صورة الدم الكاملة (CBC):</b> استبعاد فقر الدم وتقييم الهيموجلوبين.</li>
                <li><b>فصيلة الدم وعامل ريسس (Blood Group & Rh):</b> لتحديد الحاجة لحقنة Anti-D في حال كانت الأم سالب والطفل موجب.</li>
                <li><b>تحليل السكر (Fasting / Random / GTT):</b> لاستبعاد سكر الحمل (Gestational Diabetes).</li>
                <li><b>تحليل وبول وزراعة (Urinalysis & Urine Culture):</b> لاستبعاد التهابات المسالك البولية الصامتة.</li>
                <li><b>وظائف الكلى والكبد (RFT & LFT):</b> ضرورية في حالات الاشتباه بارتفاع الضغط وتسمم الحمل.</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
    with tab2:
      st.markdown("""
            <div class="card">
            <h3>📡 جدول فحوصات السونار (Ultrasound Schedule):</h3>
            <ul>
                <li><b>السونار المبكر (Early Scan - الأسابيع 6 إلى 10):</b> تأكيد وجود نبض الجنين، تحديد العمر الحملي، واستبعاد الحمل خارج الرحم.</li>
                <li><b>فحص الشفافية القفوية (NT Scan - الأسابيع 11 إلى 13+6):</b> تقييم المخاطر الجينية والكروموسومية.</li>
                <li><b>مسح التشوهات التفصيلي (Anomaly Scan - الأسابيع 18 إلى 22):</b> فحص أعضاء الجنين، القلب، الأطراف، والمشيمة بدقة متناهية.</li>
                <li><b>متابعة النمو والسائل الأمنيوسي (Growth & AFI Scan - الثلث الثالث):</b> تقييم حجم الجنين، تدفق الدم بالأشعة، وكمية السائل الأمنيوسي.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
  else:
    st.header("🔬 Laboratory Investigations & Ultrasound Guide")
    tab1, tab2 = st.tabs(["🧪 Essential Labs", "📡 Ultrasound Schedule"])
    with tab1:
      st.markdown("""
            <div class="card">
            <h3>🧪 Key Pregnancy Labs:</h3>
            <ol>
                <li><b>CBC:</b> Rule out anemia.</li>
                <li><b>Blood Group & Rh:</b> Check for Anti-D requirement.</li>
                <li><b>Gestational Diabetes Screen:</b> Fasting blood sugar or GTT.</li>
                <li><b>Urinalysis & Culture:</b> Screen for asymptomatic bacteriuria.</li>
                <li><b>RFT & LFT:</b> Essential for preeclampsia workup.</li>
            </ol>
            </div>
            """, unsafe_allow_html=True)
    with tab2:
      st.markdown("""
            <div class="card">
            <h3>📡 Ultrasound Scan Schedule:</h3>
            <ul>
                <li><b>Early Scan (Weeks 6–10):</b> Confirm heartbeat, precise dating.</li>
                <li><b>NT Scan (Weeks 11–13+6):</b> Genetic and chromosomal risk assessment.</li>
                <li><b>Anomaly Scan (Weeks 18–22):</b> Detailed fetal structural survey.</li>
                <li><b>Growth & AFI Scan (Third Trimester):</b> Fetal biometry and amniotic fluid index.</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
if lang == "العربية":
  st.markdown(
      "💡 *تم تصميم وتطوير هذا التطبيق خصيصاً لدعم العمليات السريرية واليومية"
      " للدكتورة: **Dr. aziza mohmmed***"
  )
else:
  st.markdown(
      "💡 *This application was specially designed to support clinical workflows"
      " for **Dr. aziza mohmmed***"
  )
