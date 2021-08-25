FROM python:3
COPY . /app
RUN pip install -r /app/requirements.txt
CMD python /app/main.py --color=color --width=2048 --height=2048 --mode=3tan_sqrt
