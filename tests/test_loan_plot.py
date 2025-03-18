import sys
import pandas as pd
import pytest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ..src.callbacks import create_loan_plot  

@pytest.fixture
def sample_data():
    """Fixture to create a sample DataFrame for testing."""
    return pd.DataFrame({
        "loan": ["yes", "no", "yes", "no", "yes", "no"],
        "y": ["yes", "no", "yes", "no", "no", "yes"]
    })

def test_chart_returns_dict(sample_data):
    """Test that the function returns a dictionary."""
    chart_dict = create_loan_plot(sample_data)
    assert isinstance(chart_dict, dict), "The function should return a dictionary"

def test_chart_has_correct_encoding(sample_data):
    """Test that the chart has the expected encoding fields."""
    chart_dict = create_loan_plot(sample_data)
    
    assert "encoding" in chart_dict, "Encoding is missing in the chart"
    
    enc = chart_dict["encoding"]
    
    assert "x" in enc, "X encoding is missing"
    assert enc["x"]["field"] == "loan", f"Expected 'loan' for x-axis, found {enc['x']['field']}"
    assert "y" in enc, "Y encoding is missing"
    assert enc["y"]["aggregate"] == "count", "Y-axis should use count() aggregation"
    assert "color" in enc, "Color encoding is missing"
    assert enc["color"]["field"] == "y", f"Expected 'y' for color, found {enc['color']['field']}"
    assert "xOffset" in enc, "xOffset encoding is missing"
    assert enc["xOffset"]["field"] == "y", "xOffset should be based on 'y'"

def test_chart_has_tooltip(sample_data):
    """Test that the chart includes the correct tooltip field."""
    chart_dict = create_loan_plot(sample_data)

    assert "tooltip" in chart_dict["encoding"], "Tooltip encoding is missing"
    
    tooltip_enc = chart_dict["encoding"]["tooltip"]
    
    # Handle different tooltip formats
    if isinstance(tooltip_enc, list):
        tooltip_fields = [field.get("field", field.get("aggregate", "")) for field in tooltip_enc]
    else:
        tooltip_fields = [tooltip_enc.get("field", tooltip_enc.get("aggregate", ""))]

    assert "count" in tooltip_fields, f"Expected 'count()' in tooltip, found {tooltip_fields}"

