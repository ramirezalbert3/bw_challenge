FROM alpine
MAINTAINER https://github.com/ramirezalbert3

RUN apk add --no-cache py3-pip

RUN pip3 install --upgrade pip \
    && pip3 install flask
# Do not run with root permissions
# but we should assign a password
RUN adduser -D serveradmin

COPY server.py /srv/server.py
RUN chown serveradmin:serveradmin /srv/server.py

USER serveradmin

WORKDIR /srv/
ENTRYPOINT [ "python3" ]
CMD [ "server.py" ]
