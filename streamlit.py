import streamlit as st

st.set_page_config(
    page_title="CENTRAL ENGLISH SCHOOL — Admission Portal",
    page_icon="🏫",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800&family=Merriweather:wght@700;900&display=swap');

* { font-family: 'Nunito', sans-serif; }
#MainMenu, footer, header { visibility: hidden; }

.stApp {
    background: #f0f4ff;
}

/* ── Top Banner ── */
.banner {
    background: linear-gradient(120deg, #1a237e 0%, #283593 50%, #1565c0 100%);
    border-radius: 20px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    box-shadow: 0 10px 40px rgba(26,35,126,0.25);
}
.banner-logo {
    width: 90px; height: 90px;
    background: white;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 2.8rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    flex-shrink: 0;
}
.banner-text h1 {
    font-family: 'Merriweather', serif;
    color: white;
    font-size: 2rem;
    margin: 0 0 0.2rem 0;
    text-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
.banner-text p {
    color: #90caf9;
    margin: 0;
    font-size: 1rem;
    font-weight: 400;
}
.banner-badge {
    margin-left: auto;
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    color: white;
    font-size: 0.85rem;
    text-align: center;
}
.banner-badge b { display: block; font-size: 1.1rem; }

/* ── Cards ── */
.form-card {
    background: white;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0 4px 24px rgba(26,35,126,0.08);
    border: 1px solid #e8eaf6;
    margin-bottom: 1.5rem;
}
.card-title {
    font-family: 'Merriweather', serif;
    font-size: 1.05rem;
    color: #1a237e;
    font-weight: 700;
    margin-bottom: 1.2rem;
    padding-bottom: 0.7rem;
    border-bottom: 2px solid #e8eaf6;
    display: flex; align-items: center; gap: 0.5rem;
}

/* ── Class Selector ── */
.class-btn-row { display: flex; gap: 1rem; margin-bottom: 0.5rem; }
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div {
    display: flex !important;
    gap: 1rem !important;
    flex-direction: row !important;
}
div[data-testid="stRadio"] > div > label {
    display: flex !important;
    flex: 1;
    cursor: pointer;
}
div[data-testid="stRadio"] > div > label > div:first-child { display: none; }
div[data-testid="stRadio"] > div > label > div:last-child {
    width: 100%;
    background: #f0f4ff;
    border: 2px solid #c5cae9;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    font-weight: 700;
    color: #3949ab;
    font-size: 1rem;
    transition: all 0.2s;
}
div[data-testid="stRadio"] > div > label:has(input:checked) > div:last-child {
    background: #1a237e;
    border-color: #1a237e;
    color: white;
    box-shadow: 0 4px 15px rgba(26,35,126,0.3);
}

/* ── Inputs ── */
label { color: #3949ab !important; font-weight: 600 !important; font-size: 0.88rem !important; }
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea textarea {
    border: 1.5px solid #c5cae9 !important;
    border-radius: 10px !important;
    background: #f8f9ff !important;
    color: #1a237e !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1rem !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus {
    border-color: #3949ab !important;
    box-shadow: 0 0 0 3px rgba(57,73,171,0.12) !important;
}

/* ── Submit Button ── */
.stButton > button {
    background: linear-gradient(135deg, #1a237e, #1565c0) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2rem !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
    box-shadow: 0 4px 15px rgba(26,35,126,0.3) !important;
    transition: all 0.2s !important;
    font-family: 'Nunito', sans-serif !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(26,35,126,0.45) !important;
}

/* ── Req Cards ── */
.req-card-10 {
    background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
    border-left: 5px solid #43a047;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
}
.req-card-12 {
    background: linear-gradient(135deg, #fff3e0, #fff8e1);
    border-left: 5px solid #fb8c00;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
}
.req-title { font-weight: 800; font-size: 0.95rem; margin-bottom: 0.3rem; }
.req-10 .req-title { color: #2e7d32; }
.req-12 .req-title { color: #e65100; }
.req-desc { font-size: 0.85rem; color: #555; }

/* ── Age Meter ── */
.age-meter {
    background: linear-gradient(135deg, #e8eaf6, #f3f4ff);
    border: 1px solid #c5cae9;
    border-radius: 14px;
    padding: 1.2rem;
    text-align: center;
    margin-top: 1rem;
}
.age-big { font-size: 3rem; font-weight: 800; color: #1a237e; line-height: 1; }
.age-sub { font-size: 0.8rem; color: #7986cb; margin-top: 0.2rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }
.eligible-tag {
    display: inline-block;
    margin-top: 0.8rem;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.82rem;
    font-weight: 700;
}
.tag-green { background: #e8f5e9; color: #2e7d32; }
.tag-yellow { background: #fff3e0; color: #e65100; }

/* ── Result Box ── */
.result-success {
    background: linear-gradient(135deg, #e8f5e9, #f1f8e9);
    border: 2px solid #43a047;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    margin-top: 1rem;
}
.result-fail {
    background: linear-gradient(135deg, #ffebee, #fce4ec);
    border: 2px solid #e53935;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    margin-top: 1rem;
}
.result-icon { font-size: 2.5rem; }
.result-title { font-size: 1.3rem; font-weight: 800; margin: 0.4rem 0; }
.result-sub { font-size: 0.9rem; }

/* ── Detail Table ── */
.detail-table {
    background: #f8f9ff;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-top: 1rem;
    border: 1px solid #e8eaf6;
}
.detail-row-item {
    display: flex;
    justify-content: space-between;
    padding: 0.55rem 0;
    border-bottom: 1px solid #e8eaf6;
    font-size: 0.9rem;
}
.detail-row-item:last-child { border-bottom: none; }
.d-label { color: #7986cb; font-weight: 600; }
.d-value { color: #1a237e; font-weight: 700; }

/* ── Step Indicator ── */
.steps {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
    align-items: center;
}
.step {
    flex: 1;
    height: 5px;
    border-radius: 10px;
    background: #e8eaf6;
}
.step-active { background: #1a237e; }
.step-label {
    font-size: 0.78rem;
    color: #9fa8da;
    text-align: center;
    margin-top: 0.3rem;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Classes
# ─────────────────────────────────────────────
class Student:
    def __init__(self, name, age, email, phone, gender, address):
        self.name    = name
        self.age     = age
        self.email   = email
        self.phone   = phone
        self.gender  = gender
        self.address = address

class Class10(Student):
    def __init__(self, name, age, email, phone, gender, address):
        super().__init__(name, age, email, phone, gender, address)
        self.admitted = True
        self.message  = "Admission Confirmed!"

class Class12(Student):
    def __init__(self, name, age, email, phone, gender, address):
        super().__init__(name, age, email, phone, gender, address)
        if self.age >= 16:
            self.admitted = True
            self.message  = "Admission Confirmed!"
        else:
            self.admitted = False
            self.message  = "Not Eligible for Class 12"

# ─────────────────────────────────────────────
# Banner
# ─────────────────────────────────────────────
st.markdown("""
<div class="banner">
    <div class="banner-logo">🏫</div>
    <div class="banner-text">
        <h1>CENTRAL ENGLISH SCHOOL</h1>
        <p>C.E.S(Central English School) — Excellence in Education Since 1886</p>
    </div>
    <div class="banner-badge">
        <b>2026–27</b>
        Admissions Open
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Layout
# ─────────────────────────────────────────────
col_form, col_right = st.columns([2.2, 1.2])

with col_form:
    # Class Selector
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">🎓 Select Target Class</div>', unsafe_allow_html=True)
    target_class = st.radio("", ["Class 10th", "Class 12th"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Personal Info
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">👤 Personal Information</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("Full Name", placeholder="e.g. Rahul Sharma")
    with c2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    c3, c4 = st.columns(2)
    with c3:
        age = st.number_input("Date of Birth (Age)", min_value=5, max_value=25, value=15, step=1)
    with c4:
        phone = st.text_input("Contact Number", placeholder="+91 XXXXX XXXXX")

    email = st.text_input("Email Address", placeholder="student@example.com")
    address = st.text_area("Residential Address", placeholder="House No., Street, City, State", height=80)
    st.markdown('</div>', unsafe_allow_html=True)

    # Submit
    submit = st.button("📨 Submit Application")

    # Result
    if submit:
        if not name.strip() or not email.strip() or not phone.strip() or not address.strip():
            st.warning("⚠️ Please fill in all required fields.")
        else:
            if target_class == "Class 10th":
                student = Class10(name, age, email, phone, gender, address)
            else:
                student = Class12(name, age, email, phone, gender, address)

            if student.admitted:
                st.markdown(f"""
                <div class="result-success">
                    <div class="result-icon">🎉</div>
                    <div class="result-title" style="color:#2e7d32">{student.message}</div>
                    <div class="result-sub" style="color:#388e3c">
                        Welcome to CENTRAL ENGLISH SCHOOL, {student.name.split()[0]}!<br>
                        Your application for <b>{target_class}</b> has been received.
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="detail-table">
                    <div class="detail-row-item"><span class="d-label">👤 Full Name</span><span class="d-value">{student.name}</span></div>
                    <div class="detail-row-item"><span class="d-label">🎂 Age</span><span class="d-value">{student.age} years</span></div>
                    <div class="detail-row-item"><span class="d-label">⚧ Gender</span><span class="d-value">{student.gender}</span></div>
                    <div class="detail-row-item"><span class="d-label">📧 Email</span><span class="d-value">{student.email}</span></div>
                    <div class="detail-row-item"><span class="d-label">📱 Phone</span><span class="d-value">{student.phone}</span></div>
                    <div class="detail-row-item"><span class="d-label">🏠 Address</span><span class="d-value">{student.address}</span></div>
                    <div class="detail-row-item"><span class="d-label">🏫 Class</span><span class="d-value">{target_class}</span></div>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div class="result-fail">
                    <div class="result-icon">❌</div>
                    <div class="result-title" style="color:#c62828">{student.message}</div>
                    <div class="result-sub" style="color:#e53935">
                        Your age is <b>{student.age} years</b>. Class 12th requires minimum <b>16 years</b>.<br>
                        You can still apply for <b>Class 10th</b>.
                    </div>
                </div>
                """, unsafe_allow_html=True)

with col_right:
    # Requirements
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📌 Admission Requirements</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="req-card-10">
        <div class="req-title" style="color:#2e7d32">✅ Class 10th</div>
        <div class="req-desc">Open for all students. No strict age restriction applied.</div>
    </div>
    <div class="req-card-12">
        <div class="req-title" style="color:#e65100">⚠️ Class 12th</div>
        <div class="req-desc">Minimum age of <b>16 years</b> required. Students below 16 are not eligible.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Age Display
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📊 Your Age Status</div>', unsafe_allow_html=True)

    tag = '<span class="eligible-tag tag-green">✅ Eligible for Both Classes</span>' if age >= 16 else '<span class="eligible-tag tag-yellow">⚠️ Eligible for Class 10th Only</span>'

    st.markdown(f"""
    <div class="age-meter">
        <div class="age-big">{age}</div>
        <div class="age-sub">Years Old</div>
        {tag}
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Contact Card
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">📞 Contact Us</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.88rem; color:#3949ab; line-height:2;">
        📧 admission@Cesschool.edu.in<br>
        📱 +91 98765 43210<br>
        🕐 Mon–Sat: 9AM – 4PM<br>
        📍 CENTRAL ENGLISH SCHOOL, Sector 14
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
