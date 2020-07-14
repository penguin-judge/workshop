FROM python:3.7-slim

WORKDIR /penguin

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y install git vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy==1.17.4 scipy==1.3.2 scikit-learn==0.21.3 \
    && pip install git+https://github.com/penguin-judge/rime.git \
    && rm -rf ~/.cache

ENTRYPOINT ["/bin/bash", "-c"]
