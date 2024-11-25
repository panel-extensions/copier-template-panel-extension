# Panel Extension Copier Template

A [*Copier*](https://copier.readthedocs.io/en/stable/) template for creating Panel extensions, leveraging the [Pixi](https://github.com/prefix-dev/pixi) package manager to simplify setup and management.

This template comes preconfigured with essential tools and best practices to help you develop, document, and distribute high-quality Panel-based applications or extensions.

* [X] **Hatch-based Packaging**: Managed by [Hatch](https://hatch.pypa.io/latest/install/) for streamlined dependency management and build processes.
* [X] **Linting and Code Quality with [`ruff`](https://github.com/charliermarsh/ruff)**: A fast and configurable linting tool for maintaining consistent code style.
* [X] **Testing with [`pytest`](https://github.com/pytest-dev/pytest)**: Includes support for async tests and thorough configuration for reliable testing.
* [X] **Documentation Generation**: Leverages [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) for beautiful documentation and [mkdocstrings](https://mkdocstrings.github.io/) for automatic API documentation.
* [X] **GitHub Actions CI/CD**: Preconfigured workflows for automated testing, building, and publishing.
* [X] **Pixi Package Management**: Integrated with Pixi for efficient and reproducible environment management.
* [X] **Update Flexibility**: Easily update your project to newer template versions with minimal disruption.
* [X] **BSD License**: Uses the OSI-approved BSD license, ideal for open-source projects.

To install and get started with Pixi, please refer to the [Pixi documentation](https://pixi.sh).

## Getting Started

### Step 1 - Create from Template

To create a new Panel extension:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier copy --trust https://github.com/panel-extensions/copier-template-panel-extension <panel-extension-name>
```

### Step 2 - Create and Add Remote Repository

Go to Github and create your repository with the <panel-extension-name>. Then set the remote:

```bash
git remote add origin https://github.com/<github-user>/<panel-extension-name>.git
```

The push your new repository

```bash
git push --set-upstream origin main
```

### Step 3 - Set Up GitHub Pages Docs

Enable GitHub Pages through **Settings > Pages** on the GitHub toolbar:

<img width="710" alt="image" src="https://private-user-images.githubusercontent.com/42288570/389284308-9bd345e5-7f3f-47c6-80e9-719063396f27.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzI0NjE5NTAsIm5iZiI6MTczMjQ2MTY1MCwicGF0aCI6Ii80MjI4ODU3MC8zODkyODQzMDgtOWJkMzQ1ZTUtN2YzZi00N2M2LTgwZTktNzE5MDYzMzk2ZjI3LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDExMjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMTI0VDE1MjA1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY2ZTZjM2ZlOGFjMjBjNWM2YmRkZjE4ZjNkMzMyZjczMDVkOGFiMWM3NTA1OTVmZTY4NzE3NTdmZDE1NTM4ODImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.rj-hZ-dWRsQUgaE4FYd2H9VBdK7UyBC09zt2P8PAv_c">

On your GitHub repo's **About** section in the sidebar, be sure to add the link to your docs page:

https://<github-user>.github.io/<panel-extension-name>/

If your docs page is missing a sidebar, remember to add imports to `src/__init__.py` and include them in `__all__`.

### Step 4 - Link to PyPI

Head over to [PyPI](https://pypi.org/manage/account/publishing) and fill out the form:

<img width="797" alt="image" src="https://github.com/user-attachments/assets/69ea7626-a2df-4fbe-a1d4-d20eb5e0cdd7">

### Step 5 - Release with a Tag

Once you've populated the template, you can release to PyPI by creating a tag!

![image](https://github.com/user-attachments/assets/970fe011-2ca4-4018-b541-478ac76d3185)

![image](https://github.com/user-attachments/assets/374cd1ec-b1ea-4aef-b1a7-b2818660b0e8)

## Updating the Template

To update to the latest template version run:

```bash
pixi exec --spec copier --spec ruamel.yaml -- copier update --defaults --trust
```

Note: `copier` will show `Conflict` for files with manual changes during an update. This is normal. As long as there are no merge conflict markers, all patches applied cleanly.
