
import streamlit as st
from groq import Groq

# CONFIG
client = Groq(
    api_key="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"
)

st.set_page_config(
    page_title="SmartStudy AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 SmartStudy AI")
st.caption("Dashboard Pembelajaran Berbasis LLM")

# SIDEBAR
menu = st.sidebar.radio(
    "Pilih Fitur",
    [
        "Ringkasan Materi",
        "Flashcard",
        "Chat AI"
    ]
)

# RINGKASAN
if menu == "Ringkasan Materi":

    st.header("📄 Ringkasan Materi")

    materi = st.text_area(
        "Masukkan materi yang ingin diringkas",
        height=250
    )

    if st.button("Buat Ringkasan"):

        if materi:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"Ringkas materi berikut dalam poin-poin:\n\n{materi}"
                    }
                ]
            )

            st.success("Ringkasan berhasil dibuat")

            st.write(
                response.choices[0].message.content
            )
# FLASHCARD
elif menu == "Flashcard":

    st.header("🧠 Flashcard Otomatis")

    materi = st.text_area(
        "Masukkan materi",
        height=250
    )

    if st.button("Generate Flashcard"):

        if materi:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Buatkan 10 flashcard.

                        Format:
                        Q:
                        A:

                        Materi:
                        {materi}
                        """
                    }
                ]
            )

            st.write(
                response.choices[0].message.content
            )
# CHATBOT
elif menu == "Chat AI":
    st.header("💬 Chat dengan AI")
    pertanyaan = st.text_area(
        "Tulis pertanyaan"
    )

    if st.button("Kirim"):
        if pertanyaan:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": pertanyaan
                    }
                ]
            )

            st.write(
                response.choices[0].message.content
            )
