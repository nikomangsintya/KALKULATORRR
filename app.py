import streamlit as st
import pandas as pd

st.title("🎓 Kalkulator FPB dan KPK")
st.write("Menggunakan Algoritma Euclid")

def hitung_fpb(a, b):
    langkah = []

    while b != 0:
        q = a // b
        r = a % b

        langkah.append([a, b, q, r])

        a, b = b, r

    return a, langkah

a = st.number_input("Masukkan bilangan pertama", step=1)
b = st.number_input("Masukkan bilangan kedua", step=1)

if st.button("Hitung"):

    fpb, langkah = hitung_fpb(int(a), int(b))

    kpk = abs(int(a) * int(b)) // fpb if fpb != 0 else 0

    st.success(f"FPB = {fpb}")
    st.success(f"KPK = {kpk}")

    st.subheader("Langkah Algoritma Euclid")

    df = pd.DataFrame(
        langkah,
        columns=[
            "Bilangan Pertama",
            "Bilangan Kedua",
            "Hasil Bagi",
            "Sisa"
        ]
    )

    st.table(df)
