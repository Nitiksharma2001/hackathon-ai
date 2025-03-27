import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify
from routes import routes

def get_icon(icon):
    return DashIconify(icon=icon, height=16)

navbar = [
    dmc.NavLink(label=dmc.Text(route['title'], size='lg', fw=500), href=route['link'] ) for route in routes
]