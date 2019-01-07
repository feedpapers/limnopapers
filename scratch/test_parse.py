toot = "Modeling benthic vs. hyporheic nutrient uptake in unshaded streams with varying substrates. Journal of Geophysical Research: Biogeosciences. https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/2018JG004684?af=R"


def toot_split(toot):
    res = toot.split(". ")
    prism_url = res[len(res) - 1]
    dc_source = res[len(res) - 2]
    title = '. '.join(res[0:len(res) - 2])
    return([title, dc_source, prism_url])

title, dc_source, prism_url = toot_split(toot)
