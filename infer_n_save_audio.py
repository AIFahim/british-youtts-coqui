from TTS.utils.synthesizer import Synthesizer
import requests
import json
import base64
import wave
import numpy as np


def infer(grapheme):

    synth=Synthesizer(tts_checkpoint="./weight_hf/checkpoint_85000.pth",tts_config_path="./weight_hf/config.json",tts_speakers_file="./weight_hf/supplemental/speakers.json")

    wav=synth.tts(grapheme, speaker_name="VCTK_p226",language_name="en")
    synth.save_wav(wav,"./infered_audio/youtts.wav")
 
if __name__ == "__main__":
    infer("My name is Jak. I'm from England. How are you?")

    
