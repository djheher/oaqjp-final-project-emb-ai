''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/emotionDetector")
def emotion_detecter():
    '''Retrive input entered into form. Pass the input to be analyzed by the emotion detector.
    If the user entered valid input return the list of scores and the domninate emotion. If the
    user did not enter valid input return an error message.
    '''

    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
    f"For the given statement, the system response is:\n"
    f"anger: {anger}, "
    f"disgust: {disgust}, "
    f"fear: {fear}, "
    f"joy: {joy}, "
    f"sadness: {sadness}\n"
    f"The dominant emotion is <b>{dominant_emotion}</b>")

@app.route("/")
def render_index_page():
    '''Render the index page to the user. This page will allow the user to enter a string
    to be analyzed.
    '''
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    