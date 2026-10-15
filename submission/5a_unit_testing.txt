"""Assignment integration tests: require access to Watson NLP."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Verify the five required sentences against the real service."""

    def test_emotion_detector(self):
        """Verify the expected dominant emotion for each sentence."""
        cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgust just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear',
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(emotion_detector(text)['dominant_emotion'], expected)


if __name__ == '__main__':
    unittest.main()
