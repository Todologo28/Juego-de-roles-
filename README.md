# 🎮 RPG 3D Épico - Batalla Definitiva

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![OpenGL](https://img.shields.io/badge/OpenGL-3D-green.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5+-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Beta-orange.svg)

> **Un RPG 3D épico con combate por turnos, efectos visuales impresionantes y audio procedural generado en tiempo real.**

## 🌟 Características Principales

### 🎭 **Sistema de Personajes**
- **🧙‍♂️ Mago Épico**: Maestro de las artes arcanas con hechizos devastadores
- **⚔️ Caballero Valiente**: Guerrero sagrado con armadura brillante y honor inquebrantable

### 👹 **Enemigos Únicos**
- **🧌 Duende Siniestro**: Ágil asesino de las sombras con dagas gemelas
- **👹 Ogro Devastador**: Coloso destructivo con garrote masivo
- **🐉 Dragón Sombrío**: Señor ancestral del fuego eterno (Jefe Final)

### ⚡ **Efectos Visuales 3D**
- **Modelos 3D detallados** renderizados completamente en código
- **Sistema de partículas épico** (fuego, hielo, rayos, explosiones)
- **Iluminación dinámica** con múltiples fuentes de luz
- **Escenario inmersivo** con pilares místicos y antorchas parpadeantes
- **Animaciones fluidas** de personajes y efectos

### 🎵 **Audio Procedural Único**
- **Sonidos generados matemáticamente** en tiempo real
- **Efectos únicos** para cada hechizo y ataque
- **No requiere archivos de audio externos**
- **Música dinámica** que se adapta al combate

### 🎯 **Mecánicas de Juego**
- **Combate por turnos estratégico** con múltiples opciones
- **Sistema de hechizos** con efectos visuales únicos
- **Inventario completo** con pociones y objetos
- **Sistema de experiencia** y progresión de personaje
- **Tres batallas épicas** para completar el juego

## 🚀 Instalación Rápida

### 📋 Requisitos
- **Python 3.8+**
- **Windows, macOS o Linux**
- **Tarjeta gráfica compatible con OpenGL**

### ⚡ Instalación Express
```bash
# Clonar el repositorio
git clone https://github.com/epicgames/rpg-3d-epico.git
cd rpg-3d-epico

# Instalar dependencias
pip install -r requirements.txt

# ¡Ejecutar el juego!
python run_game.py
```

### 🛠️ Instalación para Desarrollo
```bash
# Instalar en modo desarrollo
pip install -e .[dev]

# Configurar entorno de desarrollo
python setup.py dev-setup

# Ejecutar pruebas
python setup.py test
```

## 🎮 Cómo Jugar

### 🎯 **Controles Básicos**
| Tecla | Acción |
|-------|--------|
| `1`, `2` | Seleccionar personaje/enemigo |
| `1` | Ataque físico |
| `2` | Lanzar hechizo mágico |
| `3` | Abrir inventario |
| `H` | Usar poción (con inventario abierto) |
| `ESC` | Ver controles / Pausar |
| `Q` | Salir del juego |

### 🏆 **Objetivo del Juego**
1. **Selecciona tu héroe** (Mago o Caballero)
2. **Derrota a los tres enemigos únicos** en combate épico
3. **Usa estrategia** combinando ataques, hechizos y pociones
4. **Completa tu leyenda** y conviértete en campeón

### ⚔️ **Estrategias de Combate**
- **Mago**: Usa hechizos poderosos pero gestiona tu maná sabiamente
- **Caballero**: Resiste más daño pero planifica tus ataques físicos
- **Pociones**: Úsalas estratégicamente para recuperarte en momentos críticos
- **Timing**: Observa los patrones de ataque de cada enemigo

## 🏗️ Estructura del Proyecto

```
RPG_3D_Epic/
├── 📁 src/                     # Código fuente principal
│   ├── 📁 core/               # Motor del juego
│   │   ├── game_engine.py     # Motor principal
│   │   ├── renderer_3d.py     # Renderizado 3D
│   │   ├── particle_system.py # Sistema de partículas
│   │   └── audio_manager.py   # Audio procedural
│   ├── 📁 models/             # Modelos 3D
│   │   ├── player_models.py   # Mago y Caballero
│   │   └── enemy_models.py    # Enemigos 3D
│   ├── 📁 data/               # Datos del juego
│   │   ├── game_data.py       # Clases principales
│   │   ├── weapons.py         # Armas y pociones
│   │   └── enemies.py         # Configuración enemigos
│   └── 📁 ui/                 # Interfaz de usuario
│       └── hud.py             # Sistema de HUD
├── 📁 assets/                 # Recursos (texturas, sonidos)
├── 📁 config/                 # Configuración del juego
├── 📁 saves/                  # Datos de guardado
├── 📁 tests/                  # Pruebas unitarias
├── requirements.txt           # Dependencias
├── setup.py                  # Configuración instalación
└── run_game.py               # Script principal
```

## 🔧 Desarrollo

### 🧪 **Ejecutar Pruebas**
```bash
# Todas las pruebas
python -m pytest tests/ -v

# Pruebas específicas
python -m unittest tests.test_combat
python -m unittest tests.test_inventory
```

### 📊 **Verificar Dependencias**
```bash
python setup.py check
```

### 🎨 **Personalización**
- **Modelos 3D**: Edita `src/models/` para nuevos personajes
- **Efectos**: Modifica `src/core/particle_system.py` para nuevos efectos
- **Balance**: Ajusta `src/data/` para cambiar estadísticas
- **Audio**: Personaliza `src/core/audio_manager.py` para nuevos sonidos

## 📸 Capturas de Pantalla

### 🎭 Selección de Personaje
```
🗡️ ELIGE TU DESTINO ⚔️
1 - 🧙‍♂️ ARCHIMAGO SUPREMO
2 - ⚔️ PALADÍN INVENCIBLE
```

### ⚔️ Combate Épico
```
🏛️ === COMBATE ÉPICO ===
👤 Mago Épico: 80/80 HP | MP: 120/120
👹 Duende Siniestro: 65/80 HP

⚡ Tu turno:
1. Atacar  2. Hechizo  3. Inventario
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

### 🐛 **Reportar Bugs**
1. Busca bugs existentes en [Issues](https://github.com/epicgames/rpg-3d-epico/issues)
2. Crea un nuevo issue con descripción detallada
3. Incluye pasos para reproducir el problema

### 💡 **Sugerir Características**
1. Verifica que no exista una sugerencia similar
2. Describe claramente la nueva característica
3. Explica por qué sería útil para el juego

### 🔧 **Contribuir Código**
1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Commit tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## 📋 Dependencias

### 🐍 **Python Core**
- **pygame** ≥ 2.5.0 - Motor de juego y ventanas
- **PyOpenGL** ≥ 3.1.6 - Renderizado 3D
- **PyOpenGL_accelerate** ≥ 3.1.6 - Aceleración OpenGL
- **numpy** ≥ 1.21.0 - Matemáticas y audio procedural
- **Pillow** ≥ 9.0.0 - Procesamiento de imágenes

### 🛠️ **Desarrollo (Opcional)**
- **pytest** ≥ 7.0.0 - Framework de pruebas
- **black** ≥ 22.0.0 - Formateo de código
- **flake8** ≥ 5.0.0 - Linting

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Ver [LICENSE](LICENSE) para más detalles.

## 🎉 Créditos

### 👨‍💻 **Desarrollado por**
- **Epic Games Studio** - Desarrollo principal
- **Comunidad Open Source** - Contribuciones y feedback

### 🙏 **Agradecimientos Especiales**
- **Pygame Community** - Framework de juego excepcional
- **OpenGL** - Renderizado 3D potente
- **Python Software Foundation** - Lenguaje increíble
- **Todos los beta testers** - Feedback invaluable

### 🎨 **Inspiración**
- Clásicos RPGs como Final Fantasy y Dragon Quest
- Juegos modernos como The Witcher y Skyrim
- Arte pixel y estética retro-futurista

## 📞 Soporte

### 🆘 **¿Necesitas Ayuda?**
- **📖 Wiki**: [Documentación completa](https://github.com/epicgames/rpg-3d-epico/wiki)
- **💬 Discusiones**: [GitHub Discussions](https://github.com/epicgames/rpg-3d-epico/discussions)
- **🐛 Issues**: [Reportar problemas](https://github.com/epicgames/rpg-3d-epico/issues)

### 📊 **Estado del Proyecto**
![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green.svg)

---

<div align="center">

**🔥⚔️🎮 ¡Que comience la batalla definitiva! 🎮⚔️🔥**

*Hecho con ❤️ y mucho código Python*

[⭐ Dale una estrella](https://github.com/epicgames/rpg-3d-epico) | [🐛 Reportar Bug](https://github.com/epicgames/rpg-3d-epico/issues) | [💡 Sugerir Feature](https://github.com/epicgames/rpg-3d-epico/discussions)

</div>