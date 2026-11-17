"""Smoke test for the Streamlit page: both views and demo mode must render without an exception."""

from pathlib import Path

import pytest
from streamlit.testing.v1 import AppTest

import tire_model as tm

APP = str(Path(__file__).resolve().parents[1] / "app.py")


@pytest.mark.parametrize("view", ["Simple", "Technical"])
@pytest.mark.parametrize("vehicle", list(tm.VEHICLES))
def test_page_renders_for_every_vehicle_in_both_views(view, vehicle):
    app = AppTest.from_file(APP, default_timeout=30)
    app.session_state["view"] = view
    app.session_state["vehicle"] = vehicle
    app.run()
    assert not app.exception


def test_demo_mode_renders():
    app = AppTest.from_file(APP, default_timeout=30)
    app.session_state["demo"] = True
    app.session_state["demo_pending"] = True
    app.run()
    assert not app.exception
