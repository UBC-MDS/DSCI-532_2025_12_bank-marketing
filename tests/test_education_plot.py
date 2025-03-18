import sys
import pandas as pd
import pytest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ..src.callbacks import create_education_plot  

@pytest.fixture
def sample_data():
    """Fixture to create a sample DataFrame for testing."""
    return pd.DataFrame({
        "education": ["primary", "secondary", "tertiary", "primary", "secondary", "tertiary"],
        "y": ["yes", "no", "yes", "no", "yes", "no"]
    })

def test_chart_returns_dict(sample_data):
    """Test that the function returns a dictionary."""
    chart_dict = create_education_plot(sample_data)
    assert isinstance(chart_dict, dict), "The function should return a dictionary"

def test_chart_has_correct_encoding(sample_data):
    """Test that the chart has the expected encoding fields."""
    chart_dict = create_education_plot(sample_data)
    
    assert "encoding" in chart_dict, "Encoding is missing in the chart"
    
    enc = chart_dict["encoding"]
    
    assert "x" in enc, "X encoding is missing"
    assert enc["x"]["field"] == "education", f"Expected 'education' for x-axis, found {enc['x']['field']}"
    assert "y" in enc, "Y encoding is missing"
    assert enc["y"]["field"] == "proportion", "Y-axis should be proportion"
    assert enc["y"].get("stack") == "zero", "Y-axis should be stacked"

    assert "color" in enc, "Color encoding is missing"
    assert enc["color"]["field"] == "y", f"Expected 'y' for color, found {enc['color']['field']}"
    
def test_chart_has_tooltip(sample_data):
    """Test that the chart includes the correct tooltip field."""
    chart_dict = create_education_plot(sample_data)

    assert "tooltip" in chart_dict["encoding"], "Tooltip encoding is missing"
    
    tooltip_enc = chart_dict["encoding"]["tooltip"]
    
    # Handle different tooltip formats
    if isinstance(tooltip_enc, list):
        tooltip_fields = [field.get("field", field.get("aggregate", "")) for field in tooltip_enc]
    else:
        tooltip_fields = [tooltip_enc.get("field", tooltip_enc.get("aggregate", ""))]

    assert "proportion" in tooltip_fields, f"Expected 'proportion' in tooltip, found {tooltip_fields}"