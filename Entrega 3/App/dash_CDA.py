import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import json
import requests

#Create the app
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets = [external_stylesheets])
app.title = "CDA: Proyecto Final"
app.layout = html.Div(
    children = 
        [html.Div(
            children=[
                    html.P(children="🤖", className="header-emoji"),
                    html.P(children="CDA: Proyecto Final", className="header-description"),
                    html.H1(children="Predicción de default"
                                    " de un cliente",
                        className="header-title",),
                    ]
        ),
    html.Div(
            children=[
                html.Div(
                     html.H2("🧑 Informacion Demografica", id='title_main1',className="menu-title"), #Creates the title of the app
                )]),
    #html.Div(
    html.H3("Seleccione un género:", id='title1', className='dropdown'),
    dcc.Dropdown(
        options=[
            {'value': 'women', 'label': 'Mujer'},
            {'value': 'man', 'label': 'Hombre'},
            {'value': 'no-info', 'label': 'Sin información'}
        ],
        value='',
        id='gender',
        className='dropdown',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',}
    ),
    html.H3("Seleccione nivel educativo:", id='title2', className='dropdown'),
    dcc.Dropdown(    # Edu
        options=[
            {'value': 'high', 'label': 'Bachillerato'},
            {'value': 'bsc', 'label': 'Universitario'},
            {'value': 'msc', 'label': 'Posgrado'},
            {'value': 'other', 'label': 'Otros'},
        ],
        value='',
        id='edu',
        className='dropdown',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',}
    ),
    html.H3("Seleccione estado civil:", id='title3', className='dropdown'),
    dcc.Dropdown(    # Estado civil
        options=[
            {'value': 'marr', 'label': 'Casado'},
            {'value': 'single', 'label': 'Soltero'},
            {'value': 'other', 'label': 'Otros'},
        ],
        value='',
        id='estado_civil',
        className='dropdown',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',}
    ), #className='menu'),
         
         
    html.H3("Por favor ingrese la edad:", id='title4', className='dropdown'),
    dcc.Input(
        placeholder='Edad',
        type='number',
        value='',
        min=18, max=100, step=1,
        id='edad',
        className='center'
    ),
    html.H2("💸 Informacion Comportamiento Financiero", id='dropdown',className="menu-title"), #################
    html.H3("Por favor ingrese el monto de desembolso [USD]:", id='title5', className='dropdown'),
    dcc.Input(
        placeholder='Monto',
        type='number',
        value='',
        min=0, max=1000000, step=1000,
        id='amount',
        className='center'
    ),
    html.H3("Seleccione el estado de la cuenta del cliente el mes pasado:", id='title_retrasos1', className='dropdown'),
    dcc.Dropdown(    #X6
        options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes1',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 2 meses:", id='title_retrasos2', className='dropdown'),
    dcc.Dropdown(    #X7
        options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes2',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 3 meses:", id='title_retrasos3', className='dropdown'),
    dcc.Dropdown(    #X8
       options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes3',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 4 meses:", id='title_retrasos4', className='dropdown'),
    dcc.Dropdown(    #X9
        options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes4',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 5 meses:", id='title_retrasos5', className='dropdown'),
    dcc.Dropdown(    #X10
        options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes5',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Seleccione el estado de la cuenta del cliente hace 6 meses:", id='title_retrasos6', className='dropdown'),
    dcc.Dropdown(    #X11
        options=[
            {'value': -1, 'label': 'Pagó debidamente'},
            {'value': 1, 'label': 'Retraso en el pago durante un mes'},
            {'value': 2, 'label': 'Retraso en el pago durante 2 meses'},
            {'value': 3, 'label': 'Retraso en el pago durante 3 meses'},
            {'value': 4, 'label': 'Retraso en el pago durante 4 meses'},
            {'value': 5, 'label': 'Retraso en el pago durante 5 meses'},
            {'value': 6, 'label': 'Retraso en el pago durante 6 meses'},
            {'value': 7, 'label': 'Retraso en el pago durante 7 meses'},
            {'value': 8, 'label': 'Retraso en el pago durante 8 meses'},
            {'value': 9, 'label': 'Retraso en el pago durante 9 meses'}, 
        ],
        value='',
        id='retraso_mes6',
        style = {'width': '100%',  'align-items': 'center', 'justify-content': 'center',},
        className='dropdown',
    ),
    html.H3("Por favor ingrese el valor de la factura de los ultimos 6 meses:", id='title6', className='dropdown'),##################################
    dcc.Input(
        placeholder='Factura mes pasado',
        type='number',
        value='',
        id='bill1',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Factura hace 2 meses',
        type='number',
        value='',
        id='bill2',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Factura hace 3 meses',
        type='number',
        value='',
        id='bill3',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Factura hace 4 meses',
        type='number',
        value='',
        id='bill4',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Factura hace 5 meses',
        type='number',
        value='',
        id='bill5',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Factura hace 6 meses',
        type='number',
        value='',
        id='bill6',
        className='dropdown'
    ),
    html.H3("Por favor ingrese los valores pagados los ultimos 6 meses:", id='title7', className='dropdown'),##################################
    dcc.Input(
        placeholder='El mes pasado',
        type='number',
        value='',
        id='pay1',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Hace 2 meses',
        type='number',
        value='',
        id='pay2',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Hace 3 meses',
        type='number',
        value='',
        id='pay3',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Hace 4 meses',
        type='number',
        value='',
        id='pay4',
        className='dropdown'
    ),dcc.Input(
        placeholder='Hace 5 meses',
        type='number',
        value='',
        id='pay5',
        className='dropdown'
    ),
    dcc.Input(
        placeholder='Hace 6 meses',
        type='number',
        value='',
        id='pay6',
        className='dropdown'
    ),
    html.H1('\n', id='relleno1'),
    html.H1('\n', id='relleno2'),
    html.H1('\n', id='relleno3'),
         
         html.H2("🔮 Prediccion del cliente", id='predict',className="menu-title"),
    html.Button('Predecir', id='button', style={'width':'300px', 'height':'40px',"horizontalAlign": "middle", "verticalalAlign": "middle"}, className="center2 dropdown",),##################################
         # 
    html.H2(id='output',
             children='Ingrese un valor y presione "subir"',
            className="menu-title"),
],
className="header"
)

def predict(x):  
    url = 'http://127.0.0.1:5000/'
    params = {'query':x}
    response = requests.get(url, params)
    return response.json()

#We need this for function callbacks not present in the app.layout
app.config.suppress_callback_exceptions = True

@app.callback(
    Output('output', 'children'),
    [Input('button', 'n_clicks')],
     State('gender', 'value'),
     State('edu', 'value'),
     State('estado_civil', 'value'),
     State('edad', 'value'),
     State('amount', 'value'),
     State('retraso_mes1', 'value'),
     State('retraso_mes2', 'value'),
     State('retraso_mes3', 'value'),
     State('retraso_mes4', 'value'),
     State('retraso_mes5', 'value'),
     State('retraso_mes6', 'value'),
     State('bill1', 'value'),
     State('bill2', 'value'),
     State('bill3', 'value'),
     State('bill4', 'value'),
     State('bill5', 'value'),
     State('bill6', 'value'),
     State('pay1', 'value'),
     State('pay2', 'value'),
     State('pay3', 'value'),
     State('pay4', 'value'),
     State('pay5', 'value'),
     State('pay6', 'value'),
    )


def update_output(n_clicks, gender, edu, estado_civil, edad,amount, retraso_mes1,retraso_mes2,retraso_mes3,retraso_mes4,retraso_mes5,retraso_mes6, bill1,bill2,bill3,bill4,bill5,bill6, pay1,pay2,pay3,pay4,pay5,pay6):
    x = []
    x.append(amount)
    print(x)
    x.extend([bill1,bill2,bill3,bill4,bill5,bill6])
    print(x)
    x.extend([pay1,pay2,pay3,pay4,pay5,pay6])
    print(x)
    x.extend([retraso_mes1,retraso_mes2,retraso_mes3,retraso_mes4,retraso_mes5,retraso_mes6])
    print(x)
    x.append(edad)
    print(x)
    #Genero:
    if gender == 'women':
        x.append(1)
    else:
        x.append(0)
    print(x)
    # educacion:
    if edu == 'high':
        x.extend([1,0,0,0])
    elif edu == 'other':
        x.extend([0,1,0,0])
    elif edu == 'msc':
        x.extend([0,0,1,0])
    elif edu == 'bsc':
        x.extend([0,0,0,1])
    else:
        x.extend([0,0,0,0])
    print(x)
    # estado civil   
    if estado_civil == 'marr':
        x.extend([1,0,0])
    elif estado_civil == 'other':
        x.extend([0,1,0])
    elif estado_civil == 'single':
        x.extend([0,0,1])
    else:
        x.extend([0,0,0])
    print(len(x))
    print(x)
    # predecimos
    pred = predict(x)
      
    if pred['prediction'] == 'Este usuario NO ES propenso a dejar de pagar.':
        value = 'NO'
    else:
        value = 'SI'
    return 'El cliente {} es propenso a hacer default el proximo mes'.format(value)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050',debug=True)