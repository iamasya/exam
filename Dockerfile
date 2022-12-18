FROM python
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY . /exam
WORKDIR /exam
CMD ["python3", "exam.py"]