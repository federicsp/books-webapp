.PHONY: json_to_db

json_to_db:
	@echo "Importing JSON to DB..."
	python manage.py runscript importer