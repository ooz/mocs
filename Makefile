.PHONY: clean clean_coverage \
install_pipenv init test deploy \
all help newpost openlatest update

all: ## Build the site, generate all pages from *.md files
	pipenv run python gg.py ./

help: ## Show this help
	@grep -Eh '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

newpost: ## Create a new post .md file with current time
	pipenv run python gg.py --newpost

openlatest: ## Open the latest .md file in vim
	@ls -1t `find . -type f -name '*.md'` | head -n 1 | xargs -o vim

update: ## Update ggpy
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/gg.py -O gg.py
	wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Pipfile -O Pipfile
	@echo "Unfortunately the Makefile cannot be updated automatically!"
	@echo "Run the following command to update:"
	@echo "wget -q https://raw.githubusercontent.com/ooz/ggpy/master/Makefile -O Makefile"

# Setup / dependencies / CI/CD
install_pipenv: ## Install pipenv for initial setup or CI
	pip3 install pipenv

init: ## Initial setup of pipenv
	pipenv --python 3
	pipenv install

test: | clean_coverage ## Run ggpy tests
	pipenv install --dev
	pipenv run coverage run --source=. -m pytest -vv
	pipenv run coverage html --omit="test/*"
	pipenv run coverage report --omit="test/*"

deploy: all ## Build and publish by CI
	git add .
	git commit -m "Build by CircleCI `date` [skip ci]" || true
	git push

# Cleanup
clean: ## Cleanup python artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf .cache
	rm -rf dist
	rm -f *.egg-info
	pipenv --rm || true

clean_coverage: ## Cleanup python test coverage artifacts
	rm -rf htmlcov/
	rm -f .coverage
