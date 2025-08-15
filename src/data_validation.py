import pandas as pd

class DataValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_missing(self):
        """Return columns with missing values and their counts."""
        return self.df.isnull().sum()[self.df.isnull().sum() > 0]

    def check_duplicates(self):
        """Return number of duplicate rows."""
        return self.df.duplicated().sum()

    def check_column_types(self, expected_types: dict):
        """
        Check if columns match expected types.
        expected_types: dict of {column_name: type}
        Returns columns with mismatched types.
        """
        mismatches = {}
        for col, expected_type in expected_types.items():
            if col in self.df.columns:
                actual_type = self.df[col].dtype
                if actual_type != expected_type:
                    mismatches[col] = str(actual_type)
        return mismatches

    def check_value_ranges(self, ranges: dict):
        """
        Check if numeric columns are within specified ranges.
        ranges: dict of {column_name: (min, max)}
        Returns columns with out-of-range values.
        """
        out_of_range = {}
        for col, (min_val, max_val) in ranges.items():
            if col in self.df.columns:
                below = (self.df[col] < min_val).sum()
                above = (self.df[col] > max_val).sum()
                if below > 0 or above > 0:
                    out_of_range[col] = {'below_min': below, 'above_max': above}
        return out_of_range