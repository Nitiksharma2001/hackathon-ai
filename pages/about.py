import dash_mantine_components as dmc

text1 = """
This AI-generated masterpiece is a fusion of creativity and technology. Every pixel, carefully crafted by algorithms, brings forth a vision beyond human limits—where colors blend, patterns emerge, and forms evolve into something uniquely captivating. Dive into this world where the boundaries of art are redefined, and the canvas is limitless.
"""
text2 = """
Let this image ignite your imagination and transport you into a world where art and technology coalesce in perfect harmony.
"""

about = [
    dmc.Title('Why AI is the future..?'),
    dmc.Space(h="xl"),
    dmc.Text(text1, size="xl"),
    dmc.Space(h="xl"),
    dmc.Text(text2, size="xl"),
]