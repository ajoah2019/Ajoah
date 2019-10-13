FROM python 

RUN pip3 install firebase_admin
RUN pip3 install telegram
ADD examples /var/etc/MyData

WORKDIR /var/etc/MyData

CMD python3 conversationbot.py

