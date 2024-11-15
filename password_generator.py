import streamlit as st
import random

betuk = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

szamok = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

spec_karakterek = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', 
                   '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', 
                   ',', '<', '.', '>', '/', '?', '`', '~']

st.write("Szia, ez egy jelszo generator!")

betuk_sz = st.slider("Hany betubol alljon a jelszo?\n")
szamok_sz = st.slider("Hany szambol alljon a jelszo?\n")
spec_karakterek_sz = st.slider("Hany specialis karakterbol alljon a jelszo?\n")

jelszo = []

for i in random.sample(betuk, betuk_sz):
    jelszo.append(i)

for i in random.sample(szamok, szamok_sz):
    jelszo.append(i)
    
for i in random.sample(spec_karakterek, spec_karakterek_sz):
    jelszo.append(i)
    
random.shuffle(jelszo)
st.write(f"A jelszavad: {"".join(jelszo)}")