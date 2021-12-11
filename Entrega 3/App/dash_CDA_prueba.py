import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import base64
import json


external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
#Create the app
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.H1("CDA - Proyecto Final", id='title'), #Creates the title of the app
    html.H2("Informacion Demografica", id='title_main1'), #Creates the title of the app
    html.H3("Por favor seleccione un género:", id='title1'),
    dcc.Dropdown(
        options=[
            {'value': 'women', 'label': 'Mujer'},
            {'value': 'man', 'label': 'Hombre'},
            {'value': 'no-info', 'label': 'Sin información'}
        ],
        value='',
        id='gender'
    ),
    html.H3("Por favor seleccione nivel educativo:", id='title2'),
    dcc.Dropdown(    # Edu
        options=[
            {'value': 'high', 'label': 'Bachillerato'},
            {'value': 'bsc', 'label': 'Universitario'},
            {'value': 'msc', 'label': 'Posgrado'},
            {'value': 'other', 'label': 'Otros'},
        ],
        value='',
        id='edu'
    ),
    html.H3("Por favor seleccione estado civil:", id='title3'),
    dcc.Dropdown(    # Estado civil
        options=[
            {'value': 'marr', 'label': 'Casado'},
            {'value': 'single', 'label': 'Soltero'},
            {'value': 'other', 'label': 'Otros'},
        ],
        value='',
        id='estado_civil'
    ),
    html.H3("Por favor ingrese la edad:", id='title4'),
    dcc.Input(
        placeholder='Edad',
        type='number',
        value='',
        id='age'
    ),
    html.Button('Subir', id='button1'),
    html.H2("Informacion Comportamiento Financiero", id='title_main2'), #################
    html.H3("Por favor ingrese el monto de desembolso:", id='title5'),
    dcc.Input(
        placeholder='Monto',
        type='number',
        value='',
        id='amount'
    ),
    html.Button('Subir', id='button2'),
    html.H3("Seleccione el estado de la cuenta del cliente el mes pasado:", id='title_retrasos1'),
    dcc.Dropdown(    #X6
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes1'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 2 meses:", id='title_retrasos2'),
    dcc.Dropdown(    #X7
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes2'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 3 meses:", id='title_retrasos3'),
    dcc.Dropdown(    #X8
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes3'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 4 meses:", id='title_retrasos4'),
    dcc.Dropdown(    #X9
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes4'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 5 meses:", id='title_retrasos5'),
    dcc.Dropdown(    #X10
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes5'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 6 meses:", id='title_retrasos6'),
    dcc.Dropdown(    #X11
        options=[
            {'value': 'marr', 'label': 'Pagó debidamente'},
            {'value': 'single', 'label': 'Retraso en el pago durante un mes'},
            {'value': 'other', 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 'other', 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes6'
    ),
    html.H3("Por favor ingrese el valor de la factura de los ultimos 6 meses:", id='title6'),##################################
    dcc.Input(
        placeholder='Factura mes pasado',
        type='number',
        value='',
        id='bill1'
    ),
    dcc.Input(
        placeholder='Factura hace 2 meses',
        type='number',
        value='',
        id='bill2'
    ),
    dcc.Input(
        placeholder='Factura hace 3 meses',
        type='number',
        value='',
        id='bill3'
    ),
    dcc.Input(
        placeholder='Factura hace 4 meses',
        type='number',
        value='',
        id='bill4'
    ),
    dcc.Input(
        placeholder='Factura hace 5 meses',
        type='number',
        value='',
        id='bill5'
    ),
    dcc.Input(
        placeholder='Factura hace 6 meses',
        type='number',
        value='',
        id='bill6'
    ),
    html.H3("Por favor ingrese los valores pagados los ultimos 6 meses:", id='title7'),##################################
    dcc.Input(
        placeholder='El mes pasado',
        type='number',
        value='',
        id='pay1'
    ),
    dcc.Input(
        placeholder='Hace 2 meses',
        type='number',
        value='',
        id='pay2'
    ),
    dcc.Input(
        placeholder='Hace 3 meses',
        type='number',
        value='',
        id='pay3'
    ),
    dcc.Input(
        placeholder='Hace 4 meses',
        type='number',
        value='',
        id='pay4'
    ),dcc.Input(
        placeholder='Hace 5 meses',
        type='number',
        value='',
        id='pay5'
    ),
    dcc.Input(
        placeholder='Hace 6 meses',
        type='number',
        value='',
        id='pay6'
    ),
    html.Button('Subir', id='button'),##################################
    html.H3(id='output',
             children='Ingrese un valor y presione "subir"'),
])

#We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True

title=html.Div(className="ds4a-title", 
    children=[
        dbc.Row([
            dbc.Col(
                html.H1("US Sales Dashboard"),
                width={"size": 6, "offset": 3}
                )
        ])
    ],
    id="title")


#img = html.Div(
#    children=[html.Img(src=app.get_asset_url('Uniandes.png'), id="img",)],
#)

image_filename = 'Uniandes.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#app.layout = html.Div([
#    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))
#])



sidebar = html.Div(
    [
        html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()),style={'height':'10%', 'width':'10%'}),  # Add the DS4A_Img located in the assets folder
        html.Hr(),  # Add an horizontal line
        ####################################################
        # Place the rest of Layout here
        ####################################################
        html.H5("Select dates"),
        html.Hr(),
        html.H5("Select states"),
        html.Hr(),
    ],
    className="ds4a-sidebar",
)


map1 = html.Div(
    [
        # Place the main graph component here:
        html.H5("Hi!"),
    ],
    className="ds4a-body",
)

stats = html.Div(
    [
            dbc.Row([
                    dbc.Col(dcc.Input(
                            placeholder='Hace 6 meses',
                            type='number',
                            value='',
                            id='pay68'
                        )),
                    dbc.Col(dcc.Input(
                            placeholder='Hace 6 meses',
                            type='number',
                            value='',
                            id='pay67'
                        )),
                    dbc.Col(dcc.Input(
                            placeholder='Hace 6 meses',
                            type='number',
                            value='',
                            id='pay66'
                        )),
                    dbc.Col(dcc.Input(
                            placeholder='Hace 6 meses',
                            type='number',
                            value='',
                            id='pay65'
                        )),
                ]),
    ],
    className="ds4a-body",
)

app.layout = html.Div(
    [title, sidebar, stats],
    className="ds4a-app",  # You can also add your own css files by locating them into the assets folder
)


@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('pay5', 'value')])

def update_output(n_clicks, value):
    return 'La probabilidad de hacer default es "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050',debug=True)