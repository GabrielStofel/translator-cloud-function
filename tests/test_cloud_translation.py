import unittest
from unittest.mock import patch, Mock

from src.api.cloud_translation import CloudTranslator


class TestCloudTranslation(unittest.TestCase):
    @patch("src.api.cloud_translation.translate_v2")
    def test_translate(self, translate_v2_mock):
        client_mock = Mock()
        client_mock.translate.return_value = {
            "detectedSourceLanguage": "pt",
            "translatedText": "test"
        }
        translate_v2_mock.Client.return_value = client_mock
        output = CloudTranslator().translate("teste", "en")
        client_mock.translate.assert_called_once_with("teste", target_language="en")
        self.assertTupleEqual(output, ("pt", "test"))
