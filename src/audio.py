import sabesp
from gtts import gTTS
from playsound import playsound

def produzir_audio(volume_total):

    audio_principal= f'Bom dia. O volume total de água armazenado hoje na Região Metropolitana de São Paulo é de {volume_total} por cento.'
    
    if float(volume_total.replace(',', '.')) < 60. :
        audio_final= f'{audio_principal} Faça a sua parte! Economize mais água.'
        print(audio_final)
    else:
        audio_final= audio_principal
        print(audio_final)
        

    frase = gTTS(audio_final, lang='pt')
    frase.save('frase.mp3')
    playsound('frase.mp3')

