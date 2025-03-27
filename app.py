import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, callback, dcc, html
from components.navbar import navbar
from pages.main import upload_file
from pages.about import about
from dotenv import load_dotenv

load_dotenv() 

app = Dash(external_stylesheets=dmc.styles.ALL, suppress_callback_exceptions=True)

layout = dmc.AppShell(
    [
        dcc.Location('url'),
        dmc.AppShellHeader(
            dmc.Group(
                [
                    dmc.Burger(id="burger", size="sm", hiddenFrom="sm", opened=False),
                    dmc.Image(src='/assets/logo.png', h=50, visibleFrom="sm"),
                    dmc.NavLink(label=dmc.Title("BYTE BATTLEGROUND", c="orange"), href='/', style={'textWrap': 'nowrap', 'zIndex': 100},),
                ],
                h="100%",
                px="md",
                wrap="nowrap",
            )
        ),
        dmc.AppShellNavbar(
            id="navbar",
            children=[
                *navbar
            ],
            p="md",
        ),
        dmc.AppShellMain(None, id="main"),
    ],
    header={"height": 60},
    padding="md",
    navbar={
        "width": 250,
        "breakpoint": "sm",
        "collapsed": {"mobile": True},
    },
    id="appshell",
)

app.layout = dmc.MantineProvider(layout)

@callback(
        Output('main', 'children'),
        Input('url', 'pathname')
)
def on_component_mount(pathname):
    if pathname == '/':
        return upload_file  
    if pathname == '/about':
        return about
      
@callback(
    Output("appshell", "navbar"),
    Input("burger", "opened"),
    State("appshell", "navbar"),
)
def navbar_is_open(opened, navbar):
    navbar["collapsed"] = {"mobile": not opened}
    return navbar

if __name__ == "__main__":
    app.run(debug=True)