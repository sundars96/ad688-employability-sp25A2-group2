import pandas as pd
import plotly.express as px

data = {
    "Job Role": ["Machine Learning Engineer", "Data Scientist", "AI Risk Analyst",
                 "Software Developer", "Mechanical Engineer", "Customer Service Rep"],
    "AI-Powered": ["Yes", "Yes", "Yes", "No", "No", "No"],
    "Average Salary ($)": [140000, 125000, 118000, 95000, 85000, 45000]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x="Job Role",
    y="Average Salary ($)",
    color="AI-Powered",
    title="<b>AI vs. Non-AI Job Salaries in 2024</b>",
    labels={
        "Job Role": "<i>Career Path</i>",
        "Average Salary ($)": "<i>Annual Salary ($)</i>"
    },
    barmode="group",
    color_discrete_sequence=px.colors.qualitative.Bold  # Bold color palette
)

fig.update_layout(
    font=dict(family="Arial", size=14),
    title_font_size=20,
    plot_bgcolor="rgba(240,240,240,0.9)",  # light background
    paper_bgcolor="rgba(240,240,240,0.95)",
    legend_title_text="<b>Category</b>",
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=True, gridcolor="lightgrey", zeroline=False)
)

fig.update_traces(marker_line_width=1.5, marker_line_color='black')

fig.show()

