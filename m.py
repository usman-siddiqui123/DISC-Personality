import streamlit as st





col1, col2 = st.columns([1, 6]) 

with col1:
    st.image("DISC LOGO.png", width=80)  

with col2:
    st.markdown("""
    <div style='line-height: 1.3;'>
        <h4>DISC - (Dominance, Influence, Steadiness,Conscientiousness)</h4>
        <h3 style='margin-top:0; margin-left=80px;'>Personality Quiz:</h3>
    </div>
    """, unsafe_allow_html=True)

def run_quiz():
    questions = [
        {"question": "When I hear from a college coach, I want them to:", "options": [
            "Be direct and tell me where I stand. (D)",
            "Make it exciting and energetic. (I)",
            "Be friendly, genuine, and take their time. (S)",
            "Provide all the info I need to make a smart decision. (C)"
        ]},
        {"question": "The thing that matters most in a program is:", "options": [
            "How competitive and successful it is. (D)",
            "The vibe, relationships, and culture. (I)",
            "Feeling like I belong and will be supported. (S)",
            "The structure, development plan, and academic strength. (C)"
        ]},
        {"question": "When a coach visits or calls me, I prefer they:", "options": [
            "Cut to the chase and talk about what they can offer me. (D)",
            "Connect with me and make the conversation fun. (I)",
            "Ask about me and show they care about more than just sports. (S)",
            "Come prepared and explain everything clearly. (C)"
        ]},
        {"question": "I usually make decisions by:", "options": [
            "Trusting my gut and taking action fast. (D)",
            "Talking it out with others and going with what feels right. (I)",
            "Taking time to think and talk with my family. (S)",
            "Doing research and comparing all the options. (C)"
        ]},
        {"question": "In conversations with coaches, I respond best when they:", "options": [
            "Speak confidently and set clear expectations. (D)",
            "Joke around, smile, and keep it real. (I)",
            "Listen carefully and don't rush me. (S)",
            "Are professional, thoughtful, and organized. (C)"
        ]},
        {"question": "When visiting a campus, I care most about:", "options": [
            "Seeing how serious and competitive the team is. (D)",
            "Meeting players and feeling the energy. (I)",
            "Feeling like I'd be part of a close-knit team. (S)",
            "Getting a full breakdown of facilities, academics, and the daily schedule. (C)"
        ]},
        {"question": "The kind of coach I respond to best is:", "options": [
            "Strong, driven, and holds people accountable. (D)",
            "High-energy, positive, and fun to be around. (I)",
            "Supportive, calm, and approachable. (S)",
            "Knowledgeable, methodical, and well-prepared. (C)"
        ]},
        {"question": "When I feel pressure in the recruiting process, I:", "options": [
            "Push through and make quick decisions. (D)",
            "Stay upbeat and talk to people I trust. (I)",
            "Get a little quiet and need time to process. (S)",
            "Slow down and try to organize everything. (C)"
        ]},
        {"question": "I like coaches who:", "options": [
            "Are confident and challenge me to level up. (D)",
            "Are personable and make things fun. (I)",
            "Are steady, loyal, and consistent. (S)",
            "Are structured, smart, and precise. (C)"
        ]},
        {"question": "When it comes to choosing a school, I am:", "options": [
            "Focused on winning and advancing to the next level. (D)",
            "Looking for a team and experience I'll enjoy. (I)",
            "Wanting a place that feels like family. (S)",
            "Analyzing what will set me up long-term, both in and out of sports. (C)"
        ]}
    ]

  

    # st.image("DISC LOGO.png", width=150)
    # st.title("DISC - (Dominance, Influence, Steadiness, Conscientiousness) Personality Quiz:")



    score = {"D": 0, "I": 0, "S": 0, "C": 0}
    full_names = {
        "D": "Dominance",
        "I": "Influence",
        "S": "Steadiness",
        "C": "Conscientiousness"
    }

    for i, q in enumerate(questions):
        st.subheader(f"Q{i+1}: {q['question']}")
        choice = st.radio("", q['options'], key=i)
        if choice:
            selected_letter = choice.split(" ")[-1].strip("()")
            score[selected_letter] += 1

    if st.button("Submit"):
        st.markdown("---")
        st.subheader("Result Summary")

        sorted_scores = sorted(score.items(), key=lambda x: x[1], reverse=True)

        for letter, val in sorted_scores:
            if val >= 7:
                level = "High"
            elif val >= 3:
                level = "Moderate"
            else:
                level = "Low"
            st.write(f"**{full_names[letter]}**: {val} points - {level}")

        top_letter = sorted_scores[0][0]
        top_trait = full_names[top_letter]
        top_level = "High" if sorted_scores[0][1] >= 7 else "Moderate" if sorted_scores[0][1] >= 3 else "Low"
        st.success(f"You are: **{top_trait}** - {top_level}")

# Run the quiz
run_quiz()
