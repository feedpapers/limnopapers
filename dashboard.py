import git
import datetime
import numpy as np
import pandas as pd

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
# df["prism_url"] = (
#     '<a href="' + df['prism_url'] + '" target="_blank">' + df['prism_url'] + '</a>'
# )

df["date"] = pd.to_datetime(df["git_date"])
df = df[::-1]
# df = df.sort_values("date", ascending=False)
df = df.reset_index(drop=True)
df.to_csv("dashboard.csv", index=False)
