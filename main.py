import streamlit as st
import matplotlib.pyplot as plt

# 1. 페이지 설정
st.set_page_config(
    page_title="소수 놀이터",
    page_icon="🍬",
    layout="centered"
)

# 2. 타이틀
st.title("🍬 2랑 3으로 묶어봐요!")
st.write("외톨이가 남는 수가 '소수'랍니다 ⭐")
st.write("---")

# 3. 숫자 버튼 생성
st.write("👉 숫자를 눌러보세요:")
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
st.header(f"선택한 숫자: {current_num}")

# 4. 묶음 그리기 함수
def draw_bundles(total, bundle_size, color, title):
    bundles = total // bundle_size
    remains = total % bundle_size
    
    fig, ax = plt.subplots(figsize=(5, 2.5))
    ax.axis('off')
    ax.set_title(title, fontsize=14, pad=10, color='#333333', weight='bold')
    
    x_idx = 0
    for b in range(bundles):
        bundle_center_x = x_idx + (bundle_size - 1) / 2
        rect = plt.Circle((bundle_center_x, 0), radius=bundle_size*0.4, color=color, alpha=0.2, ec=color, lw=2, ls='--')
        ax.add_patch(rect)
        
        for p in range(bundle_size):
            ax.scatter(x_idx, 0, color=color, s=350, zorder=3, edgecolor='white', lw=1.5)
            x_idx += 1
        x_idx += 0.8
        
    for r in range(remains):
        ax.scatter(x_idx, 0, color='#A8A8A8', s=350, marker='X' if total in [2, 3, 5, 7, 11, 13] else 'o', zorder=3)
        ax.text(x_idx, -0.3, "외톨이", ha='center', fontsize=9, color='#BF616A')
        x_idx += 1
        
    ax.set_xlim(-0.5, max(x_idx, 4))
    ax.set_ylim(-0.8, 0.8)
    return fig

# 두 개의 방 보여주기
view_col1, view_col2 = st.columns(2)

with view_col1:
    fig2 = draw_bundles(current_num, 2, '#4E9F3D', "🍏 2개씩 묶기")
    st.pyplot(fig2)

with view_col2:
    fig3 = draw_bundles(current_num, 3, '#D87040', "🍊 3개씩 묶기")
    st.pyplot(fig3)

# 5. 소수 판별 결과 (줄바꿈 오류 방지를 위해 문장을 완전히 축소)
is_prime = current_num in [2, 3, 5, 7, 11, 13]
st.write("---")

if is_prime:
    st.success(f"👑 {current_num}은 소수 보석!")
    st.balloons()
else:
    st.info(f"🍫 {current_num}은 묶이는 수!")
