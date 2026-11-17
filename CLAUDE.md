# ESA-03 tire fitment explorer

Streamlit display that sits beside the poster for the ESA-03 Fleet Tire Optimization Strategy capstone (client: Ontario's Electrical Safety Authority). It shows how tire width, rim diameter, tire type, tread depth and pressure change stopping distance, slip and other health and safety indicators in summer and winter.

## Layout

- `tire_model.py`: the model. Lookup tables and pure functions, no Streamlit. `evaluate(cfg, env)` returns every output for one tire setup in one condition.
- `app.py`: the Streamlit page. Sidebar controls, braking animation (HTML canvas in `st.iframe`), tire size picture (SVG drawn to scale, shown with `st.image`), Plotly charts, Simple and Technical views, demo mode.
- `tests/test_model.py`: calibration anchors and sanity checks for the model.
- `tests/test_app.py`: smoke test that the page renders in both views and in demo mode.
- `.streamlit/config.toml`: light theme and minimal toolbar for the hosted version.

## Commands

- Run: `streamlit run app.py`
- Test: `python -m pytest -q`
- Install: `pip install -r requirements.txt` (add `pytest` for tests)

## Rules for changes

- This is a screening model calibrated to published tire tests, not measured data. Never word UI text as if a number were a measurement of a specific tire.
- Any change to friction tables, exponents or the hydroplaning formula must keep `tests/test_model.py` passing. If an anchor needs to move, cite the test or paper that justifies it in the test docstring and in the "Model and sources" tab.
- Keep the model free of Streamlit imports.
- Keep code simple and readable: plain functions and dicts, no clever abstractions. Explain in prose (docstrings, README, the model tab), not inline comments.
- UI wording is plain language for a poster audience. The Simple view carries no jargon; the Technical view may.
- Chart colours: selected setup is blue `#2a78d6`, reference is grey dashed, tire types keep their fixed colours in `COMPOUND_COLOR`. Do not reuse status colours for series.
- Streamlit is pinned in `requirements.txt`. `st.iframe` and `width="stretch"` need a recent version, so do not lower the pin without testing.

## Known gaps

- Vehicle classes in `VEHICLES` are generic placeholders. Replace with the ESA fleet list and factory sizes when available.
- Price, wear, fuel, wheel weight, ride and damage indices are simple scaling rules. Replace with ESA purchase and service records where the project has them.
- No studded tires, load transfer, ABS tuning or brand differences.
- Standing water and slush are the least calibrated region. When the braking speed is close to the hydroplaning onset, distance becomes very sensitive to tread, width and pressure (for example 6 psi low adding about 55% in slush at 80 km/h). The direction is right; the size has no published anchor yet.
- The quick-fitment buttons pick the nearest 5-point aspect ratio, which is not always a size that is sold.
