import limnopapers as lp
import pandas as pd
import pkg_resources
# help(lp.filter_limno)

d = {'title': ["Environmental drivers of mixotrophs in boreal lakes"], 'summary': ["Uranium contamination of groundwater remains a pressing problem at many former uranium mining and milling operations, such as the Rifle, Integrated Field Research Challenge (IFRC) site. Biostimulation of the subsurface with an organic carbon source such as acetate, followed by the microbially-induced reductive precipitation of uranium has been proposed as an effective remediation strategy. While uranium bioreduction has been studied in several field experiments, the transformation and fate of injected carbon remains poorly understood. This study evaluated the impact of added organic carbon on the long-term biogeochemical attenuation of uranium in the subsurface of a former mill tailings site. Fluorescence and ultraviolet–visible absorbance analyses were used together with dissolved organic carbon (DOC) measurements to track organic carbon dynamics during and post-biostimulation of the 2011 Rifle IFRC experiment. An electron mass balance was performed on well CD01 to account for any unidentified carbon sinks. Measured DOC values increased to 1.76 mM-C during biostimulation, and to 3.18 mM-C post-biostimulation over background DOC values of 0.3–0.4 mM-C. Elevated DOC levels persisted for 90 days after acetate injections ceased. The electron mass balance revealed that assumed electron acceptors would not account for the total amount of acetate consumed. Excitation–emission matrices showed an increase in signals associated with soluble microbial products, during biostimulation, which disappeared post-biostimulation despite an increase in total DOC. Specific ultraviolet absorbance analyses, indicated that DOC present post-biostimulation is less aromatic in nature, compared to background DOC. Our results suggest that microbes convert injected acetate into a form of solid phase organic matter that may be available to sustain iron reduction post-stimulation."]}
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
