import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Large‐scale landscape drivers of CO2, CH4, DOC and DIC in boreal river networks"], 'summary': ["The boreal biome is characterized by extremely dense and complex fluvial networks that are closely coupled to land. Reconstructing the role that these fluvial networks play in regional C budgets requires identifying landscape and environmental drivers of riverine C that operate at the whole network scale and that can be applied across landscapes. Here we explore drivers of CO2, CH4, and dissolved organic and inorganic C across 190 streams and rivers spanning 8 Strahler orders over an area of 500,000 km2 of heterogeneous boreal landscape in Québec, focusing on those drivers that can be readily obtained from remote sensing data. Each C species (except DIC) could be modeled as a function of a proximal network‐scale property, such as flow distance or elevation, but adding regional structure to these models greatly improved predictions. These modeled regional effects were similar for DOC, CO2 and CH4, and were strongly related to average regional soil organic content and especially to NPP, the latter integrating regional differences in climate and other environmental factors. These results suggest that there may be regional C baselines determined by a combination of landscape and climate features, which simultaneously influence the average CO2, DOC, and CH4 within fluvial networks, albeit through different underlying mechanisms and with varying degrees of influence on each C species. The latter two C species appear to be more sensitive to regional differences in soil, NPP, and climate than CO2 or DIC, and therefore more likely to shift under future scenarios of change in northern landscapes."]}
dt = pd.DataFrame(data = d)
test = lp.filter_limno(dt)
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
