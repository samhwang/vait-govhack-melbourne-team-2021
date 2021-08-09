##############
# BASE LAYER #
##############
FROM python:3.8-buster as base
RUN pip3 install pipenv
ENV PYROOT /pyroot
ENV PATH ${PYROOT}/bin:$PATH
ENV PYTHONUSERBASE ${PYROOT}

#####################
# DEVELOPMENT IMAGE #
#####################
FROM base as development
WORKDIR /src
COPY Pipfile Pipfile.lock ./
RUN pipenv install \
    --system \
    --deploy \
    --ignore-pipfile \
    --dev

COPY . .

ENV FLASK_ENV=development
CMD ["flask", "run", "--host=0.0.0.0"]

###############
# BUILD STAGE #
###############
FROM development as build
RUN pipenv install \
    --system \
    --deploy \
    --ignore-pipfile

####################
# PRODUCTION IMAGE #
####################
FROM python:3.8-buster-slim as production

ENV PYROOT /pyroot
ENV PATH ${PYROOT}/bin:$PATH
ENV PYTHONUSERBASE ${PYROOT}
ENV PYTHONPATH $PYROOT/lib/python:$PATH

COPY --from=build ${PYROOT}/lib/ ${PYROOT}/lib/
COPY --from=builder ${PYROOT}/bin/ ${PYROOT}/bin/

USER daemon
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
