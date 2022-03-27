sudo apt-get update
sudo apt install python3-pip -y
wget https://github.com/yuya-takeyama/percentile/releases/download/v0.0.1/linux_amd64_0.0.1.zip -o percentile.zip
unzip percentile.zip
wget https://github.com/yuya-takeyama/ntimes/releases/download/v0.1.0/linux_amd64_0.1.0.zip -o ntimes.zip
unzip ntimes.zip
./ntimes -- curl https://api.binance.com/api/v3/ping -s -o /dev/null -w  "%{time_starttransfer}\n" | ./percentile