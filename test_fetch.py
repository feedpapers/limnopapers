from limnopapers import *
from colorama import Fore

if(len(sys.argv) == 2):
    data = get_papers(day = sys.argv[1], limno = False, to_csv=True)
else:
    data = get_papers(day = str(datetime.date.today()), limno = False,
                      to_csv = True)

filtered = filter_limno(data)
data = data.append(filtered)
data = data.drop_duplicates(keep = False)

if(len(data.index) != 0):
    print(Fore.RED + "Excluded: ")
    print()
    toots = data['title'] + ". " + data['dc_source'] + ". " + data['prism_url']
    for toot in toots:
        print(Fore.RED + toot)
        print()

    print(Fore.GREEN + "Filtered: ")
    print()
    toots = filtered['title'] + ". " + filtered['dc_source'] + ". " + \
        filtered['prism_url']
    for toot in toots:
        print(Fore.GREEN + toot)
        print()
