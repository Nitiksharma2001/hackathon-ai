from dash import Dash, html
import dash_mantine_components as dmc
from pages.main import upload_file_layout
from components.navbar import navbar

app = Dash(external_stylesheets=[dmc.styles.ALL])

app.layout = dmc.MantineProvider(html.Div([navbar, dmc.Space(h="xl"), upload_file_layout]))

if __name__ == "__main__":
    app.run()