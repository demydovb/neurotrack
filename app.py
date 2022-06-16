import os
from flask import Flask

from src import views

template_dir = os.path.abspath('./src/templates')
app = Flask(__name__, template_folder=template_dir)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/process/<string:selected_item>/<int:inserted_amount>', view_func=views.process_order)
app.add_url_rule('/cancel/', view_func=views.cancel_order)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'

if __name__ == '__main__':
    app.run(debug=True)

