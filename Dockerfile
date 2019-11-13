FROM python:alpine
RUN pip install requests
WORKDIR /checkbuild
COPY checkbuild.py .
ENTRYPOINT [ "python", "checkbuild.py" ]