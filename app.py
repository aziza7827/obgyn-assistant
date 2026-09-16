import streamlit as st

# إعدادات صفحة التطبيق
st.set_page_config(
    page_title="OB/GYN Smart Assistant / المساعد الذكي",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# اختيار اللغة من الشريط الجانبي
language = st.sidebar.selectbox(
    "🌐 Choose Language / اختر اللغة", 
    ["العربية", "English"]
)

# القواميس النصية الشاملة حسب اللغة المختارة
if language == "العربية":
    t = {
        "title": "🩺 المساعد الذكي للتشخيص التفريقي (نساء وولادة)",
        "subtitle": "نظام دعم القرار السريري الشامل للحالات الطارئة والتشخيص التفريقي",
        "sidebar_header": "إعدادات وتقييم الحالة الإكلينيكية",
        "category_label": "اختر ففة العرض الإكلينيكي:",
        "categories": [
            "نزيف أول الحمل (First Trimester Bleeding)",
            "آلام البطن والحوض الحادة (Acute Abdominal/Pelvic Pain)",
            "اضطرابات ضغط الدم الحملي (Hypertensive Disorders in Pregnancy)",
            "نزيف ما بعد الولادة (Postpartum Hemorrhage - PPH)",
            "الحمى والعدوى النفاسية أو الحوضية (Puerperal / Pelvic Infections)",
            "اضطرابات حركة الجنين أو تخطيطه (Fetal Movement / CTG Concerns)"
        ],
        "analyze_btn": "🔍 بدء التحليل الإكلينيكي الشامل",
        "results_header": "📋 نتائج التشخيص التفريقي والإدارة الطبية",
        "differential": "التشخيص التفريقي المحتمل:",
        "investigations": "الفحوصات المطلوبة (Investigations):",
        "management": "خطة الإدارة الطبية الطارئة والتدخل (Management):",
        "warning": "⚠️ تنبيه طبي: هذا النظام هو أداة مساعدة لدعم القرار الإكلينيكي ولا يغني عن التقييم السريري المباشر والخبرة الطبية.",
        "select_prompt": "الرجاء تحديد الفئة والأعراض الإكلينيكية من القائمة الجانبية ثم الضغط على زر التحليل للبدء."
    }
else:
    t = {
        "title": "🩺 OB/GYN Smart Differential Diagnosis Assistant",
        "subtitle": "Comprehensive Clinical Decision Support System for Emergency & Differential Diagnosis",
        "sidebar_header": "Clinical Case Settings & Evaluation",
        "category_label": "Select Clinical Presentation Category:",
        "categories": [
            "First Trimester Bleeding",
            "Acute Abdominal/Pelvic Pain",
            "Hypertensive Disorders in Pregnancy",
            "Postpartum Hemorrhage - PPH",
            "Puerperal / Pelvic Infections",
            "Fetal Movement / CTG Concerns"
        ],
        "analyze_btn": "🔍 Start Comprehensive Clinical Analysis",
        "results_header": "📋 Differential Diagnosis & Clinical Management Results",
        "differential": "Potential Differential Diagnosis:",
        "investigations": "Required Investigations:",
        "management": "Emergency Management & Intervention Plan:",
        "warning": "⚠️ Medical Disclaimer: This system is a clinical decision support tool and does not replace direct clinical evaluation and medical expertise.",
        "select_prompt": "Please select the category and clinical symptoms from the sidebar, then click the analysis button to begin."
    }

# عنوان التطبيق
st.title(t["title"])
st.markdown(f"*{t['subtitle']}*")
st.divider()

# الشريط الجانبي للإدخال
st.sidebar.header(t["sidebar_header"])
selected_category = st.sidebar.selectbox(t["category_label"], t["categories"])

# تفاصيل إضافية حسب الفئة المختارة بكامل الأقسام
symptom_details = ""
if "First Trimester" in selected_category or "نزيف أول الحمل" in selected_category:
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("الأعراض والعلامات المصاحبة:", [
            "ألم شديد في البطن/الحوض (Severe Pain)", 
            "نزيف مستمر مع قطع نسجية (Tissue Passage)", 
            "دوخة أو إغماء / صدمة (Dizziness / Shock)", 
            "غياب نبض الجنين بالسونار (Absent Fetal Heartbeat)",
            "نزيف خفيف متقطع مع مغص خفيف (Spotting/Mild Cramps)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Associated Symptoms & Signs:", [
            "Severe abdominal/pelvic pain", 
            "Ongoing bleeding with tissue passage", 
            "Dizziness or fainting / Shock", 
            "Absent fetal heartbeat on ultrasound",
            "Light intermittent bleeding with mild cramps"
        ])

elif "Abdominal" in selected_category or "آلام البطن" in selected_category:
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("الأعراض والعلامات المصاحبة:", [
            "تأخر الدورة + اختبار حمل إيجابي (Missed Period + +ve Test)", 
            "حمى واهتزاز / غثيان (Fever / Chills / Nausea)", 
            "ألم في الكتف / تهيج بريتوني (Shoulder Tip Pain / Peritonism)", 
            "كتلة ملحقة بالحوض محسوسة أو مؤلمة (Adnexal Mass / Tenderness)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Associated Symptoms & Signs:", [
            "Missed period + positive pregnancy test", 
            "Fever and chills / Nausea", 
            "Shoulder tip pain / Peritoneal irritation", 
            "Palpable or tender adnexal mass"
        ])

elif "Hypertensive" in selected_category or "اضطرابات ضغط الدم" in selected_category:
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("العلامات والأعراض المصاحبة:", [
            "ضغط الدم >= 140/90 (بشكل متكرر)", 
            "صداع شديد أو زغللة في العيون (Severe Headache / Visual Disturbances)", 
            "ألم في المراس العلوي الأيمن / شرسوفي (RUQ / Epigastric Pain)", 
            "انتفاخ مفاجئ وذمة في الوجه والأطراف (Sudden Generalized Edema)",
            "نقص الصفائح أو ارتفاع انزيمات الكبد (HELLP features)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Associated Signs & Symptoms:", [
            "Blood Pressure >= 140/90 (persistent)", 
            "Severe headache or visual disturbances", 
            "Right upper quadrant (RUQ) / Epigastric pain", 
            "Sudden facial/peripheral edema",
            "Thrombocytopenia or elevated liver enzymes (HELLP features)"
        ])

elif "PPH" in selected_category or "نزيف ما بعد الولادة" in selected_category:
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("تفاصيل حالة النزيف:", [
            "رحم طري وغير متقبض تماماً (Boggy / Atonic Uterus)", 
            "نزيف بغزارة شديدة بعد الولادة مباشرة (Massive Immediate Bleeding)", 
            "وجود تمزقات في المهبل أو عنق الرحم (Genital Tract Lacerations)", 
            "شكوك حول وجود بقايا مشيمية داخل الرحم (Retained Placental Tissue)",
            "صدمة وعائية / انخفاض حاد بالضغط (Hypovolemic Shock)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Bleeding Details & Clinical Signs:", [
            "Boggy / completely atonic uterus", 
            "Massive heavy bleeding immediately post-delivery", 
            "Genital tract lacerations (cervical/vaginal)", 
            "Suspected retained placental tissues",
            "Hypovolemic shock / sharp BP drop"
        ])

elif "Infections" in selected_category or "الحمى والعدوى" in selected_category:
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("أعراض العدوى:", [
            "ارتفاع حرارة الجسم > 38 درجة (Fever > 38°C)", 
            "إفرازات مهبلية ذات رائحة كريهة (Foul-smelling Lochia / Discharge)", 
            "ألم رحمي مضغوط أو حساسية في البطن (Uterine Tenderness)", 
            "أعراض بولية / حرقان (Dysuria / Urinary Symptoms)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Infection Symptoms:", [
            "Elevated body temperature > 38°C", 
            "Foul-smelling lochia or vaginal discharge", 
            "Uterine tenderness or lower abdominal pain", 
            "Dysuria / urinary tract symptoms"
        ])

else:  # Fetal Movement / CTG Concerns
    if language == "العربية":
        symptom_details = st.sidebar.multiselect("ملاحظات الجنين:", [
            "نقص أو انعدام حركة الجنين الملحوظة (Decreased / Absent Fetal Movements)", 
            "تخطيط قلب الجنين غير مطمئن / تباطؤات (Non-reassuring CTG / Decelerations)", 
            "قلة السائل الامينوسي المكتشفة بالسونار (Oligohydramnios)",
            "تأخر نمو الجنين داخل الرحم (IUGR suspicion)"
        ])
    else:
        symptom_details = st.sidebar.multiselect("Fetal Status Observations:", [
            "Decreased or absent fetal movements", 
            "Non-reassuring CTG / decelerations", 
            "Oligohydramnios on ultrasound",
            "Suspected Intrauterine Growth Restriction (IUGR)"
        ])

analyze_clicked = st.sidebar.button(t["analyze_btn"], type="primary")

# عرض النتائج عند الضغط على زر التحليل
if analyze_clicked:
    st.subheader(t["results_header"])
    
    # محتوى النتائج الشامل بناءً على الفئة المختارة واللغة
    if "First Trimester" in selected_category or "نزيف أول الحمل" in selected_category:
        if language == "العربية":
            diff = "- حمل خارج الرحم (Ectopic Pregnancy - يجب استبعاده أولاً)\n- إجهاض منذر، حتمي، غير كامل، أو منساق (Abortions spectrum)\n- الحمل العنقودي / الغشائي (Gestational Trophoblastic Disease)\n- نزيف انغراس البويضة أو أسباب عنق الرحم الحميدة"
            inv = "- فحص هرمون الحمل الكمي الرقمي (Quantitative Beta-hCG)\n- تصوير بالموجات فوق الصوتية عبر المهبل (Transvaginal Ultrasound - TVS)\n- صورة دم كاملة (CBC)، فصيلة الدم وعامل ريسوس (Blood Group & Rh)\n- تحديد جاهزية الدم للنقل عند الحاجة"
            mgmt = "- إنعاش السوائل الوريدية وتقييم الاستقرار الديموديناميكي (Hemodynamic stability)\n- التدخل الجراحي الفوري (تنظير بطن أو استكشاف) في حالات اشتباه انفجار الحمل خارج الرحم\n- إعطاء حقنة المضاد ريسوس (Anti-D Immunoglobulin) خلال 72 ساعة للأمهات Rh سلبيات\n- الاستشارة والمتابعة النفسية والسريرية"
        else:
            diff = "- Ectopic Pregnancy (Must be ruled out urgently)\n- Abortion spectrum (Threatened, Inevitable, Incomplete, Missed)\n- Gestational Trophoblastic Disease (Molar Pregnancy)\n- Implantation bleeding or benign cervical lesions"
            inv = "- Quantitative Beta-hCG\n- Transvaginal Ultrasound (TVS)\n- Complete Blood Count (CBC) & Blood Group and Rh\n- Type and screen/crossmatch if needed"
            mgmt = "- IV fluid resuscitation and hemodynamic stability assessment\n- Urgent surgical intervention (laparoscopy/laparotomy) if ruptured ectopic is suspected\n- Administer Anti-D Immunoglobulin within 72 hours for Rh-negative mothers\n- Clinical counseling and follow-up"
            
    elif "Abdominal" in selected_category or "آلام البطن" in selected_category:
        if language == "العربية":
            diff = "- التهاب الزائدة الدودية الحاد (Acute Appendicitis - يتغير مكانها بالحمل)\n- التواء المبيض أو الأنبوب (Ovarian/Adnexal Torsion)\n- تمزق أو نزيف كيس المبيض (Ruptured Ovarian Cyst)\n- التهاب الحوض الحاد أو تفاقم حصوات المرارة/الكلى"
            inv = "- سونار دوبلر حوضي وبطني (Pelvic & Abdominal Doppler US)\n- صورة دم كاملة (CBC)، تحليل بول (Urinalysis)، ووظائف الكلى\n- استشارة جراحية مبكرة عند الشك في جراحة بطنية حادة"
            mgmt = "- السيطرة على الألم، الإماهة الوريدية الموجهة، والمراقبة السريرية الحثيثة\n- التدخل الجراحي/النسائي العاجل بناءً على نتائج الدوبلر، العلامات البريتونية، والتقييم الإكلينيكي"
        else:
            diff = "- Acute Appendicitis (position alters during pregnancy)\n- Ovarian or Adnexal Torsion\n- Ruptured or Hemorrhagic Ovarian Cyst\n- Pelvic Inflammatory Disease (PID) or acute biliary/renal colic"
            inv = "- Pelvic & Abdominal Doppler Ultrasound\n- Complete Blood Count (CBC), Urinalysis, Renal Profile\n- Early surgical consultation if acute abdomen is suspected"
            mgmt = "- Pain control, targeted IV hydration, and close clinical observation\n- Urgent surgical/GYN intervention based on Doppler flow findings, peritoneal signs, and diagnostic scores"
            
    elif "Hypertensive" in selected_category or "اضطرابات ضغط الدم" in selected_category:
        if language == "العربية":
            diff = "- تسمم الحمل (Pre-eclampsia) بعلامات خطورة أو بدونها\n- ارتفاع ضغط الدم المزمن أو الحملي العابر\n- متلازمة هيلپ (HELLP Syndrome)\n- تشنج الحمل (Eclampsia)"
            inv = "- فحص زلال البول (Spot Urine Protein-to-Creatinine Ratio أو جمع بول 24 ساعة)\n- وظائف الكبد والكلى (AST, ALT, Serum Creatinine, Bilirubin)\n- تعداد الصفائح الدموية واختبارات التخثر\n- تقييم صحة الجنين (NST وسونار قياس السوائل ونمو الجنين)"
            mgmt = "- بدء خافضات ضغط الدم السريعة (مثل Labetalol أو Nifedipine oral) إذا كان الضغط >= 160/110 مم زئبق\n- إعطاء كبريتات المغنيسيوم (MgSO4) للوقاية أو علاج التشنجات في حالات تسمم الحمل الشديد\n- تحديد توقيت وطريقة الولادة المثلى بناءً على عمر الحمل واستقرار الحالة الأمومية والجنينية"
        else:
            diff = "- Pre-eclampsia (with or without severe features)\n- Chronic or Gestational Hypertension\n- HELLP Syndrome\n- Eclampsia"
            inv = "- Urine protein evaluation (Spot Protein/Creatinine Ratio or 24-hr collection)\n- Liver and renal function tests (AST, ALT, Creatinine, Bilirubin)\n- Platelet count and coagulation profile\n- Fetal well-being assessment (NST, biophysical profile)"
            mgmt = "- Administer acute antihypertensives (e.g., Labetalol or Nifedipine) if BP >= 160/110 mmHg\n- Administer Magnesium Sulfate (MgSO4) for seizure prophylaxis/treatment in severe pre-eclampsia\n- Determine optimal timing and mode of delivery based on gestational age and maternal/fetal stability"
            
    elif "PPH" in selected_category or "نزيف ما بعد الولادة" in selected_category:
        if language == "العربية":
            diff = "- ارتخاء الرحم (Uterine Atony - يمثل نحو 70-80% من الحالات)\n- بقايا الأنسجة المشيمية أو المشيمة الملتصقة (Retained/Accreta Placenta)\n- تمزقات قناة الولادة والأنسجة الرخوة (Genital Tract Lacerations)\n- انخفاض عوامل التخثر أو الخثارة الدموية (Coagulopathy)"
            inv = "- قياس العلامات الحيوية بشكل متسارع وتقدير حجم الدم المفقود بدقة\n- فحص سريري دقيق (تقييم قوام الرحم، فحص عنق الرحم والمهبل والمشيمة الخارجة)\n- فحوصات مخبرية فورية (CBC, Coagulation Profile: PT/INR, Fibrinogen)"
            mgmt = "- تطبيق تدليك الرحم ثنائي الجانب الفوري (Bimanual uterine massage)\n- إعطاء الأدوية القابضة للرحم المتسلسلة (Oxytocin infusion, Ergometrine, Carboprost, Misoprostol)\n- إدخال قسطرة بولية لضمان تفراغ المثانة وتحسين انقباض الرحم\n- تفعيل بروتوكول نقل الدم الضخم واستدعاء فريق الطوارئ المتعدد التخصصات"
        else:
            diff = "- Uterine Atony (accounts for 70-80% of cases)\n- Retained placental tissue or morbidly adherent placenta\n- Genital tract lacerations and soft tissue trauma\n- Coagulation disorders and DIC"
            inv = "- Rapid vital signs monitoring and objective blood loss estimation\n- Careful clinical examination (uterine tone, inspection of cervix, vagina, and placenta)\n- Immediate lab tests (CBC, Coagulation profile: PT/INR, Fibrinogen)"
            mgmt = "- Perform immediate bimanual uterine massage\n- Administer sequential uterotonic agents (Oxytocin infusion, Ergometrine, Carboprost, Misoprostol)\n- Insert Foley catheter for bladder drainage and monitoring\n- Activate Massive Transfusion Protocol (MTP) and call multidisciplinary emergency team"

    elif "Infections" in selected_category or "الحمى والعدوى" in selected_category:
        if language == "العربية":
            diff = "- التهاب بطانة الرحم النفاسي (Puerperal Endometritis)\n- التهاب الجرح القيصري أو العجاني (Wound/Episiotomy Infection)\n- التهاب الكلى والمسالك البولية الحاد (Pyelonephritis / UTI)\n- التهاب الثدي النفاسي (Mastitis / Breast Abscess)"
            inv = "- صورة دم كاملة (CBC) مع قياس علامات الالتهاب (CRP / Procalcitonin)\n- مزرعة بول وبكتيريا الدم عند الارتفاع الشديد للحرارة (Blood & Urine Cultures)\n- مسحة من الجرح أو إفرازات الرحم عند الإمكان"
            mgmt = "- البدء بمضادات حيوية وريدية واسعة النطاق (Broad-spectrum IV antibiotics)\n- خافضات الحرارة والتحكم بالسوائل والترطيب\n- تصريف الجراجات أو خراجات الثدي/الجرح عند تشكيلها جراحياً"
        else:
            diff = "- Puerperal Endometritis\n- Cesarean or Episiotomy Wound Infection\n- Acute Pyelonephritis / Severe UTI\n- Puerperal Mastitis or Breast Abscess"
            inv = "- Complete Blood Count (CBC) and inflammatory markers (CRP / Procalcitonin)\n- Urine culture and blood cultures if high spikes of fever occur\n- Wound or lochia swabs when clinically indicated"
            mgmt = "- Initiate broad-spectrum IV antibiotic therapy\n- Antipyretics and supportive IV hydration\n- Surgical drainage of wound abscesses or breast collections if localized"

    else:  # Fetal Movement / CTG Concerns
        if language == "العربية":
            diff = "- ضيق أو معاناة الجنين داخل الرحم (Fetal Distress / Hypoxia)\n- فشل أو قصور المشيمة الوظيفي (Placental Insufficiency)\n- قلة السائل الامينوسي الحادة (Oligohydramnios)\n- التفاف الحبل السري أو الضغط عليه (Cord Compression)"
            inv = "- تخطيط نبض قلب الجنين المستمر (CTG / Electronic Fetal Monitoring)\n- تصوير تلفزيوني تفصيلي وتقييم مؤشر السائل الامينوسي (AFI / Ultrasound BPP)\n- دوبلر الشريان السري والمخي الأوسط (Umbilical & Middle Cerebral Artery Doppler)"
            mgmt = "- وضع الحامل على جانبها الأيسر وإعطاء الأكسجين عند الحاجة (Left lateral position & oxygen)\n- توقف أي منشطات للرحم قد تسبب انقباضات مفرطة (Discontinue uterotonics if any)\n- التقييم العاجل لإمكانية إنهاء الحمل وولادة طارئة (سريعة) إذا استمر النمط غير المطمئن في التخطيط"
        else:
            diff = "- Fetal Distress / Hypoxia\n- Placental Insufficiency\n- Severe Oligohydramnios\n- Cord compression or nuchal cord entanglement"
            inv = "- Continuous Electronic Fetal Monitoring (CTG)\n- Detailed obstetric ultrasound and Amniotic Fluid Index (AFI / BPP)\n- Umbilical and Middle Cerebral Artery Doppler studies"
            mgmt = "- Place mother in left lateral position and provide supplemental oxygen\n- Discontinue any uterine stimulants causing hyperstimulation\n- Urgent evaluation for emergency delivery if non-reassuring CTG persists"

    # عرض النتائج الكاملة في مربعات واضحة ومنظمة
    st.success(f"**{t['differential']}**\n\n{diff}")
    st.info(f"**{t['investigations']}**\n\n{inv}")
    st.warning(f"**{t['management']}**\n\n{mgmt}")

else:
    st.info(t["select_prompt"])

st.divider()
st.caption(t["warning"])
