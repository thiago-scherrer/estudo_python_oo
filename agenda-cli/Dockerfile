FROM python:3

RUN useradd agenda-cli \
    && mkdir -p /home/agenda-cli/.local

WORKDIR /home/agenda-cli

COPY . .

RUN chown agenda-cli. /home/agenda-cli -R

USER agenda-cli

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "agenda/core.py" ]
