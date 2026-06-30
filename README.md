# Project 008

A minimal Streamlit test app used to verify GitHub-to-Streamlit deployment.

## App

The app currently displays:

```text
Hello world!
```

It also includes a simple hover icon demo with four inline SVG icon cards:

| Icon | Purpose |
|---|---|
| Plug | Connection test |
| AI | Simple animation test |
| Deploy | GitHub-to-Streamlit deployment concept |
| Settings | Hover animation test |

## Hover icon note

The hover icon section is inspired by [Its Hover](https://www.itshover.com/icons), which provides animated React + Motion icon components.

Because this repo is a Python Streamlit app rather than a React app, `app.py` uses `streamlit.components.v1.html` with lightweight inline SVG and CSS hover animations instead of importing the original React components.

## Main file

```text
app.py
```

## Deploy on Streamlit Community Cloud

Use the following settings when creating the app:

| Setting | Value |
|---|---|
| Repository | `ThianYong/project-008` |
| Branch | `main` |
| Main file path | `app.py` |
