import face_recognition
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Message d'accueil
print("╔════════════════════════════════════╗")
print("║ Welcome to the Where is the Face? ║")
print("╚════════════════════════════════════╝")
print()
print("Discover the magic of face recognition.")
print()

# Obtenir le chemin de l'image manuellement
image_path = input("Enter the path of the image file: ")

# Chargement de l'image
print(f"Loading image from: {image_path}")
image = face_recognition.load_image_file(image_path)

# Détection des visages
print("Detecting faces...")
face_locations = face_recognition.face_locations(image)

# Affichage des résultats
if face_locations:
    print("Found faces at the following locations:")
    
    # Affichage de l'image avec les rectangles autour des visages
    plt.imshow(image)
    ax = plt.gca()
    
    for face_location in face_locations:
        top, right, bottom, left = face_location
        width = right - left
        height = bottom - top
        
        # Création d'un rectangle autour du visage
        rect = patches.Rectangle((left, top), width, height, linewidth=2, edgecolor='r', facecolor='none')
        
        # Ajout du rectangle à l'axe
        ax.add_patch(rect)

    plt.show()

else:
    print("No faces were found in the image.")

