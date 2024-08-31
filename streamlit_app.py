import streamlit as st

# Initialize selected_tab if it doesn't exist
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = "👧 Personal Details"

# Create two columns with adjusted width ratios
col1, col2 = st.columns([2, 1])  # Adjust the ratio to control spacing

with col1:
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='font-size: 3rem;'> Hello👋 I'm Cielo!</h1>
            <p>Here you can explore my personal details, likes, skills, and interests. <br/>Feel free to click on the tabs below to navigate through the content.</p>
            🦕🦖🐊
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    # Create a new column specifically for the image to align it to the left
    col2_left, _ = st.columns([1, 3])  # Ratio to control image alignment
    with col2_left:
        st.image("images/shilo.png", width=300)  # Adjust the width as needed

# Add centered gradient divider
st.markdown(
    """
    <div style='text-align: center; margin: 20px 0;'>
        <div style='display: inline-block; height: 4px; width: 100%; background: linear-gradient(to right, #84ffc9, #aab2ff,#eca0ff);'></div>
    </div>
    """,
    unsafe_allow_html=True
)



# Define the tab options
tabs = ["👧 Personal Details", "💗 Likes / Dislikes", "⭐ Skills", "📚 Interests"]

# Create a container for buttons with equal width
button_container = st.container()

# Create a centered row for buttons
with button_container:
    cols = st.columns(len(tabs))  # Create columns for each tab button

    for i, tab in enumerate(tabs):
        with cols[i]:
            if st.button(tab):
                st.session_state.selected_tab = tab

# Display content based on the selected tab
if st.session_state.selected_tab == "👧 Personal Details":
    st.subheader("Personal Details")
    st.markdown(
        """
        <div style='font-size: 1.2rem;'>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>😄 Name:</strong> Cielo C. Alegam</p>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>🏫 Study:</strong> Cebu Institute of Technology - University</p>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>📍 Hometown:</strong> Cebu City, Philippines</p>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>♋ Zodiac Sign:</strong> Cancer</p>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>💡 MBTI:</strong> INFJ</p>
            <p style='font-size: 1.2rem; font-weight: bold''><strong>🩸 Blood Type:</strong> O+</p>
        </div>
        """,
        unsafe_allow_html=True
    )
elif st.session_state.selected_tab == "💗 Likes / Dislikes":
    st.subheader("Likes/Dislikes")
    
    # Create two columns for Likes and Dislikes
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div style='font-size: 1.2rem;'>
                <h3>👍 Likes</h3>
                <ul>
                    <li style='font-size: 1.1rem; font-weight: bold'>🍃 I like green colors.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🏊‍♀️ I like swimming.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🐕 I like dogs.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🍜 I like ramen noodles.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🍵 I like matcha and coke.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='font-size: 1.2rem;'>
                <h3>👎 Dislikes</h3>
                <ul>
                    <li style='font-size: 1.1rem; font-weight: bold'>🐛 I don't like bugs.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🔥 I don't like a very hot weather.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🛌 I don't like waking up early.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>👩‍💼 I don't like presenting in a large audience.</li>
                    <li style='font-size: 1.1rem; font-weight: bold'>🚃 I don’t like people who don't help in handing over the money to the driver in jeepney rides.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
elif st.session_state.selected_tab == "⭐ Skills":
    st.subheader("Skills")
    st.write("Here you can add your skills.")
elif st.session_state.selected_tab == "📚 Interests":
    st.subheader("Interests")
    st.write("Here you can list your interests.")
