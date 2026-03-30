import streamlit as st

st.set_page_config(page_title="Животинска Галерия", layout="wide")
st.title("Галерия от любими животни")

if "animals" not in st.session_state:
    st.session_state.animals = []

st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area("Описание")
image_url = st.text_input("URL на картинка")

if st.button("Добави в галерията"):
    if name and description and image_url:
        st.session_state.animals.append({
            "име": name,
            "описание": description, 
            "картинка": image_url
        })
        st.success(f" {name} беше добавено успешно!")
       
        st.rerun()
    else:
        st.warning(" Моля, попълнете всички полета!")

st.divider()

if st.session_state.animals:
    st.header(" Премахни животно")
  
    animal_names = [a["име"] for a in st.session_state.animals]
    remove_name = st.selectbox("Избери животно за премахване", animal_names)
    
    if st.button("Премахни избраното"):
      
        st.session_state.animals = [a for a in st.session_state.animals if a["име"] != remove_name]
        st.success(f"Премахнато: {remove_name}")
        st.rerun()

st.divider()

st.header("Галерия")
if st.session_state.animals:
    cols = st.columns(3)
    for idx, animal in enumerate(st.session_state.animals):
        with cols[idx % 3]:
            st.subheader(animal["име"])
            st.image(animal["картинка"], use_container_width=True)
            st.write(animal["описание"])
else:
    st.info("Галерията е празна. Добавете животни от формата по-горе!")
