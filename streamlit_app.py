import streamlit as st 

# Function to add background image
def add_bg_from_local():
    bg_image = "https://s1.bwallpapers.com/wallpapers/2014/01/18/happy-valentines-day-wide_104144.jpg"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({bg_image});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()

# Function to autoplay background music (hidden)
def autoplay_music():
    music_file = "https://www.bensound.com/bensound-music/bensound-romantic.mp3"
    st.markdown(
        f"""
        <audio autoplay loop>
            <source src="{music_file}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

autoplay_music()

# Define Love Language Quiz Questions
questions = [
    ("How do you feel most loved?", [
        "Hearing kind and encouraging words", 
        "Receiving thoughtful gifts", 
        "Spending quality time together", 
        "Being physically close (hugs, kisses, etc.)", 
        "When they do something helpful for me"
    ]),
    ("What makes you happiest in a relationship?", [
        "Sweet compliments and appreciation",
        "Surprise presents that show they care",
        "Uninterrupted one-on-one time",
        "Holding hands, cuddling, or physical touch",
        "Acts of service like helping out when I'm busy"
    ]),
    ("If your partner forgot your birthday, what would upset you most?", [
        "They didn’t write me a heartfelt message",
        "They didn’t get me a thoughtful gift",
        "They didn’t spend time with me",
        "They didn’t hug or kiss me that day",
        "They didn’t help make the day easier for me"
    ]),
    ("How do you prefer to show love to others?", [
        "Writing heartfelt notes and compliments",
        "Giving meaningful gifts",
        "Planning special moments together",
        "Showing physical affection",
        "Helping with tasks and responsibilities"
    ]),
    ("What makes you feel closest to your partner?", [
        "Having deep, meaningful conversations",
        "Getting small surprises from them",
        "Spending the whole day together",
        "Being wrapped in their arms",
        "When they support me in practical ways"
    ]),
    ("When you’re feeling down, what helps the most?", [
        "Hearing encouraging words",
        "Getting a thoughtful surprise",
        "Having someone spend time with me",
        "Getting a comforting hug",
        "Having someone take care of things for me"
    ]),
    ("What’s the best way to end a perfect date?", [
        "A sweet message about how much they enjoyed it",
        "A surprise little gift to remember the moment",
        "Talking and laughing together for hours",
        "A long, warm hug or kiss",
        "Helping me feel relaxed and stress-free"
    ])
]

love_languages = ["Words of Affirmation", "Receiving Gifts", "Quality Time", "Physical Touch", "Acts of Service"]
scores = {lang: 0 for lang in love_languages}

# Streamlit UI
st.title("💞 💞 **VALE** 💕 💕")
st.subheader("What's Your Love Language?")
st.write("Discover your love language and get a personalized poem & relationship advice! ✨")

for i, (question, options) in enumerate(questions):
    answer = st.radio(question, options, key=f'q{i}')
    if answer:
        scores[love_languages[options.index(answer)]] += 1

if st.button("Find My Love Language 💌"):
    love_language = max(scores, key=scores.get)
    st.success(f"Your Love Language is: **{love_language}** 💖")
    
    # Static relationship advice
    advice = {
        "Words of Affirmation": "Express appreciation through words. Compliment and encourage your partner often! 📝💕",
        "Receiving Gifts": "Show love with thoughtful presents that reflect your partner’s interests. 🎁💝",
        "Quality Time": "Spend uninterrupted time together doing activities you both enjoy. ⏳💑",
        "Physical Touch": "Hug, hold hands, and show physical affection to make your partner feel loved. 🤗💞",
        "Acts of Service": "Do helpful things for your partner, like running errands or cooking a meal. 🏡💓"
    }
    
    poetry = {
        "Words of Affirmation": "Your words are stars that light my sky,\nA love so deep, it lifts me high.\nEach whisper echoes in my heart,\nA melody we’ll never part. 💖",
        "Receiving Gifts": "Wrapped in paper, or just a thought,\nThe love you give is never bought.\nA single rose, a gift so true,\nEvery token reminds me of you. 🎁🌹",
        "Quality Time": "With you, the world fades out of sight,\nEvery moment, pure delight.\nNo need for words, no need for rhyme,\nJust your presence, marking time. ⏳💑",
        "Physical Touch": "A touch so warm, a hug so tight,\nIn your embrace, all feels right. 🤗💞",
        "Acts of Service": "In deeds of love, your care is shown,\nA quiet way to make love known.\nThrough hands that help, through tasks you do,\nI feel the love that flows from you. 💖🏡"
    }
    
    st.subheader("💬 Relationship Advice for Your Love Language")
    st.write(advice[love_language])
    
    st.subheader("💌 A Love Poem Just for You")
    st.write(poetry[love_language])
