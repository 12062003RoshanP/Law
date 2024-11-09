import streamlit as st
import time
from PIL import Image

# Predefined dictionary of scenario-based legal summaries
qa_data = {
    "speeding": "Under the Motor Vehicles Act, speeding is punishable with a fine ranging from Rs. 1000 to Rs. 2000. Repeat offenses can lead to increased penalties or even suspension of the license. Always adhere to speed limits to avoid accidents and fines.",
    "accident ":"In the event of a car accident, especially if it involves injury or damage, you may be liable under the Motor Vehicles Act.Operating a vehicle negligently can lead to penalties. Serious accidents may also involve imprisonment or fines.Depending on the severity, fines may range from ₹2,000 to ₹10,000, and/or imprisonment.",
    "parking": "Parking laws vary by region, but generally, improper parking in a residential or restricted area can lead to fines. Many local authorities impose fines up to Rs. 500 for first-time violations, while repeated offenses can lead to higher fines or vehicle towing.",
    " Hack" :"Hacking into a website without permission, even if you didn’t intend to cause harm, is still a violation under the Information Technology (IT) Act. Unauthorized access to someone else’s system or data is punishable under Section 66 of the IT Act, which can lead to imprisonment for up to 3 years and/or a fine of up to ₹5 lakh. You may be prosecuted even if there was no intention to harm, as the law focuses on the act of unauthorized access itself.",
    "license": "Driving without a valid license is a serious offense under the Motor Vehicles Act. Fines may start from Rs. 5000, and repeat offenses can lead to imprisonment of up to 3 months or more severe penalties, depending on the jurisdiction.",
    "helmet": "According to the Motor Vehicles Act, riding without a helmet is a punishable offense, typically with a fine of Rs. 1000. Even if you were unaware that helmet use was mandatory in your state, it is unlikely that this will serve as a valid excuse. Compliance with the law is expected, and you may have to pay the fine. In some cases, you might be able to request a hearing to explain the situation, but the law generally requires helmet use for safety..",
    "stolen ": "If your vehicle is stolen, the first step is to file a First Information Report (FIR) at the nearest police station, providing details like the vehicle's make, model, registration number, and insurance papers. The police will investigate the theft, and the FIR serves as an official record. This report is also crucial for filing an insurance claim, as it may be required for reimbursement or compensation. Stay in touch with both the police and your insurance company for updates and to ensure the necessary documentation is provided..",
    "Speeding in School Zone":"Exceeding the speed limit in a school zone can result in a higher fine due to the increased safety risks for children. Speed limits in school zones are generally lower, and being unaware of this won't usually be accepted as a valid reason for avoiding the fine. You can request a hearing or appeal if you believe it was an honest mistake."
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
                st.write("Sorry, I don't have an answer for that question.")

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
                        <p>Karnataka High Court</p>
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
                        <p>Karnataka High Court</p>
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
elif menu == "Emergency Legal Consultations":
    st.write("## Emergency Legal Consultations - We're Here for You 24/7")
    
    st.write("""
    **In case of an emergency**, we understand that time is of the essence, and legal support is often critical to resolving issues swiftly. 
    That's why we offer immediate access to legal professionals who are available to help in urgent situations. Whether you're facing a legal crisis, 
    need advice in a high-pressure scenario, or need emergency representation, Nyaya-Buddy is here to assist you.
    """)

    st.write("""
    ### 24/7 Emergency Legal Hotline:
    For urgent legal concerns, contact our **24/7 emergency hotline** at:
    **+91-XXXX-XXXX**. Our team of experienced attorneys is ready to assist you.
    Whether it’s a criminal issue, civil litigation, or personal injury case, we have you covered with quick responses and practical solutions.
    """)

    st.write("""
    ### Immediate Legal Assistance Form:
    Fill out the form below to get in touch with our emergency legal team right away. 
    Our experts will respond within minutes, providing personalized legal advice or connecting you with the appropriate legal professionals.
    """)

    emergency_form = st.form(key="emergency_form")
    with emergency_form:
        name = st.text_input("Your Name")
        phone = st.text_input("Your Contact Number")
        legal_issue = st.text_area("Briefly describe your legal issue")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.write("Thank you! Our team will contact you shortly.")

elif menu == "Legal Community Membership":
    st.write("## Join the Nyaya-Buddy Legal Community")
    
    st.write("""
    At Nyaya-Buddy, we believe in fostering a community of like-minded legal professionals, enthusiasts, and individuals who are passionate about 
    understanding and navigating the legal landscape. By joining our Legal Community, you'll have access to exclusive content, resources, 
    networking opportunities, and much more.
    """)
    
    st.write("""
    ### Why Join?
    - **Networking Opportunities:** Connect with lawyers, paralegals, legal advisors, and students from various fields of law.
    - **Exclusive Webinars & Events:** Attend online webinars and workshops hosted by top legal professionals. 
    - **Stay Updated:** Get the latest updates on law changes, case studies, and legal trends delivered straight to your inbox.
    - **Collaborative Learning:** Share knowledge and resources with other members to enhance your own understanding of legal matters.
    - **Access to Resources:** Gain access to exclusive resources, including templates, legal articles, case analyses, and much more.

    ### Membership Benefits:
    - Free access to our legal insights newsletter.
    - Invitations to legal community events and networking sessions.
    - Discounts on legal consultations with top-rated attorneys.

    Join today and be part of a community that is dedicated to understanding, sharing, and growing in the field of law!
    """)
    
    st.write("To sign up for the community, please provide your details below:")

    community_form = st.form(key="community_form")
    with community_form:
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        area_of_interest = st.selectbox("Area of Legal Interest", ["Corporate Law", "Criminal Law", "Family Law", "Real Estate Law", "Tax Law", "Others"])
        submit_button = st.form_submit_button("Join Now")

    if submit_button:
        st.write(f"Thank you for joining the Nyaya-Buddy Legal Community, {first_name}! You'll start receiving updates shortly.")

elif menu == "About Us":
    st.write("## About Nyaya-Buddy - Your Trusted Legal Companion")

    st.write("""
    **Nyaya-Buddy** is a revolutionary legal tech platform designed to provide fast, reliable, and affordable legal assistance for individuals, businesses, 
    and organizations. Our mission is to make the law more accessible and understandable to everyone, regardless of their background or legal expertise.
    """)
    
    st.write("""
    ### Our Vision:
    Our vision is to empower people with the legal knowledge they need and the resources to take informed decisions. We want to bridge the gap between law 
    and society by offering a solution that is easily accessible, cost-effective, and efficient.
    """)
    
    st.write("""
    ### Our Services:
    Nyaya-Buddy offers a wide range of legal services, including:
    - **24/7 Legal Consultation:** Get immediate access to lawyers and legal advisors for urgent matters.
    - **Document Preparation and Review:** Ensure your contracts, agreements, and legal documents are properly drafted and reviewed by experts.
    - **Case Analysis:** Use our case analysis feature to understand past cases that resemble your legal situation, helping you form a stronger argument or strategy.
    - **Legal Resources and Tools:** Access valuable resources, including legal templates, advice columns, and guides to help navigate your legal journey.
    - **Lawyer Referral Service:** We connect you with a qualified lawyer for further legal representation, wherever needed.

    ### Our Team:
    Our team consists of seasoned legal professionals, consultants, and support staff who are dedicated to providing top-tier legal services and advice. We are committed to ensuring our clients receive prompt and reliable legal assistance in every situation.

    ### Contact Us:
    If you have any questions or need assistance, don't hesitate to reach out to us:
    - Email: **support@nyaya-buddy.com**
    - Phone: **+91-XXXX-XXXX**
    - Visit: **www.nyaya-buddy.com/contact**

    **Nyaya-Buddy** – Because legal matters shouldn’t be stressful.
    """)

    st.write("We’re here to guide you every step of the way.")
