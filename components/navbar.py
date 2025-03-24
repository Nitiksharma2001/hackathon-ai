import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
from routes import routes

def get_icon(icon):
    return DashIconify(icon=icon, height=16)


navbar = html.Div(
    [
        html.Div(dmc.NavLink(label=dmc.Title("God Of AI"), rightSection=get_icon('mingcute/ai-fill'), href='/')),
        html.Div([ 
            dmc.NavLink(label=dmc.Text(route['title'], size='lg'), href=route['link'], style={'text-wrap': 'nowrap'} ) for route in routes 
        ], style={'display': 'flex'})
    ],
    style={'display': 'flex', 'padding': '8px', 'justify-content': 'space-between'}
)