VIRTUALENV_PATH:=virtualenv

serve: ./virtualenv
	python manage.py runserver

install_local_deps:
	pip install -r requirements/local.txt

docs: install_local_deps
	@echo "Construindo documentação..."
	mkdocs build --clean
	@echo "Feito!"
