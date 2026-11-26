
import streamlit as st

# Настройки на приложението
st.set_page_config(
    page_title="Моята библиотека",
    page_icon="📚",
    layout="centered"
)

# Заглавие
st.title("📚 Моята библиотека")
st.write("Добре дошли в приложението за управление на книги!")

# Създаване на списък с книги
if "books" not in st.session_state:
    st.session_state.books = [
        "Хари Потър",
        "Малкият принц",
        "Хобит",
        "1984",
        "Под игото"
    ]

# Добавяне на книга
st.header("➕ Добавяне на книга")

new_book = st.text_input("Въведете заглавие на книга:")

if st.button("Добави книга"):
    if new_book.strip():
        if new_book.strip() not in st.session_state.books:
            st.session_state.books.append(new_book.strip())
            st.success("Книгата е добавена успешно!")
            st.rerun()
        else:
            st.warning("Тази книга вече съществува!")
    else:
        st.warning("Моля, въведете заглавие.")

st.divider()

# Показване на книгите
st.header("📖 Налични книги")

if st.session_state.books:
    st.write(f"Общо книги: {len(st.session_state.books)}")

    for index, book in enumerate(st.session_state.books, start=1):
        st.write(f"{index}. 📘 {book}")
else:
    st.info("Библиотеката е празна.")

st.divider()

# Изтриване на книга
st.header("🗑️ Изтриване на книга")

if st.session_state.books:
    selected_book = st.selectbox(
        "Изберете книга:",
        st.session_state.books
    )

    if st.button("Изтрий избраната книга"):
        st.session_state.books.remove(selected_book)
        st.success("Книгата е изтрита!")
        st.rerun()
else:
    st.write("Няма налични книги за изтриване.")

st.divider()

# Допълнителна информация
st.caption("📚 Приложение за управление на лична библиотека.")


