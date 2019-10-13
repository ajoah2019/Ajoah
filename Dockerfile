FROM python 

ADD python-telegram-bot /var/etc/MyData
WORKDIR /var/etc/MyData

RUN pip install -U setuptools pip
RUN pip install firebase_admin
RUN pip install python-telegram-bot --upgrade
RUN ls
RUN python setup.py install 

WORKDIR /var/etc/MyData/examples
CMD python3 conversationbot.py

