# Pisky
A Raspberry Pi-powered photo frame using a WaveShare 7.5 inch HD e-ink display.

## Table of content
- [Pisky](#pisky)
  - [Table of content](#table-of-content)
  - [Motivation](#motivation)
  - [Screenshots](#screenshots)
  - [Installation \& Usage](#installation--usage)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Contributing](#contributing)
  - [History](#history)
  - [Credits](#credits)
  - [License](#license)

## Motivation
The motivation behind this project stemmed from a desire to utilize an e-ink display, known for its low power consumption and paper-like appearance, ideal for creating a minimalist home decor piece that seamlessly integrates into any environment. Inspired by the concept of slow technology, which emphasizes mindfulness and deliberate interaction with devices, the project aims to offer a serene and unobtrusive way to display a rotating gallery of images. This setup not only enhances the aesthetic appeal of the space but also encourages a more contemplative viewing experience compared to traditional digital displays.

## Screenshots
TODO: Screenshots of the project

## Installation & Usage
### Installation
1. **Install Dependencies:**
   - Ensure your Raspberry Pi is running Raspbian OS with internet access.
   - Install required packages and libraries:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pip python3-pil python3-rpi.gpio
     sudo pip3 install waveshare_epd
     ```

2. **Download the Script:**
   - Download the script to your Raspberry Pi:
     ```bash
     wget https://raw.githubusercontent.com/gitzain/piksy/master/piksy.py
     ```
     Or clone the repository if using Git:
     ```bash
     git clone https://github.com/gitzain/piksy.git
     ```

### Usage

1. **Run the Script:**
   - Navigate to the directory containing your script:
     ```bash
     cd /path/to/your/script
     ```
   - Execute the script:
     ```bash
     python3 piksy.py
     ```


## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Added some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D



## History
09/04/22: v1 published to github. 



## Credits
- Created by <a href="https://iamzain.com">Zain Khan</a>.
- Template for this README is <a href="https://github.com/gitzain/template-README">template-readme</a> created by <a href="https://iamzain.com">Zain Khan</a>



## License
See the LICENSE file in this project's directory.
