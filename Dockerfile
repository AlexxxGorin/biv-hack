FROM python:3.11

COPY requirements.txt setup.py /workdir/

WORKDIR /workdir

COPY payments_main.tsv /workdir/payments_main.tsv
COPY inference.py /workdir/inference.py

RUN pip install -U -e .

ENTRYPOINT ["python", "/workdir/inference.py"]
