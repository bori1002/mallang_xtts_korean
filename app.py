import streamlit as st
from st_audiorec import st_audiorec
from xtts_korean import *

st.title("XTTS Korean(mallang service)")
st.markdown("---")
st.write("이 프로젝트는 XTTS Korean의 TTS 서비스입니다.")
st.markdown("---")
st.header("음성 녹음 또는 파일 업로드")
st.write("10초 이상의 음성을 녹음하거나, 오디오 파일을 업로드해주세요.")
file_upload = st.checkbox("오디오 파일 업로드(mp3, wav)")

if not file_upload :
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        with open('./wavs/input.wav', 'wb') as f:
                f.write(wav_audio_data)
else:
    wav_audio_data = st.file_uploader("Upload audio", type=['wav'])
    if wav_audio_data is not None:
        st.audio(wav_audio_data, format='audio/wav')
        # 오디오 저장
        with open('./wavs/input.wav', 'wb') as f:
            f.write(wav_audio_data.read())
        
st.header("재생시킬 텍스트 입력")
st.write("읽히고 싶은 텍스트를 입력해주세요.")

text = st.text_area("텍스트 입력", "하느님 저희를 구해주시려면 새 동아줄을 내려주시고, 그렇지 않으면 썩은 동아줄을 내려주세요.")

if st.button("변환"):
    if wav_audio_data is not None and text is not None:
        tts(text)
        st.audio("./wavs/output.wav", format='audio/wav')
    else:
        st.write("음성 파일과 텍스트를 모두 입력해주세요.")