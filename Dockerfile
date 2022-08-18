FROM python:3.8

WORKDIR /fastapi_crud

COPY requirements.txt .

RUN pip install -U pip && pip install -r requirements.txt

COPY initializer.sh .

COPY . /fastapi_crud

RUN chmod +x initializer.sh

EXPOSE 8000

ENTRYPOINT [ "./initializer.sh" ]

