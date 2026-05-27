import streamlit as st

# ─────────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Student Admission Portal",
    page_icon="🎓",
    layout="wide"
)

# ─────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap');

* { font-family: 'Poppins', sans-serif; }

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    min-height: 100vh;
}

/* Hide default streamlit header */
#MainMenu, footer, header { visibility: hidden; }

/* Main Title */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: #ffffff;
    text-align: center;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 30px rgba(130, 100, 255, 0.6);
}

.sub-title {
    text-align: center;
    color: #a89ee0;
    font-size: 1rem;
    margin-bottom: 2rem;
    font-weight: 300;
}

/* Card */
.card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 25px 50px rgba(0,0,0,0.3);
}

/* Section Header */
.section-header {
    font-size: 1.1rem;
    font-weight: 600;
    color: #c4b5fd;
    border-bottom: 2px solid rgba(196, 181, 253, 0.3);
    padding-bottom: 0.5rem;
    margin-bottom: 1.2rem;
}

/* Requirement Box */
.req-box-10 {
    background: rgba(52, 211, 153, 0.15);
    border-left: 4px solid #34d399;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    margin-bottom: 0.8rem;
    color: #a7f3d0;
    font-size: 0.9rem;
}

.req-box-12 {
    background: rgba(251, 191, 36, 0.15);
    border-left: 4px solid #fbbf24;
    border-radius: 10px;
    padding: 0.8rem 1rem;
    margin-bottom: 0.8rem;
    color: #fde68a;
    font-size: 0.9rem;
}

/* Age Display */
.age-display {
    background: rgba(139, 92, 246, 0.2);
    border: 1px solid rgba(139, 92, 246, 0.4);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    margin-top: 1rem;
}

.age-number {
    font-size: 2.5rem;
    font-weight: 700;
    color: #c4b5fd;
}

.age-label {
    color: #a89ee0;
    font-size: 0.85rem;
}

/* Success Box */
.success-box {
    background: rgba(52, 211, 153, 0.15);
    border: 1px solid #34d399;
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    animation: fadeIn 0.5s ease;
}

.error-box {
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid #ef4444;
    border-radius: 15px;
    padding: 1.5rem;
    text-align: center;
    animation: fadeIn 0.5s ease;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Detail Row */
.detail-row {
    display: flex;
    justify-content: space-between;
    padding: 0.6rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    color: #e2d9f3;
    font-size: 0.9rem;
}

.detail-label { color: #a89ee0; }
.detail-value { font-weight: 500; color: #ffffff; }

/* Input label color override */
label { color: #c4b5fd !important; font-size: 0.9rem !important; }

/* Selectbox */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: white !important;
}

/* Text Input */
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: white !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2rem !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(124, 58, 237, 0.6) !important;
}

/* Divider */
hr { border-color: rgba(255,255,255,0.1) !important; }

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Classes
# ─────────────────────────────────────────────

class Student:
    def __init__(self, name, age, email, phone_number):
        self.name         = name
        self.age          = age
        self.email        = email
        self.phone_number = phone_number


class Class10(Student):
    def __init__(self, name, age, email, phone_number):
        super().__init__(name, age, email, phone_number)
        self.admitted = True
        self.message  = "Admission Successful!"


class Class12(Student):
    def __init__(self, name, age, email, phone_number):
        super().__init__(name, age, email, phone_number)
        if self.age >= 16:
            self.admitted = True
            self.message  = "Admission Successful!"
        else:
            self.admitted = False
            self.message  = "Admission Failed! Age must be 16 or above for Class 12."


# ─────────────────────────────────────────────
# UI Layout
# ─────────────────────────────────────────────

# Header
st.markdown('<div class="main-title">🎓 Student Admission Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Complete the form below to secure your admission</div>', unsafe_allow_html=True)

# 3 Columns Layout
col_nav, col_form, col_req = st.columns([1.2, 2.5, 1.5])

# ── Left: Navigation ──────────────────────────
with col_nav:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧭 Navigation")
    st.markdown("---")
    st.markdown("📝 **Apply for Admission**")
    st.markdown("👥 View Registered Students")
    st.markdown("---")
    st.markdown("### 💬 Help & Support")
    st.markdown("For queries, contact:")
    st.markdown("📧 support@eduportal.com")
    st.markdown('</div>', unsafe_allow_html=True)

# ── Middle: Form ──────────────────────────────
with col_form:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">📋 Application Form</div>', unsafe_allow_html=True)

    # Class Selection
    target_class = st.selectbox("Select Target Class", ["Class 10th", "Class 12th"])

    # Name & Age side by side
    c1, c2 = st.columns([2, 1])
    with c1:
        name = st.text_input("Full Name", placeholder="Enter your full name")
    with c2:
        age = st.number_input("Age", min_value=5, max_value=25, value=15, step=1)

    # Email
    email = st.text_input("Email Address", placeholder="johndoe@example.com")

    # Phone
    phone = st.text_input("Contact Number", placeholder="+1 234 567 890")

    st.markdown("<br>", unsafe_allow_html=True)

    # Submit Button
    submit = st.button("🎯 Submit Application")

    # Result
    if submit:
        if not name or not email or not phone:
            st.warning("⚠️ Please fill in all fields before submitting.")
        else:
            if target_class == "Class 10th":
                student = Class10(name, age, email, phone)
            else:
                student = Class12(name, age, email, phone)

            st.markdown("<br>", unsafe_allow_html=True)

            if student.admitted:
                st.markdown(f"""
                <div class="success-box">
                    <div style="font-size:2.5rem">🎉</div>
                    <div style="font-size:1.3rem; font-weight:700; color:#34d399; margin:0.5rem 0">{student.message}</div>
                    <div style="color:#a7f3d0; font-size:0.9rem">Welcome to {target_class}!</div>
                </div>
                """, unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown("**📄 Student Details:**")
                st.markdown(f"""
                <div style="background:rgba(255,255,255,0.05); border-radius:12px; padding:1rem;">
                    <div class="detail-row"><span class="detail-label">👤 Name</span><span class="detail-value">{student.name}</span></div>
                    <div class="detail-row"><span class="detail-label">🎂 Age</span><span class="detail-value">{student.age} years</span></div>
                    <div class="detail-row"><span class="detail-label">📧 Email</span><span class="detail-value">{student.email}</span></div>
                    <div class="detail-row"><span class="detail-label">📱 Phone</span><span class="detail-value">{student.phone_number}</span></div>
                    <div class="detail-row"><span class="detail-label">🏫 Class</span><span class="detail-value">{target_class}</span></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="error-box">
                    <div style="font-size:2.5rem">❌</div>
                    <div style="font-size:1.3rem; font-weight:700; color:#ef4444; margin:0.5rem 0">{student.message}</div>
                    <div style="color:#fca5a5; font-size:0.9rem">Your age: {student.age} years | Required: 16+ years</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Right: Requirements ───────────────────────
with col_req:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 📌 Admission Requirements")
    st.markdown("---")

    st.markdown("""
    <div class="req-box-10">
        ✅ <strong>Class 10th</strong><br>
        No strict age restriction.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="req-box-12">
        ⚠️ <strong>Class 12th</strong><br>
        Mandatory age of <strong>16 years or older</strong>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Your Inputted Age**")

    st.markdown(f"""
    <div class="age-display">
        <div class="age-number">{age}</div>
        <div class="age-label">years old</div>
        <div style="margin-top:0.5rem; font-size:0.85rem; color: {'#34d399' if age >= 16 else '#fbbf24'}">
            {'✅ Eligible for both classes' if age >= 16 else '⚠️ Eligible for Class 10th only'}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
