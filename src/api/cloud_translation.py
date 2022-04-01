import six
import logging
from google.cloud import translate_v2

logger = logging.getLogger()


class CloudTranslator:
    translate_client = translate_v2.Client()

    def translate(self, text, target) -> tuple[str, str]:
        if isinstance(text, six.binary_type):
            text = text.decode("utf-8")

        logger.info(f"Text to be translated: {text}")
        result = self.translate_client.translate(text, target_language=target)

        detected_language = result["detectedSourceLanguage"]
        translated_text = result["translatedText"]

        logger.info(f"Detected language: {detected_language}")
        logger.info(f"Translated text: {translated_text}")
        return detected_language, translated_text
