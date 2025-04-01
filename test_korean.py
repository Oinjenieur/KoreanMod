import os
import sys
import logging
import numpy as np
import sounddevice as sd
from pathlib import Path
import soundfile as sf

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_korean_synthesis():
    # Texte de test en coréen : "Bonjour! Le temps est beau aujourd'hui."
    text = "안녕하세요! 오늘은 날씨가 좋네요."
    
    logger.info("Démarrage de la synthèse vocale en coréen...")
    logger.info(f"Texte : {text}")
    
    try:
        # Import du model_manager après la configuration du logging
        from src.core.voice_cloning import model_manager
        
        # Création du dossier de sortie si nécessaire
        output_dir = Path("test_output")
        output_dir.mkdir(exist_ok=True)
        
        # Synthèse avec Bark
        logger.info("Démarrage de la synthèse...")
        audio_data, sample_rate = model_manager.synthesize(
            text=text,
            language="ko",
            params={
                "emotion": "happy",
                "engine_type": "bark",
                "speed": 1.0,
                "pitch": 0
            }
        )
        
        # Sauvegarde de l'audio
        output_file = output_dir / "korean_test.wav"
        sf.write(output_file, audio_data, sample_rate)
        logger.info(f"Audio sauvegardé dans : {output_file}")
        
        # Lecture de l'audio
        logger.info("Lecture de l'audio...")
        sd.play(audio_data, sample_rate)
        sd.wait()
        
        logger.info("Test terminé avec succès!")
        
    except Exception as e:
        logger.error(f"Erreur lors du test : {str(e)}", exc_info=True)
        return False
    
    return True

if __name__ == "__main__":
    success = test_korean_synthesis()
    sys.exit(0 if success else 1) 