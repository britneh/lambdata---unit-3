from pandas import DataFrame
df = DataFrame({'abbrev': ['CT', 'CO', 'CA', 'TX']})

class DataFrameProcessor():
    def __init__(self, df):
        """
        Params (df) a Dataframe with a column called " abbrev" that has state abbrev
        """
        self.df = df

def add_state_names_column(self):
    """
    Add a oolumn of corresponding state names to a dataframe.
    return a copy of the original dataframe, but with an extra column
    """
    #new_df = self.df.copy()
    names_map = {
        "CT": "Connecticut",
        "CO": "Colorado",
        "CA": "Cali",
        "TX": "Texas"}
    self.df["name"] = self.df["abbrev"].map(names_map)
    return self

if __name__ == "__main__":
    print(df.head)
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())

    processor = DataFrameProcessor(df=df)
    print(processor.df.head())
    processor.add_state_names_column()
    print(processor.df.head())
    #how to inspect the dataframe for example df.head()