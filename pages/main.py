from dash import dcc, html, State, Input, Output, callback
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
import base64, io, time
from PIL import Image
import numpy as np
from dash_iconify import DashIconify

# Layout of the app
upload_file = dmc.Container([
    dmc.Title(
        children = [
            "Upload your file to check whether it's ",
            dmc.Text("AI Generated", span=True, c="orange", inherit=True),
            " or not."
        ]
    ),
    dmc.Space(h="xl"),
    dmc.Group(
        [
            dcc.Upload(
                id='upload-data',
                children=[dmc.Button("Upload File",color='#6dcdb8', leftSection=DashIconify(icon="material-symbols:upload"), id='upload-file')],
                multiple=False
            ),
            dmc.Button("Check", id='submit-image', color='#6dcdb8')
    ]),
    html.Div(id='uploaded-image'),
    html.Div(id='response-check'),
])

@callback(
    [Output('upload-file', 'children'), Output('uploaded-image', 'children')], 
    Input('upload-data', 'filename'), State('upload-data', 'contents'), 
    prevent_initial_call=True
)
def display_file(file_name, contents):
    if file_name is None:    
        return "No file uploaded", PreventUpdate
    
    _, content_string = contents.split(',')
    
    # Decode the base64 string
    decoded_image = base64.b64decode(content_string)
    
    # Open the image
    image = Image.open(io.BytesIO(decoded_image))
    
    # Re-encode the image into base64 to display it
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    encoded_image = base64.b64encode(buffer.getvalue()).decode()
    
    return file_name, dmc.Image(
                        radius="lg",
                        m='sm',
                        h=300,
                        w=300,
                        src=f"data:image/png;base64,{encoded_image}",
                    )

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

    return dmc.Text(["Uploaded Image is ", dmc.Text("AI Generated", span=True, inherit=True, fw='700', size='xl')], c='red', size='lg')