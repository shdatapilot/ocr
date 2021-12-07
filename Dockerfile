FROM python:3.8.12-slim
COPY . /app
WORKDIR /app

RUN apt update
RUN apt install libgl1
RUN apt install libsm6
RUN apt install libxrender1
RUN apt install libfontconfig1
RUN apt install libice6
RUN apt install libgl1-mesa-glx
RUN apt install libglib2.0-0

RUN pip install -r requirements.txt
EXPOSE 80

RUN mkdir ~/.streamlit
RUN cp config.toml ~/.streamlit/config.toml
RUN cp credentials.toml ~/.streamlit/credentials.toml
RUN cp AAntiCorona-L3Ax3.ttf /app/AAntiCorona-L3Ax3.ttf

WORKDIR /app
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]