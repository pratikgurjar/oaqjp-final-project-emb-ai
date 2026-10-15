# Assignment submission guide

The source files are ready. Public GitHub URLs, live Watson outputs, screenshots,
and the Skills Network terminal path must come from your actual environment.
No placeholder URL or simulated terminal output should be submitted as evidence.

1. Fork the original repository linked in your course. Rename your fork
   `oaqjp-final-project-emb-ai`, keep it public, and upload these project files.
   README starts with `Final Project`. Q1: copy the actual README file URL.
2. Q2: paste `submission/2a_emotion_detection.txt`.
3. Q3: in `/home/project/final_project`, run the interactive commands below and
   `python3 test_emotion_detection.py`. Save your real terminal output as
   `2b_application_creation.txt`. The final implementation returns a dictionary;
   for the earlier raw-response stage, temporarily use the Task 2 source.
4. Q4: paste `submission/3a_output_formatting.txt`.
5. Q5: run the formatted-output command below; save as `3b_formatted_output_test.txt`.
6. Q6: copy your actual GitHub URL for `EmotionDetection/__init__.py`.
7. Q7: run the packaging command below; save as `4b_packaging_test.txt`.
8. Q8: paste `submission/5a_unit_testing.txt`.
9. Q9: run `python3 test_emotion_detection.py`; save real results as `5b_unit_testing_result.txt`.
10. Q10: paste `submission/6a_server.txt`.
11. Q11: run `python3 server.py`, open port 5000, enter `I am glad this happened`,
    click Analyze emotions, and capture the actual result as `6b_deployment_test.png`.
12. Q12: paste `submission/7a_error_handling_function.txt`.
13. Q13: paste `submission/7b_error_handling_server.txt`.
14. Q14: clear the input, click Analyze emotions, and capture the invalid-text
    message as `7c_error_handling_interface.png`.
15. Q15: paste `submission/8a_server_modified.txt`.
16. Q16: run `python3 -m pylint server.py`; save its actual output as
    `8b_static_code_analysis.txt`. Do not claim a score before running it.

## Interactive test (Q3)

```bash
cd /home/project/final_project
python3
```
```python
from emotion_detection import emotion_detector
print(emotion_detector('I am really mad about this'))
exit()
```
```bash
python3 test_emotion_detection.py
```

## Formatted output (Q5)

```bash
python3 -c "from emotion_detection import emotion_detector; print(emotion_detector('I am glad this happened'))"
```

## Packaging (Q7)

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

Run terminal commands in the actual lab so `/home/project/final_project` is visible.
If Watson is unreachable, resolve lab access before collecting live evidence.
`test_offline.py` verifies behavior with mocked responses and is additional
developer validation, not a replacement for the required live-service tests.
