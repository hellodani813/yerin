import streamlit as st
import matplotlib.pyplot as plt

# 1. 페이지 설정 (코지 & 트렌디 캐주얼)
st.set_page_config(
    page_title="말랑말랑 묶음 놀이터 🍬",
    page_icon="🍬",
    layout="centered"
)

# 아이들 맞춤형 부드러운 폰트와 디자인 CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
    html, body, [data-testid="stWidgetLabel"] {
        font-family: 'Gamja+Flower', cursive !important;
    }
    .main-title {
        color: #FF6B6B;
        font-size: 2.8rem !important;
        text-align: center;
        margin-bottom: 5px;
    }
    .bubble-box {
        background-color: #FFF9E6;
        padding: 18px;
        border-radius: 15px;
        border: 2px dashed #FFAEBC;
        text-align: center;
        font-size: 1.4rem;
        color: #4A4A4A;
        margin-bottom: 25px;
    }
    .block-label {
        font-size: 1.3rem !important;
        font-weight: bold;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🍬 2랑 3으로 묶어봐요!</h1>', unsafe_allow_html=True)

st.markdown("""
    <div class="bubble-box">
        지정된 숫자가 <b>2개씩</b> 혹은 <b>3개씩</b> 예쁘게 묶이는지 확인해 봐요!<br>
        아무리 묶어도 <b>조각이 남는 단단한 수</b>가 바로 <b>'소수'</b>랍니다 ⭐
    </div>
""", unsafe_allow_html=True)

# 2. 버튼 클릭으로 숫자 선택하기 (유치원생 취향 저격 큼직한 버튼)
st.markdown("<p class='block-label'>👉 궁금한 숫자를 콕! 눌러보세요:</p>", unsafe_allow_html=True)
cols = st.columns(6)
numbers_to_show = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# 세션 상태(Session State)를 이용해 현재 선택된 숫자 기억하기
if 'chosen_num' not in st.session_state:
    st.session_state.chosen_num = 2

for idx, num in enumerate(numbers_to_show):
    with cols[idx % 6]:
        # 현재 선택된 숫자는 이모지를 붙여서 표시
        label = f"⭐ {num}" if st.session_state.chosen_num == num else f"{num}"
        if st.button(label, key=f"btn_{num}", use_container_width=True):
            st.session_state.chosen_num = num

current_num = st.session_state.chosen
