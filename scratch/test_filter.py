import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Zooplankton functional-approach studies in continental aquatic environments: a systematic review"], 'summary': ["Functional-approach studies are currently increasing in ecology. However, for zooplankton communities, studies are mostly concentrated in marine environments. This study provides a systematic review to reveal the trends and gaps in scientific literature regarding zooplankton functional-approach in continental aquatic environments, including its main groups (testate amoebas, cladocerans, copepods, and rotifers). We focused on determining which functional traits were evaluated for these groups and whether they were based on direct measurements or on literature. We found that despite the recent increase in publications, most studies were limited to Canada, USA, Brazil, and Italy. Publications have been increasing over the last 3 years, representing an advance toward the understanding of the dynamics of these organisms in relation to environmental variations. Most studies used size-related functional traits. Nonetheless, other studies that deal with dietary and feeding strategies have improved the understanding of the dynamics of these organisms. Therefore, we highlight that the use of functional approach is an important tool to understand ecosystem processes and thus to contribute to the knowledge of biodiversity conservation and ecosystem dynamics."]}
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
