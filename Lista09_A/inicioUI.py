import streamlit as st
from Q1 import Equacao

class InicioUI:
    def main():
        st.header("Equação do II Grau: y = ax**2+bx+c")
        a = st.text_input("A")
        b = st.text_input("B")
        c = st.text_input("C")
        if st.button("Calcular"):
            e = Equacao(float(a), float(b), float(c))
            st.write(e)
            st.write(f'Delta: {e.delta()}')
            st.write(f'Y: {e.Y()}')
