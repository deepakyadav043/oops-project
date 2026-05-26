import streamlit as st

class Student:
    def __init__(self, name, age, email, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.phone_number = phone_number

    def display(self):
        st.success("✅ Student Details")
        st.write(f"**Name:** {self.name}")
        st.write(f"**Age:** {self.age}")
        st.write(f"**Email:** {self.email}")
        st.write(f"**Phone Number:** {self.phone_number}")


class Class10(Student):
    def __init__(self, name, age, email, phone_number):
        super().__init__(name, age, email, phone_number)
        st.success("🎉 Admission Successful for Class 10!")


class Class12(Student):
    def __init__(self, name, age, email, phone_number):
        super().__init__(name, age, email, phone_number)
        if self.age >= 16:
            st.success("🎉 Admission Successful for Class 12!")
        else:
            st.error("❌ Admission Failed! Age must be 16 or above for Class 12.")


# ─── Streamlit UI ───────────────────────────────────────────
st.title("🏫 School Admission Portal")

choice = st.radio("Select Class for Admission:", ["Class 10", "Class 12"])

st.subheader("📋 Enter Student Details")

name         = st.text_input("Name")
age          = st.number_input("Age", min_value=1, max_value=100, step=1)
email        = st.text_input("Email")
phone_number = st.text_input("Phone Number")

if st.button("Submit Admission"):
    if name and email and phone_number:
        if choice == "Class 10":
            student = Class10(name, int(age), email, phone_number)
            student.display()
        else:
            student = Class12(name, int(age), email, phone_number)
            student.display()
    else:
        st.warning("⚠️ Please fill all the details!")