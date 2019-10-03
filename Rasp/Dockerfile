FROM python

RUN mkdir -p /var/etc/MyData
RUN apt-get install python

add ajoah_toilet_monitor.py /var/etc/MyData/ajoah_toilet_monitor.py

WORKDIR /var/etc/MyData

CMD python ajoah_toilet_monitor.py



