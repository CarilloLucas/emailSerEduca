from dash import Dash, html, dcc

app = Dash(__name__)

tela = []

app.layout = html.Div(children= tela )

if __name__ == '__main__':
    app.run_server(debug=True)