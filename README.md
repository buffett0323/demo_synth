# Audio Pairs Collection Website

A modern, responsive website showcasing 32 pairs of audio data, each containing 5 WAV files. Built for deployment on GitHub Pages.

## Features

- **32 Audio Pairs**: Each pair contains 5 WAV audio files
- **5 Audio Types**: orig, ref, gt, proposed_recon, no_ca_recon
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Modern UI**: Beautiful gradient background with card-based layout
- **Audio Controls**: Individual audio controls for each file
- **Bulk Operations**: Play All, Stop All, and Pause All functionality
- **Search Functionality**: Filter audio pairs by name
- **Keyboard Shortcuts**: Ctrl+P (Play All), Ctrl+S (Stop All), Ctrl+Space (Pause All)
- **Visual Feedback**: Hover effects, animations, and status indicators
- **Accessibility**: Proper labels and keyboard navigation

## File Structure

```
demo_githubio/
├── index.html          # Main HTML file
├── styles.css          # CSS styling and responsive design
├── script.js           # JavaScript functionality
├── README.md           # This file
└── audio/              # Audio files directory
    ├── pair00/
    │   ├── orig.wav
    │   ├── ref.wav
    │   ├── gt.wav
    │   ├── proposed_recon.wav
    │   └── no_ca_recon.wav
    ├── pair01/
    │   ├── orig.wav
    │   ├── ref.wav
    │   ├── gt.wav
    │   ├── proposed_recon.wav
    │   └── no_ca_recon.wav
    └── ... (continues for all 32 pairs)
```

## Audio Requirements

- **Format**: WAV files
- **Total Files**: 160 WAV files (32 pairs × 5 files per pair)
- **File Types per Pair**:
  - `orig.wav` - Original audio
  - `ref.wav` - Reference audio
  - `gt.wav` - Ground truth audio
  - `proposed_recon.wav` - Proposed reconstruction
  - `no_ca_recon.wav` - No-CA reconstruction

## Deployment to GitHub Pages

### Method 1: Automatic Deployment (Recommended)

1. **Create a new repository** on GitHub
   - Repository name: `yourusername.github.io` (replace `yourusername` with your actual GitHub username)
   - Make it public
   - Don't initialize with README, .gitignore, or license

2. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/yourusername/yourusername.github.io.git
   cd yourusername.github.io
   ```

3. **Copy all project files** to the repository folder:
   - `index.html`
   - `styles.css`
   - `script.js`
   - `README.md`
   - `audio/` directory with all 32 pairs

4. **Commit and push** your changes:
   ```bash
   git add .
   git commit -m "Initial commit: Audio Pairs Collection Website - 32 pairs with 5 audio files each"
   git push origin main
   ```

5. **Wait for deployment**: GitHub Pages will automatically deploy your site within a few minutes

6. **Access your site**: Visit `https://yourusername.github.io`

### Method 2: Manual Deployment

1. **Create a new repository** on GitHub (any name)
2. **Upload all files** including the audio files
3. **Go to Settings** → **Pages**
4. **Source**: Select "Deploy from a branch"
5. **Branch**: Select `main` (or `master`)
6. **Folder**: Select `/ (root)`
7. **Click Save**

## Customization

### Changing Colors
Edit `styles.css` to modify the color scheme:
- Primary gradient: Lines 18-19
- Button colors: Lines 108-130
- Text colors: Lines 25, 60, 75

### Adding More Audio Pairs
1. Copy an existing audio pair div in `index.html`
2. Update the pair number and file paths
3. Add corresponding CSS animations in `styles.css`
4. Update the JavaScript if needed

### Modifying Audio Controls
Edit `script.js` to:
- Change keyboard shortcuts (lines 95-107)
- Modify bulk operations (lines 20-65)
- Add new functionality

## Browser Compatibility

- ✅ Chrome (recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Edge
- ⚠️ Internet Explorer (limited support)

## Performance Notes

- Audio files are loaded on-demand
- Responsive grid layout adapts to screen size
- Smooth animations with CSS transitions
- Efficient event handling for multiple audio elements

## Troubleshooting

### Audio Not Playing
- Ensure WAV files are properly formatted
- Check file paths in HTML
- Verify browser supports WAV format
- Check browser console for errors

### Site Not Loading
- Verify repository is public
- Check GitHub Pages settings
- Ensure `index.html` is in the root directory
- Wait a few minutes for deployment

### Layout Issues
- Clear browser cache
- Check CSS file is properly linked
- Verify responsive breakpoints in CSS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Review browser console for errors
3. Verify all files are properly uploaded
4. Check GitHub Pages deployment status

---

**Note**: Make sure your WAV files are properly formatted for the best user experience. The website will work without audio files, but the audio controls will show errors.
