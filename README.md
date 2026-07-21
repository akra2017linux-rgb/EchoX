# 🎵 EchoX - Modern Music Player for Windows

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-Modern%20UI-FF6B6B?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Windows](https://img.shields.io/badge/OS-Windows-0078D4?style=flat-square&logo=windows)](https://www.microsoft.com/windows)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)](https://github.com/akra2017linux-rgb/EchoX)

**A sleek, modern music player inspired by Spotify, built with Python and packed with powerful features for the ultimate listening experience.**

[🚀 Download Latest Release](#-download) • [📖 Documentation](#-documentation) • [🤝 Contributing](#-contributing) • [📝 License](#-license)

</div>

---

## ✨ Features

- **🎨 Modern Dark UI** - Sleek interface inspired by Spotify with dark theme (#121212) and accent green (#1DB954)
- **📁 Smart Folder Management** - Automatic MP3 detection with deep folder scanning for effortless music organization
- **🔍 Real-time Search** - Instant filtering to find your favorite songs as you type
- **🎲 Shuffle & Repeat** - Multiple playback modes including shuffle, repeat one, and repeat all
- **⌨️ Keyboard Shortcuts** - Quick access with F5-F8 shortcuts for seamless control
- **🖼️ Album Artwork** - Automatic extraction and display of album covers from MP3 ID3 tags
- **💾 Persistent Library** - Your music library and settings are saved between sessions
- **🚀 Fast & Lightweight** - Efficient performance with minimal resource usage

---

## 📸 Screenshots

> Screenshots coming soon. Check back for visual previews of the sleek EchoX interface!

---

## 🚀 Quick Start

### For End Users

#### Option 1: Download Pre-built Installer (Recommended) ⭐

1. Go to the [Releases](https://github.com/akra2017linux-rgb/EchoX/releases) page
2. Download the latest `EchoX-Setup.exe` installer
3. Run the installer and follow the setup wizard
4. Launch EchoX from your Start Menu or Desktop shortcut
5. Add music folders and start listening! 🎧

**[📥 Download Latest Release](https://github.com/akra2017linux-rgb/EchoX/releases)**

#### Option 2: Run from Source Code

**Requirements:**
- Windows 10 or later
- Python 3.8 or higher
- pip (Python package manager)

**Installation Steps:**

```bash
# Clone the repository
git clone https://github.com/akra2017linux-rgb/EchoX.git
cd EchoX

# Create virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| **F5** | Play / Pause |
| **F6** | Previous Track |
| **F7** | Next Track |
| **F8** | Toggle Shuffle |
| **Ctrl + S** | Open Settings |
| **Ctrl + F** | Focus Search Bar |

> **Pro Tip:** Global shortcuts work even when EchoX is minimized! 🎯

---

## 📦 Installation & Setup

### Complete Installation Guides

For detailed installation instructions, see:

- **[Complete Installation Guide](docs/INSTALLATION.md)** - Step-by-step setup for all methods
- **[FAQ & Troubleshooting](docs/FAQ.md)** - Answers to common questions

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **OS** | Windows 10 | Windows 11 |
| **RAM** | 512 MB | 2 GB+ |
| **Disk Space** | 50 MB | 100 MB |
| **CPU** | Intel Core i3 | Intel Core i5+ |

### Quick Requirements Installation

```bash
# From source code directory
pip install -r requirements.txt
```

**Key Dependencies:**
- `customtkinter` - Modern UI framework
- `pygame` - Audio playback engine
- `mutagen` - ID3 tag reading & metadata extraction
- `pyinstaller` - Executable building (if developing)

---

## 🛠️ For Developers

### Project Structure

```
EchoX/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── config.json            # User configuration
├── config_example.json    # Configuration template
├── ui/
│   ├── __init__.py
│   ├── main_window.py     # Main UI window
│   ├── components.py      # Reusable UI components
│   └── styles.py          # Theme and styling
├── audio/
│   ├── __init__.py
│   ├── player.py          # Audio playback engine
│   └── playlist.py        # Playlist management
├── utils/
│   ├── __init__.py
│   ├── file_scanner.py    # Music library scanner
│   ├── metadata.py        # ID3 tag reading
│   └── settings.py        # User settings management
├── docs/
│   ├── INSTALLATION.md    # Detailed setup guide
│   └── FAQ.md             # Frequently asked questions
└── build/
    └── inno_setup.iss     # Inno Setup configuration
```

### Setting Up Development Environment

```bash
# Clone and setup
git clone https://github.com/akra2017linux-rgb/EchoX.git
cd EchoX

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install pytest flake8 black  # Optional: for linting & formatting

# Run the application
python main.py
```

### Building the Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build the executable
pyinstaller main.spec

# The executable will be in the dist/ folder
```

### Creating the Installer

1. Install [Inno Setup](https://jrsoftware.org/isdl.php)
2. Open `build/inno_setup.iss` in Inno Setup
3. Compile to generate the installer executable

**Detailed build instructions:** [See INSTALLATION.md](docs/INSTALLATION.md)

---

## 🐛 Troubleshooting

### Issue: No sound when playing music

**Solution:**
- Ensure your audio drivers are up to date
- Check that the MP3 file format is supported
- Try reinstalling Pygame: `pip install --upgrade pygame`

### Issue: Album artwork not displaying

**Solution:**
- The MP3 file must have ID3v2 tags with embedded cover art
- Try using a tool like [MP3Tag](https://www.mp3tag.de/) to add covers to your files
- EchoX supports JPEG and PNG formats

### Issue: Application crashes on startup

**Solution:**
- Delete the config file: `%APPDATA%\EchoX\config.json`
- Reinstall Python dependencies: `pip install --upgrade -r requirements.txt`
- Check Event Viewer for detailed error information

**More troubleshooting:** [See FAQ.md](docs/FAQ.md)

---

## 📝 Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation, your help makes EchoX better.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write clear commit messages
- Test your changes before submitting a PR
- Update documentation as needed
- Be respectful and constructive in discussions

**Detailed contributing guide:** [See CONTRIBUTING.md](CONTRIBUTING.md)

---

## 🎯 Roadmap

### Version 1.1.0 (Planned)
- [ ] Playlist creation and management
- [ ] Audio equalizer with presets
- [ ] Improved search with advanced filters

### Version 1.2.0 (Planned)
- [ ] Lyrics display integration
- [ ] Dark/Light theme toggle
- [ ] Music library statistics and insights

### Future Releases
- [ ] Cross-platform support (Linux, macOS)
- [ ] Integration with online music services
- [ ] Community playlists and sharing
- [ ] Support for additional audio formats (FLAC, WAV, M4A)
- [ ] Advanced metadata editing

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License allows:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

With the requirement:
- ℹ️ Include license and copyright notice

---

## 🙏 Acknowledgments

### Libraries & Tools
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) - Modern UI framework
- [Pygame](https://www.pygame.org/) - Audio playback engine
- [Mutagen](https://mutagen.readthedocs.io/) - Audio metadata library
- [PyInstaller](https://pyinstaller.org/) - Executable creation
- [Inno Setup](https://jrsoftware.org/isinfo.php) - Windows installer

### Inspiration
- [Spotify](https://www.spotify.com/) - UI/UX design philosophy

---

## 📚 Documentation

- **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
- **[FAQ](docs/FAQ.md)** - Frequently asked questions
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Security Policy](SECURITY.md)** - Reporting vulnerabilities
- **[Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines
- **[Changelog](CHANGELOG.md)** - Version history

---

## 💬 Community & Support

### Get Help
- **Issues:** Report bugs and request features on [GitHub Issues](https://github.com/akra2017linux-rgb/EchoX/issues)
- **Discussions:** Join conversations on [GitHub Discussions](https://github.com/akra2017linux-rgb/EchoX/discussions)
- **FAQ:** Check [Frequently Asked Questions](docs/FAQ.md)
- **Email:** akra2017.linux@gmail.com

### Report a Bug

1. Check if the issue already exists on [GitHub Issues](https://github.com/akra2017linux-rgb/EchoX/issues)
2. If not, click "New Issue" and use the bug report template
3. Include: description, steps to reproduce, system info, and screenshots

### Suggest a Feature

1. Check if the feature is already planned in the [Roadmap](#-roadmap)
2. Check existing [Issues](https://github.com/akra2017linux-rgb/EchoX/issues) and [Discussions](https://github.com/akra2017linux-rgb/EchoX/discussions)
3. Open a new issue using the feature request template

---

## 🌟 Show Your Support

If you like EchoX, please consider:

- ⭐ **Star this repository** - It helps others discover the project
- 🐦 **Share it with friends** - Spread the word on social media
- 🤝 **Contribute improvements** - Report bugs or submit PRs
- 💬 **Provide feedback** - Share your thoughts and suggestions
- 🐛 **Report issues** - Help us find and fix bugs

---

## 📊 Project Stats

- **Language:** Python 3.8+
- **License:** MIT
- **Platform:** Windows 10/11
- **Latest Version:** 1.0.0
- **Status:** Active Development

---

## 🔐 Security

For security concerns, please see [SECURITY.md](SECURITY.md)

Report security vulnerabilities responsibly to: **akra2017.linux@gmail.com**

---

<div align="center">

### Made with ❤️ by [akra2017linux-rgb](https://github.com/akra2017linux-rgb)

**Happy listening! 🎵**

[⬆ Back to top](#-echox---modern-music-player-for-windows)

</div>