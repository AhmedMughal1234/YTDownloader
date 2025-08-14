from flask import Flask, request, send_file, render_template_string
from pytube import YouTube
import os

app = Flask(__name__)

HTML = '''
<form method="POST">
  YouTube URL: <input type="text" name="url" />
  <input type="submit" value="Download" />
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        file_path = stream.download(filename='video.mp4')

        # Send the video file as download to user
        return send_file(file_path, as_attachment=True)
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
