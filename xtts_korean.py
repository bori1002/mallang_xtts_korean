import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from huggingface_hub import snapshot_download

snapshot_download(repo_id="princesslucy/mallang_xtts_large", local_dir='./model')
config = XttsConfig()
config.load_json("./model/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="./model")
model.cuda()

def tts(text, audio="./wavs/input.wav"):
    gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[audio])

    out = model.inference(
    text,
    gpt_cond_latent=gpt_cond_latent,
    speaker_embedding=speaker_embedding,
    temperature=0.3, # Add custom parameters here
    language="ko",
)
    return torchaudio.save("./wavs/output.wav", torch.tensor(out["wav"]).unsqueeze(0), 24000)