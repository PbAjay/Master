if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/PbAjay/Master.git /Master
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Master
fi
cd /Master
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
