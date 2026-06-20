import streamlit as st
import matplotlib.pyplot as plt

# 1. 페이지 설정
st.set_page_config(
    page_title="단단한 숫자 보석, 소수 놀이터 💎",
    page_icon="💎",
    layout="centered"
)

# 코지 & 트렌디 감성 CSS 스타일링
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap');
    html, body, [data-testid="stWidgetLabel"] {
        font-family: 'Gamja+Flower', cursive !important;
    }
    .main-title {
        color: #4A90E2;
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
        background-color: #E8F4F8;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed #90CAF9;
        text-align: center;
        font-size: 1.4rem;
        color: #333333;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 상단 타이틀
st.markdown('<h1 class="main-title">💎 반짝반짝 소수 놀이터</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">더 이상 쪼갤 수 없는 특별한 숫자 보석을 찾아라!</p>', unsafe_allow_html=True)

# 3. 아이 맞춤형 개념 설명
st.markdown("""
    <div class="bubble-box">
        🎈 <b>"소수"</b>는 다른 숫자로 나누어지지 않는 아주 단단한 숫자에요!<br>
        아래 조절 버튼을 움직이며 어떤 숫자가 <b>반짝이는 보석(소수)</b>인지 찾아보세요.
    </div>
""", unsafe_allow_html=True)

# 4. 직관적인 숫자 슬라이더 (유치원 아이들이 다루기 좋은 2~20 범위)
number = st.slider(
    "👉 숫자를 바꿔보며 보석을 찾아보세요!",
    min_value=2,
    max_value=20,
    value=2,
    step=1
)

# 5. 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 약수 구하기 (아이들에게 시각적으로 보여주기 위함)
divisors = [i for i in range(1, number + 1) if number % i == 0]
is_number_prime = is_prime(number)

# 6. 동그라미 조각으로 시각화 (Matplotlib)
# 예: 6이면 2개씩 3줄, 혹은 약수의 형태로 묶이는 모습을 보여주면 좋지만,
# 유치원생에게는 '보석 개수'만큼 정렬되어 나오는 것이 직관적입니다.
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('off')

# 소수면 예쁜 하늘색 보석, 합성수면 부드러운 핑크색 조각
dot_color = '#4A90E2' if is_number_prime else '#FF8A8A'
marker_style = 'D' if is_number_prime else 'o' # 소수는 다이아몬드(D), 합성수는 동그라미(o)

# 가로로 숫자만큼 기호 그리기
for i in range(number):
    ax.scatter(i, 0, color=dot_color, s=500, marker=marker_style, edgecolor='white', linewidth=2)

ax.set_xlim(-0.5, max(number - 0.5, 4.5))
ax.set_ylim(-0.5, 0.5)
st.pyplot(fig)

# 7. 결과 피드백 & 연출
st.write("---")

if is_number_prime:
    # 소수일 때 (보석 팡팡!)
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color: #4A90E2;'>🎉 찾았다! {number}번은 단단한 보석 소수!</h2>
            <p style='font-size: 1.3rem; color: #555;'>1과 {number} 자기 자신으로만 나누어져요!</p>
        </div>
    """, unsafe_allow_html=True)
    st.balloons() # 풍선 효과
else:
    # 소수가 아닐 때 (나누어지는 수)
    st.markdown(f"""
        <div style='text-align: center;'>
            <h2 style='color: #FF8A8A;'>🍪 {number}번은 쪼개지는 부드러운 수!</h2>
            <p style='font-size: 1.3rem; color: #555;'>이 숫자는 <b>{', '.join(map(str, divisors[1:-1]))}</b> 등으로 이쁘게 나누어떨어져요.</p>
        </div>
    """, unsafe_allow_html=True)
