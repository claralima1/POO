import streamlit as st
import pandas as pd
from view import View

class ManterProduto:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar"],["Inserir"], ["Atualizar", "Excluir"])
        with tab1: ManterProduto.listar()
        with tab2: ManterProduto.inserir()
        with tab3: ManterProduto.atualizar()
        with tab4: ManterProduto.excluir()
    
    def listar():
        produtos = []
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for p in produtos: dic.append(p.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        desc = st.text_input("Informe o Produto")
        preco = st.text_input("Informe o preço")
        estoque = st.text_input("Informe a quntidade")
        if st.button("Inserir"):
            View.inserir_produtos(desc, preco, estoque)
