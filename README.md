# ESA-03 tire fitment explorer

Interactive Streamlit display for the ESA-03 Fleet Tire Optimization Strategy capstone. It shows how tire width, rim diameter, tire type, tread depth and pressure change stopping distance, slip and other health and safety indicators in summer and winter conditions.

It is a screening model calibrated to published tire tests, not measured data for any specific tire. See the "Model and sources" tab in the Technical view.

## Run locally

```
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

Sign in at share.streamlit.io with this GitHub account, choose this repository, branch `main`, and main file `app.py`.
