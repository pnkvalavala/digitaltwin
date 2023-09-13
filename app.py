import base64
import requests
import streamlit as st

st.set_page_config(
    page_title="Digital Twin",
    page_icon="💻",
    menu_items={
        'Report a bug': "https://github.com/pnkvalavala/digitaltwin/issues",
        'About': "With Single image and 10 seconds of sample audio, you can create video as if you were talking your desired text."
    }
)

st.markdown(
    "<h1 style='text-align: center;'>Digital Twin</h1>",
    unsafe_allow_html=True
)

if 'first' not in st.session_state:
    st.session_state.first = True

if 'audio_bytes' not in st.session_state:
    st.session_state.audio_bytes = None

public_url_1 = "https://xxxxxxxxxxxxxxx.ngrok-free.app/" # TorTTS_API.ipynb
public_url_2 = "https://xxxxxxxxxxxxxxx.ngrok-free.app/" # Vid_API.ipynb

with st.form("tts"):
    audio_file = st.file_uploader("Choose an audio file of your voice with no disturbances", type=['wav'])
    prompt = st.text_input("Enter prompt text")
    submit_tts = st.form_submit_button("Submit")

first = True

if st.session_state.first and audio_file and prompt:
    audio_bytes = audio_file.read()
    audio_b64 = base64.b64encode(audio_bytes).decode()
    data1 = {'audio': audio_b64, 'prompt': prompt}
    res = requests.post(f'{public_url_1}', json=data1)

    audio_result = res.json()['audio']
    with open('tts.wav','wb') as f:
        f.write(base64.b64decode(audio_result))
    cloned_audio_file = open('tts.wav', 'rb')
    audio_out_bytes = cloned_audio_file.read()
    if audio_out_bytes:
        st.session_state.first = False
        st.session_state.audio_bytes = audio_out_bytes


if not st.session_state.first:
    image_file = st.file_uploader("Upload image file", type=['png'])
    if image_file and st.session_state.audio_bytes:
        audio_out_b64 = base64.b64encode(st.session_state.audio_bytes).decode()
        image_bytes = image_file.read()
        image_b64 = base64.b64encode(image_bytes).decode()

        data2 = {'image': image_b64, 'audio': audio_out_b64}
        res = requests.post(f'{public_url_2}', json=data2)

        video_b64 = res.json()['video']
        video_bytes = base64.b64decode(video_b64)

        st.video(video_bytes)