NAME = posos-challenge
PWD = $(shell pwd)


.PHONY: build_train
build_train:
	docker build -f trainer.Dockerfile --tag $(NAME)_train .

.PHONY: train
train:
	docker run --rm \
	--mount type=bind,source=$(PWD),target=$(PWD) \
	 $(NAME)_train\

.PHONY: build_api
build_api:
	docker build -f api.Dockerfile --tag $(NAME)_api .

.PHONY: api
api:
	docker run -t --rm -p 8501:4002 \
    $(NAME)_api &

.PHONY: clean
clean:
	docker rm -f $(NAME)_exp 2> /dev/null || true