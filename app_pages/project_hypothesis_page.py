import streamlit as st
import matplotlib.pyplot as plt


def project_hypothesis_page_body():
    st.write("### Hypotesis 1 and validation")

    st.success(
        f"Infected leaves have clear marks differentiating them from the healthy leaves."
    )
    st.info(
        f"We suspect cherry leaves affected by powdery mildew have clear marks, "
        f"typically the first symptom is a light-green, circular lesion on either leaf surface,"
        f" then a subtle white cotton-like growth develops in the infected area."
    )
    st.write("To visualize a thorough investigation of infected and healthy leaves visit the Leaves Visualiser tab.")
     
    st.warning(
        f"The model was able to detect such differences and learn how to differentiate and generalize in order to make accurate predictions."
        f" A good model trains its ability to predict classes on a batch of data without adhering too closely to that set of data."
        f" In this way the model is able to generalize and predict future observation reliably because it didn't 'memorize' the relationships between features and labels"
        f" as seen in the training dataset but the general pattern from feature to labels. "
    )

    st.write(
        f"For additional information, please **read**\n "
        f"[this project's README.md file](https://github.com/Flora-King/Mildew_Detection_pjkt.git)."
        )