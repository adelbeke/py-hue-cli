# hue-cli

A CLI tool to control Philips Hue lights from the terminal.

Disclaimer: This project is for learning purposes but meant to be used.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

On first run, a `config.json` is generated with your Hue Bridge IP and API key. This file is gitignored — do not commit it.

## Usage

```bash
python main.py --help
```
