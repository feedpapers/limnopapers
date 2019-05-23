import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["The response of cyanobacteria and phytoplankton abundance to warming, extreme rainfall events and nutrient enrichment"], 'summary': ["Cyanobacterial blooms are an increasing threat to water quality and global water security caused by the nutrient enrichment of freshwaters. There is also a broad consensus that blooms are increasing with global warming, but the impacts of other concomitant environmental changes, such as an increase in extreme rainfall events, may affect this response. One of the potential effects of high rainfall events on phytoplankton communities is greater loss of biomass through hydraulic flushing. Here we used a shallow lake mesocosm experiment to test the combined effects of: warming (ambient vs +4°C increase), high rainfall (flushing) events (no events vs seasonal events) and nutrient loading (eutrophic vs hypertrophic) on total phytoplankton chlorophyll‐a and cyanobacterial abundance and composition. Our hypotheses were that: (1) total phytoplankton and cyanobacteria abundance would be higher in heated mesocosms; (2) the stimulatory effects of warming on cyanobacterial abundance would be enhanced in higher nutrient mesocosms, resulting in a synergistic interaction; (3) the recovery of biomass from flushing induced losses would be quicker in heated and nutrient enriched treatments, and during the growing season. The results supported the first and, in part, the third hypotheses: total phytoplankton and cyanobacterial abundance increased in heated mesocosms with an increase in common bloom‐forming taxa ‐ Microcystis spp. and Dolichospermum spp. Recovery from flushing was slowest in the winter, but unaffected by warming or higher nutrient loading. Contrary to hypothesis two, an antagonistic interaction between warming and nutrient enrichment was detected for both cyanobacteria and chlorophyll‐a demonstrating that ecological surprises can occur, dependent on the environmental context. While this study highlights the clear need to mitigate against global warming, over‐simplification of global change effects on cyanobacteria should be avoided; stressor gradients and seasonal effects should be considered as important factors shaping the response."]}
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
