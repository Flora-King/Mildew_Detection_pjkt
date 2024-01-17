import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def powdery_mildew_detector_page_body():
    st.info(
        f"* The client is interested to tell whether a given cherry leaf contains mildew"
        f" or not."
    )

    st.write(
        f"* Download a set of leaves containing a powdery mildew or healthy leaves for live prediction. "
        f"To make a live prediction, download the images from [here](https://www.kaggle.com/codeinstitute/cherry-leaves)"
    )

    st.write("---")

    images_buffer = st.file_uploader('Upload cherry leaf samples. You may select more than one.',
                                     type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if images_buffer is not None:
        df_report_data = []
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry leaves Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report_data.append({"Name": image.name, 'Result': pred_class})

        df_report = pd.DataFrame(df_report_data)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)

    st.write(
        f"For additional information, please visit **read** "
        f"[this project's README.md file](https://github.com/Flora-King/Mildew_Detection_pjkt.git)."
    )
