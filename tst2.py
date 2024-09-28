import streamlit as st

st.set_page_config(page_title="Joanne's Portfolio", page_icon="👩‍💻", layout="wide")

st.title("Joanne Alice Thomas")
st.subheader("Computer Science Engineering Student at MITS")


menu = ["About", "Projects", "Skills", "Contact"]
choice = st.sidebar.selectbox("Select an option", menu)

if choice == "About":
    st.header("About Me")
    st.write("""
        Hello! I'm Joanne, currently a second-year Computer Science Engineering student at Muthoot Institute of Technology and Science. 
        My passion for technology and coding drives me to constantly explore new ideas and innovate. As an AI enthusiast, I'm deeply invested 
        in understanding the cutting-edge developments in artificial intelligence, from machine learning algorithms to neural networks.
        
        I thrive on expanding my knowledge and skills, whether it's through hands-on projects, hackathons, or staying updated with the latest trends in AI. 
        My goal is to not just learn AI but also apply it to solve real-world problems, making a meaningful impact in the tech world.
    """)

elif choice == "Projects":
    st.header("Projects")
    st.write("""
        Here are some of my notable projects:
    """)
    
    st.subheader("Sush-Bot")
    st.write("""
        Sushibot is an AI-powered chatbot designed to handle a wide variety of prompts and provide accurate, context-aware responses. 
        It leverages state-of-the-art technologies like Langchain, Groq API, and Streamlit to deliver fast, efficient, and intuitive user interactions.
    """)
    st.markdown("[View Sush-Bot](https://sushi-ai-mbnzpsdwm8n6vnvgzaamrd.streamlit.app/)")

elif choice == "Skills":
    st.header("Skills")
    skills = [
        "Programming Languages: Python, Java, C, C++, MySQL",
        "Web Development: HTML, CSS",
        "Data Structures & Algorithms",
        "Generative AI",
        "AI Tools"
    ]
    
    for skill in skills:
        st.write(f"- {skill}")

elif choice == "Contact":
    st.header("Contact Me")
    st.write("""
        If you'd like to get in touch, feel free to reach out via email: [joannealicethomas@gmail.com](mailto:joannealicethomas@gmail.com)
    """)

# Footer Section
st.markdown("<footer style='text-align: center;'><p>&copy; 2024 Joanne. All rights reserved.</p></footer>", unsafe_allow_html=True)
