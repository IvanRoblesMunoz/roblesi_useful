"""  eda (function): returns description of the columns in a given dataset"""

import pandas as pd


def eda(data, unique=False, unique_ls="all"):
    """
    Returns a review of the column types, number and percentages of Null and unique values

    Args:
      data (pandasDataFrame) : data to be evaluated
      unique (boolean) :  If true return count and percentage of unique values otherwise dont return
      unique_ls (list or string) :  if 'all' is returned as a string, then return all columns,
              otherwise pass a list of column names to be evaluated, all other columns will be empty

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

    if unique:

        # If all columns are selected, then
        if unique_ls == "all":
            unique_ls = data.columns

        # Count Number of unique values
        nunique = pd.DataFrame(data[unique_ls].nunique(), columns=["unique_count"])

        nunique["unique_count_perc"] = nunique["unique_count"] / len(data) * 100
        nunique = nunique.reset_index().rename(columns={"index": "col_name"})
        columns = columns.merge(
            nunique, left_on="col_name", right_on="col_name", how="outer"
        )

    return columns
