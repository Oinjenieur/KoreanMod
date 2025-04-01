# KoreanMod - Support Coréen pour Bark TTS

Ce projet ajoute le support complet de la langue coréenne au moteur Bark TTS, avec des fonctionnalités avancées de traitement phonétique et de gestion des émotions.

## Fonctionnalités

- Support complet de la langue coréenne
- Conversion automatique des caractères coréens
- Gestion des règles de liaison phonétique
- Support des émotions en coréen
- Validation du texte coréen
- Sauvegarde des fichiers audio générés

## Prérequis

- Python 3.8+
- Bark TTS
- NumPy
- SoundDevice
- SoundFile

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```python
from src.core.voice_cloning import model_manager

# Exemple de synthèse vocale en coréen
text = "안녕하세요! 오늘은 날씨가 좋네요."
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
```

## Test

Pour exécuter les tests :

```bash
python test_korean.py
```

## Structure du Projet

```
KoreanMod/
├── src/
│   └── core/
│       ├── voice_cloning.py
│       └── korean_language_support.py
├── test_output/
├── test_korean.py
├── requirements.txt
└── README.md
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.
