
from pathlib import Path
import sys

import cv2
import numpy as np
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

st.set_page_config(
    page_title="Concrete Crack Detection",
    page_icon="🔍",
    layout="wide",
)

st.title("Automated Concrete Crack Detection")
st.caption(
    "Computer Vision for Structural Health Monitoring"
)

st.sidebar.header("Research Information")
st.sidebar.write("Methods: Canny, Adaptive Thresholding, Morphology")
st.sidebar.write("Dataset: 40,000 concrete images")
st.sidebar.write("Evaluation: 280 held-out test images")
st.sidebar.metric("Canny Test Accuracy", "94.29%")

st.info(
    "Upload a concrete surface image to run "
    "the OpenCV crack detection pipeline."
)

uploaded = st.file_uploader(
    "Choose a concrete image",
    type=["jpg", "jpeg", "png"],
)

if uploaded is not None:
    file_bytes = np.frombuffer(uploaded.getvalue(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if image is None:
        st.error("Unable to read the uploaded image.")
        st.stop()

    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (227, 227))
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    canny = cv2.Canny(blurred, 50, 150)

    threshold = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2,
    )

    kernel = np.ones((3, 3), np.uint8)
    morphology = cv2.morphologyEx(
        threshold,
        cv2.MORPH_OPEN,
        kernel,
    )

    # Threshold obtained from the earlier calibration experiment.
    # It is not a probability or confidence score.
    canny_threshold = 0.01005259174445458
    edge_density = np.count_nonzero(canny) / canny.size

    st.subheader("Detection Result")

    if edge_density >= canny_threshold:
        st.error("Crack Detected")
    else:
        st.success("No Crack Detected")

    st.write(f"Canny edge density: {edge_density:.4f}")
    st.caption(
        "Classification uses the threshold calibrated on "
        "the original dataset. Predictions on new images "
        "may be less reliable."
    )

    st.subheader("Image Processing Results")

    col1, col2 = st.columns(2)
    with col1:
        st.image(original, caption="Original Image", width="stretch")
    with col2:
        st.image(canny, caption="Canny Edge Detection",
                 width="stretch", clamp=True)

    col3, col4 = st.columns(2)
    with col3:
        st.image(threshold, caption="Adaptive Threshold",
                 width="stretch", clamp=True)
    with col4:
        st.image(morphology, caption="Morphological Opening",
                 width="stretch", clamp=True)

    st.subheader("Research Performance Comparison")

    st.bar_chart({
        "Canny": 94.29,
        "Adaptive Thresholding": 58.21,
        "Morphology": 69.64,
    })

    st.caption(
        "Chart values represent test accuracy (%) "
        "from the preliminary 280-image evaluation."
    )

st.divider()
st.caption(
    "Academic research prototype. "
    "Not intended for structural safety assessment."
)
