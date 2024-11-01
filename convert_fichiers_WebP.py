from PIL import Image
import os

def convert_png_to_webp(input_folder):
    # Parcourt tous les fichiers du dossier
    for filename in os.listdir(input_folder):
        # Vérifie si le fichier a l'extension .png
        if filename.endswith(".png"):
            png_path = os.path.join(input_folder, filename)
            webp_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            # Ouvre l'image PNG, la convertit en WebP et la sauvegarde
            with Image.open(png_path) as img:
                img.save(webp_path, "WEBP")
            
            # Supprime le fichier PNG original
            os.remove(png_path)
            print(f"Converted and deleted: {filename} -> {os.path.basename(webp_path)}")

# Exemple d'utilisation
input_folder = 'C:\\Users\\nathanael\\Desktop\\GamemodeAssets\\clothing\\male\\mask'
convert_png_to_webp(input_folder)

