from goodwaygroup/ubuntu1604-python36:latest

RUN apt-get update

RUN pip install pandas

RUN pip install xlrd

RUN pip install scikit-learn

COPY . /avarali/

ENTRYPOINT ["python"]

CMD ["/avarali/classifyIMDCycloneData.py"]