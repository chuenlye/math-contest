import re
import glob

import streamlit as st


st.set_page_config(
    page_title="Sapix Math Contest",
    page_icon=":sunglasses:",
    # layout: centered or wide
    layout="centered",
    initial_sidebar_state="expanded",
)

latex_files = glob.glob("./data/*.latex")
chapters = [ re.search("math(.+?).latex", x).group(1) for x in latex_files ]

chapter = st.sidebar.selectbox("Chapters", options=chapters)

# chapter like "4-32"
def verify_all_questions(chapter):
    with open("./data/math{}.latex".format(chapter)) as f:
        for x in f.readlines():
            st.latex(x)

#verify_all_questions("4-33")

st.title(f"計算力コンテスト { chapter } :sunglasses:")
st.write("----")

# using variable is NG. now use session instead.
#gameover = False
if 'gameover' not in st.session_state:
    st.session_state['gameover'] = False

with open("./data/math{}.latex".format(chapter)) as f1, open("./data/math{}-answer.txt".format(chapter)) as f2:
    all_questions = f1.readlines()
    all_answers = f2.readlines()
    placeholder = st.empty()
    for x in range(len(all_questions)):
        if st.session_state["gameover"]:
            break
        with placeholder.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                if x > 0:
                    st.success("問題 {} 成功！頑張れ！ :smile:".format(x))
                st.subheader("問題 {}".format(x+1))
                st.latex(all_questions[x])
                st.write("----")
                st.subheader("答えは")
                # random string key is NG. Why ?
                answer = st.text_input("", key=x)
                if answer.strip() == "":
                    st.stop()
                elif answer.strip() != all_answers[x].strip():
                    st.session_state["gameover"] = True
                    break
                if x == len(all_questions) - 1:
                    st.balloons()
                    st.header("仙人、おめでとうございます!❤️")
                    st.header("🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕🍕")
                    st.header("🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀")
                    st.header("👍👍👍👍👍👍👏👏👏👏👏👏👏👏")
        placeholder.empty()
    st.write("----")
    st.header(":cry: :cry: GAME OVER! :cry: :cry: まだね！ :sunglasses: :sunglasses:")

