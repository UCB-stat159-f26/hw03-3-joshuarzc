import matplotlib.pyplot as plt


COLORS = {"won": "#70C8E9", "lost": "#8A4088"}
LABELS = {"won": "Match won", "lost": "Match lost"}


def _plot_match_results(axes, matches):
    """Plot match results with separate colors for wins and losses."""
    for result in ["won", "lost"]:
        subset = matches[matches["result"] == result]
        axes.scatter(subset["player_age"], subset["age_difference"], s=14, color=COLORS[result], alpha=0.85, edgecolors="none", label=LABELS[result])


def _style_axes(axes):
    """Apply the shared axis style for the career match plot."""
    axes.set_xlabel("Player age")
    axes.set_ylabel("Age difference with opponent")
    axes.xaxis.tick_top()
    axes.xaxis.set_label_position("top")
    axes.tick_params(axis="both", length=0, colors="#8F8F8F", labelsize=9)
    axes.grid(color="#E9E9E9", linewidth=0.8)
    axes.axhline(0, color="#898989", linewidth=0.9)
    for spine in axes.spines.values():
        spine.set_visible(False)


def plot_career_matches(matches):
    """
    Create a career scatter plot from clean match data.

    Parameters:
    matches : A data frame returned by get_career_matches().

    Returns:
    A Matplotlib figure with match results colored by outcome.
    """
    figure, axes = plt.subplots(figsize=(12, 9))
    figure.subplots_adjust(top=0.75)
    _plot_match_results(axes, matches)
    _style_axes(axes)
    figure.suptitle("Professional Tennis Matches", fontsize=15, fontweight="bold", y=0.9)
    axes.legend(loc="lower center", bbox_to_anchor=(0.5, 1.08), frameon=False, ncol=2, fontsize=12)
    return figure
