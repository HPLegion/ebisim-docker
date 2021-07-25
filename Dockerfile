
FROM python:3.8-slim

RUN apt-get update && apt-get install -y git
RUN pip install git+https://github.com/HPLegion/ebisim#egg=ebisim

CMD /bin/bash
