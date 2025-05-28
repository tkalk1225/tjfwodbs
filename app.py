
import streamlit as st
from simulation import simulate_multi_species
import matplotlib.pyplot as plt

st.title("tjfwodbs: 세균 증식 시뮬레이션")

species_count = st.slider("세균 종 수", 1, 3, 2)
generations = st.slider("세대 수", 10, 50, 25)

params = []
for i in range(species_count):
    st.subheader(f"세균 {i+1}")
    name = st.text_input(f"이름 (세균 {i+1})", f"Bacteria_{i+1}", key=f"name_{i}")
    N0 = st.number_input(f"초기 개체 수", value=100, key=f"N0_{i}")
    rate = st.slider("증식 배율", 0.5, 2.0, 1.0, key=f"rate_{i}")
    uv_kill = st.slider("자외선 치사율", 0.0, 1.0, 0.3, key=f"uv_{i}")
    phage_kill = st.slider("파지 치사율", 0.0, 1.0, 0.4, key=f"phage_{i}")
    resistance_rate = st.slider("내성 증가 속도", 0.0, 0.2, 0.05, key=f"resist_{i}")
    params.append((name, N0, rate, uv_kill, phage_kill, resistance_rate))

if st.button("시뮬레이션 실행"):
    history = simulate_multi_species(params, generations)
    st.subheader("시뮬레이션 결과")
    for name, values in history.items():
        st.line_chart(values)
