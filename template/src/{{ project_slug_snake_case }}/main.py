"""Main module for the Panel application."""

import panel as pn


def create_app() -> pn.Row:
    """Create the main Panel application.

    Returns
    -------
    pn.Row
        A Panel Row containing an interactive slider and its squared value.

    Examples
    --------
    >>> app = create_app()
    >>> app.servable()
    """
    pn.extension()

    x_slider = pn.widgets.IntSlider(name="x", start=0, end=100)

    def apply_square(x: int) -> str:
        return f"{x} squared is {x**2}"

    return pn.Row(x_slider, pn.bind(apply_square, x_slider))


if __name__ == "__main__":
    create_app().servable()
