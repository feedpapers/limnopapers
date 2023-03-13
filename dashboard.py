# https://gist.github.com/exzhawk/33e5dcfc8859e3b6ff4e5269b1ba0ba4
import os
import git
import requests
import datetime
import numpy as np
import pandas as pd
from dash import Dash, dash_table, html
from html.parser import HTMLParser
from dash.dependencies import Input, Output


def patch_file(file_path: str, content: bytes, extra: dict = None) -> bytes:
    if file_path == "index.html":
        index_html_content = content.decode("utf8")
        extra_jsons = f"""
        var patched_jsons_content={{
        {','.join(["'/" + k + "':" + v.decode("utf8") + "" for k, v in extra.items()])}
        }};
        """
        patched_content = (
            index_html_content.replace(
                "<footer>",
                f"""
            <footer>
            <script>
            """
                + extra_jsons
                + """
            const origFetch = window.fetch;
            window.fetch = function () {
                const e = arguments[0]
                if (patched_jsons_content.hasOwnProperty(e)) {
                    return Promise.resolve({
                        json: () => Promise.resolve(patched_jsons_content[e]),
                        headers: new Headers({'content-type': 'application/json'}),
                        status: 200,
                    });
                } else {
                    return origFetch.apply(this, arguments)
                }
            }
            </script>
            """,
            )
            .replace('href="/', 'href="')
            .replace('src="/', 'src="')
        )
        return patched_content.encode("utf8")
    else:
        return content


def write_file(
    file_path: str,
    content: bytes,
    target_dir="docs",
):
    target_file_path = os.path.join(target_dir, file_path.lstrip("/").split("?")[0])
    target_leaf_dir = os.path.dirname(target_file_path)
    os.makedirs(target_leaf_dir, exist_ok=True)
    with open(target_file_path, "wb") as f:
        f.write(content)
    pass


class ExternalResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.resources = []

    def handle_starttag(self, tag, attrs):
        if tag == "link":
            for k, v in attrs:
                if k == "href":
                    self.resources.append(v)
        if tag == "script":
            for k, v in attrs:
                if k == "src":
                    self.resources.append(v)


def make_static(base_url, target_dir="docs"):
    index_html_bytes = requests.get(base_url).content
    json_paths = [
        "_dash-layout",
        "_dash-dependencies",
    ]
    extra_json = {}
    for json_path in json_paths:
        json_content = requests.get(base_url + json_path).content
        extra_json[json_path] = json_content

    patched_bytes = patch_file("index.html", index_html_bytes, extra=extra_json)
    write_file("index.html", patched_bytes, target_dir)
    parser = ExternalResourceParser()
    parser.feed(patched_bytes.decode("utf8"))
    extra_js = [
        "_dash-component-suites/dash/dcc/async-graph.js",
        "_dash-component-suites/dash/dcc/async-plotlyjs.js",
        "_dash-component-suites/dash/dash_table/async-table.js",
        "_dash-component-suites/dash/dash_table/async-highlight.js",
    ]
    for resource_url in parser.resources + extra_js:
        resource_url_full = base_url + resource_url
        print(f"get {resource_url_full}")
        resource_bytes = requests.get(resource_url_full).content
        patched_bytes = patch_file(resource_url, resource_bytes)
        write_file(resource_url, patched_bytes, target_dir)


def main():
    port = 9050

    df = pd.read_csv("log.csv")

    repo = git.Repo()
    git_dates = [
        datetime.datetime.fromtimestamp(x.commit.committed_date).strftime("%Y-%m-%d")
        for x in repo.blame_incremental("HEAD", file="log.csv")
    ]
    git_linenos = [x.linenos for x in repo.blame_incremental("HEAD", file="log.csv")]
    git_linenos = [
        np.where([i in list(x) for x in git_linenos])[0] for i in range(df.shape[0])
    ]
    git_linenos[0] = np.array(0)
    git_linenos = [int(x) for x in git_linenos]

    git_dates_res = pd.DataFrame(
        {"line": git_linenos, "git_date": [git_dates[i - 1] for i in git_linenos]}
    )
    df = pd.concat([df, git_dates_res], axis=1)

    df = df[~pd.isna(df["title"])]
    df = df[[x in ["y", "", np.nan] for x in df["posted"]]]
    df = df.drop(columns=["posted"])
    df["prism_url"] = (
        "<a href='" + df["prism_url"] + "' target='_blank'>" + df["prism_url"] + "</a>"
    )

    df["date"] = pd.to_datetime(df["git_date"])
    df = df.sort_values("date", ascending=False)
    df = df.reset_index(drop=True)

    app = Dash(__name__)
    app.scripts.config.serve_locally = True
    app.css.config.serve_locally = True
    # app.config.update({"requests_pathname_prefix": "/limnopapers/"})

    app.layout = html.Div(
        children=[
            html.Button("save static", id="save", n_clicks=0),
            html.Span("", id="saved"),
            dash_table.DataTable(
                id="table",
                columns=[
                    {"name": "Title", "id": "title", "type": "text"},
                    {"name": "Source", "id": "dc_source", "type": "text"},
                    {
                        "name": "Link",
                        "id": "prism_url",
                        "type": "text",
                        "presentation": "markdown",
                    },
                    {"name": "Date", "id": "date", "type": "text"},
                ],
                markdown_options={"html": True},
                data=df.to_dict("records"),
                filter_action="native",
                style_table={
                    "height": 400,
                },
                style_data={
                    "width": "150px",
                    "minWidth": "150px",
                    "maxWidth": "150px",
                    "overflow": "hidden",
                    "textOverflow": "ellipsis",
                },
            ),
        ]
    )

    @app.callback(
        Output("saved", "children"),
        Input("save", "n_clicks"),
    )
    def save_result(n_clicks):
        make_static(f"http://127.0.0.1:{port}/")
        return "saved"

    app.run_server(debug=False, port=port)


if __name__ == "__main__":
    main()
