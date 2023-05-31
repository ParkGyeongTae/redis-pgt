FROM ubuntu:20.04

LABEL name='ParkGyeongTae'
LABEL email='pgt0409@gmail.com'

USER root

RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa -y && \
    apt update && \
    apt install python3-pip -y && \
    pip install --upgrade pip

RUN ln -s /usr/bin/python3.8 /usr/bin/python

COPY ./python_settings/requirements.txt /opt/requirements.txt

RUN pip install -r /opt/requirements.txt && \
    pip freeze > /opt/requirements-result.txt

WORKDIR /code

# DEBIAN_FRONTEND=noninteractive
#     apt install vim -y && \
#     apt install net-tools -y && \
#     apt install iputils-ping -y

# RUN /usr/local/bin/python -m pip install --upgrade pip

# COPY ./asset/requirements.txt /opt/requirements.txt

# RUN pip install -r /opt/requirements.txt && \
#     pip freeze > /opt/requirements-result.txt
#     # bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)

# RUN mkdir /code && \
#     mkdir /result && \
#     chmod -R 777 /code && \
#     chmod -R 777 /result

# COPY ./code /code
# COPY ./result /result

# WORKDIR /code

# ENTRYPOINT bash