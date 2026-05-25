# Installation Instructions

## Quick Install for IBM Bob

```bash
# From the AI-TechByte/bob-watch-video directory
cp -r .bob/skills/watch-video ~/.bob/skills/watch-video
```

## Or Clone Directly

```bash
# Clone the entire AI-TechByte repository
git clone https://github.com/YOUR_USERNAME/AI-TechByte.git

# Copy the skill to Bob's skills directory
cp -r AI-TechByte/bob-watch-video/.bob/skills/watch-video ~/.bob/skills/watch-video
```

## Setup

1. **Configure API Keys (Optional)**
   ```bash
   cd ~/.bob/skills/watch-video
   cp .env.example .env
   # Edit .env and add your GROQ_API_KEY or OPENAI_API_KEY
   ```

2. **First Use**
   - Bob will automatically guide you through installing dependencies
   - On macOS: ffmpeg and yt-dlp install automatically via Homebrew
   - On Linux/Windows: Follow the on-screen instructions

3. **Try It**
   ```
   /watch https://youtu.be/VIDEO_ID
   ```

## Full Documentation

- [README.md](README.md) - Complete feature documentation
- [BOB_SETUP.md](.bob/skills/watch-video/BOB_SETUP.md) - Detailed setup guide
- [BOBIFICATION_SUMMARY.md](BOBIFICATION_SUMMARY.md) - Adaptation details

## Credits

Adapted from [claude-video](https://github.com/bradautomates/claude-video) by Bradley Bonanno ([@bradautomates](https://github.com/bradautomates))