import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import summary_page_body
from app_pages.page_leaves_visualizer import leaves_visualizer_page_body
from app_pages.page_powdery_mildew_detector import powdery_mildew_detector_page_body
from app_pages.page_project_hypothesis import project_hypothesis_page_body
from app_pages.page_ml_performance import ml_performance_metrics_page

app = MultiPage(app_name="Cherry Powdery Mildew detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", summary_page_body)
app.add_page("Leaves Visualiser", leaves_visualizer_page_body)
app.add_page("Powdery Mildew detector", powdery_mildew_detector_page_body)
app.add_page("Project Hypothesis", project_hypothesis_page_body)
app.add_page("ML Performance Metrics", ml_performance_metrics_page)

app.run()  