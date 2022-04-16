# Translator Cloud Function
Project containing code for a Cloud Function that receives a text and translates it to a target language passed in the request
using the Cloud Translation API provided by GCP.

This project also uses Terraform for infrastructure as code practices.

## How to translate text
### Request
Once the Cloud Function is up and running, all you need to do is send a POST request to the Cloud Function's HTTPS endpoint
containing the following mandatory data:
````json
{
  "text": "Here you'll pass the actual text that you wish to translate",
  "targetLanguage": "The target language for the translation must be an ISO 639-1 language code"
}
````

### Response
After sending a POST request with valid data containing both `text` and `targetLanguage`, you'll receive the translated text
and the detected language of the text:
````json
{
  "detectedLanguage": "The detected language of the text",
  "translatedText": "The text translated using the Cloud Translation API"
}
````
