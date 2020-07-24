"""  eda (function): returns description of the columns in a given dataset"""

import pandas as pd


def eda(data):
    """
    Returns a review of the column types, number and percentages of Null and unique values

    Args:
      data (pandasDataFrame) : data to be evaluated
    Returns:
      Columns (pandasDataFrame) : a pandas dataframe with the overview of the data as mentioned
      above, it contains a row per column in the orginal dataframe to evaluate
    """

    # search column names, types, Nulls
    columns = pd.DataFrame(columns=["col_name"], data=data.columns)
    columns["col_type"] = pd.DataFrame(
        columns=["col_type"], data=data.dtypes
    ).set_index(columns.index)

    # Columns with missing values
    nulls = pd.DataFrame(data.isnull().sum(), columns=["Null"])
    nulls["Null_perc"] = nulls["Null"] / len(data) * 100
    nulls = nulls.reset_index().rename(columns={"index": "col_name"})
    columns = columns.merge(nulls, left_on="col_name", right_on="col_name", how="outer")

    # Count Number of unique values
    nunique = pd.DataFrame(
        data[list(columns["col_name"])].nunique(), columns=["unique_count"]
    )

    nunique["unique_count_perc"] = nunique["unique_count"] / len(data) * 100
    nunique = nunique.reset_index().rename(columns={"index": "col_name"})
    columns = columns.merge(
        nunique, left_on="col_name", right_on="col_name", how="outer"
    )
    return columns
