import streamlit as st
from PIL import Image
from datetime import datetime

# App Title
st.title("Editable Biography App")

# Create two columns for layout
col1, col2 = st.columns([3, 1])

# Editable Personal Details (in the first column)
with col1:
    st.header("About Me")
    name = st.text_input("Enter your full name", "Danica Villanueva Dagohoy")
    bio = st.text_area("Write a short bio about yourself", 
                       "Hola! I'm passionate about traveling and exploring new places it's my way of finding adventure and inspiration. When I'm not traveling, you'll often find me on the volleyball court, enjoying the game I love. Life's all about balance and chasing what makes you happy!")
    birthday = st.text_input("Enter your birthday", "July 26, 2005")
    
    # Add age input, automatically calculate age based on birthday
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%B %d, %Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
    # Display calculated age
    st.write(f"Age: {age}")
    
    # Add Gender input
    gender = st.selectbox("Select your gender", ["Female", "Male", "Other", "Prefer not to say"])

    # Editable Educational Attainment (Checklist)
    st.header("Educational Attainment")
    
    # Educational Attainment Checklist
    education_options = [
        "College Graduate",
        "College Level",
        "High School Graduate",
        "Middle School Level",
        "Elementary Graduate",
        "Others"
    ]
    
    education_selected  = ["College Level"]
    
    for option in education_options:
        if st.checkbox(option):
            education_selected.append(option)
    
    # Display the selected educational background
    st.write("**Your Selected Educational Attainment:**")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")
    
    # Editable Parental Information
    st.header("Parental Information")
    father_name = st.text_input("Father's Name", "Mr. Danilo Ñ. Dagohoy")
    father_occupation = st.text_input("Father's Occupation", "Electrician")
    mother_name = st.text_input("Mother's Name", "Mrs. Maricel V. Dagohoy")
    mother_occupation = st.text_input("Mother's Occupation", "Housewife")

    # Editable Contact Information
    st.header("Contact Information")
    email = st.text_input("Email", "danicadagohoy21@gmail.com")
    phone = st.text_input("Phone", "09666931171")
    facebook = st.text_input("Facebook Profile URL", "https://www.facebook.com/princessdanica.dagohoy")


    # Editable Hobbies/Interests
    st.header("Hobbies & Interests")
    hobbies = st.text_area("List your hobbies or interests", 
                           " Playing Badminton & Volleyball, Swimming, Photography ")
# Editable Photo (in the second column)
with col2:
    st.subheader("Photo")
    st.write("You can upload a profile photo below:")
    uploaded_photo = st.file_uploader("C:\Windows\Web\Wallpaper\ThemeC\img30.jpg", type=["jpg", "jpeg", "png"])

    if uploaded_photo:
        photo = Image.open(uploaded_photo)
        st.image(photo, caption=f"{name}'s Photo", use_column_width=True)
    else:
        st.write("No photo uploaded.")

# Display the User's Input as a Profile in two columns

# Left column: User's info
col1, col2 = st.columns([3, 1])

with col1:
    st.header("Your Profile")
    st.subheader(f"Name: {name}")
    st.write(f"*Bio:* {bio}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    
    st.subheader("Educational Attainment")
    if education_selected:
        for item in education_selected:
            st.write(f"- {item}")
    else:
        st.write("No educational background selected.")

    st.subheader("Parental Information")
    st.write(f"*Father's Name:* {father_name}  \n**Occupation:** {father_occupation}")
    st.write(f"*Mother's Name:* {mother_name}  \n**Occupation:** {mother_occupation}")

    st.subheader("Contact Information")
    st.write(f"- *Email:* {email}  \n- *Phone:* {phone}")
    st.write(f"- *Facebook:* [Profile]({facebook})")

    st.subheader("Hobbies & Interests")
    st.write(hobbies)

# Right column: Photo (positioned on the upper right)
with col2:
    if uploaded_photo:
        st.image(photo, caption=f"{name}'s Photo", use_column_width=True)
    else:
        st.write("No photo uploaded.")
