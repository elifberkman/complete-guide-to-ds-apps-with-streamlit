import pandas as pd
import streamlit as st
import altair as alt

# https://vega.github.io/vega-themes/?theme=urbaninstitute
# alt.themes.enable("urbaninstitute")
# alt.themes.enable("dark")


@st.cache_data
def load_data():
    df = pd.read_csv("../data/ted.csv")
    return df


df = load_data()


def main():
    page = st.sidebar.selectbox(
        "Select a page",
        [
            "Vega Lite",
            "Line Plot",
            "Bar",
            "Scatter",
            "Area Chart",
            "Scatter Matrix",
            "Link Scatter",
            "Heatmap",
            "Horizontal Bar",
            "Grouped Bar",
            "Stacked Bar",
            "Normalized Stacked Bar",
            "Normalized Stacked Bar with Text",
            "Box Plot",
            "Interactive Legend",
            "Concatenate",
            "Dual Y Axes",
            "Horizontal Concatenation",
            "Vertical Concatenation",
            "Interactive Chart"
        ]
    )

    if page == "Vega Lite":
        st.header("Vega Lite")
        vegalite()

    elif page == "Line Plot":
        st.header("Line Plot")
        visualize_line()

    elif page == "Bar":
        st.header("Bar")
        bar()

    elif page == "Scatter":
        st.header("Scatter")
        scatter()

    elif page == "Area Chart":
        st.header("Area Chart")
        area_chart()

    elif page == "Scatter Matrix":
        st.header("Scatter Matrix")
        scatter_matrix()

    elif page == "Link Scatter":
        st.header("Scatter Matrix with Href")
        link_scatter()

    elif page == "Heatmap":
        st.header("Heatmap")
        heatmap()

    elif page == "Horizontal Bar":
        st.header("Horizontal Bar")
        horizontal_bar()

    elif page == "Grouped Bar":
        st.header("Grouped Bar")
        grouped_bar()

    elif page == "Stacked Bar":
        st.header("Stacked Bar")
        stacked_bar()

    elif page == "Normalized Stacked Bar":
        st.header("Normalized Stacked Bar")
        normalized_stacked_bar()

    elif page == "Normalized Stacked Bar with Text":
        st.header("Normalized Stacked Bar with Text")
        normalized_stacked_bar_with_text()

    elif page == "Box Plot":
        st.header("Box Plot")
        boxplot()

    elif page == "Interactive Legend":
        st.header("Interactive Legend")
        interactive_legend()

    elif page == "Concatenate":
        st.header("Concatenate")
        concatenate()

    elif page == "Dual Y Axes":
        st.header("Dual Y Axes")
        dual_y_axes()

    elif page == "Horizontal Concatenation":
        st.header("Horizontal Concatenation")
        horizontal_concat()

    elif page == "Vertical Concatenation":
        st.header("Vertical Concatenation")
        vertical_concat()

    elif page == "Interactive Chart":
        st.header("Interactive Chart")
        interactive_chart()


def vegalite():
    st.vega_lite_chart(df, {
        'mark': {'type': 'circle', 'tooltip': True},
        'width': 650,
        'height': 500,
        'encoding': {
            'x': {'field': 'duration', 'type': 'quantitative'},
            'y': {'field': 'views', 'type': 'quantitative'},
            'size': {'field': 'languages', 'type': 'quantitative'},
            'color': {'field': 'languages', 'type': 'quantitative'}
        }
    })


def visualize_line():
    df_copy = df.copy()
    # df_copy = (
    #     df_copy[
    #         (df_copy["film_year"] == 1999) |
    #         (df_copy["film_year"] == 2000) |
    #         (df_copy["film_year"] == 2001)
    #     ]
    # )

    df_copy = df_copy[df_copy["film_year"].isin(range(1999,2002))]
    df_copy["film_date"] = pd.to_datetime(df_copy["film_date"], format='mixed')
    line = (
        alt.Chart(df_copy)
        .mark_line()
        .encode(x="film_date", y="views")
        .properties(width=650, height=500)
        .interactive()
    )
    st.altair_chart(line)


def bar():
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)
    sort = st.checkbox("Sort")
    if sort:
        chart = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(
                x=alt.X('event:N', sort='-y'),
                y='views'
                # y='sum(views)'
            )
            .properties(width=650, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(bar_data)
            .mark_bar()
            .encode(x="event", y="views")
            .properties(width=650, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def scatter():
    toogle = st.checkbox("Tooggle Scatter")
    if toogle:
        chart = (
            alt.Chart(df, background="maroon")
            .mark_point()
            .encode(
                x="duration",
                y="views",
                size="languages",
                color="languages",
                tooltip=["duration", "views", "comments", "languages"]
            )
            .properties(width=650, height=500)
        )
    else:
        chart = (
                alt.Chart(df)
                .mark_point()
                .encode(
                    x="duration",
                    y="views",
                    size="languages",
                    color="languages",
                    tooltip=["duration", "views", "comments", "languages"]
                )
                .properties(width=650, height=500)
            )

    st.altair_chart(chart)


def area_chart():
    df_copy = df[df["film_year"] == 2012]
    df_copy["film_date"] = pd.to_datetime(df_copy["film_date"], format="mixed")
    radio_button = st.radio("Filled or Not", ("filled", "not filled"))
    if radio_button == "filled":
        chart = (
            alt.Chart(df_copy)
            .mark_area(color="maroon", line=True)
            .encode(
                x="film_date",
                y="views"
            )
            .properties(width=650, height=500)
        )
    else:
        chart = (
            alt.Chart(df_copy)
            .mark_area(color="maroon")
            .encode(
                x="film_date",
                y="views"
            )
            .properties(width=650, height=500)
        )
    st.altair_chart(chart)


def scatter_matrix():
    chart = (
        alt.Chart(df)
        .mark_circle()
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            color="published_day"
        )
        .properties(width=150, height=150)
        .repeat(
            row = ["duration", "views", "comments"],
            column= ["comments", "views", "duration"]
        )
        .interactive()
    )
    st.altair_chart(chart, theme=None)


def link_scatter():
    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="duration",
            y="comments",
            color="published_month",
            href="url:N",
            tooltip=["event","url:N"]
        )
        .interactive()
        .properties(width=650, height=500)
        .configure_legend(
            strokeColor="#ea4663",
            fillColor="#EEEEEE",
            padding=10,
            cornerRadius=10,
            orient="top-right"
        )
    )
    st.altair_chart(chart)


def heatmap():
    chart = (
        alt.Chart(df)
        .mark_rect()
        .encode(
            x="published_year:O",
            y="published_day",
            color="languages",
            tooltip=["languages", "published_day"]
        )
        .interactive()
        .properties(width=650, height=500)
    )
    st.altair_chart(chart)


def horizontal_bar():
    bar_data = df.sort_values(by="views", ascending=False)
    bar_data = bar_data.head(20)

    chart = (
        alt.Chart(bar_data)
        .mark_bar()
        .encode(
            x="views",
            y="event"
        )
        .properties(width=650, height=500)
        .interactive()
    )
    st.altair_chart(chart)


def grouped_bar():
    # dff = df[(df["published_day"] == "Monday") | (df["published_day"] == "Tuesday")]
    dff = df[df["published_day"].isin(["Monday", "Tuesday"])]
    toggle = st.checkbox("Toggle Horizontal")
    if toggle:
        chart = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                y="published_year:O",
                x=alt.X("sum(views):Q", title="Sum of Views"),
                color="published_year:N",
                column="published_day:N"
                # row="published_day:N"
            )
            .properties(width=500, height=500)
        )
    else:
        chart = (
            alt.Chart(dff)
            .mark_bar()
            .encode(
                x="published_year:O",
                y=alt.Y("sum(views):Q", title="Sum of Views"),
                color="published_year:N",
                column="published_day:N"
                # row="published_day:N"
            )
            .properties(width=500, height=500)
        )
    st.altair_chart(chart)


def stacked_bar():
    toggle = st.checkbox("Toggle this")
    if toggle:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y="published_year:O",
                x="sum(views)",
                color="published_day",
                tooltip=["sum(views)"]
            )
            .properties(width=700, height=500)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x="published_year:O",
                y="sum(views)",
                color="published_day",
                tooltip=["sum(views)"]
            )
            .properties(width=700, height=500)
            .interactive()
        )
    st.altair_chart(chart)


def normalized_stacked_bar():
    toggle = st.checkbox("Toggle this")
    if toggle:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                y=alt.X("mean(views)", stack="normalize"),
                x="published_year:O",
                color="published_day",
                tooltip=["mean(views)", "published_day"]
            )
            .properties(width=800, height=700)
            .interactive()
        )
    else:
        chart = (
            alt.Chart(df)
            .mark_bar()
            .encode(
                x=alt.X("mean(views)", stack="normalize"),
                y="published_year:O",
                color="published_day",
                tooltip=["mean(views)", "published_day"]
            )
            .properties(width=800, height=700)
            .interactive()
        )
    st.altair_chart(chart)


def normalized_stacked_bar_with_text():
    text = (
        alt.Chart(df)
        .mark_text(dx=-16, color="white")
        .encode(
            x=alt.X("sum(num_speaker):Q", stack="normalize"),
            y="published_year:O",
            detail="published_day",
            text=alt.Text("sum(num_speaker):Q", format=".1f")
        )
    )

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("sum(num_speaker)", stack="normalize"),
            y="published_year:O",
            color="published_day",
            tooltip=["sum(num_speaker)", "published_day"]
        )
        .properties(width=700, height=500)
        .interactive()
    )
    st.altair_chart(chart + text)


def boxplot():
    chart = (
        alt.Chart(df)
        .mark_boxplot()
        .encode(
            x="published_year:O",
            y="duration"
        )
        .properties(width=700, height=500)
        .interactive()
    )
    st.altair_chart(chart)


def interactive_legend():
    text = (
        alt.Chart(df)
        .mark_text(dx=-16, color="white")
        .encode(
            x=alt.X("sum(num_speaker):Q", stack="normalize"),
            y="published_year:O",
            detail="published_day",
            text=alt.Text("sum(num_speaker):Q", format=".1f")
        )
    )
    selection = alt.selection_multi(fields=["published_day"], bind="legend")
    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x=alt.X("sum(num_speaker)", stack="normalize"),
            y="published_year:O",
            color="published_day",
            tooltip=["sum(num_speaker)", "published_day"],
            opacity=alt.condition(selection, alt.value(1), alt.value(0.2)),
        )
        .properties(width=700, height=500)
        .interactive()
        .add_selection(selection)
    )
    st.altair_chart(chart + text)


def concatenate():
    scatter_plot =(
        alt.Chart(df)
        .mark_point()
        .encode(
            x="duration",
            y="views:Q"
        )
        .properties(width=250, height=250)
    )

    chart = (
        alt.concat(
            scatter_plot.encode(color="published_month"),
            scatter_plot.encode(color="published_day")
        )
        .resolve_scale(color="independent")
    )
    st.altair_chart(chart)


def dual_y_axes():
    base = (
        alt.Chart(df)
        .encode(
            alt.X("year(published_date):T")
        )
    )

    line_A = (
        base.mark_line(color="#ea4663")
        .encode(
            alt.Y("average(views):Q", axis=alt.Axis(titleColor="#ea4663"))
        )
    )

    line_B = (
        base.mark_line(color="#1a9988")
        .encode(
            alt.Y("average(comments):Q", axis=alt.Axis(titleColor="#1a9988"))
        )
    )

    chart = (
        alt.layer(line_A, line_B)
        .resolve_scale(y="independent")
        .properties(width=700, height=500)
    )
    st.altair_chart(chart)


def horizontal_concat():
    chart1 = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="duration",
            y="views"
        )
        .properties(width=300, height=300)
    )

    chart2 = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="languages",
            y="views"
        )
        .properties(width=300, height=300)
    )

    # alternatively
    # chart = chart1 | chart2
    chart = alt.hconcat(chart1, chart2)
    st.altair_chart(chart)


def vertical_concat():
    base = (
        alt.Chart(df)
        .mark_area()
        .encode(
            x="published_date:T",
            y="languages:O"  # he did Q but it didn't work for me, so it looks upside down :)
        )
        .properties(width=600, height=200)
    )

    brush = alt.selection(type="interval", encodings=["x"])

    upper = (
        base.encode(
            alt.X("published_date:T", scale=alt.Scale(domain=brush))
        )
    )

    lower = (
        base.properties(height=60)
        .add_selection(brush)
    )

    # alternatively
    # chart = upper & lower
    chart = alt.vconcat(upper, lower)
    st.altair_chart(chart)


def interactive_chart():
    brush = alt.selection_interval()
    chart = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="languages:Q",
            y="views:Q",
            color=alt.condition(brush, "languages:Q", alt.value("gray"))
        )
        .properties(width=600, height=500)
        .add_selection(brush)
    )
    st.altair_chart(chart)


if __name__ == "__main__":
    main()
