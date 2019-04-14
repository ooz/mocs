all:
	pipenv run python gg.py ./

fire: all
	git commit -am "Lazy auto update `date`" || true
	git push

realfire: all
	git commit -am "Emergency update `date`" || true
	git push -f origin master

newpost:
	bash newpost.sh

# Uhhh, manual effort needed every year! Fix!
openlatest:
	@vim 2018/`ls 2018/ -t | head -n 1`

update:
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/gg.py -O gg.py
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Pipfile -O Pipfile
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/newpost.sh -O newpost.sh
	@echo "Unfortunately the Makefile cannot be updated automatically!"
	@echo "Run the following command to update:"
	@echo "wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Makefile -O Makefile"

# Setup / dependencies
install_pipenv:
	pip3 install pipenv

init:
	pipenv --python 3
	pipenv install

test: all
	pipenv install --dev
	pipenv run pytest

# Cleanup
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .cache
	rm -rf dist
	rm -f *.egg-info
	pipenv --rm || true

.PHONY: clean \
install_pipenv init test \
all fire realfire newpost openlatest update
