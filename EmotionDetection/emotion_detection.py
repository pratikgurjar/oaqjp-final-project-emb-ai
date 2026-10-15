"""Detect emotions using the Watson NLP service."""
import requests

URL = ("https://sn-watson-emotion.labs.skills.network/v1/"
       "watson.runtime.nlp.v1/NlpService/EmotionPredict")
HEADERS = {"grpc-metadata-mm-model-id":
           "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion.

    Blank text or HTTP 400 returns None for every result field.
    Other service failures raise requests exceptions for the caller.
    """
    empty = dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    if not isinstance(text_to_analyse, str) or not text_to_analyse.strip():
        return empty
    response = requests.post(
        URL, json={"raw_document": {"text": text_to_analyse}},
        headers=HEADERS, timeout=30,
    )
    if response.status_code == 400:
        return empty
    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {name: emotions[name] for name in EMOTIONS}
    result["dominant_emotion"] = max(result, key=result.get)
    return result
