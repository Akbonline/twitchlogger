<!-- TABLE OF CONTENTS -->
## Table of Contents

* [twitchlogger](#twitchlogger)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
* [License](#license)
* [Contact](#contact)
* [Disclaimer](#disclaimer)

# twitchlogger
Contains the python based Advanced Keylogger Part-1 files, livecoded during AkB_C317's twtich stream on August 18th 2020. Link to the Stream: https://www.twitch.tv/videos/725629026

## Part 1:
1. Recording the keystrokes
2. Update the keystrokes every consecutive seconds(interval)
3. Capturing the system information
4. Take Screenshots
    
##### ISSUE: 
> There are redundant enteries in our file (RESOLVED! thanks to bokeh_joe)

## Part 2(To be done...):
5. Encryption of the log text file
6. Find a way to setup a remote server to send our logs
7. Embed our keylogger into an image file and deploy
8. Package and Convert our python files into a .exe file
9. Package our .py into .exe

<!-- GETTING STARTED -->
## Getting Started

Once you have downloaded the repo, to get the keylogger running follow these simple steps.

### Prerequisites

You'll need the following python modules before using the keylogger:
* keyboard (For recording the keystrokes)
```sh
pip install keyboard
```
* pyautogui (For taking the screenshots)
```sh
pip install pyautogui
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/Akbonline/twitchlogger.git
```

### Usage

1. Running the keylogger
```sh
python .\keylogger.py 'esc' 5 5
```
Notice the first argument 'esc' is the keyboard interrupt for stopping the keylogger, and the rest two args are the intervals for capturing the keystrokes and taking the screenshots.

### License

Distributed under the MIT License. See `LICENSE` for more information.

### Contact

My Socials:
* gitHub: [@https://github.com/Akbonline] (https://github.com/Akbonline)
* website: [@https://akbexpo.blogspot.com/] (https://akbexpo.blogspot.com/)
* Twitch: [@https://www.twitch.tv/akb_c317] (https://www.twitch.tv/akb_c317)
* YouTube: [@https://www.youtube.com/channel/UCPe0vD3pfd6WGSji2LAGufw] (https://www.youtube.com/channel/UCPe0vD3pfd6WGSji2LAGufw)
* instagram: [@https://www.instagram.com/akbon9/] (https://www.instagram.com/akbon9/)
* Twitter: [@https://twitter.com/akb_c317] (https://twitter.com/akb_c317)
* linkedIN: [@https://www.linkedin.com/in/akshat-bajpai-09/] (https://www.linkedin.com/in/akshat-bajpai-09/)

### Disclaimer

The material, information and techniques expressed during the stream or shown in this video are solely meant for educational purposes only. I am not responsible for any misuse of any information contained in the stream/video. The primary purpose of this stream/video is to educate and inform. 
The stream/video is available for public, non-commercial use only. Advertising which is incorporated into, placed in association with, or targeted toward the content of this stream/video, without the express approval or knowledge of the admin of this channel, is forbidden. You may not edit, modify, or redistribute this stream/video without the consent. I will assume no liability for any activities in connection with this stream/video or for use of this stream/video in connection with any other Web site, computer or playing device.
