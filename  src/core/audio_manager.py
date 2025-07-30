"""
Sistema de audio épico para el RPG 3D
"""

import pygame
import os
import random
from typing import Dict, Optional

class AudioManager:
    """Gestor de audio épico con efectos dinámicos"""

    def __init__(self):
        self.enabled = True
        self.music_volume = 0.7
        self.sfx_volume = 0.8
        self.current_music = None
        self.sound_cache: Dict[str, pygame.mixer.Sound] = {}

        # Inicializar pygame mixer
        try:
            pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
            pygame.mixer.init()
            print("🔊 Sistema de audio inicializado")
        except pygame.error as e:
            print(f"⚠️ Error inicializando audio: {e}")
            self.enabled = False

    def load_sound(self, sound_name: str, file_path: str) -> bool:
        """Cargar sonido en la caché"""
        if not self.enabled:
            return False

        try:
            if os.path.exists(file_path):
                sound = pygame.mixer.Sound(file_path)
                self.sound_cache[sound_name] = sound
                print(f"🎵 Sonido cargado: {sound_name}")
                return True
            else:
                # Crear sonidos procedurales si no existe el archivo
                self.create_procedural_sound(sound_name)
                return True
        except pygame.error as e:
            print(f"❌ Error cargando {sound_name}: {e}")
            self.create_procedural_sound(sound_name)
            return False

    def create_procedural_sound(self, sound_name: str):
        """Crear sonidos procedurales épicos"""
        if not self.enabled:
            return

        try:
            duration = 0.5
            sample_rate = 44100

            if sound_name == "sword_hit":
                # Sonido metálico de espada
                sound_data = self.generate_metallic_clang(duration, sample_rate)
            elif sound_name == "fireball":
                # Sonido de bola de fuego
                sound_data = self.generate_fire_whoosh(duration, sample_rate)
            elif sound_name == "ice_spell":
                # Sonido cristalino de hielo
                sound_data = self.generate_ice_crystal(duration, sample_rate)
            elif sound_name == "lightning":
                # Sonido de rayo eléctrico
                sound_data = self.generate_lightning_crack(duration, sample_rate)
            elif sound_name == "heal":
                # Sonido de curación mágica
                sound_data = self.generate_healing_chime(duration, sample_rate)
            elif sound_name == "monster_roar":
                # Rugido de monstruo
                sound_data = self.generate_monster_roar(duration * 2, sample_rate)
            elif sound_name == "victory":
                # Fanfarria de victoria
                sound_data = self.generate_victory_fanfare(duration * 3, sample_rate)
            elif sound_name == "footsteps":
                # Pasos
                sound_data = self.generate_footstep(duration * 0.3, sample_rate)
            else:
                # Sonido genérico
                sound_data = self.generate_generic_beep(duration, sample_rate)

            # Crear surface de sonido
            sound = pygame.sndarray.make_sound(sound_data)
            self.sound_cache[sound_name] = sound

        except Exception as e:
            print(f"⚠️ Error creando sonido procedural {sound_name}: {e}")

    def generate_metallic_clang(self, duration: float, sample_rate: int):
        """Generar sonido metálico de espada"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Frecuencias metálicas
        freq1 = 2000 + 500 * np.sin(t * 50)
        freq2 = 3000 + 300 * np.sin(t * 30)

        # Ondas con decay exponencial
        wave1 = np.sin(2 * np.pi * freq1 * t) * np.exp(-t * 8)
        wave2 = np.sin(2 * np.pi * freq2 * t) * np.exp(-t * 6)

        # Ruido para textura metálica
        noise = np.random.normal(0, 0.1, samples) * np.exp(-t * 10)

        # Combinar y normalizar
        sound_wave = (wave1 + wave2 * 0.7 + noise) * 0.3
        return (sound_wave * 32767).astype(np.int16)

    def generate_fire_whoosh(self, duration: float, sample_rate: int):
        """Generar sonido de fuego"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Ruido filtrado para simular fuego
        noise = np.random.normal(0, 1, samples)

        # Filtro pasa-bajos simple
        filtered_noise = np.zeros_like(noise)
        alpha = 0.1
        for i in range(1, len(noise)):
            filtered_noise[i] = alpha * noise[i] + (1 - alpha) * filtered_noise[i-1]

        # Envelope con attack y decay
        envelope = np.exp(-t * 3) * (1 - np.exp(-t * 20))

        sound_wave = filtered_noise * envelope * 0.4
        return (sound_wave * 32767).astype(np.int16)

    def generate_ice_crystal(self, duration: float, sample_rate: int):
        """Generar sonido cristalino de hielo"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Frecuencias altas cristalinas
        freqs = [3000, 4500, 6000, 7500]
        sound_wave = np.zeros(samples)

        for i, freq in enumerate(freqs):
            phase_offset = i * np.pi / 4
            wave = np.sin(2 * np.pi * freq * t + phase_offset)
            decay = np.exp(-t * (5 + i * 2))
            sound_wave += wave * decay * (0.8 - i * 0.15)

        sound_wave *= 0.3
        return (sound_wave * 32767).astype(np.int16)

    def generate_lightning_crack(self, duration: float, sample_rate: int):
        """Generar sonido de rayo"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Ruido blanco con modulación rápida
        noise = np.random.normal(0, 1, samples)

        # Modulación AM rápida
        modulation = 1 + 0.5 * np.sin(2 * np.pi * 100 * t)
        modulated_noise = noise * modulation

        # Envelope muy sharp para simular crack
        envelope = np.exp(-t * 15) * (t < 0.1)

        sound_wave = modulated_noise * envelope * 0.5
        return (sound_wave * 32767).astype(np.int16)

    def generate_healing_chime(self, duration: float, sample_rate: int):
        """Generar sonido mágico de curación"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Acordes mágicos
        freqs = [523, 659, 784, 1047]  # Do, Mi, Sol, Do octava
        sound_wave = np.zeros(samples)

        for i, freq in enumerate(freqs):
            delay = i * 0.1
            delayed_t = t - delay
            delayed_t[delayed_t < 0] = 0

            wave = np.sin(2 * np.pi * freq * delayed_t)
            envelope = np.exp(-delayed_t * 2) * (delayed_t >= 0)
            sound_wave += wave * envelope * 0.25

        return (sound_wave * 32767).astype(np.int16)

    def generate_monster_roar(self, duration: float, sample_rate: int):
        """Generar rugido de monstruo"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Frecuencias graves moduladas
        base_freq = 80 + 40 * np.sin(t * 5)
        harmonic1 = 160 + 60 * np.sin(t * 3)
        harmonic2 = 240 + 80 * np.sin(t * 7)

        wave1 = np.sin(2 * np.pi * base_freq * t)
        wave2 = np.sin(2 * np.pi * harmonic1 * t) * 0.7
        wave3 = np.sin(2 * np.pi * harmonic2 * t) * 0.5

        # Ruido para textura orgánica
        noise = np.random.normal(0, 0.3, samples)

        # Envelope de rugido
        envelope = np.exp(-t * 1.5) * (1 + 0.5 * np.sin(t * 8))

        sound_wave = (wave1 + wave2 + wave3 + noise) * envelope * 0.4
        return (sound_wave * 32767).astype(np.int16)

    def generate_victory_fanfare(self, duration: float, sample_rate: int):
        """Generar fanfarria de victoria"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Melodía épica ascendente
        melody_times = [0, 0.5, 1.0, 1.5, 2.0, 2.5]
        melody_freqs = [262, 330, 392, 523, 659, 784]  # Do, Mi, Sol, Do, Mi, Sol

        sound_wave = np.zeros(samples)

        for i, (start_time, freq) in enumerate(zip(melody_times, melody_freqs)):
            if start_time >= duration:
                break

            note_duration = min(0.6, duration - start_time)
            note_samples = int(note_duration * sample_rate)
            start_idx = int(start_time * sample_rate)
            end_idx = min(start_idx + note_samples, samples)

            if start_idx < samples:
                note_t = np.linspace(0, note_duration, end_idx - start_idx)
                note_wave = np.sin(2 * np.pi * freq * note_t)
                note_envelope = np.exp(-note_t * 2)

                sound_wave[start_idx:end_idx] += note_wave * note_envelope * 0.3

        return (sound_wave * 32767).astype(np.int16)

    def generate_footstep(self, duration: float, sample_rate: int):
        """Generar sonido de paso"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        # Ruido filtrado para simular contacto con suelo
        noise = np.random.normal(0, 1, samples)

        # Filtro pasa-bajos
        filtered_noise = np.zeros_like(noise)
        alpha = 0.3
        for i in range(1, len(noise)):
            filtered_noise[i] = alpha * noise[i] + (1 - alpha) * filtered_noise[i-1]

        # Envelope muy corto y punchy
        envelope = np.exp(-t * 25) * (1 - np.exp(-t * 100))

        sound_wave = filtered_noise * envelope * 0.6
        return (sound_wave * 32767).astype(np.int16)

    def generate_generic_beep(self, duration: float, sample_rate: int):
        """Generar beep genérico"""
        import numpy as np

        samples = int(duration * sample_rate)
        t = np.linspace(0, duration, samples)

        freq = 800
        wave = np.sin(2 * np.pi * freq * t)
        envelope = np.exp(-t * 5)

        sound_wave = wave * envelope * 0.3
        return (sound_wave * 32767).astype(np.int16)

    def play_sound(self, sound_name: str, volume: float = 1.0):
        """Reproducir sonido"""
        if not self.enabled or sound_name not in self.sound_cache:
            return

        try:
            sound = self.sound_cache[sound_name]
            sound.set_volume(volume * self.sfx_volume)
            sound.play()
        except pygame.error as e:
            print(f"❌ Error reproduciendo {sound_name}: {e}")

    def play_music(self, music_path: str, loops: int = -1):
        """Reproducir música de fondo"""
        if not self.enabled:
            return

        try:
            if os.path.exists(music_path):
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.set_volume(self.music_volume)
                pygame.mixer.music.play(loops)
                self.current_music = music_path
            else:
                print(f"⚠️ Archivo de música no encontrado: {music_path}")
        except pygame.error as e:
            print(f"❌ Error reproduciendo música: {e}")

    def stop_music(self):
        """Detener música"""
        if self.enabled:
            pygame.mixer.music.stop()
            self.current_music = None

    def set_music_volume(self, volume: float):
        """Establecer volumen de música (0.0 - 1.0)"""
        self.music_volume = max(0.0, min(1.0, volume))
        if self.enabled:
            pygame.mixer.music.set_volume(self.music_volume)

    def set_sfx_volume(self, volume: float):
        """Establecer volumen de efectos (0.0 - 1.0)"""
        self.sfx_volume = max(0.0, min(1.0, volume))

    def load_default_sounds(self):
        """Cargar sonidos por defecto del juego"""
        default_sounds = [
            "sword_hit",
            "fireball",
            "ice_spell",
            "lightning",
            "heal",
            "monster_roar",
            "victory",
            "footsteps"
        ]

        for sound_name in default_sounds:
            # Intentar cargar desde assets, sino crear procedural
            file_path = f"assets/sounds/{sound_name}.wav"
            self.load_sound(sound_name, file_path)

        print(f"🎵 {len(self.sound_cache)} sonidos cargados")

    def play_combat_sound(self, action_type: str, character_type: str = ""):
        """Reproducir sonidos específicos de combate"""
        if action_type == "attack":
            if character_type == "knight":
                self.play_sound("sword_hit", 0.8)
            else:
                self.play_sound("sword_hit", 0.6)

        elif action_type == "spell":
            spell_sounds = ["fireball", "ice_spell", "lightning"]
            sound = random.choice(spell_sounds)
            self.play_sound(sound, 0.7)

        elif action_type == "heal":
            self.play_sound("heal", 0.6)

        elif action_type == "monster_attack":
            self.play_sound("monster_roar", 0.5)

        elif action_type == "victory":
            self.play_sound("victory", 0.9)

    def is_music_playing(self) -> bool:
        """Verificar si la música está reproduciéndose"""
        if not self.enabled:
            return False
        return pygame.mixer.music.get_busy()

    def cleanup(self):
        """Limpiar recursos de audio"""
        if self.enabled:
            pygame.mixer.music.stop()
            for sound in self.sound_cache.values():
                sound.stop()
            pygame.mixer.quit()
            print("🔇 Sistema de audio finalizado")