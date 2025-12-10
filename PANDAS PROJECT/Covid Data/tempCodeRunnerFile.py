
print(covid.groupby('Region')['Confirmed' ,'Deaths','Recovered' ].sum())