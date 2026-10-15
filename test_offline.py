"""Deterministic tests; service responses are mocked, not live predictions."""
import unittest
from unittest.mock import Mock, patch
import requests
from EmotionDetection.emotion_detection import emotion_detector
from server import app


class OfflineTests(unittest.TestCase):
    def test_five_emotions(self):
        for dominant in ('anger', 'disgust', 'fear', 'joy', 'sadness'):
            with self.subTest(dominant=dominant):
                scores = dict.fromkeys(('anger', 'disgust', 'fear', 'joy', 'sadness'), 0.01)
                scores[dominant] = 0.96
                reply = Mock(status_code=200)
                reply.json.return_value = {'emotionPredictions': [{'emotion': scores}]}
                with patch('EmotionDetection.emotion_detection.requests.post', return_value=reply):
                    result = emotion_detector('test sentence')
                self.assertEqual(result, dict(scores, dominant_emotion=dominant))

    def test_http_400(self):
        with patch('EmotionDetection.emotion_detection.requests.post', return_value=Mock(status_code=400)):
            self.assertTrue(all(value is None for value in emotion_detector('invalid').values()))

    def test_blank_skips_service(self):
        with patch('EmotionDetection.emotion_detection.requests.post') as post:
            for text in ('', '   ', None):
                self.assertIsNone(emotion_detector(text)['dominant_emotion'])
            post.assert_not_called()

    def test_server_blank(self):
        client = app.test_client()
        for path in ('/emotionDetector', '/emotionDetector?textToAnalyze='):
            self.assertEqual(client.get(path).text, 'Invalid text! Please try again!')

    def test_server_success(self):
        scores = dict.fromkeys(('anger', 'disgust', 'fear', 'joy', 'sadness'), 0.01)
        with patch('server.emotion_detector', return_value=dict(scores, dominant_emotion='joy')):
            self.assertIn('The dominant emotion is joy.', app.test_client().get('/emotionDetector?textToAnalyze=happy').text)

    def test_server_outage(self):
        with patch('server.emotion_detector', side_effect=requests.Timeout):
            self.assertEqual(app.test_client().get('/emotionDetector?textToAnalyze=hello').status_code, 502)

    def test_home(self):
        self.assertEqual(app.test_client().get('/').status_code, 200)


if __name__ == '__main__':
    unittest.main()
