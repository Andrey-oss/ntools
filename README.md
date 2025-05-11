# NTools v1.2-5

**NTools** is a very simple graphical tool for basic network diagnostics and information lookup. It uses `tkinter` for the interface and `requests` to fetch external IP and ISP data.

## Features

- Show your external IP address
- Check IP forwarding status
- Display your ISP name and hostname
- Basic help dialog
- Clean and minimal GUI
- Show some debug information (for future developers)

## Requirements

- Python 3.x
- `requests` library (install below)

## Installation

Clone the repository and install the required Python package:

```bash
git clone https://github.com/Andrey-oss/ntools.git
cd ntools
pip3 install requests
```

## Usage

Run the application:

```bash
python ntools.py
```

## Notes

- Requires an active internet connection for full functionality
- GUI built with `tkinter`, which is included with most Python installations
