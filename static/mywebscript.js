document.getElementById('emotion-form').addEventListener('submit', async (event) => {
  event.preventDefault();
  const result = document.getElementById('system_response');
  result.textContent = 'Analyzing.';
  const query = new URLSearchParams({textToAnalyze: document.getElementById('textToAnalyze').value});
  try {
    const response = await fetch('/emotionDetector?' + query.toString());
    result.textContent = await response.text();
  } catch (error) {
    result.textContent = 'Unable to reach the server. Please try again.';
  }
});
