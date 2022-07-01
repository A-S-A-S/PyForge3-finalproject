FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# here we create non-root user, home dir & make sure bash is default shell
RUN useradd --create-home --shell /bin/bash app

WORKDIR /home/app

COPY ./requirements.txt ./

RUN apt-get update && apt-get install -y netcat
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER app

COPY . .

# ENTRYPOINT ["./entrypoint.sh"]
# ENTRYPOINT [ "python", "main.py" ]
ENTRYPOINT ["bash"]
