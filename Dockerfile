FROM python:3.10

EXPOSE 80

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
COPY ./prediction_transforms.py /code/prediction_transforms.py
COPY ./app.py /code/app.py
COPY ./scheduling_algo.py /code/scheduling_algo.py
COPY ./models /code/models
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "app:app","--host","0.0.0.0","--port","80"]