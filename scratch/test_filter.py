import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Hillslope Hydrology in Global Change Research and Earth System Modeling"], 'summary': ["Earth System Models (ESMs) are essential tools for understanding and predicting global change, but they cannot explicitly resolve hillslope‐scale terrain structures that fundamentally organize water, energy, and biogeochemical stores and fluxes at subgrid scales. Here we bring together hydrologists, Critical Zone scientists, and ESM developers, to explore how hillslope structures may modulate ESM grid‐level water, energy, and biogeochemical fluxes. In contrast to the one‐dimensional (1‐D), 2‐ to 3‐m deep, and free‐draining soil hydrology in most ESM land models, we hypothesize that 3‐D, lateral ridge‐to‐valley flow through shallow and deep paths and insolation contrasts between sunny and shady slopes are the top two globally quantifiable organizers of water and energy (and vegetation) within an ESM grid cell. We hypothesize that these two processes are likely to impact ESM predictions where (and when) water and/or energy are limiting. We further hypothesize that, if implemented in ESM land models, these processes will increase simulated continental water storage and residence time, buffering terrestrial ecosystems against seasonal and interannual droughts. We explore efficient ways to capture these mechanisms in ESMs and identify critical knowledge gaps preventing us from scaling up hillslope to global processes. One such gap is our extremely limited knowledge of the subsurface, where water is stored (supporting vegetation) and released to stream baseflow (supporting aquatic ecosystems). We conclude with a set of organizing hypotheses and a call for global syntheses activities and model experiments to assess the impact of hillslope hydrology on global change predictions."]}
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
