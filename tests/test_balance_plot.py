import sys
import pandas as pd
import pytest
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from ..src.callbacks import create_balance_plot

@pytest.fixture
def sample_data():
    """Fixture to create a sample DataFrame for testing."""
    return pd.DataFrame({
        "balance": [100, 200, 300, 400, 500, 600],
        "y": ["yes", "no", "yes", "no", "yes", "no"]
    })

def test_output_type(sample_data):
    """Test that the function returns a dictionary."""
    chart_dict = create_balance_plot(sample_data)
    assert isinstance(chart_dict, dict)

def test_chart_contains_density_transform(sample_data):
    """Test that the density transform is present in the Altair chart."""
    chart_dict = create_balance_plot(sample_data)
    assert "transform" in chart_dict
    assert any(transform["density"] == "balance" for transform in chart_dict["transform"])

def test_chart_encodings(sample_data):
    """Test that the chart has correct encodings for x, y, and color."""
    chart_dict = create_balance_plot(sample_data)
    encodings = chart_dict["encoding"]
    
    assert "x" in encodings
    assert encodings["x"]["field"] == "balance"
    assert encodings["x"]["type"] == "quantitative"

    assert "y" in encodings
    assert encodings["y"]["field"] == "density"
    assert encodings["y"]["type"] == "quantitative"

    assert "color" in encodings
    assert encodings["color"]["field"] == "y"
    assert encodings["color"]["type"] == "nominal"

def test_chart_interactivity(sample_data):
    """Test that the chart has interactivity enabled."""
    chart_dict = create_balance_plot(sample_data)
    assert "selection" in chart_dict or "params" in chart_dict  # Checking for interactivity

def test_chart_has_correct_colors(sample_data):
    """Test that the chart uses the correct colors for 'yes' and 'no'."""
    chart_dict = create_balance_plot(sample_data)
    color_scale = chart_dict["encoding"]["color"]["scale"]

    assert "domain" in color_scale
    assert color_scale["domain"] == ["yes", "no"]

    assert "range" in color_scale
    assert color_scale["range"] == ["#60ac5a", "#d16f6f"]



