import streamlit as st
import pandas as pd
import time

from view import View

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    
    def listar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o número de telefone")
        #senha = st.text_input("Informe a senha")
        if st.button("Inserir"):
            View.cliente_inserir(nome, email, fone)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email =  st.text_input("Informe um novo email", op.get_email())
            fone = st.text_input("Informe um novo fone")
            if st.button("Atualizar"):
                id= op.get_id()
                View.cliente_atualizar(id, nome, email, fone)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    
    def excluir():
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                View.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
                
       