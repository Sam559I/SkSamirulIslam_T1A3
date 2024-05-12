#!/bin/bash

# Check if Python 3 is installed
if command -v python3 &>/dev/null; then
    python3_version=$(python3 --version 2>&1)
    if [[ $python3_version == *"Python 3"* ]]; then
        echo "Python 3 is installed and the default version."

        # Install rich package
        echo "Installing rich package..."
        python3 -m pip install rich
        echo "rich package installed successfully."

        # Install art package
        echo "Installing art package..."
        python3 -m pip install art
        echo "art package installed successfully."

        # install color50 package
        echo "Installing color50  package..."
        python3 -m pip install color50 
        echo "color50  package installed successfully."
        
    else
        echo "Python 3 is installed but not the default version."
    fi
else
    echo "Python 3 is not installed."
fi
