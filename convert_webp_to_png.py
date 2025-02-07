import os
from PIL import Image

def convert_webp_to_png(input_folder):
    # Parcourt tous les fichiers du dossier
    for filename in os.listdir(input_folder):
        # Vérifie si le fichier a l'extension .webp
        if filename.endswith(".webp"):
            webp_path = os.path.join(input_folder, filename)
            png_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.png")
            
            # Ouvre l'image WebP, la convertit en PNG et la sauvegarde
            with Image.open(webp_path) as img:
                img.save(png_path, "PNG")
            
            # Supprime le fichier WebP original
            os.remove(webp_path)
            print(f"Converted and deleted: {filename} -> {os.path.basename(png_path)}")

# Exemple d'utilisation
input_folder = 'C:\\Users\\nathanael\\Desktop\\GamemodeAssets\\vehicles'
convert_webp_to_png(input_folder)
