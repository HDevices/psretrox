from googletrans import Translator

def sync_and_translate(file_path):
    translator = Translator()

    # Lista de frases que no deben ser traducidas
    exclusions = ["- **Retrox Engine**:"]

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Define los rangos de líneas para inglés y español
    english_start, english_end = 9, 70
    spanish_start = 70

    # Extraer contenido en inglés para traducir (excluyendo líneas específicas)
    english_content = []
    for i in range(english_start, english_end):
        line = lines[i]
        if i < 19 or i > 27:  # Excluir líneas 19-27 (imágenes de progreso)
            # Verificar si la línea contiene una frase excluida
            if any(exclusion in line for exclusion in exclusions):
                english_content.append(line)  # Mantener la línea intacta
            else:
                english_content.append(line)

    # Traducir el contenido al español
    english_text = ''.join(english_content)
    translated_text = translator.translate(english_text, src='en', dest='es').text

    # Reemplazar las frases excluidas en el texto traducido
    for exclusion in exclusions:
        translated_text = translated_text.replace(translator.translate(exclusion, src='en', dest='es').text, exclusion)

    # Actualizar la sección en español
    spanish_content = lines[spanish_start:]
    updated_content = (
        lines[:spanish_start] +  # Mantener todo antes de la sección en español
        [f"## Español\n\n"] +  # Agregar el encabezado de la sección en español
        translated_text.splitlines(keepends=True) +  # Agregar el contenido traducido
        spanish_content[len(spanish_content):]  # Mantener cualquier contenido restante
    )

    # Escribir el contenido actualizado de nuevo en el archivo
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_content)

    print("README.md ha sido sincronizado y traducido.")

# Ruta al archivo README.md
readme_path = "/home/h/psretrox/psretrox/README.md"
sync_and_translate(readme_path)