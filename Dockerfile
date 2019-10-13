FROM python 

ADD python-telegram-bot /var/etc/MyData

RUN pip install firebase_admin
RUN python /var/etc/MyData/python-telegram-bot/setup.py install 
RUN pip install python-telegram-bot --upgrade

WORKDIR /var/etc/MyData

CMD python3 conversationbot.py

