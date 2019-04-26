import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Shining light on the storm: in-stream optics reveal hysteresis of dissolved organic matter character"], 'summary': ["The quantity and character of dissolved organic matter (DOM) can change rapidly during storm events, affecting key biogeochemical processes, carbon bioavailability, metal pollutant transport, and disinfection byproduct formation during drinking water treatment. We used in situ ultraviolet–visible spectrophotometers to concurrently measure dissolved organic carbon (DOC) concentration and spectral slope ratio, a proxy for DOM molecular weight. Measurements were made at 15-minute intervals over three years in three streams draining primarily agricultural, urban, and forested watersheds. We describe storm event dynamics by calculating hysteresis indices for DOC concentration and spectral slope ratio for 220 storms and present a novel analytical framework that can be used to interpret these metrics together. DOC concentration and spectral slope ratio differed significantly among sites, and individual storm DOM dynamics were remarkably variable at each site and among the three sites. Distinct patterns emerged for storm DOM dynamics depending on land use/land cover (LULC) of each watershed. In agricultural and forested streams, DOC concentration increased after the time of peak discharge, and spectral slope ratio dynamics indicate that this delayed flux was of relatively higher molecular weight material compared to the beginning of each storm. In contrast, DOM character during storms at the urban stream generally shifted to lower molecular weight while DOC concentration increased on the falling limb, indicating either the introduction of lower molecular weight DOM, the exhaustion of a higher molecular weight DOM sources, or a combination of these factors. We show that the combination of high-frequency DOM character and quantity metrics have the potential to provide new insight into short-timescale DOM dynamics and can reveal previously unknown effects of LULC on the chemical nature, source, and timing of DOM export during storms."]}
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
