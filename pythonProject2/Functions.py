#collecting total number of votes - ALGERIA
test_df = melted.loc[melted["COUNTRY"] == "UNITED_STATES", :]
test_tot = (test_df["RATING"].astype(int)).astype(bool).sum()

test_5 = test_df.apply(lambda x: True if x["RATING"] == 5 else False, axis=1)
test_5_count = test_5.sum()

test_5_perc = test_5_count / test_tot * 100

print("The total percentage of 5-Ratings for UNITED STATES is: ", end="")
print("%.2f" % test_5_perc, end="")
print("%")

#setting up the country count dict
for i in range(len(country_name)):
    country_perc[country_name[i]] = 0
print(country_perc)