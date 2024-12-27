import streamlit as st

st.set_page_config(page_title="About Me",page_icon=":headphone:",layout="centered")

with st.container(border=True):
    with st.container():
        st.title("GET TO KNOW ME")
        st.subheader("Kylle C. Nacionales")
        st.subheader("A Grade 12 ICT Student in RTU")
        st.write("This website is created solely using python and streamlit which is an open-source framework that helps in making custom web apps ")
        st.image ("brim.jpg")
        st.divider()
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.text("Hello, My name is Kylle C. Nacionales, an 18 year old ICT student in Rizal Technological University. Currently we are tasked to create a website about ourselves and i don't mind sharing a bit about myself either, just something a bit about myself, what i like and what i do outside of school.")
        with right_column:
            st.image ("me.jpg")
        st.write("#")
        col1, col2 = st.columns([150,250])
        with col1:
            st.image ("Gaming.jpeg")
        with col2:
            st.text("first off one of my very hobbies, is pretty much just gaming, i use the name nico as my alias. currently my setup is around low-mid end depending on how you see it. i play a handful of games ranging from competitive to casual and story based games. im very much into horror or games that tackle very deep topics and are pretty bleak in their themes. Recently during christmas break i have been playing solo and coop with my friends, notable games like TmodLoader, The forest and Gmod for Coop. and i just finished the very recent Horror game released last year known as Amnesia the Bunker, Hands down one of my favorite games. ")
        col1, col2 = st.columns([150, 250])
        with col1:
            st.image("drums.jpg")
        with col2:
            st.text("I also like listening to music of various genres, most notably im into metal and that pretty much inspired me to pick up the drums. i'm not sure if i do want to play in a band yet since i would still consider myself fairly beginner. Mike Portnoy, Tomas Haake, II are just some example of Drumming Figures i look up to and lastly just a small slip but my top track atm is Nazareth by Sleep Token")
        col1, col2 = st.columns([150, 250])
        with col1:
            st.image("movies.png")
        with col2:
            st.text("Just recently i developed an interest for watching films from time to time, i usually enjoy deep films with a bit of mind bending experiences. Recently a series i have finished was Arcane along with a movie named Everything Everywhere All at Once. Pretty late to watch both but it was still an enjoyable experience. One of my favorite films has to be Eternal Sunshine of the Spotless Mind which is played by Jim Carrey which is notably one of his serious roles. ")
        st.write("#")
        st.text("Other stuff i like are Synthwave, Movies, Music, Games. I just find the theme of it very appealing like the bright neon lights, warm and nostalgic feeling it has and being futuristic at the same time. One of my favorite dish has to be sisig which i know some people know. i may not look all that talkative but all we need is just a common ground to stand on, i mostly just make friends through stuff im interested in.\n\n Currently my goal is to just be financially successful and live a comfortable life where i can offer a good amount of time to the stuff i'm interested in. and with that i'll plug in my socials to those who are interested.")
    with st.container():
        st.divider()
        st.subheader("My Socials and Others")
        col1, col2 = st.columns([1, 25])
        with col1:
            st.image("facebook.jpg")
        with col2:
            st.write("[My Facebook](https://www.facebook.com/kylle.nacionales/)")
        col1, col2 = st.columns([1, 25])
        with col1:
            st.image("steam.png")
        with col2:
            st.write("[My Steam](https://steamcommunity.com/id/NlKOlAI//)")
        col1, col2 = st.columns([1, 25])
        with col1:
            st.image("youtube.png")
        with col2:
            st.write("[Guide i used to create this Website](https://www.youtube.com/watch?v=VqgUkExPvLY)")