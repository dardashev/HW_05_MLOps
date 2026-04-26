import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Пример использования расширения Marimo для VSCode
    """)
    return


@app.cell
def _():
    print('Hello, Marimo')
    return


@app.cell
def _():
    'Hello, Marimo'
    return


@app.cell
def _():
    forty_two = 42
    forty_two
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('src\Iris.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


if __name__ == "__main__":
    app.run()
