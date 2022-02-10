i, j = input().split()
sites = []
findSites = []

for k in range(int(i)):
    sites.append(input().split())

print(sites)
for l in range(int(j)):
    site = input()
    if site in sites:
        print("d")
    # print(sites.index(site))

# print(sites)