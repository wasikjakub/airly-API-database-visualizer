import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Air pollution in Poland', style={'filter': 'brightness(5)', 'textAlign': 'center'}), 
    html.H2(
        [
            'The data source is an application monitoring air quality conditions globally: ',
            html.A(
                'airly.org', 
                href='https://airly.org/pl/', 
                target='_blank',  
                style={ 'filter': 'brightness(5)', 'color': 'yellow', 'textDecoration': 'none'}  
            )
        ],
        style={'filter': 'brightness(5)'},
    ),
    html.H2('This project aims to create an interactive dashboard using Dash, a Python framework for building analytical web applications. The dashboard will provide users with comprehensive visualizations and insights into air quality data collected by Airly and stored in MySQL database.', style={'filter': 'brightness(5)'}),
    html.H2('Authors:', style={'filter': 'brightness(5)'}),  
    html.Ul([
        html.Li('Michał Ściubisz', style={'filter': 'brightness(5)'}),  
        html.Li('Tomisław Tarnawski', style={'filter': 'brightness(5)'}),  
        html.Li('Wojciech Tokarz', style={'filter': 'brightness(5)'}),  
        html.Li('Jakub Wąsik', style={'filter': 'brightness(5)'}), 
    ])
])

