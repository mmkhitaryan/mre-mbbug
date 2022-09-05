FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt install -y git make gcc
WORKDIR /home/radare2
RUN git clone https://github.com/radareorg/radare2.git --depth 1
RUN radare2/sys/install.sh
RUN pip install r2pipe

WORKDIR /code
COPY . /code/

ENTRYPOINT ["sh", "r2.sh"]