from pandas import DataFrame
df = DataFrame({'abbrev': ['CT', 'CO', 'CA', 'TX']})


def add_state_names_column(my_df):
    """
    Add a oolumn of corresponding state names to a dataframe.
    Params (my_df) a Dataframe with a column called " abbrev" that has state abbrev
    return a copy of the original dataframe, but with an extra column
    """
    new_df = my_df_copy()
    names_map = {
        "CT": "Connecticut",
        "CO": "Colorado",
        "CA": "Cali",
        "TX": "Texas"}
    new_df["name"] = new_df["abbrev"].map(names_map)


if __name__ == "__main__":
    .
    print(df.head)
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
