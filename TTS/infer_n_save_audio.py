# import torchaudio
from TTS.utils.synthesizer import Synthesizer
import requests
import json
import base64
import wave
import numpy as np
# url = "https://dev.revesoft.com:6790/phonemizer"

def infer(grapheme):

    synth=Synthesizer(tts_checkpoint="/home/asif/tts_all/coqui_tts/my_exp/coqui_yourtts_british_english_infer/weight_from_hf/models--voices--VCTK_British_English_Males/snapshots/ed90149993e154251e15c4ce5248a9cfc501937a/checkpoint_85000.pth",tts_config_path="/home/asif/tts_all/coqui_tts/my_exp/coqui_yourtts_british_english_infer/weight_from_hf/models--voices--VCTK_British_English_Males/snapshots/ed90149993e154251e15c4ce5248a9cfc501937a/config.json",tts_speakers_file="/home/asif/tts_all/coqui_tts/my_exp/coqui_yourtts_british_english_infer/weight_from_hf/models--voices--VCTK_British_English_Males/snapshots/ed90149993e154251e15c4ce5248a9cfc501937a/supplemental/speakers.json")
    # payload = json.dumps({
    # "text": grapheme
    # })
    # headers = {
    # 'Content-Type': 'application/json'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    # phonme = response.json()['output']
    # phonme = " ".join(phonme)
    
    # wav=synth.tts(phonme)
    wav=synth.tts(grapheme)
    synth.save_wav(wav,"/home/asif/tts_all/coqui_tts/my_exp/coqui_yourtts_british_english_infer/infered_audio/youtts.wav")
 
if __name__ == "__main__":
    infer("My name is Jak. I'm from England. How are you?")

    
