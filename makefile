# Global variables
$(eval S3_BUCKET="planet.joffreybvn.be")
$(eval LIBRARY_NAME="python-sdk")

doc:
	echo "Build documentation"
	cd ./docs; \
	rm -rf build; \
	make html

doc-push:
	echo "Upload documentation to S3"
	aws s3 sync ./docs/build/html s3://$(S3_BUCKET)/$(LIBRARY_NAME)

test:
	echo "Running Pytest with coverage"
	pytest --cov=typer tests/

monkey-type:
	echo "Run the code and generates types"
	monkeytype run scripts/monkey_type.py

monkey-apply:
	echo "Edit code files with the types"
	monkeytype apply typer.type.athena
	monkeytype apply typer.typer.big_query
	monkeytype apply typer.typer.pandas
	monkeytype apply typer.type

pure:
	echo "Update requirements versions"
	pur -r requirements.txt
	pur -r requirements-dev.txt

safe:
	echo "Check dependencies vulnerabilities"
	safety check
