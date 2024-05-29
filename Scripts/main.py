from redblacktree import RedBlackTree
import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx
import time


session = st.session_state

if 'tree' not in session:
    session.tree = RedBlackTree()

if 'inserted_values' not in session:
    session.inserted_values = []

if 'session_iteration' not in session:
    session.session_iteration = 0

st.title('RedBlackTree')

sidebar = st.sidebar

# вставка чисел
sidebar.subheader('Вставка чисел')
sidebar.text_input(label='Введите числа:', key='insert_field', label_visibility='collapsed')
def clear_insert_text():
    session.new_values = session.insert_field
    session["insert_field"] = ""
sidebar.button(label='Вставить', key='insert_button', on_click=clear_insert_text, use_container_width=True)


figsize = sidebar.slider(
    label='Масштабирование',
    min_value=9,
    max_value=120
)

if session.insert_button:
    try:
        new_values = [int(value) for value in 
                      session.new_values.split()]
    except ValueError as e:
        new_values = None
        st.error(f'Неправильный ввод: {e}')

    correct_values = []
    wrong_values = []
    for value in new_values:
        try:
            session.tree.insert(value)
            session.inserted_values.append(value)
            correct_values.append(value)
        except ValueError:
            wrong_values.append(value)


if session.inserted_values:
    tree = session.tree
    g, pos, options = tree.realize()
    fig = plt.figure(figsize=[figsize]*2)
    plt.axis('off')
    nx.draw_networkx(g, pos, **options)
    st.pyplot(fig)

