import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Estimation of water quality profiles in deep lakes based on easily measurable constituents at the water surface using artificial neural networks coupled with stationary wavelet transform"], 'summary': ["This study proposes a novel framework to accurately estimate water quality profiles in deep lakes based on parameters measured at the water surface, considering Boulder Basin of Lake Mead as a case study. Hourly-measured meteorological data were used to compute heat exchange between lake and atmosphere. Heat fluxes combined with every 6-hour measured water temperature, conductivity, and dissolved oxygen (DO) profiles, from the water surface to a depth of 100 m over a 48-month period, were used to train seven different artificial neural network-based methods for estimating water quality profiles. Effects of different factors influencing lake water quality, including lake-atmosphere interactions, wind-induced mixing, thermocline depth, winter turnover, oxygen depletion and other factors were investigated in different methods. A method employing stationary wavelet transform with a depth-progressive estimation of temperature, conductivity, and DO generated the smallest average relative errors of 0.52%, 0.22%, and 0.62%, respectively in the water column over a 48-month period. Abrupt changes in temperature, conductivity, and DO profiles due to thermal stratification, winter turnover, and oxygen hypoxia increased estimation errors. The largest errors occurred near the interface between the epilimnion and metalimnion, where vertical mixing intensity significantly decreased."]}
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
