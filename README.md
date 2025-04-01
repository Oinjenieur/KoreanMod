# KoreanMod - Korean Language Support for Bark TTS

Ce projet ajoute le support complet de la langue coréenne au moteur Bark TTS, avec des fonctionnalités avancées de traitement phonétique et de gestion des émotions.

This project adds complete Korean language support to the Bark TTS engine, with advanced phonetic processing and emotion management features.

## Fonctionnalités / Features

- Support complet de la langue coréenne / Complete Korean language support
- Conversion automatique des caractères coréens / Automatic Korean character conversion
- Gestion des règles de liaison phonétique / Phonetic liaison rules management
- Support des émotions en coréen / Korean emotion support
- Validation du texte coréen / Korean text validation
- Sauvegarde des fichiers audio générés / Generated audio file saving

## Prérequis / Prerequisites

- Python 3.8+
- Bark TTS
- NumPy
- SoundDevice
- SoundFile

## Installation / Installation

### Windows

```bash
pip install -r requirements.txt
```

### macOS

1. Installer Homebrew si ce n'est pas déjà fait / Install Homebrew if not already installed:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Installer les dépendances système / Install system dependencies:
```bash
brew install portaudio
```

3. Installer les dépendances Python / Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Pour les utilisateurs M1/M2, installer PyTorch spécifiquement / For M1/M2 users, install PyTorch specifically:
```bash
pip install torch torchvision torchaudio
```

## Utilisation / Usage

```python
from src.core.voice_cloning import model_manager

# Exemple de synthèse vocale en coréen / Example of Korean speech synthesis
text = "안녕하세요! 오늘은 날씨가 좋네요."  # "Hello! The weather is nice today."
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

### Windows

```bash
python test_korean.py
```

### macOS

```bash
python3 test_korean_mac.py
```

## Structure du Projet / Project Structure

```
KoreanMod/
├── src/
│   └── core/
│       ├── voice_cloning.py
│       └── korean_language_support.py
├── test_output/
├── test_korean.py
├── test_korean_mac.py
├── requirements.txt
└── README.md
```

## Contribution / Contributing

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Licence / License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

This project is licensed under the MIT License. See the `LICENSE` file for more details.
