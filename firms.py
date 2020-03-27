from flask import Flask, render_template
app = Flask(__name__)
application = app

import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts

firms_list = convert_to_dict("top20prfirms.csv")

pairs_list = []
for f in firms_list:
    pairs_list.append( (f['ID'], f['Name']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Firms Index")

@app.route("/firm/<num>")
def firm(num):
    firm = firms_list[int(num) - 1]
    return render_template("firm.html", firm=firm)

if __name__ == '__main__':
    app.run(debug=True)
