import torchaudio
from TTS.utils.synthesizer import Synthesizer
import requests
import json
import base64
import wave
import numpy as np
from fastapi import FastAPI, File, UploadFile, Request
import json
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class Body(BaseModel):
    grapheme:str


@app.get('/')
async def home():
    return "Fast server is working!"


@app.post("/infer_tts/")
async def infer(body:Body):
    grapheme = body.dict()['grapheme']
    synth=Synthesizer(tts_checkpoint="./weight_hf/checkpoint_85000.pth",tts_config_path="./weight_hf/config.json",tts_speakers_file="./weight_hf/supplemental/speakers.json")
    
    wav=synth.tts(grapheme, speaker_name="VCTK_p226",language_name="en")
    synth.save_wav(wav,"./infered_audio/youtts.wav")

    with open("./infered_audio/youtts.wav", "rb") as f:
        audio_data = f.read()

    base64_audio = base64.b64encode(audio_data).decode("utf-8") 
    return base64_audio 

    
if __name__ == "__main__": 
    uvicorn.run("infer_fast_api:app", host='0.0.0.0', port = 7373, reload = True)
