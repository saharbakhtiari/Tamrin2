from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import base64

from flask import Flask, render_template #this has changed


app = Flask(__name__)

@app.route("/")
def chart():
    data = pd.read_csv("titanic.csv")
    df = data.groupby("Age")['Survived'].aggregate(lambda x: len(x))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    df.plot(ax=ax)

    io = BytesIO()
    fig.savefig(io, format='png')
    data = base64.b64encode(io.getvalue())

    return render_template("chart.html", result=data.decode('utf8'))


if __name__ == '__main__':
    # chart()
    app.debug = True
    app.run()
