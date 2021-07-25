.PHONY: build push test

CONTAINERTAG = hplegion/ebisim

build:
	docker build . -t $(CONTAINERTAG)

push:
	docker push $(CONTAINERTAG)

test:
	docker run -v $(shell pwd):/scratch -w /scratch -it -u $(shell id -u):$(shell id -g) $(CONTAINERTAG) ./test.py