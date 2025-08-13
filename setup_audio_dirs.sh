#!/bin/bash

# Audio Pairs Collection - Directory Setup Script
# This script creates the directory structure for 16 audio pairs

echo "Setting up audio directory structure for Audio Pairs Collection..."

# Create main audio directory
mkdir -p audio

# Create directories for all 16 pairs
for i in {1..16}; do
    mkdir -p "audio/pair$i"
    echo "Created directory: audio/pair$i"
done

echo ""
echo "Directory structure created successfully!"
echo ""
echo "Next steps:"
echo "1. Add your WAV files to each pair directory:"
echo "   - audio/pair1/file1.wav"
echo "   - audio/pair1/file2.wav"
echo "   - audio/pair1/file3.wav"
echo "   - audio/pair1/file4.wav"
echo "   (repeat for pairs 2-16)"
echo ""
echo "2. Ensure each WAV file is exactly 1 second long"
echo "3. Use the naming convention: file1.wav, file2.wav, file3.wav, file4.wav"
echo ""
echo "Total directories created: 16"
echo "Total WAV files needed: 64 (16 pairs × 4 files per pair)"
