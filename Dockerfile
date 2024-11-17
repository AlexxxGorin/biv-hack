FROM python:3.11

COPY requirements.txt setup.py /workdir/

WORKDIR /workdir

COPY turbo_bert /workdir/turbo_bert
COPY inference.py /workdir/inference.py

RUN pip install -U -e .

ENTRYPOINT ["python", "/workdir/inference.py"]