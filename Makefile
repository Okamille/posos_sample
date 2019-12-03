NAME = posos-challenge
PWD = $(shell pwd)
UID = $(shell id -u)
GID = $(shell id -g)


.PHONY: train
train:
	docker build -f Dockerfile --tag $(NAME)_exp\
			--build-arg uid=$(UID)\
			--build-arg gid=$(GID)\

.PHONY: clean
clean:
	docker rm -f $(NAME)_exp 2> /dev/null || true