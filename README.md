# Final Project

## Emotion Detection with Watson NLP

Analyze English text for anger, disgust, fear, joy and sadness using Watson NLP,
and display its dominant emotion through Flask.

Repository name: `oaqjp-final-project-emb-ai`.

### Run in Skills Network

```bash
cd /home/project/final_project
python3 -m pip install -r requirements.txt
python3 test_emotion_detection.py
python3 server.py
```

Open the lab's application preview on port 5000. The Watson endpoint may require
the Skills Network lab network; this project does not substitute made-up predictions.

### Checks

```bash
python3 -m unittest test_offline -v
python3 test_emotion_detection.py
python3 -m pylint server.py
```

Offline tests use mocks. Integration tests call the actual Watson service.
See SUBMISSION_GUIDE.md for the 16 assignment answers and evidence commands.
