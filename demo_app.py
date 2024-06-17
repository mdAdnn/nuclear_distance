import cv2
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from streamlit_drawable_canvas import st_canvas
from PIL import Image  # Import the Image class from PIL

st.title("OpenCV Demo App")
st.subheader("This app allows you to play with Image filters!")
st.text("We use OpenCV and Streamlit for this demo")

# Upload options for control and experimental images
control_uploaded_file = st.file_uploader("Choose a Control Image", type=["jpeg", "png"])
experimental_uploaded_file = st.file_uploader("Choose an Experimental Image", type=["jpeg", "png"])

# Function to convert uploaded file to OpenCV image
def uploaded_file_to_cv2_image(uploaded_file):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image
    return None

# Process the uploaded control image
control_image = uploaded_file_to_cv2_image(control_uploaded_file)

# Process the uploaded experimental image
experimental_image = uploaded_file_to_cv2_image(experimental_uploaded_file)

# Display images and provide annotation canvas
if control_image is not None and experimental_image is not None:
    st.success("Both images uploaded successfully. Proceed with annotation.")

    # Convert images to RGB for display in Streamlit
    control_image_rgb = cv2.cvtColor(control_image, cv2.COLOR_BGR2RGB)
    experimental_image_rgb = cv2.cvtColor(experimental_image, cv2.COLOR_BGR2RGB)

    st.write("Annotate the Control Image:")
    control_canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="green",
        background_image=Image.fromarray(control_image_rgb),
        update_streamlit=True,
        height=control_image.shape[0],
        width=control_image.shape[1],
        drawing_mode="circle",
        key="control_canvas",
    )

    st.write("Annotate the Experimental Image:")
    experimental_canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=2,
        stroke_color="yellow",
        background_image=Image.fromarray(experimental_image_rgb),
        update_streamlit=True,
        height=experimental_image.shape[0],
        width=experimental_image.shape[1],
        drawing_mode="circle",
        key="experimental_canvas",
    )

    # Extract the annotations from the canvas result
    if control_canvas_result.json_data is not None:
        control_nucleus_positions = [(shape['left'], shape['top']) for shape in control_canvas_result.json_data['objects']]
        st.write(f"Control Nucleus positions: {control_nucleus_positions}")

    if experimental_canvas_result.json_data is not None:
        experimental_nucleus_positions = [(shape['left'], shape['top']) for shape in experimental_canvas_result.json_data['objects']]
        st.write(f"Experimental Nucleus positions: {experimental_nucleus_positions}")

    # Create a figure to display images and plots
    fig, axs = plt.subplots(1, 2, figsize=(18, 12))

    # Display the control image with annotated nuclei positions
    axs[0].imshow(control_image_rgb)
    axs[0].set_title('Control Image')
    axs[0].axis('off')
    for position in control_nucleus_positions:
        axs[0].plot(position[0], position[1], marker='o', markersize=6, color='green')

    # Display the experimental image with annotated nuclei positions
    axs[1].imshow(experimental_image_rgb)
    axs[1].set_title('Experimental Image')
    axs[1].axis('off')
    for position in experimental_nucleus_positions:
        axs[1].plot(position[0], position[1], marker='o', markersize=6, color='yellow')

    st.pyplot(fig)
else:
    st.warning("Please upload both control and experimental images to proceed.")
