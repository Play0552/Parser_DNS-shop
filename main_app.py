from flask import Flask, render_template, send_file
from Parser import take_excel

app = Flask(__name__)


@app.route("/")  # главная страница
def main():
    return render_template("main.html")


@app.route('/download')  # скачивание excel-файла
def generate_excel():
    take_excel()
    excel_file = 'Parsing.xlsx'
    """Ответ на запрос скачивания excel-файла"""
    return send_file(
        excel_file,
        as_attachment=True,
        download_name=f'Parsing.xlsx',
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


if __name__ == "__main__":
    app.run(debug=True)
