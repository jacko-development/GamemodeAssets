import os

# Chemin vers le dossier contenant les images
dossier = 'C:\\Users\\natha\\Desktop\\GamemodeAssets\\clothing\\male\\tshirts'
# Parcours de tous les fichiers dans le dossier
for filename in os.listdir(dossier):
    # Vérifie si le fichier commence par "male_5_"
    if filename.startswith('male_8_'):
        # Extraire la partie du fichier après "male_5_"
        new_name = filename.replace('male_8_', '', 1)
        # Renommer le fichier
        os.rename(os.path.join(dossier, filename), os.path.join(dossier, new_name))

print("Renommage terminé!")
