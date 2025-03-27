from dash import dcc, html, State, Input, Output, callback, no_update
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import base64, io
from PIL import Image
from dash_iconify import DashIconify
from model import is_image_AI

upload_file = dmc.Container([
    dmc.Title(
        children = [
            "Upload your file to check whether it's ",
            dmc.Text("AI Generated", span=True, c="blue", inherit=True),
            " or not."
        ]
    ),
    dmc.Space(h="xl"),
    dcc.Upload(
        id='upload-data',
        children=dmc.Button("Upload File"),
        multiple=False  # Set to True if you want to allow multiple files
    ),
    html.Div(id='response-check'),
    dmc.Space(h="xl"),
    dmc.Button("Check", id='submit-image'),
])

@callback(
    [Output('uploaded-image', 'children'),  Output('response-check', 'children', allow_duplicate=True)],
    Input('upload-data', 'filename'), 
    State('upload-data', 'contents'), 
    prevent_initial_call=True
)
def display_file(file_name, contents):
    if file_name is None:    
        return PreventUpdate, dmc.Text('No File Uploaded', size='lg')
    
    _, content_string = contents.split(',')
    decoded_image = base64.b64decode(content_string)
    
    # Open the image
    image = Image.open(io.BytesIO(decoded_image))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    return dmc.Image( radius="lg", m='sm', h=300, w=300, src=f"data:image/png;base64,{encoded_image}"), no_update

@callback(
    Output('response-check', 'children'),
    Input('submit-image', 'n_clicks'), 
    State('upload-data', 'contents'), 
    running=(Input('submit-image', 'loading'), True, False),
    prevent_initial_call=True
)
def display_file(_, contents):
    if contents is None:    
        return "No file uploaded"
    
    prediction = is_image_AI(contents)

    if prediction:
        return dmc.Text(["Uploaded Image is ", dmc.Text("AI Generated", span=True, inherit=True, fw='700', size='xl')], c='red', size='lg')

    return dmc.Text(["Uploaded Image is a ", dmc.Text("Real Image", span=True, inherit=True, fw='700', size='xl')], c='green', size='lg')
