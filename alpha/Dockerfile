FROM ubuntu:18.04


RUN apt-get update && \
    apt-get install -y python3.8 python3.8-dev python3.8-disutils build-essential ca-certificates curl openjdk-8-jdk-headless vim && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --set python /usr/bin/python3.8 && \
    curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean


COPY dist/*.whl /tmp/
RUN LATEST_WHL=$(ls -v /tmp/alpha-*.whl | tail -n 1) && \
    pip3 --no-cache-dir install $LATEST_WHL && \
    rm -rf /tmp/alpha-*.whl

ENTRYPOINT ["python", "-m", "src.main"]
