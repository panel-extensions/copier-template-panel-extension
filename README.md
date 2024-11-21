# copier-template-panel-extension

A copier template for creating Panel extensions, leveraging the [pixi](https://github.com/prefix-dev/pixi) package manager to simplify setup and management. 

This template comes pre-configured with essential tools and best practices to help you develop, document, and distribute high-quality Panel-based applications or extensions.

* [X] **Hatch-based Packaging**: Managed by [Hatch](https://hatch.pypa.io/latest/install/) for streamlined dependency management and build processes.
* [X] **Linting and Code Quality with [`ruff`](https://github.com/charliermarsh/ruff)**: Fast and configurable linting tool for maintaining consistent code style.
* [X] **Testing with [`pytest`](https://github.com/pytest-dev/pytest)**: Includes support for async tests and thorough configuration for reliable testing.
* [X] **Documentation Generation**: Leverages [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for beautiful documentation and [mkdocstrings](https://mkdocstrings.github.io/) for automatic API documentation.
* [X] **GitHub Actions CI/CD**: Pre-configured workflows for automated testing, building, and publishing.
* [X] **Pixi Package Management**: Integrated with pixi for efficient and reproducible environment management.
* [X] **Update Flexibility**: Easily update your project to newer template versions with minimal disruption.
* [X] **BSD License**: Uses the OSI-approved BSD license, ideal for open-source projects.

For more on pixi, see the [documentation here](https://pixi.sh).

## Getting Started

### Step 1 - Create from template

To create a new Panel extension:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier copy --trust https://github.com/panel-extensions/copier-template-panel-extension <panel-extension-name>
```

To update to a newer template version:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier update --defaults --trust
```

Note: `copier` will show `Conflict` for files with manual changes during an update—this is normal. As long as there are no merge conflict markers, all patches applied cleanly.

### Step 2 - Setup GitHub Pages docs

Enable GitHub Pages through Settings > Pages on the GitHub toolbar:

<img width="801" alt="image" src="https://github.com/ahuang11/cookiecutter-hipster-pypackage/assets/15331990/accd33a5-dc64-4df1-a009-07a3eed0bc38">

On your GitHub repo's sidebar's About section, be sure to add the link to your docs page and some tags!

If your docs page is missing a sidebar, remember to add imports to `src/__init__.py` and add them to `__all__`!

### Step 3 - Link to PyPi

Head over to https://pypi.org/manage/account/publishing and fill out the form:

<img width="813" alt="image" src="https://github.com/user-attachments/assets/8f3a5aad-1394-4d74-a4fc-cbefb18777ff">

#### Step 4 - Release with a tag

Now, when you've populated the template, you can release to PyPi by making a tag!

<img width="1169" alt="image" src="https://github.com/ahuang11/cookiecutter-hipster-pypackage/assets/15331990/7820461a-d559-4018-b50c-c77a612cb81d">

<img width="938" alt="image" src="https://github.com/ahuang11/cookiecutter-hipster-pypackage/assets/15331990/3ac62bd3-8a1f-47c1-80c9-109db0b9a0ba">
