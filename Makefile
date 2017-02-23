dev:
	dev_appserver.py . --log_level=debug --host=0.0.0.0 --admin_host=0.0.0.0

test:
	python -m unittest discover -p '*_test.py'

deploy:
	gcloud app deploy app.yaml
