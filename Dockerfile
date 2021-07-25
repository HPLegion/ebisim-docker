
FROM python:3.8-slim

RUN apt-get update && apt-get install -y git

RUN pip install git+https://github.com/HPLegion/ebisim#egg=ebisim

# This container should work without root priviliges
# Some writeable caches are required (recommended)
ENV NUMBA_CACHE_DIR=/tmp/numba_cache MPLCONFIGDIR=/tmp/mpl_cache
RUN mkdir $NUMBA_CACHE_DIR $MPLCONFIGDIR && chmod 777 $NUMBA_CACHE_DIR $MPLCONFIGDIR

CMD /bin/bash
