"""Main module."""

import panel as pn


def create_app():
    """Create the main Panel application."""
    pn.extension()

    x_slider = pn.widgets.IntSlider(name="x", start=0, end=100)

    def apply_square(x):
        return f"{x} squared is {x**2}"

    return pn.Row(x_slider, pn.bind(apply_square, x_slider))


if __name__ == "__main__":
    create_app().servable()
