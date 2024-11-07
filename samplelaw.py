import streamlit as st
import time
from PIL import Image

# Predefined dictionary of scenario-based legal summaries
qa_data = {
    "speeding": "Under the Motor Vehicles Act, speeding is punishable with a fine ranging from Rs. 1000 to Rs. 2000. Repeat offenses can lead to increased penalties or even suspension of the license. Always adhere to speed limits to avoid accidents and fines.",
    "parking": "Parking laws vary by region, but generally, improper parking in a residential or restricted area can lead to fines. Many local authorities impose fines up to Rs. 500 for first-time violations, while repeated offenses can lead to higher fines or vehicle towing.",
    "license": "Driving without a valid license is a serious offense under the Motor Vehicles Act. Fines may start from Rs. 5000, and repeat offenses can lead to imprisonment of up to 3 months or more severe penalties, depending on the jurisdiction.",
    "helmet": "According to the Motor Vehicles Act, wearing a helmet is mandatory while riding two-wheelers. Non-compliance may result in a fine of Rs. 1000. Helmets protect riders from severe injuries and are compulsory in most states.",
    "stolen vehicle": "To report a stolen vehicle, file an FIR at the nearest police station with your vehicle details and insurance papers. The police will investigate and, if necessary, provide documentation for insurance claims. This documentation can help in future inquiries about the vehicle."
}

# Case details and arguments
case_summary = """
The case of *Jageshwar Prasad Namdeo vs. Smt. Kalpana Pathak* involves a dispute under the Motor Vehicles Act. 
The appeal was filed by Jageshwar Prasad Namdeo, who challenged an award by the Motor Accident Claims Tribunal (MACT) in Satna. 
This arose from a motorcycle accident in which Omkar Pathak, the deceased, was riding as a pillion passenger on Jageshwar Prasad Namdeo’s motorcycle. 
Due to alleged negligent driving by Namdeo, the motorcycle slipped, leading to serious injuries for Pathak, who later died. 
Pathak’s family filed a claim, arguing that Namdeo's rash driving caused the accident, while Namdeo argued he was the pillion rider and contested jurisdiction.
"""

arguments = [
    ("Jurisdiction - Appellant’s Lawyer", 
     "Your Honor, the primary issue here is jurisdiction. The accident took place in Panna, and both the appellant and the claimants reside there. According to Section 166(2) of the Motor Vehicles Act, the claim must be filed in the jurisdiction where the accident occurred or where the parties reside. The Satna tribunal should not entertain this claim as it lacks jurisdiction."),
    
    ("Jurisdiction - Respondent’s Lawyer", 
     "Respectfully, Your Honor, while the accident did occur in Panna, the claimant, Mrs. Kalpana Pathak, was living temporarily in Satna at the time of filing. Her son, one of the minor claimants, was studying in Satna, and she was residing there to care for him. Section 166(2) allows for filing where the claimant resides, which includes Satna."),
    ("Negligence and Fault in the Accident-Appellant’s Lawyer",
     "Your Honor, the deceased, Mr. Omkar Pathak, was driving the motorcycle, and my client, Mr. Namdeo, was merely the pillion passenger. It was the deceased's own negligence that led to the accident, not my client's actions. We urge the court to recognize that the responsibility lies solely with the deceased")
]

# Streamlit app setup
st.set_page_config(page_title="Nyaya-Buddy in Law", layout="wide", page_icon="⚖️")

# Set the theme to dark mode
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #333333;
        color: #ffffff;
    }
    .stButton button {
        background-color: #f7941d;
        color: white;
        border-radius: 5px;
    }
    .stButton button:hover {
        background-color: #f77f24;
    }
    .stTextInput input {
        background-color: #444444;
        color: #ffffff;
    }
    .stSelectbox select {
        background-color: #444444;
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #444444;
        color: #ffffff;
    }
    .css-1v3fvcr {
        background-color: #333333;
    }
    .css-ffhzg2 {
        background-color: #121212;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center; color: #f7941d;'>Nyaya-Buddy in Law 24/7</h1>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.title("Nyaya-Buddy Menu")
    st.write("### 💬 Chat with Nyaya-Buddy")
    st.write("Chat with Nyaya-Buddy for any legal queries.")
    menu = st.radio("Choose an option", ["Know Your Law", "Book a Lawyer", "Emergency Legal Consultations", "Legal Community Membership", "About Us"])

# Main Content based on selection from sidebar
if menu == "Know Your Law":
    # Chatbot embedded inside "Know Your Law" Section
    st.write("## Chat with Nyaya-Buddy for Legal Queries")
    
    # Predefined Legal Insights
    def predefined_qa():
        user_input = st.text_input("Enter your legal question or scenario (e.g., speeding, parking):").strip().lower()

        if user_input:
            found_answer = False
            for keyword, answer in qa_data.items():
                if keyword in user_input:
                    st.write("Answer:", answer)
                    found_answer = True
                    break
            if not found_answer:
                st.write("Sorry, I don't have an answer for that question. Try asking about 'speeding', 'parking', 'license', 'helmet', or 'stolen vehicle'.")

    predefined_qa()

    st.write("## Case Analysis")
    
    # Upload and Case Analysis
    uploaded_file = st.file_uploader("Upload case document (PDF)", type="pdf")
    if uploaded_file:
        st.write("File uploaded successfully.")
    
    # Case Summary Section
    if 'summary_generated' not in st.session_state:
        st.session_state.summary_generated = False

    if not st.session_state.summary_generated:
        if st.button("Generate Case Summary"):
            st.session_state.summary_generated = True
            st.write("### Case Summary")
            words = case_summary.split()
            sentence = ""
            text_placeholder = st.empty()
            for word in words:
                sentence += f" {word}"
                text_placeholder.markdown(f'<span style="font-size:20px">{sentence}</span>', unsafe_allow_html=True)
                time.sleep(0.5)
    else:
        st.write("### Case Summary (Already Generated)")
        st.write(case_summary)
        
    # Argument Section
    if 'arguments_generated' not in st.session_state:
        st.session_state.arguments_generated = False
    
    if not st.session_state.arguments_generated:
        if st.button("View Arguments"):
            st.session_state.arguments_generated = True
            st.write("### Lawyer Arguments")
            for title, statement in arguments:
                st.write(f"**{title}**")
                st.write(f"<span style='font-size:20px'>{statement}</span>", unsafe_allow_html=True)
                time.sleep(2)
    else:
        st.write("### Lawyer Arguments (Already Generated)")
        for title, statement in arguments:
            st.write(f"**{title}**\n{statement}")
        
elif menu == "Book a Lawyer":
    # Quick Book Section
    st.write("## Quick Book")
    with st.form(key="search_form"):
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

        with col1:
            location = st.text_input("Preferred Location/Pincode", "Bangalore")
        with col2:
            date = st.date_input("Select Date")
        with col3:
            specialty = st.selectbox("Select Specialty", [
                "Corporate Law", "Criminal Law", "Civil Law", "Real Estate Law",
                "Intellectual Property Law", "Tax Law", "Immigration Law", "Health Care Law"
            ])
        with col4:
            st.write("")  # empty space
            search_button = st.form_submit_button(label="Search")

    # Consultation buttons
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        in_person_button = st.button("In-Person Visit")
    with col2:
        video_consult_button = st.button("Video Consult")

    # Lawyer Cards Section with booking options and photos, full outer box
    st.write("### Best matching lawyers for your Search")

    if in_person_button:
        # Show both lawyers for In-Person Visit
        col1, col2 = st.columns(2)
        
        # Lawyer 1
        with col1:
            with st.container():
                st.markdown("""
                    <div style="border: 2px solid #f7941d; border-radius: 10px; padding: 15px; background-color: #222222;">
                        <img src="https://via.placeholder.com/150" width="100" style="border-radius: 50%;"/>
                        <h4 style="color: #f7941d;">Advocate Rajiv Kumar</h4>
                        <p><strong>10 years</strong> - Criminal Law, Civil Law</p>
                        <p>Supreme Court of India</p>
                        <p><strong>₹3000</strong></p>
                        <p>⭐⭐⭐⭐☆</p>
                        <p>Available tomorrow at 3:00 PM</p>
                        <p><em>No Booking Fees</em></p>
                        <button style="background-color: #f7941d; color: white; border: none; padding: 10px 20px; border-radius: 5px;">
                            Book Now
                        </button>
                    </div>
                """, unsafe_allow_html=True)

        # Lawyer 2
        with col2:
            with st.container():
                st.markdown("""
                    <div style="border: 2px solid #f7941d; border-radius: 10px; padding: 15px; background-color: #222222;">
                        <img src="https://via.placeholder.com/150" width="100" style="border-radius: 50%;"/>
                        <h4 style="color: #f7941d;">Advocate Sneha Mehta</h4>
                        <p><strong>15 years</strong> - Corporate Law, Tax Law</p>
                        <p>Mumbai High Court, Mahim District</p>
                        <p><strong>₹2200</strong></p>
                        <p>⭐⭐⭐⭐☆</p>
                        <p>Available tomorrow at 1:00 PM</p>
                        <p><em>No Booking Fees</em></p>
                        <button style="background-color: #f7941d; color: white; border: none; padding: 10px 20px; border-radius: 5px;">
                            Book Now
                        </button>
                    </div>
                """, unsafe_allow_html=True)

    if video_consult_button:
        # Show one lawyer for Video Consult
        col1, col2 = st.columns(2)
        with col1:
            with st.container():
                st.markdown("""
                    <div style="border: 2px solid #f7941d; border-radius: 10px; padding: 15px; background-color: #222222;">
                        <img src="https://via.placeholder.com/150" width="100" style="border-radius: 50%;"/>
                        <h4 style="color: #f7941d;">Advocate Rajiv Kumar</h4>
                        <p><strong>10 years</strong> - Criminal Law, Civil Law</p>
                        <p>Supreme Court of India</p>
                        <p><strong>₹3000</strong></p>
                        <p>⭐⭐⭐⭐☆</p>
                        <p>Available tomorrow at 3:00 PM</p>
                        <p><em>No Booking Fees</em></p>
                        <button style="background-color: #f7941d; color: white; border: none; padding: 10px 20px; border-radius: 5px;">
                            Book Now
                        </button>
                    </div>
                """, unsafe_allow_html=True)
