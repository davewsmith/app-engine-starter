dev:
	dev_appserver.py . --log_level=debug --host=0.0.0.0

test:
	python -m unittest discover -p '*_test.py'

deploy:
	@[ -z "${APP}"] && echo "Set APP to application ID and try again"
	@[ -z "${APP}"] && exit 1

	@echo "Reminder: deploy make require 'gcloud init'"
	@echo deploying...

