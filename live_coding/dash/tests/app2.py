import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H3("Calculer le Carré d'un Nombre",
            style={'textAlign': 'center', 'color': 'blue'}))),
    dbc.Row([
        dbc.Col(dcc.Input(id='input-number', type='number',
                placeholder='Entrez un nombre'), md=4),
        dbc.Col(html.Div(id='output-square',
                style={'textAlign': 'center', 'color': 'red'}), md=6)
    ])
])


@app.callback(
    Output('output-square', 'children'),
    [Input('input-number', 'value')]
)
def update_output(value):
    if value is not None:
        return f'Le carré de {value} est {value**2}'
    else:
        return 'On va calculer le carré'


if __name__ == '__main__':
    app.run_server(debug=True)

