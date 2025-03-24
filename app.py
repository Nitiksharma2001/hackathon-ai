import dash
from dash import Dash
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from pages.main import upload_file_layout
from components.navbar import navbar

app = Dash(external_stylesheets=[dmc.styles.ALL])

app.layout = dmc.MantineProvider([navbar, upload_file_layout])

if __name__ == "__main__":
    app.run(debug=True)