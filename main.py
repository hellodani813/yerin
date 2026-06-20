import streamlit as st
import matplotlib.pyplot as plt

# 1. 페이지 설정
st.set_page_config(
    page_title="소수 놀이터",
    page_icon="🍬",
    layout="centered"
)

# 2. 타이틀
st.title("🍬 내 숫자는 어떻게 묶일까?")
st.write("숫자에 딱 맞게 묶어봐요! 안 묶이는 단단한 수가 '소수'에요 ⭐")
st.write("---")

# 3. 숫자 버튼 누르기
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

# 4. 숫자에 맞춤형으로 묶음 크기(방식) 결정하기
# 2로 나눠떨어지면 2개씩 묶고, 아니면 3으로 나눠보고, 둘 다 아니면 소수(일렬 배치)
if current_num % 2 == 0:
    bundle_size = 2
    room_title = f"🍏 {current_num}은 2개씩 예쁘게 묶여요!"
    is_prime = (current_num == 2) # 2는 2로 묶이지만 소수임
elif current_num % 3 == 0:
    bundle_size = 3
    room_title = f"🍊 {current_num}은 3개씩 예쁘게 묶여요!"
    is_prime = (current_num == 3) # 3은 3으로 묶이지만 소수임
else:
    bundle_size = 1 # 묶이지 않는 소수 (5, 7, 11, 13 등)
    room_title = f"💎 {current_num}은 안 묶이는 단단한 소수 보석!"
    is_prime = True

# 5. 결정된 방식대로 그림 그리기
fig, ax = plt.subplots(figsize=(6, 3))
ax.axis('off')
ax.set_title(room_title, fontsize=15, pad=15, color='#333333', weight='bold')

x_idx = 0
color = '#4E9F3D' if bundle_size == 2 else ('#D87040' if bundle_size == 3 else '#4A90E2')

if bundle_size > 1 and not is_prime:
    # 합성수: 예쁘게 묶이는 상자들과 알맹이 그리기
    bundles = current_num // bundle_size
    for b in range(bundles):
        # 묶음 주머니 테두리
        bundle_center_x = x_idx + (bundle_size - 1) / 2
        rect = plt.Circle((bundle_center_x, 0), radius=bundle_size*0.45, color=color, alpha=0.15, ec=color, lw=2.5, ls='--')
        ax.add_patch(rect)
        # 알맹이 동그라미
        for p in range(bundle_size):
            ax.scatter(x_idx, 0, color=color, s=400, zorder=3, edgecolor='white', lw=1.5)
            x_idx += 1
        x_idx += 0.8
else:
    # 소수(2,
