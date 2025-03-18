import sys
import pandas as pd
import pytest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.callbacks import create_contact_plot

@pytest.fixture
def sample_data():
    """Fixture to create a sample DataFrame for testing."""
    return pd.DataFrame({
        "campaign": [1, 2, 3, 4, 5, 6],
        "y": ["yes", "no", "yes", "no", "yes", "no"]
    })

def test_output_type(sample_data):
    """Test that the function returns a dictionary."""
    chart_dict = create_contact_plot(sample_data)
    assert isinstance(chart_dict, dict)

def test_chart_has_mark_type(sample_data):
    """Test that the chart uses a square mark."""
    chart_dict = create_contact_plot(sample_data)
    assert chart_dict["mark"]["type"] == "square"

def test_chart_encodings(sample_data):
    """Test that the chart has correct encodings for x, y, color, and size."""
    chart_dict = create_contact_plot(sample_data)
    encodings = chart_dict["encoding"]

    assert "x" in encodings
    assert encodings["x"]["field"] == "campaign"
    assert encodings["x"]["type"] == "quantitative"

    assert "y" in encodings
    assert encodings["y"]["field"] == "y"
    assert encodings["y"]["type"] == "nominal"

    assert "color" in encodings
    assert encodings["color"]["field"] == "y"
    assert encodings["color"]["type"] == "nominal"

    assert "size" in encodings
    assert encodings["size"]["aggregate"] == "count"

def test_chart_has_tooltip(sample_data):
    """Test that the chart includes the correct tooltip fields."""
    chart_dict = create_contact_plot(sample_data)
    
    assert "tooltip" in chart_dict["encoding"], "Tooltip encoding is missing"

    tooltip_enc = chart_dict["encoding"]["tooltip"]
    
    # Handle both list of dicts and shorthand format
    if isinstance(tooltip_enc, list):
        tooltip_fields = [field.get("field", field.get("aggregate", "")) for field in tooltip_enc]
    else:
        tooltip_fields = [tooltip_enc.get("field", tooltip_enc.get("aggregate", ""))]

    assert "campaign" in tooltip_fields, f"Expected 'campaign' in tooltip, found {tooltip_fields}"
    assert "y" in tooltip_fields, f"Expected 'y' in tooltip, found {tooltip_fields}"
    assert "count" in tooltip_fields, f"Expected 'count' in tooltip, found {tooltip_fields}"

def test_chart_has_correct_colors(sample_data):
    """Test that the chart uses the correct colors for 'yes' and 'no'."""
    chart_dict = create_contact_plot(sample_data)
    color_scale = chart_dict["encoding"]["color"]["scale"]

    assert "domain" in color_scale
    assert color_scale["domain"] == ["yes", "no"]

    assert "range" in color_scale
    assert color_scale["range"] == ["#60ac5a", "#d16f6f"]

def test_chart_interactivity(sample_data):
    """Test that the chart has interactivity enabled."""
    chart_dict = create_contact_plot(sample_data)
    assert "selection" in chart_dict or "params" in chart_dict

