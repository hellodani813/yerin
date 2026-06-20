import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="소수 놀이터", page_icon="🍬", layout="centered")
st.title("🍬 2랑 3으로 묶어봐요!")
st.write("외톨이가 남는 수가 '소수'랍니다 ⭐")
st.write("---")

cols = st.columns(6)
numbers_to_show = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if 'chosen_num' not in st.session_state:
    st.session_state.chosen_num = 2

for idx, num in enumerate(numbers_to_show):
    with cols[idx % 6]:
        label = f"⭐ {num}" if st.session_state.chosen_num == num else f"{num}"
        if st.button(label, key=f"b_{num}", use_container_width=True):
            st.session_state.chosen_num = num

current_num = st.session_state.chosen_num
st.header(f"선택한 숫자: {current_num}")

if current_num % 2 == 0:
    bundle_size, room_title, is_prime = 2, f"🍏 {current_num}(은)는 2개씩 묶여요!", (current_num == 2)
elif current_num % 3 == 0:
    bundle_size, room_title, is_prime = 3, f"🍊 {current_num}(은)는 3개씩 묶여요!", (current_num == 3)
else:
    bundle_size, room_title, is_prime = 1, f"💎 {current_num}(은)는 안 묶이는 소수 보석!", True

fig, ax = plt.subplots(figsize=(6, 3))
ax.axis('off')
ax.set_title(room_title, fontsize=15, pad=15, weight='bold')

x_idx = 0
color = '#4E9F3D' if bundle_size == 2 else ('#D87040' if bundle_size == 3 else '#4A90E2')

if bundle_size > 1 and not is_prime:
    bundles = current_num // bundle_size
    for b in range(bundles):
        bundle_center_x = x_idx + (bundle_size - 1) / 2
        rect = plt.Circle((bundle_center_x, 0), radius=bundle_size*0.45, color=color, alpha=0.15, ec=color, lw=2.5, ls='--')
        ax.add_patch(rect)
        for p in range(bundle_size):
            ax.plot(x_idx, 0, marker='o', color=color, ms=18)
            x_idx += 1
        x_idx += 0.8
else:
    for p in range(current_num):
        m = 'D' if is_prime else 'o'
        ax.plot(x_idx, 0, marker=m, color=color, ms=18)
        x_idx += 1.0

ax.set_xlim(-0.7, max(x_idx, 4.5))
ax.set_ylim(-1.0, 1.0)
st.pyplot(fig)

st.write("---")
if is_prime:
    st.success(f"👑 {current_num}은 소수 보석!")
    st.balloons()
else:
    st.info(f"🍫 {current_num}은 묶이는 수!")
