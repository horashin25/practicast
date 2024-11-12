import streamlit as st
st.write("hola mundo")
nombre=st.text_input("Nombre")
st.write("Hola como estas: ",nombre)


if st.button('Haz clic aquí'):
    st.write("Bienvenidos a Streamlit")
edad = st.slider("Selecciona tu edad", 0, 100, 25)
st.write("Tu edad es:", edad)
opciones = st.selectbox('¿Cuál es tu color favorito?', ['Rojo', 'Azul', 
'Verde'])
st.write(f'Has seleccionado {opciones}')
genero = st.radio('Elige tu género musical', ['Chicha', 'Cumbia', 'cuarteto'])
st.write(f'Has seleccionado: {genero}')
nombre = st.text_input('¿Cómo te llamas?')
st.write(f'Hola {nombre}!')

import datetime
fecha = st.date_input("Selecciona una fecha", datetime.date(2024, 1, 1))
st.write(f'La fecha seleccionada es: {fecha}')
mensaje = st.text_area("Escribe tu mensaje:")
st.write(f"Tu mensaje: {mensaje}")