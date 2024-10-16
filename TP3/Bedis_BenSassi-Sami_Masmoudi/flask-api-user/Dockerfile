from flaskappv0:latest

#RUN useradd -m newuser #Deja Fait

#RUN su - newuser #Deja Fait

RUN apt-get update && apt-get install -y locales && \
    locale-gen fr_FR.UTF-8 && \
    update-locale LANG=fr_FR.UTF-8
