import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.summary_page import summary_page_body
from app_pages.leaves_visualizer_page import leaves_visualizer_page_body
from app_pages.powdery_mildew_detector_page import powdery_mildew_detector_page_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.ml_performance_metrics_page import ml_performance_metrics_page

# Create an instance of the app
app = MultiPage(app_name="Cherry Powdery Mildew detector")  

# Add app pages 
app.add_page("Quick Project Summary", summary_page_body)
app.add_page("Leaves Visualiser", leaves_visualizer_page_body)
app.add_page("Powdery Mildew detector", powdery_mildew_detector_page_body)
app.add_page("Project Hypothesis", project_hypothesis_page_body)
app.add_page("ML Performance Metrics", ml_performance_metrics_page)

#Run the app
app.run()  