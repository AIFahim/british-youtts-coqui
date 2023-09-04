# British-YouTTS-Coqui

## Installation

### Python Version
This project uses Python version 3.9.0.

### Installing Packages
To install the required packages, run the following command:
```bash
pip install -r requirements.txt
```

## Downloading Pre-trained TTS Weights

### Hugging Face Weights
This project uses a pre-trained TTS model from Hugging Face, trained with YouTTS. You can find the model [here](https://huggingface.co/voices/VCTK_British_English_Males).

To download the weights, run the following script:
```bash
python download_w_frm_hf.py
```

### Copy Supplemental Folder
To copy the supplemental folder, move it from \`./weight_hf/supplemental\` to \`./supplemental\`.

## Inference

### Generating Audio
To generate audio, run the following script:
```bash
python infer_n_save_audio.py
```

### Hosting with FastAPI
To host the TTS model using FastAPI, run the following script:
```bash
python infer_fast_api.py
```
