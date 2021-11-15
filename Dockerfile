FROM python:3.8.1

COPY . /source_code
WORKDIR /source_code

RUN apt-get update

RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh 
RUN conda env create -f conda.yaml
RUN conda activate my_project
RUN pip install -e ./
 
ENV PORT=5000
EXPOSE ${PORT}

CMD ["python3.8", "source_code.application.server:app", "-b", "0.0.0.0:5000"]