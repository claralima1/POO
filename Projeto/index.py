from templates.ManterCliente import ManterClienteUI
from templates.ManterProduto import ManterProdutoUI
from templates.ManterCategoria import ManterCategoria

import streamlit as st

class IndexUI:
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Categoria", "Manter Produtos", "Reajustar Preços"])
        if op == "Manter Clientes": ManterClienteUI.main()
        if op == "Manter Categoria": ManterCategoria.main()
        if op == "Manter Produtos": ManterProdutoUI.main()
        #if op == "Reajustar Preços": ReajustarPrecosUI.main()

    def sidebar():
        IndexUI.menu_admin()
    
    def main():
        IndexUI.sidebar()
        
IndexUI.main()