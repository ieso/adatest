FROM jupyter/base-notebook

USER root
WORKDIR	/tmp

RUN apt-get update && apt-get -y install gcc mono-mcs
RUN apt-get -y install g++ 

COPY --chown=1000 . .

RUN pip install transformers
RUN pip install openai
RUN pip install torch
RUN pip install ipywidgets
RUN pip install .


EXPOSE 8888/tcp
ENV JUPYTER_TOKEN="TEST"
ENV DOCKER_STACKS_JUPYTER_CMD="notebook"
