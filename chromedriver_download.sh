mkdir downloads
cd downloads
# wget https://chromedriver.storage.googleapis.com/111.0.5563.19/chromedriver_win32.zip
wget https://chromedriver.storage.googleapis.com/111.0.5563.19/chromedriver_linux64.zip
# wget https://chromedriver.storage.googleapis.com/112.0.5615.28/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
# wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo apt install ./google-chrome-stable_current_amd64.deb -y
# sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt update -y
sudo apt install chromium-chromedriver -y