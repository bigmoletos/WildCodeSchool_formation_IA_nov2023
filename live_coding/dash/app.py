# Importations
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
from dash import dash_table
import pandas as pd
import numpy as np

# Initialisation de l'application Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Création des données fictives
df = pd.DataFrame({
    'Date': pd.date_range(start='2021-01-01', periods=100, freq='D'),
    'Variable1': np.random.rand(100),
    'Variable2': np.random.rand(100) * 100,
    'Categorie': np.random.choice(['A', 'B', 'C'], 100)
})

# Fonctions pour créer des graphiques


def create_line_chart(df):
    return px.line(df, x='Date', y='Variable1', title='Graphique en ligne')


def create_bar_chart(df):
    return px.bar(df, x='Categorie', y='Variable2', title='Graphique en barres')


def create_scatter_chart(df):
    return px.scatter(df, x='Variable1', y='Variable2', color='Categorie', title='Nuage de points')


min_var1 = df['Variable1'].min()
max_var1 = df['Variable1'].max()

# Définir la mise en page
app.layout = dbc.Container([
    dbc.Row(html.H1("Application Dash avec Bootstrap"), className="mb-4"),

    # Ajout d'une table pour afficher les données
    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.head(10).to_dict('records'),
                style_cell={'textAlign': 'left'},
                style_header={
                    'backgroundColor': 'white',
                    'fontWeight': 'bold'
                }
            ),
            md=12
        )
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='line-chart'), md=6),
        dbc.Col(dcc.Graph(id='bar-chart'), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='scatter-chart'), md=12)
    ]),

    dbc.Row([
        dbc.Col(width=2),  # Espace vide sur la gauche
        dbc.Col(dcc.Dropdown(
            id='category-selector',
            options=[{'label': cat, 'value': cat}
                for cat in df['Categorie'].unique()],
            value='A',
            multi=True
        ), md=3),  # Dropdown prend 3 colonnes

        dbc.Col(dcc.DatePickerRange(
                id='date-picker',
                min_date_allowed=df['Date'].min(),
                max_date_allowed=df['Date'].max(),
                start_date=df['Date'].min(),
                end_date=df['Date'].max()
                ),
                md=6),  # DatePickerRange prend 6 colonnes
        dbc.Col(width=1)  # Espace vide sur la droite pour équilibrer
    ])
], fluid=True)

# Callbacks pour mettre à jour les graphiques


@app.callback(
    [Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('scatter-chart', 'figure')],
    [Input('category-selector', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graphs(selected_categories, start_date, end_date):
    # Filtrer les données en fonction des sélections
    if not isinstance(selected_categories, list):
        selected_categories = [selected_categories]

    filtered_df = df[df['Categorie'].isin(selected_categories) &
                     df['Date'].between(start_date, end_date)]

    # Créer les graphiques mis à jour
    line_chart = create_line_chart(filtered_df)
    bar_chart = create_bar_chart(filtered_df)
    scatter_chart = create_scatter_chart(filtered_df)
    return line_chart, bar_chart, scatter_chart


# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
