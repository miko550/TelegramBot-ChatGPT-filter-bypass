# TelegramBot-ChatGPT-filter-bypass
Simple Python Server for Telegram Bot that allows you to bypass content filtering in ChatGPT. This calls the OpenAI autocompletion API for DaVinci-003.

## Setup in Python Enviroment
1. Clone repository
  ```bash
  git clone https://github.com/miko550/TelegramBot-ChatGPT-filter-bypass.git
  cd TelegramBot-ChatGPT-filter-bypass
  ```
2. create and active python virtual environment
  ```bash
  virtualenv venv
  source venv/bin/activate
  ```
3. Install requirement
  ```bash
  pip install -r requirements.txt
  ```
4. Replace `YOUR_BOT_TOKEN` and `YOUR_API_KEY` in telebot.py
5. Run Server 
  ```bash
  python3 telebot.py
  ```



## Setup in Docker
1. Clone repository
  ```bash
  git clone https://github.com/miko550/TelegramBot-ChatGPT-filter-bypass.git
  cd TelegramBot-ChatGPT-filter-bypass
  ```
2. Replace `YOUR_BOT_TOKEN` and `YOUR_API_KEY` in telebot.py
3. Create a Docker network
  ```bash
  docker network create bridge-net
  ```
4. Built Docker Image
  ```bash
  docker build --network bridge-net -t miko/chatgpt-telebot .
  ```
  * if error try
  ```
  docker build --network host -t miko/chatgpt-telebot .
  ```
5. Run Docker Container
  ```bash
  docker run -d --network bridge-net --name chatgpt-telebot  miko/chatgpt-telebot
  ```

# Reference
- https://github.com/GrimOutlaw/ChatGPT-Bypass
