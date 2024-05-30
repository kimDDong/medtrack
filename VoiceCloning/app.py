import os
from flask import Flask, request, jsonify, send_file
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
from melo.api import TTS

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
ckpt_converter = os.path.join(base_dir, 'checkpoints_v2', 'converter')
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = os.path.join(base_dir, 'outputs_v2')

tone_color_converter = ToneColorConverter(os.path.join(ckpt_converter, 'config.json'), device=device)
tone_color_converter.load_ckpt(os.path.join(ckpt_converter, 'checkpoint.pth'))

@app.route('/api/tts', methods=['POST'])
def tts():
    text = request.form['text']
    language = request.form['language']
    speaker_key = request.form['speaker_key']
    reference_audio = request.files['reference_audio']

    src_path = os.path.join(output_dir, 'tmp.wav')
    speed = 1.0

    model = TTS(language=language, device=device)
    speaker_ids = model.hps.data.spk2id
    print(speaker_ids)
    speaker_id = speaker_ids[speaker_key]

    

    source_se = torch.load(os.path.join(base_dir, 'checkpoints_v2', 'base_speakers', 'ses', f'{speaker_key}.pth'), map_location=device)
    model.tts_to_file(text, speaker_id, src_path, speed=speed)
    save_path = os.path.join(output_dir, f'output_{speaker_key}.wav')

    reference_audio_path = os.path.join(base_dir, 'uploads', 'reference_audio.wav')
    reference_audio.save(reference_audio_path)

    target_se, _ = se_extractor.get_se(reference_audio_path, tone_color_converter, vad=False)

    encode_message = "@MyShell"
    tone_color_converter.convert(
        audio_src_path=src_path, 
        src_se=source_se, 
        tgt_se=target_se, 
        output_path=save_path,
        message=encode_message)

    return send_file(save_path, mimetype='audio/wav')

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'uploads'), exist_ok=True)
    app.run(debug=True)