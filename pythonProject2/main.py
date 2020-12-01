import pandas as pd

#print(df.isnull().sum()) - check how many null values
#creating modified df to fill N/A w/ 0s

def melt_df(modded_df):
    melted_df = pd.melt(modded_df,
                        id_vars = ["ID","INT_FAMILIARITY", "INT_INTEREST", "GENDER", "AGE", "HOUSEHOLD_INCOME",
                                   "EDUCATION","REGION"],
                        var_name = "COUNTRY",
                        value_name = "RATING")
    return melted_df

def calc_country_percent(place, melt):
    country_df = melt.loc[melt["COUNTRY"] == place, :]
    country_tot =(country_df["RATING"].astype(int)).astype(bool).sum()

    country_5 = country_df.apply(lambda x: True if x["RATING"] == 5 else False, axis=1)
    country_5_count = country_5.sum()

    country_5_perc = country_5_count / country_tot * 100
    return country_5_perc


#print(mod_df.isnull().sum()) - check if there are any more n/a
#print(df.info())

if __name__ == "__main__":
    url = (r"https://raw.githubusercontent.com/fivethirtyeight/data/master/food-world-cup/food-world-cup-data.csv")
    df = pd.read_csv(url, encoding="latin-1")

    # changing column names to shorten
    df.columns = ["ID", 'INT_FAMILIARITY', 'INT_INTEREST', "ALGERIA", "ARGENTINA", "AUSTRALIA", "BELGIUM",
                  "BOSNIA_AND_HERZEGOVINA", "BRAZIL", "CAMEROON", "CHILE", "COLUMBIA", "COSTA RICA", "CROATIA",
                  "ECUADOR",
                  "ENGLAND", "FRANCE", "GERMANY", "GHANA", "GREECE", "HONDURAS", "IRAN", "ITALY", "IVORY COAST",
                  "JAPAN",
                  "MEXICO", "NETHERLANDS", "NIGERIA", "PORTUGAL", "RUSSIA", "SOUTH KOREA", "SPAIN", "SWITZERLAND",
                  "UNITED_STATES", "URUAGUAY", "CHINA", "INDIA", "THAILAND", "TURKEY", "CUBA", "ETHIOPIA", "VIETNAM",
                  "IRELAND",
                  "GENDER", "AGE", "HOUSEHOLD_INCOME", "EDUCATION", "REGION"]

    mod_df = df.fillna("0")  # pass by ref for melt_df

    # initializing dict to store countries and list to store scores
    country_perc = {}  # countries and scores
    country_score = [] # intermediate list for scores

    # populating the country name list
    country_name = list(df.columns)
    country_name = country_name[3:43]
#    print(len(country_name))

    melted = melt_df(mod_df)

    # stores scores in a list
    for i in range(len(country_name)):
         country_score.append(calc_country_percent(country_name[i], melted))


    # populate the country_perc dict
    country_perc["Country"] = country_name
    country_perc["5-Ratings"] = country_score

    print(country_score)
    print(country_perc)

    # export as CSV
    output = pd.DataFrame(country_perc, columns=["Country", "5-Ratings"])
    output.to_csv(r"C:\Users\Cliff Chen\Desktop\Country_Food_5_Ratings_Proportions.csv", index = False, header=True)

    mod_df.to_csv(r"C:\Users\Cliff Chen\Desktop\Country (ALL) Scores.csv", index = False, header=True)

    melted.to_csv(r"C:\Users\Cliff Chen\Desktop\Melted Scores CSV.csv", index = False, header=True)

#        country_perc[country_name[i]] = calc_country_percent(country_name[i], melted)
#        print("The total percentage of 5-Ratings for", country_name[i], end="")
#        print(" is: ", end="")
#        print(" - - - - - - %.2f" %country_perc[country_name[i]], end="")
#       print("%")





