from converter_gregorian import GregorianConverter
from JDtoJadwalSolat import jadwal_solat
import streamlit as st

st.set_page_config(
    page_title="Date Converter",
    page_icon="👋",
)

st.title("Jadwal Solat")
st.markdown("### Isi kolom berikut lalu masukan klik cari")

"""
input :
lattitude (L),
logitude (B),
time_zone (Z),
Ketinggian lokasi (H),
Tetapan ashar (KA=1 default value),
JD_local based on L & B.
"""

bulan_greg = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4, "Mei": 5, "Juni": 6,
    "Juli": 7, "Agustus": 8, "September": 9, "Oktober": 10, "November": 11, "Desember": 12
}
bulan_greg_reverse = {v: k for k, v in bulan_greg.items()} 

with st.form("form_input"):
    st.write("Isi form berikut ini")
    Lattitude = st.number_input("Masukan Lattitude", value=-7.9839)
    Longitude = st.number_input("Masukan Longitude", value=112.6214)
    Timezone = st.number_input("Masukan Timezone", value=+7.0, step=0.15, min_value=-12., max_value=14.)
    Ketinggian = st.number_input("Masukan Ketinggian sekarang (m)", value=500)

    hari = st.number_input("Masukan tanggal:", value=1, min_value=1, max_value=31, key="hari_greg_jd")
    bulan = st.selectbox("Pilih bulan:", list(bulan_greg.keys()), key="bulan_greg_jd")
    tahun = st.number_input("Masukan tahun:", value=2025, min_value=-4713, max_value=2500, key="tahun_greg_jd")
    submit_form = st.form_submit_button("Cari")


if submit_form:
    bulan_angka = bulan_greg[bulan]
    try:
        jd_lokal = GregorianConverter(year=tahun, month=bulan_angka, day=hari).to_JD()
        st.success(f"Sukses")

        hasil = jadwal_solat(jd_lokal, Lattitude, Longitude, Timezone, altitude=Ketinggian)

        st.write("### Jadwal Solat")
        for nama, jam in hasil.items():
            st.markdown(f"**{nama}**: {jam}")

    except ValueError as e:
        st.error(f"Error: {e}")


