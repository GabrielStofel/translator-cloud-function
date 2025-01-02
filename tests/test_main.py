import unittest
from flask import Response
from unittest.mock import patch, Mock

from src.main import run, get_data_from


class TestMain(unittest.TestCase):
    @patch("src.main.jsonify")
    @patch("src.main.get_data_from")
    @patch("src.main.CloudTranslator")
    def test_run(self, cloud_translator_mock, get_data_from_mock, jsonify_mock):
        request_mock = Mock()
        get_data_from_mock.return_value = ("foo bar", "pt")
        cloud_translator_mock.return_value.translate.return_value = ("en", "foo bar")
        expected_response = {"detectedLanguage": "en", "translatedText": "foo bar"}
        jsonify_mock.return_value = Mock(spec=Response)
        output = run(request_mock)
        self.assertIsInstance(output, Response)
        jsonify_mock.assert_called_with(expected_response)

    def test_get_data_from(self):
        request_mock = Mock()
        request_mock.get_json.return_value = {"text": "foo bar", "targetLanguage": "en"}
        output = get_data_from(request_mock)
        self.assertTupleEqual(output, ("foo bar", "en"))
