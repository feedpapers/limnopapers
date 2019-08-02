import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Spatial and temporal variation of ecosystem properties at macroscales"], 'summary': ["Although spatial and temporal variation in ecological properties has been well‐studied, crucial knowledge gaps remain for studies conducted at macroscales and for ecosystem properties related to material and energy. We test four propositions of spatial and temporal variation in ecosystem properties within a macroscale (1000 km's) extent. We fit Bayesian hierarchical models to thousands of observations from over two decades to quantify four components of variation – spatial (local and regional) and temporal (local and coherent); and to model their drivers. We found strong support for three propositions: (1) spatial variation at local and regional scales are large and roughly equal, (2) annual temporal variation is mostly local rather than coherent, and, (3) spatial variation exceeds temporal variation. Our findings imply that predicting ecosystem responses to environmental changes at macroscales requires consideration of the dominant spatial signals at both local and regional scales that may overwhelm temporal signals."]}
df = pd.DataFrame(data = d)
test = lp.filter_limno(df)

print(list(test['filter_against']))



keywords = pd.read_csv(pkg_resources.resource_filename('limnopapers',
                                                       'keywords.csv'))
filter_for = keywords['filter_for'].tolist()
filter_for = [x for x in filter_for if str(x) != 'nan']
filter_against = keywords['filter_against'].tolist()



test = pd.read_csv(pkg_resources.resource_filename('limnopapers',
                                                   'keywords.csv'))
for item in test['filter_against'].tolist():
    print(type(item))

filter_for = test['filter_for'].tolist()
filter_for = [x for x in filter_for if str(x) != 'nan']
