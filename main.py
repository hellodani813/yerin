import streamlit as st
import matplotlib.pyplot as plt

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="말랑말랑 묶음 놀이터 🍬",
    page_icon="🍬",
    layout="centered"
)

# 2. 상단 타이틀 및 가이드 (문자열 끊김 예방을 위해 간단하게 처리)
st.title("🍬 2랑 3으로 묶어봐요!")
st.subheader("도중에 조각이 남는 단단한 수가 바로 '소수'랍니다 ⭐")

st.write("---")

# 3. 버튼 클릭으로 숫자 선택하기
st.write("👉 궁금한 숫자를 콕! 눌러보세요:")
cols = st.columns(6)
numbers_to_show = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if 'chosen_num' not in st.session_state:
    st.session_state.chosen_num = 2

for idx, num in enumerate(numbers_to_show):
    with cols[idx % 6]:
        label = f"⭐ {num}" if st.session_state.chosen_num == num else f"{num}"
        if st.button(label, key=f"btn_{num}", use_container_width=True):
            st.session_state.chosen_num = num

current_num = st.session_state.chosen_num

# 에러가 나던 줄바꿈 f-string을 st.header로 안전하게 변경!
st.header(f"지금 선택한 숫자: {current_num}")

# 4. 2로 묶기 vs 3으로 묶기 시각화 (Matplotlib)
def draw_bundles(total, bundle_size, color, title):
    bundles = total // bundle_size
    remains = total % bundle_size
    
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    ax.set_title(title, fontsize=14, pad=10, color='#333333', weight='bold')
    
    x_idx = 0
    # 묶음 그리기
    for b in range(bundles):
        bundle_center_x = x_idx + (bundle_size - 1) / 2
        rect = plt.Circle((bundle_center_x, 0), radius=bundle_size*0.4, color=color, alpha=0.2, ec=color, lw=2, ls='--')
        ax.add_patch(rect)
        
        for p in range(bundle_size):
            ax.scatter(x_idx, 0, color=color, s=350, zorder=3, edgecolor='white', lw=1.5)
            x_idx += 1
        x_idx += 0.8
        
    # 남은 외톨이 조각들 그리기
    for r in range(remains):
        ax.scatter(x_idx, 0, color='#A8A8A8', s=350, marker='X' if total in [2, 3, 5, 7, 11, 13] else 'o', zorder=3)
        ax.text(x_idx, -0.3, "외톨이", ha='center', fontsize=9, color='#BF616A')
        x_idx += 1
        
    ax.set_xlim(-0.5, max(x_idx, 4))
    ax.set_ylim(-0.8, 0.8)
    return fig

# 화면에 두 개의 묶음 방 보여주기
view_col1, view_col2 = st.columns(2)

with view_col1:
    fig2 = draw_bundles(current_num, 2, '#4E9F3D', "🍏 2개씩 묶어보기")
    st.pyplot(fig2)

with view_col2:
    fig3 = draw_bundles(current_num, 3, '#D87040', "🍊 3개씩 묶어보기")
    st.pyplot(fig3)

# 5. 소수 판별 결과 출력 (여기도 안전한 구조로 변경)
is_prime = current_num in [2, 3, 5, 7, 11, 13]

st.write("---")
if is_prime:
    st.success(f"👑 {current_num}은(는) 멋진 '소수' 보석이에요!")
    st.write("2개씩 혹은 3개씩 묶어도 딱 나눠떨어지지 않고 외톨이 조각이 남는 단단한 수랍니다.")
    st.balloons()
else:
    st.info(f"🍫 {current_num}은(는) 부드럽게 묶이는 수에요!")
    st.write("2개나 3개씩 예쁜 세트로 묶여서 외톨이가 생
