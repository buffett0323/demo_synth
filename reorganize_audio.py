#!/usr/bin/env python3
"""
Audio Reorganization Script
Reorganizes audio files from the current structure to a new structure with 5 files per pair.
"""

import os
import shutil
from pathlib import Path

def reorganize_audio_files():
    """Reorganize audio files into new structure with 5 files per pair."""
    
    # Create new audio directory structure
    new_audio_dir = Path("audio_new")
    new_audio_dir.mkdir(exist_ok=True)
    
    # Get all pair numbers from the proposed folder
    proposed_dir = Path("proposed")
    no_ca_dir = Path("no_ca")
    
    # Find all unique pair numbers
    pair_numbers = set()
    for file_path in proposed_dir.glob("*.wav"):
        filename = file_path.stem  # Remove .wav extension
        if "_" in filename:
            pair_num = filename.split("_")[0]
            pair_numbers.add(pair_num)
    
    # Sort pair numbers for consistent ordering
    pair_numbers = sorted(list(pair_numbers))
    
    print(f"Found {len(pair_numbers)} pairs: {pair_numbers}")
    
    # Create new structure for each pair
    for pair_num in pair_numbers:
        pair_dir = new_audio_dir / f"pair{pair_num}"
        pair_dir.mkdir(exist_ok=True)
        
        print(f"Processing pair {pair_num}...")
        
        # Define source files for this pair
        # Use files from proposed folder for orig, ref, gt
        orig_file = proposed_dir / f"{pair_num}_orig.wav"
        ref_file = proposed_dir / f"{pair_num}_ref.wav"
        gt_file = proposed_dir / f"{pair_num}_gt.wav"
        
        # Use reconstruction files from respective folders
        proposed_recon_file = proposed_dir / f"{pair_num}_recon.wav"
        no_ca_recon_file = no_ca_dir / f"{pair_num}_recon.wav"
        
        # Copy files with new names
        files_to_copy = [
            (orig_file, pair_dir / "orig.wav"),
            (ref_file, pair_dir / "ref.wav"),
            (gt_file, pair_dir / "gt.wav"),
            (proposed_recon_file, pair_dir / "proposed_recon.wav"),
            (no_ca_recon_file, pair_dir / "no_ca_recon.wav")
        ]
        
        for src, dst in files_to_copy:
            if src.exists():
                shutil.copy2(src, dst)
                print(f"  Copied {src.name} -> {dst.name}")
            else:
                print(f"  WARNING: {src.name} not found!")
        
        print(f"  Completed pair {pair_num}")
        print()
    
    print(f"Reorganization complete! Created {len(pair_numbers)} pairs in {new_audio_dir}/")
    print(f"Each pair contains 5 audio files: orig, ref, gt, proposed_recon, no_ca_recon")
    
    return len(pair_numbers)

def update_html_for_new_structure(num_pairs):
    """Update the HTML file to work with the new 5-file structure."""
    
    # Create new HTML content for the new structure
    new_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Audio Pairs Collection - {num_pairs} Pairs</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Audio Pairs Collection</h1>
            <p>{num_pairs} pairs of audio data, each containing 5 WAV files</p>
            <p style="color: #4CAF50; font-weight: bold;">✓ New Structure: orig, ref, gt, proposed_recon, no_ca_recon</p>
        </header>
        
        <div class="audio-grid">
"""
    
    # Generate HTML for each pair
    for i in range(num_pairs):
        pair_num = f"{i:02d}"  # Format as 00, 01, 02, etc.
        new_html_content += f"""            <!-- Audio Pair {i+1} -->
            <div class="audio-pair">
                <h3>Audio Pair {i+1} (ID: {pair_num})</h3>
                <div class="audio-files">
                    <div class="audio-item">
                        <label>Original:</label>
                        <audio controls>
                            <source src="audio_new/pair{pair_num}/orig.wav" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-item">
                        <label>Reference:</label>
                        <audio controls>
                            <source src="audio_new/pair{pair_num}/ref.wav" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-item">
                        <label>Ground Truth:</label>
                        <audio controls>
                            <source src="audio_new/pair{pair_num}/gt.wav" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-item">
                        <label>Proposed Reconstruction:</label>
                        <audio controls>
                            <source src="audio_new/pair{pair_num}/proposed_recon.wav" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                    <div class="audio-item">
                        <label>No-CA Reconstruction:</label>
                        <audio controls>
                            <source src="audio_new/pair{pair_num}/no_ca_recon.wav" type="audio/wav">
                            Your browser does not support the audio element.
                        </audio>
                    </div>
                </div>
            </div>

"""
    
    # Add the closing HTML
    new_html_content += """        </div>

        <div class="controls">
            <button id="playAllBtn" class="control-btn">Play All</button>
            <button id="stopAllBtn" class="control-btn">Stop All</button>
            <button id="pauseAllBtn" class="control-btn">Pause All</button>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>"""
    
    # Write the new HTML file
    with open("index_new.html", "w") as f:
        f.write(new_html_content)
    
    print(f"Created new HTML file: index_new.html")
    print(f"Updated for {num_pairs} pairs with 5 audio files each")

def main():
    """Main function to run the reorganization."""
    print("Audio Reorganization Script")
    print("=" * 50)
    
    # Check if source directories exist
    if not Path("proposed").exists():
        print("ERROR: 'proposed' directory not found!")
        return
    
    if not Path("no_ca").exists():
        print("ERROR: 'no_ca' directory not found!")
        return
    
    # Reorganize the audio files
    num_pairs = reorganize_audio_files()
    
    # Update HTML for new structure
    update_html_for_new_structure(num_pairs)
    
    print("\n" + "=" * 50)
    print("NEXT STEPS:")
    print("1. Review the new structure in 'audio_new/' directory")
    print("2. Test the new HTML file: index_new.html")
    print("3. If satisfied, replace the old files:")
    print("   - rm -rf audio_new/")
    print("   - python3 reorganize_audio.py")
    print("   - mv index_new.html index.html")
    print("4. Deploy to GitHub Pages")

if __name__ == "__main__":
    main()
