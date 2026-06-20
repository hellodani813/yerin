import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. 웹 앱 페이지 기본 설정 (코지 & 트렌디한 타이틀)
st.set_page_config(
    page_title="말랑말랑 소수 놀이터 🍩",
    page_icon="🍩",
    layout="centered"
)

# 커스텀 CSS로 부드럽고 따뜻한 폰트와 배경 감성 한 스푼 추가 (에러 수정 완료!)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
    html, body, [data-testid="stWidgetLabel"] {
        font-family: 'Gamja+Flower', cursive !important;
    }
    .main-title {
        color: #FF8A8A;
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        color: #6C5B7B;
        font-size: 1.5rem !important;
        text-align: center;
        margin-bottom: 30px;
    }
    .bubble-box {
        background-color: #FFF5E4;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #FFC4C4;
        text-align: center;
        font-size: 1.4rem;
        color: #4A4A4A;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 상단 타이틀 영역
st.markdown('<h1 class="main-title">🍩 말랑말랑 소수 놀이터</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">도넛을 쪼개며 재미있는 소수 나라로 떠나볼까요?</p>', unsafe_allow_html=True)

# 3. 아이들을 위한 친근한 설명창
st.markdown("""
    <div class="bubble-box">
        🎈 <b>"소수"</b>는 한 개보다 작은 조각을 말해요!<br>
        아래의 동그란 조절 버튼을 좌우로 움직여서 도넛을 나누어 보세요.
    </div>
""", unsafe_allow_html=True)

# 4. 직관적인 조작을 위한 슬라이더 (0.0부터 1.0까지 0.1씩 변동)
decimal_value = st.slider(
    "👉 도넛을 얼마나 먹을까요? 조절해 보세요!",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.1,
    format="%.1f"
)

# 5. 시각화를 위한 원형 차트 (도넛 모양) 그리기
colors = ['#FF8A8A', '#F9F1F0'] 

fig, ax = plt.subplots(figsize=(6, 6))
sizes = [decimal_value, 1.0 - decimal_value]

# 값이 0이거나 1일 때의 예외 처리로 깔끔한 원 그리기
if decimal_value == 0:
    wedges, texts = ax.pie([1], colors=['#F9F1F0'], startangle=90, counterclock=False)
elif decimal_value == 1.0:
    wedges, texts = ax.pie([1], colors=['#FF8A8A'], startangle=90, counterclock=False)
else:
    wedges, texts = ax.pie(sizes, colors=colors, startangle=90, counterclock=False, 
                           wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))

ax.axis('equal')  
fig.patch.set_facecolor('#FFFFFF') 

# 스트림릿에 도넛 그래프 보여주기
st.pyplot(fig)

# 6. 현재 상태를 숫자가 아닌 감성적인 텍스트와 이모지로 표현
st.write("---")
col1, col2 = st.columns(2)

with col1:
    st.metric(label="✨ 지금 내 도넛 크기는?", value=f"{decimal_value}")

with col2:
    if decimal_value == 0.0:
        message = "도넛이 아직 접시에 없어요! 🍽️"
    elif decimal_value <= 0.3:
        message = "아기 새만큼 조금 한 조각! 🐣"
    elif decimal_value <= 0.6:
        message = "사이좋게 절반만큼 가졌어요! 🤝"
    elif decimal_value <= 0.9:
        message = "우와, 정말 커다란 조각이에요! 🦖"
    else:
        message = "와 함냐함냐! 도넛 한 개 통째로 다 내꺼! 🍩🎉"
        
    st.markdown(f"<div style='font-size: 1.5rem; padding-top: 15px; color: #6C5B7B; text-align: center;'><b>{message}</b></div>", unsafe_allow_html=True)

# 축하 효과 (1.0 완전한 한 개가 되었을 때 풍선 팡팡!)
if decimal_value == 1.0:
    st.balloons()
