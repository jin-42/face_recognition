#!/bin/bash

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "Error: pip is not installed. Please install pip before running this script."
    exit 1
fi

# Install face_recognition
pip install face_recognition

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Requirements installed successfully"
else
    echo "Error: Failed to install requirements. Please check your internet connection and try again."
    exit 1
fi

