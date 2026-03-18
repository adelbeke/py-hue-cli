# py-hue

A CLI tool to control Philips Hue lights from the terminal.

<img width="900" height="340" alt="Screenshot 2026-03-18 at 23 47 31" src="https://github.com/user-attachments/assets/50141644-a101-4683-8e7f-1fb373fef198" />

Disclaimer: This project is for learning purposes but meant to be used.

## Roadmap

- [ ] Update brightness
- [ ] Update color

## Installation

### Local (development)

```bash
make install
source .venv/bin/activate
```

### Global (recommended)

```bash
brew install pipx
pipx ensurepath
pipx install -e .
```

## Configuration

On first run, a `config.json` is generated with your Hue Bridge IP and API key. This file is gitignored — do not commit it.

## Usage

```bash
py-hue --help
```
