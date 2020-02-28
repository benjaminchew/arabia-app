import azure.cognitiveservices.speech as speechsdk
from external.google import upload_blob
import tempfile
import time

def msft_tts(text):
    text = text[0:101]
    
    # Creates an instance of a speech config with specified subscription key and service region.
    speech_key, service_region = '86a1e0bee52f41e29fee0eae40f94f3c', 'uksouth'
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # speech_config.speech_synthesis_voice_name = 'nb-NO-HuldaRUS'

    # Creates an audio configuration that points to an audio file.
    file_object = tempfile.NamedTemporaryFile(suffix='.wav')
    audio_output = speechsdk.AudioOutputConfig(
        filename=file_object.name,

    )

    # Creates a synthesizer with the given settings
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)

    # Synthesizes the text to speech.
    result = speech_synthesizer.speak_text_async(text).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to [{}] for text [{}]".format(file_object.name, text))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")

    # upload file
    gcs_key = f'audio_files/{time.time()}.wav'
    upload_blob('arabia', file_object.name, gcs_key)

    return f'https://arabia.storage.googleapis.com/{gcs_key}'
