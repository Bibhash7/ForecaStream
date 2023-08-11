from app import app
from model.user_model import Stream

obj = Stream()
@app.route("/user/stream", methods = ["POST"])
def data_stream():
    return obj.data_stream()

@app.route("/user/show", methods = ["POST"])
def show_data():
    return obj.show_data()
