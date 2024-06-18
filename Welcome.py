import cv2
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from scipy.spatial.distance import pdist

# Set page configuration
st.set_page_config(
    layout="wide",
    page_title="Nuclear Distance Analysis",
    page_icon="🖥",
)
st.title("Nuclear Distance Analysis")
st.subheader("This app allows you to annotate nuclear distance of the drosophilla muscles!")

st.markdown("This app was developed to help with nuclear distance analysis carried out by scanning the drosophila segments and understand the difference between muscle morphometric in controls and experiments.")