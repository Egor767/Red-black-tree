from redblacktree import RedBlackTree
import matplotlib.pyplot as plt
import streamlit as st
import networkx as nx
import time

st.set_page_config(
    page_title="RedBlackTree",
)

session = st.session_state

if 'tree' not in session:
    session.tree = RedBlackTree()

if 'inserted_values' not in session:
    session.inserted_values = []

if 'session_iteration' not in session:
    session.session_iteration = 0

st.title('Red Black Tree')

sidebar = st.sidebar
sidebar.title('Настройки дерева')

# вставка чисел
sidebar.subheader('Вставка')
sidebar.text_input(label='Введите числа:', key='insert_field', label_visibility='collapsed')
def clear_insert_text():
    session.new_values = session.insert_field
    session["insert_field"] = ""
sidebar.button(label='Вставить', key='insert_button', on_click=clear_insert_text, use_container_width=True)


# удаление чисел
sidebar.subheader('Удаление')
sidebar.text_input(
    label='Введите числа:',
    key='values2delete',
    label_visibility='collapsed'
)
def clear_delete_text():
    session.deleting_values = session.values2delete
    session["values2delete"] = ""
sidebar.button(label='Удалить', key='delete_button', on_click=clear_delete_text, use_container_width=True)

sidebar.header('Настройки отображения')
figsize = sidebar.slider(
    label='Размер изображения',
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
    if correct_values:
        st.success(f'Успешно добавлено: {correct_values}')
    if wrong_values:
        st.warning(f'Не добавлено: {wrong_values}')

if session.delete_button:
    try:
        values2delete = [int(value) for value in 
            session.deleting_values.split()]
    except ValueError as e:
        values2delete = None
        st.error(f'Неправильный ввод: {e}')

    correct_values = []
    wrong_values = []
    for value in values2delete:
        try:
            session.tree.delete(value)
            session.inserted_values.remove(value)
            correct_values.append(value)
        except ValueError:
            wrong_values.append(value)
    if correct_values:
        st.success(f'Успешно удалено: {correct_values}')
    if wrong_values:
        st.warning(f'Не удалено: {wrong_values}')

if session.inserted_values:
    with st.spinner('Загрузка...'):
        time.sleep(2)
    st.subheader(f'Вставленные значения: {sorted(session.inserted_values)}')
    tree = session.tree
    g, pos, options = tree.realize()
    fig = plt.figure(figsize=[figsize]*2)
    plt.axis('off')
    nx.draw_networkx(g, pos, **options)
    st.pyplot(fig)