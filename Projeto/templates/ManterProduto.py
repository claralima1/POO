import streamlit as st
import pandas as pd
from view import View
import time

class ManterProdutoUI:
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar","Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()
    
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
            st.sucess("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()
    
    def atualizar():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos)
            desc = st.text_input("Informe o novo produto", op.get_desc())
            preco = st.text_input("Informe o valor", op.get_preco())
            estoque = st.text_input("Informe a quantidade no estoque", op.get_estoque)
            if  st.button("Atualizar"):
                id = op.get_id()
                View.atualizar_produtos(id, desc, preco, estoque)
                st.suucess("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produto", produtos)
            if st.button("Excluir"):
                id = op.get_id()
                View.excluir_produto(id)
                st.sucess("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()

