import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tennis_career import plot_career_matches
from tennis_career.parser import _parse_career_js
from tennis_career.transform import _clean_career_records


def test_plot_career_matches():
    with open("tests/mock_data/male_player_career.js") as file:
        records = _parse_career_js(file.read())

    matches = _clean_career_records(records, "1986-06-03")
    figure = plot_career_matches(matches)
    axes = figure.axes[0]

    assert isinstance(figure, Figure)
    assert len(figure.axes) == 1
    assert len(axes.collections) == 2
    assert len(axes.lines) == 1

    plt.close(figure)
