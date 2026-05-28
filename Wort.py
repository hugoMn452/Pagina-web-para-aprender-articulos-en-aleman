import streamlit as st
import pandas as  pd
import random

from streamlit.runtime.state import session_state

Lista9 = ['die Wohnung', 'das Hochhaus', 'die WG', 'das Apartment', 'das Reihenhaus', 'der Raum', 'das Bad', 'die Dusche',
            'der Flur', 'die Küche', 'das Schlafzimmer', 'das Wohnzimmer', 'das Kinderzimmer', 'der Balkon', 'die Terrasse', 'der Garten', 'die Treppe', 'die Tür', 'die Decke', 'das Erdgeschoss', 'der Stock', 'die Lage', 'das Zentrum', 'der Blick', 'die Möbel', 'das Gerät',
            'die Lampe', 'das Licht', 'die Pflanze', 'das Regal', 'der Schrank', 'der Schreibtisch', 'der Sessel', 'das Sofa', 'der Stuhl', 'der Tisch', 'der Teppich', 'das Bett', 'der Fernseher', 'das Herd', 'die Kaffemaschine', 'der Kühlschrank', 'die Spülmaschine', 'die Waschmaschine', 'die Anzeige', 'der Vertrag', 'die Miete', 'der Vermieter',
            'der Umzug', 'die Feier', 'die Blume', 'der Baum', 'das Holz', 'das Heft', 'der Glückwunsch']

Traduccion9 = ['Departamento', 'Casa de varios niveles', 'Vivienda comunitaria', 'Apartamento', 'Bloque de casas iguales',
              'Cuarto', 'Cuarto de baño', 'Ducha', 'Pasillo', 'Cocina', 'Dormitorio', 'Sala de estar', 'Cuarto para los niños', 'Balcón', 'Terraza', 'Jardín', 'Gradas', 'Puerta', 'Cobija',
              'Planta baja', 'Nivel de piso', 'Posición', 'Centro', 'La vista', 'Muebles', 'Objetos','Lámpara', 'Luz', 'Planta (botánica)', 'Estante', 'Armario', 'Escritorio', 'Sillón', 'Sofá', 'Silla', 'Mesa', 'Alfombra', 'Cama', 'Televisión', 'Horno', 'Cafetera', 'Refrigerador', 'Lavaplatos', 'Lavadora', 'Anuncio', 'Contrato', 'Renta', 'Casero', 'Mudanza', 'Celebración', 'Flor', 'Árbol', 'Madera', 'Cuaderno', 'Buenos deseos']

Lista8 = ["das Alter", "die Größe", "das Gewicht", "der Körper", "der Kopf", "das Bein", "die Hand", "der Arm", "die Schulter", "der Bauch", "der Finger", "der Hals",
         "das Knie", "der Fuß", "das Gesicht", "der Mund", "das Auge", "das Haar", "das Ohr", "die Nase", "der Unfall", "der Schmerz", "der Verband", "die Salbe", "das Rezept",
         "die Krankheit", "der Schnupfen"]

Traduccion8 = ["Edad", "Estatura", "Peso corporal", "El cuerpo", "Cabeza", "Pierna", "Mano", "Brazo", "Hombro", "Panza", "Dedo", "Cuello", "Rodilla", "Pie", "Rostro",
              "Boca", "Ojo", "Cabello", "Oreja", "Nariz", "El accidente", "Dolor", "Vendaje", "Ungüento", "Receta", "Enfermedad", "Catarro"]

Lista7 = ["der Arbeitsalltag", "der Bäcker", "der Hausmeister", "der Mitarbeiter", "das Praktikum", "der Bericht", "der Fehler", "die Datei", "der Drucker", "das Passwort", "der Akku",
         "der Automat", "der Brief", "der Absender", "der Empfänger", "das Mitglied", "der Aufzug", "die Politik"]

Traduccion7 = ["Rutina de Trabajo", "Panadero", "Concerje", "Empleado", "Práctica laboral", "Informe", "El error", "Documento", "Impresora", "Contraseña", "La batería",
              "Cajero automático", "La carta", "Remitente", "Destinatario", "Miembro de algún Club", "Elevador", "Política"]

Lista = Lista9 + Lista8 + Lista7
Traduccion = Traduccion9 + Traduccion8 + Traduccion7

st.title("WILLKOMMEN! HIER KÖNNEN SIE WORTSCHATZ")

if "indice" not in st.session_state:
    st.session_state.indice = 0
if "aciertos" not in st.session_state:
    st.session_state.aciertos = 0
if "intentos" not in st.session_state:
    st.session_state.intentos = 0
if "finalizado" not in st.session_state:
    st.session_state.finalizado = False
if "x" not in st.session_state:
    st.session_state.x = random.randint(0, len(Lista) - 1)

st.sidebar.title("Einstellungen")
cantidad_objetivo = st.sidebar.slider("Wie viele Wörter möchten sie heute lernen?", 5, len(Lista))

if st.sidebar.button("Neu starten"):
    st.session_state.intentos = 0
    st.session_state.aciertos = 0
    st.session_state.finalizado = False
    st.session_state.x = random.randint(0, len(Lista) - 1)
    st.rerun()

tab1, tab2 = st.tabs(["Lernwortschatz 9", "Prüfung"])

with tab1:
    st.header("Lernwortschatz 7")
    df = pd.DataFrame({
        "Wort": Lista7,
        "Übersetzt": Traduccion7})
    st.dataframe(df, use_container_width = True)

with tab2:
    st.header("Lernwortschatz 8")
    df = pd.DataFrame({
        "Wort": Lista8,
        "Übersetzt": Traduccion8})
    st.dataframe(df, use_container_width = True)

with tab3:
    st.header("Lernwortschatz 9")
    df = pd.DataFrame({
        "Wort": Lista9,
        "Übersetzt": Traduccion9})
    st.dataframe(df, use_container_width = True)

with tab4:
    if st.session_state.intentos >= cantidad_objetivo:
        st.session_state.finalizado = True
    if st.session_state.finalizado:
        st.header("Wundabar! du hast fertiggemacht")
        nota = (st.session_state.aciertos / cantidad_objetivo*100)
        st.write("Benotung", f"{nota}")
    else:
        palabra_actual = Lista[st.session_state.x]
        art_correcto, sin_art = palabra_actual.split(" ", 1)
        st.subheader(f"Frage {st.session_state.intentos +1} von {cantidad_objetivo}")
        st.write(f"Artikel von: {sin_art}")
        respuesta = st.text_input("Schreiben Sie die Antwort: ",key = f"input_{st.session_state.intentos}")
        respuesta = respuesta.lower().strip()
        if st.button("Klicken Sie hier bitte an, um das Wort zu überprüfen"):
            if respuesta == art_correcto.lower().strip():
                st.success("Genau!")
                st.write(f"Übersetzt: {Traduccion[st.session_state.x]}")
                st.session_state.aciertos += 1
            else:
                st.error("Das ist Falsch")
        if st.button("Nächte Frage:"):
            st.session_state.intentos += 1
            st.session_state.x = random.randint(0, len(Lista) - 1)
            st.rerun()
