import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H3("Cliquez sur le Bouton"))),
    dbc.Row([
        dbc.Col(dcc.Input(id='input-text', type='text',
                placeholder='Entrez un texte')),
        dbc.Col(html.Button('Mettre à Jour', id='submit-button', n_clicks=0)),
        dbc.Col(html.Div(id='output-text'))
    ])
])


@app.callback(
    Output('output-text', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-text', 'value')]
)
def update_output(n_clicks, text):
    if n_clicks > 0:
        return text
    else:
        return 'Cliquez sur le bouton pour afficher le texte'


if __name__ == '__main__':
    app.run_server(debug=True)