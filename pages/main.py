from dash import dcc, html, State, Input, Output, callback
import dash_mantine_components as dmc
import base64, io, time
from PIL import Image
import numpy as np
from dash_iconify import DashIconify

# Layout of the app
upload_file_layout = dmc.Container([
    dmc.Title(
        children = [
            "Upload your file to check whether it's ",
            dmc.Text("AI Generated", span=True, c="blue", inherit=True),
            " or not."
        ]
    ),
    dmc.Space(h="xl"),
    dmc.Group(
        [
            dcc.Upload(
                id='upload-data',
                children=[dmc.Button("Upload File", leftSection=DashIconify(icon="material-symbols:upload"), id='upload-file')],
                multiple=False  # Set to True if you want to allow multiple files
            ),
            dmc.Button("Check", id='submit-image')
    ]),
    html.Div(id='response-check'),
])

@callback(
    Output('upload-file', 'children'),
    Input('upload-data', 'filename'), 
    prevent_initial_call=True
)
def display_file(file_name):
    if file_name is None:    
        return "No file uploaded"
    
    return file_name

@callback(
    Output('response-check', 'children'),
    Input('submit-image', 'n_clicks'), 
    State('upload-data', 'contents'), 
    running=(Input('submit-image', 'loading'), True, False),
    prevent_initial_call=True
)
def display_file(_, contents):
    time.sleep(1)
    if contents is None:    
        return "No file uploaded"
    
    # Decode the file content
    content_string = contents.split(',')[1]
    decoded = base64.b64decode(content_string)
    image = Image.open(io.BytesIO(decoded))

    # Preprocess the image for your model (resize, normalize, etc.)
    image = image.resize((224, 224))  # Example for MobileNetV2
    image_array = np.array(image) / 255.0  # Normalize the image
    image_array = np.expand_dims(image_array, axis=0) 

    return 'ai'