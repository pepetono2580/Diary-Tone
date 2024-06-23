import streamlit as st
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path
import plotly.express as px

files = glob.glob("diary/*.txt")
sorted(files)

path_names = []
for file in files:
    path_names.append(Path(file).stem)

d_files = []
for i in path_names:
    d = {"date": i}
    with open(f"diary/{i}.txt", "r", encoding="utf-8") as file:
        d["content"] = file.read()

    d_files.append(d)

analyzer = SentimentIntensityAnalyzer()

for i in d_files:
    i["sent_analysis"] = analyzer.polarity_scores(i["content"])

print(d_files[6])

st.title("Diary Tone")

st.subheader("Positivity")

dates = [dict["date"] for dict in d_files]
positivity = [dict["sent_analysis"]["pos"] for dict in d_files]
figure = px.line(x=dates, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")

negativity = [dict["sent_analysis"]["neg"] for dict in d_files]
figure2 = px.line(x=dates, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure2)