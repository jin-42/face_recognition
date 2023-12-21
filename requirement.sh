#!/bin/bash

# Fonction pour afficher un message d'erreur et quitter en cas de problème
function die {
    echo "Error: $1"
    exit 1
}

# Vérifier si pip est installé
if ! command -v pip &> /dev/null; then
    die "pip is not installed. Please install pip before running this script."
fi

# Installer face_recognition et matplotlib
echo "Installing requirements..."
pip install face_recognition matplotlib || die "Failed to install requirements. Check your internet connection and try again."

# Afficher un message de succès
echo "Requirements installed successfully"

