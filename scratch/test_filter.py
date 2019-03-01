import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Regulation of the functional structure of aquatic communities across spatial scales in a major river network"], 'summary': ["Moving beyond species count data is an essential step to better understand the effects of environmental perturbations on biodiversity and ecosystem functions, and to eventually better predict the strength and direction of those effects. Here, coupling an integrative path analysis approach with data from an extensive countrywide monitoring program, we tested the main spatial, environmental and anthropogenic drivers of change in the functional structure of aquatic macroinvertebrate communities along the entire Swiss Rhine river catchment. Functional structure was largely driven by inherent altitudinal variation influencing and cascading to regional scaled factors such as land use change and position in the riverine network, which, in turn, transformed local habitat structure variables. Those cascading effects across scales propagated through the biotic community, first affecting prey and, in turn, predators. Our results illustrate how seemingly less important local factors can act as essential transmission belts, propagating through direct and indirect pathways across scales to generate the specific context in which each functional group will strive or not, leading to characteristic landscape wide variations in functional community structure."]}
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
