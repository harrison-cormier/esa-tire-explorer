# Tire fitment explorer

Interactive Streamlit display for the Fleet Tire Optimization Strategy capstone. It shows how tire width, rim diameter, tire type, tread depth and pressure change stopping distance, slip and other health and safety indicators in summer and winter conditions.

It is a screening model calibrated to published tire tests, not measured data for any specific tire. See the "Model and sources" tab in the Technical view.

## Files

- `app.py`: the Streamlit page.
- `tire_model.py`: the model (lookup tables and functions, no Streamlit).
- `tests/test_model.py`: checks that the model still matches its published calibration anchors.

## Run locally

```
pip install -r requirements.txt
streamlit run app.py
```

## Test

```
pip install pytest
python -m pytest -q
```

## Deploy on Streamlit Community Cloud

Sign in at share.streamlit.io with this GitHub account, choose this repository, branch `main`, and main file `app.py`.
