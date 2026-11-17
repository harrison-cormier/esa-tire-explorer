# Tire fitment explorer

Interactive Streamlit display for the Fleet Tire Optimization Strategy capstone. It shows how tire width, rim diameter, tire type, tread depth and pressure change stopping distance, slip and other health and safety indicators in summer and winter conditions.

It is a screening model calibrated to published tire tests, not measured data for any specific tire. See the "Model and sources" tab in the Technical view.

## Files

- `app.py`: the Streamlit page.
- `tire_model.py`: the model (lookup tables and functions, no Streamlit).
- `tests/test_model.py`: checks that the model still matches its published calibration anchors.
- `tests/test_app.py`: smoke test that the page renders in both views, for every vehicle, and in demo mode.

## What is on the page

- Braking animation: the selected setup against the factory tire (factory size, new tread, recommended pressure). Click it to pause. The Simple view calls this the "factory tire"; the Technical view calls it the "reference".
- Tire picture: the size code as printed on a sidewall (for example 225/65R17), what each number means, and the tire drawn to scale from the front, from the side and as a footprint, with the factory size as a dashed outline.
- Simple view for a poster audience and Technical view with the charts and the model notes.
- Demo mode: cycles through preset scenarios with a large heading showing the conditions.

## Run locally

```
pip install -r requirements.txt
streamlit run app.py
```

## Test

```
pip install -r requirements-dev.txt
python -m pytest -q
```

## Deploy on Streamlit Community Cloud

Sign in at share.streamlit.io with this GitHub account, choose this repository, branch `main`, and main file `app.py`.
