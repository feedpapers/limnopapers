import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Distribution of Landscape Units Within Catchments Influences Nutrient Export Dynamics"], 'summary': ["Excess nutrients from agriculture have caused persistent eutrophication in aquatic ecosystems worldwide. Here, we present a conceptual framework for landscape management to achieve one or several water quality targets along the river continuum from headwaters to estuaries. Based on monitoring of representative headwaters and downstream reaches, we divide catchments into elementary landscape units defined by ecosystem properties and anthropogenic land use. We use a theoretical simulation to evaluate our hypothesis that the water-quality responses of redistributing these elementary units within the catchment will vary depending on the water quality targets (e.g., reduction in concentration or load). This landscape unit distribution (LUD) framework can efficiently assess the current ecohydrological functioning of a catchment and provide simple but robust predictions of its response to landscape management changes. Using simulated data, we show that different scenarios of landscape redistribution can allow attainment of one or several, but often not all desired water quality targets. Therefore, we recommend that water quality targets must be clearly defined and prioritized prior to designing landscape management strategies."]}
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
