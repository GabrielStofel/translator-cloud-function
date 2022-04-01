deploy-function:
	@gcloud functions deploy translator-function --source=src --runtime=python39 --trigger-http \
		--entry-point=run --region=us-east1