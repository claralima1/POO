import streamlit as st
import pandas as pd
from view import View
import time

class ManterCategoria:
    def main():
        st.header("Categoria")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoria.listar()
        with tab2: ManterCategoria.inserir()
        with tab3: ManterCategoria.atualizar()
        with tab4: ManterCategoria.excluir()

    def listar():
        categorias = View.listar_categoria()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            dic = []
            for categoria in categorias: dic.append(categoria.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)
    
    def inserir():
        desc = st.text_input("Informe a Categoria")
        if st.button("Inserir"):
            View.inserir_categoria(desc)
            st.success("Categoria inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        categorias = View.listar_categoria()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else: 
            op = st.selectbox("Atualização de Categoria", categorias)
            desc = st.text_input("Informe a nova categoria", op.get_desc())
            if st.button("Atualizar"):
                id = op.get_id()
                View.atualizar_categoria(id, desc)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        categorias = View.listar_categoria()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categorias)
            if st.button("Excluir"):
                id = op.get_id()
                View.excluir_categoria(id)
                st.success("Categoria Excluída com sucesso")
                time.sleep(2)
                st.rerun()