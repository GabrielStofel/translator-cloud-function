from flask import Request, Response, jsonify
from api.cloud_translation import CloudTranslator


def run(request: Request) -> Response:
    text, target_language = get_data_from(request)

    cloud_translator = CloudTranslator()
    detected_language, translated_text = cloud_translator.translate(text, target_language)

    response = {"detectedLanguage": detected_language, "translatedText": translated_text}
    return jsonify(response)


def get_data_from(request: Request) -> tuple[str, str]:
    request_json = request.get_json()
    text = request_json["text"]
    target_language = request_json["targetLanguage"]

    return text, target_language
