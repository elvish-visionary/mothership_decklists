import pandas as pd

def df_to_markdown(df):
	"""
	Converts dataframe to markdown format string
	"""
	s = "|{}|\n".format("|".join(df.columns))
	s += "|{}|\n".format(":----".join(df.columns))

	for idx, row in df.iterrows():
		s += "|{}|\n".format("|".join(str(v) for v in row.values))
	return s