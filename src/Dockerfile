FROM python:3.6
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
	apt-get install -y tzdata apt-utils

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#CMD ["python","app.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

# 
# WORKDIR /app

# 
#COPY ./requirements.txt /code/requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# # 
# COPY . /app
#EXPOSE 5000
# 
#CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
#CMD ["python","app.py"]