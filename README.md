# psretrox - Playstation 2 Decompilation & Recompilation Tool

## 🌐 Language / Idioma
- [English](#english)
- [Español](#español)

---

## English

### [Project Status]
**Due to recent attention and viral spread, I want to clarify that this project has been paused for several months. It was started as a personal and experimental exploration into low-level C++, and it is not currently under active development.
Feel free to explore and use the code freely, with no restrictions.**

PSRetrox is a C++ application designed to reverse engineer PlayStation 2 games. The primary goal of this project is to extract and process game files, enabling native PC ports of PS2 games. PSRetrox includes built-in tools for decompiling and decoding game assets, such as audio, 3D models, source code, and other game data.

### **Progress**

<img src="./progress/psretrox_progressbar.svg">

<img src="./progress/gui_progressbar.svg">

<img src="./progress/mips_progressbar.svg">

<img src="./progress/recompilation_progressbar.svg">

<img src="./progress/retroxengine_progressbar.svg">

### **Features**
- **Reverse Engineering**: Decompiles PS2 game files from extracted .ISO files.
- **Recompile**: Recompile assembly files to C code.
- **Audio Extraction**: Extracts and decodes audio tracks (e.g., `.vag` files) into standard formats like `.mp3` or `.wav`.
- **3D Model Processing**: Extracts and processes 3D model data from game files for use in modern 3D tools.
- **File Decoding**: Handles PS2-specific formats like `.MB`, `.MH`, `.BD`, `.BH`, `.PSS`, `SLUS_XXX`, and more.
- **Built-in Decompiler**: Uses Capstone for binary disassembly.
- **High Performance**: Designed for fast and efficient extraction.
- **Retrox Engine**: Tool to port PS2 recompiled .C files to PC.

### **Contributing**
We welcome contributions to enhance PSRetrox. Here's how you can contribute:

#### Code Contribution

1. Fork the repository and create your feature branch:
`git checkout -b feature/YourFeature`

2. Make your changes and commit them:
`git commit -m "Add YourFeature"`

3. Push your changes to your fork:
`git push origin feature/YourFeature`

4. Open a pull request on the main repository.

#### **Code Guidelines**
Use consistent formatting and follow modern C++ practices.

- Provide clear comments for complex logic.

- Ensure your changes do not break existing functionality.

- Reporting Issues

#### **Reporting Issues**

If you find a bug or have a feature request, please open an issue with a detailed description.

---

## Español

### [Estado del Proyecto]
**Debido a la reciente atención y difusión viral, quiero aclarar que este proyecto ha estado pausado durante varios meses. Comenzó como una exploración personal y experimental en C++ de bajo nivel, y actualmente no está en desarrollo activo.
Siéntete libre de explorar y usar el código sin restricciones.**

PSRetrox es una aplicación en C++ diseñada para realizar ingeniería inversa en juegos de PlayStation 2. El objetivo principal de este proyecto es extraer y procesar archivos de juegos, permitiendo puertos nativos de juegos de PS2 para PC. PSRetrox incluye herramientas integradas para descompilar y decodificar activos de juegos, como audio, modelos 3D, código fuente y otros datos del juego.

### **Progreso**

<img src="./progress/psretrox_progressbar.svg">

<img src="./progress/gui_progressbar.svg">

<img src="./progress/mips_progressbar.svg">

<img src="./progress/recompilation_progressbar.svg">

<img src="./progress/retroxengine_progressbar.svg">

### **Características**
- **Ingeniería inversa**: Descompila archivos de juegos de PS2 desde archivos .ISO extraídos.
- **Recompilar**: Recompilar archivos de ensamblaje a código C.
- **Extracción de audio**: Extrae y decodifica pistas de audio (por ejemplo, archivos `.vag`) en formatos estándar como `.mp3` o `.wav`.
- **Procesamiento de modelos 3D**: Extrae y procesa datos de modelos 3D de archivos de juegos para su uso en herramientas 3D modernas.
- **Decodificación de archivos**: Maneja formatos específicos de PS2 como `.MB`, `.MH`, `.BD`, `.BH`, `.PSS`, `SLUS_XXX`, y más.
- **Descompilador integrado**: Utiliza Capstone para el desensamblado binario.
- **Alto rendimiento**: Diseñado para una extracción rápida y eficiente.
- **Retrox Engine**: Herramienta para portar archivos .C recompilados de PS2 a PC.

### **Contribuyendo**
Damos la bienvenida a las contribuciones para mejorar PSRetrox. Así es como puedes contribuir:

#### Contribución de código

1. Haz un fork del repositorio y crea tu rama de características:
`git checkout -b feature/TuCaracterística`

2. Realiza tus cambios y haz commit de ellos:
`git commit -m "Añadir TuCaracterística"`

3. Empuja tus cambios a tu fork:
`git push origin feature/TuCaracterística`

4. Abre una pull request en el repositorio principal.

#### **Directrices de código**
Usa un formato consistente y sigue las prácticas modernas de C++.

- Proporciona comentarios claros para la lógica compleja.

- Asegúrate de que tus cambios no rompan la funcionalidad existente.

- Reportando problemas

#### **Reportando problemas**

Si encuentras un error o tienes una solicitud de función, por favor abre un issue con una descripción detallada.
