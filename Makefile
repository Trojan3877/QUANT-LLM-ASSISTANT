# Makefile for Quant LLM Assistant

.PHONY: lint test build install docker-build deploy clean docs serve-docs

# Lint code with flake8
lint:
	flake8 src/ tests/

# Run tests with pytest
test:
	pytest --maxfail=1 --disable-warnings -v

# Install Python dependencies
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Build project (install deps)
build: install

# Build Docker image
docker-build:
	docker build . -t quant-llm-assistant:latest

# Deploy to Kubernetes (manifests in k8s/)
deploy:
	kubectl apply -f k8s/

# Remove Python caches and reports
clean:
	rm -rf __pycache__ src/__pycache__ tests/__pycache__ build/ dist/ reports/

# Generate and serve docs with MkDocs
docs:
	mkdocs build

serve-docs:
	mkdocs serve

git add Makefile
git commit -m "Add Makefile for common tasks: lint, test, build, docker-build, deploy, docs"
