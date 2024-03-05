import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def main():
    st.title('Bike Sharing')
    st.sidebar.title("Bike Sharing Visualization")
    tabs = st.sidebar.radio("Menu", ["Data Wrangling","Pertanyaan 1", "Pertanyaan 2"])
    
    if tabs == "Data Wrangling":
        st.subheader('Data Hasil Preprocessing Daily Bike Sharing')
        file_path_day = "C:/Users/LENOVO/Documents/assignment/data/day_df.csv"
        day_data = pd.read_csv(file_path_day)

        st.write("Jumlah Data:", day_data.shape[0])
        st.write("Jumlah Data Null:", day_data.isna().sum().sum())
        st.write("Jumlah Data Duplikat:", day_data.duplicated().sum())

        st.write(day_data)

        st.subheader('Data Hasil Preprocessing Hourly Bike Sharing')
        file_path_hasil = "C:/Users/LENOVO/Documents/assignment/data/hour_df.csv"
        hour_data = pd.read_csv(file_path_hasil)

        st.write("Jumlah Data:", hour_data.shape[0])
        st.write("Jumlah Data Null:", hour_data.isna().sum().sum())
        st.write("Jumlah Data Duplikat:", hour_data.duplicated().sum())

        st.write(hour_data)
    
    elif tabs == "Pertanyaan 1":
        st.subheader("Bagaimana pola trend penyewaan sepeda setiap bulannya?")
        # Data preparation
        day_df = pd.read_csv("C:/Users/LENOVO/Documents/assignment/data/day_df.csv")
        perbulan = day_df.groupby(by=["mnth","yr"]).agg({"cnt": "sum"}).reset_index()

        # Streamlit app
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=perbulan, x="mnth", y="cnt", hue="yr", palette="viridis", marker="o")

        plt.ylabel("Jumlah")
        plt.title("Jumlah Penyewaan Sepeda Periode Bulan dan Tahun")
        plt.legend(title="Tahun", loc="upper right")
        plt.xticks(ticks=perbulan["mnth"], labels=perbulan["mnth"])
        plt.tight_layout()

        st.pyplot(plt)

        # Ganti kode ini dengan logika pengambilan data sesuai kebutuhan Anda
        st.subheader("Bagaimana pola trend penyewaan sepeda setiap jamnya?")
        hour_df = pd.read_csv("C:/Users/LENOVO/Documents/assignment/data/hour_df.csv")
        perjam = hour_df.groupby(by=["hr","yr"]).agg({"cnt": "sum"}).reset_index()
            
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=perjam, x="hr", y="cnt", hue="yr", palette="viridis", marker="o")
        plt.ylabel("Jumlah")
        plt.title("Jumlah Penyewaan Sepeda Periode Jam dan Tahun")
        plt.legend(title="Tahun", loc="upper right")
        plt.xticks(ticks=perjam["hr"], labels=perjam["hr"])
        plt.tight_layout()
        st.pyplot(plt)


    elif tabs == "Pertanyaan 2":
        st.subheader("Bagaimana pola trend penyewaan sepeda setiap bulannya?")
        day_df = pd.read_csv("C:/Users/LENOVO/Documents/assignment/data/day_df.csv")
        season_day = day_df.groupby(by=["season","yr"]).agg({"cnt": "sum"}).reset_index()

        plt.figure(figsize=(10, 6))
        sns.barplot(data=season_day, x="season", y="cnt", hue="yr", palette="viridis")
        plt.ylabel("Jumlah")
        plt.title("Jumlah Penyewaan Sepeda Berdasarkan Musim")
        plt.legend(title="Tahun", loc="upper right")
        plt.tight_layout()
        st.pyplot(plt)


if __name__ == "__main__":
    main()



