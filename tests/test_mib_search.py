import requests

def main():
    MIB_SEARCH_URL = "http://localhost:5000/search/mib"
    # oid = "1, 3, 6, 1, 4, 1, 2356, 11, 0, 0, 10000"
    oid = "1, 3, 8, 1, 4, 1, 890, 1, 15, 3, 91, 1, 1"

    params = {"oid": oid}

    response = requests.request("GET", MIB_SEARCH_URL, params=params)

    print(response.status_code)
    if response.status_code != 200:
        print("Can Not find the oid")
    else:
        print (response.text)

if __name__ == '__main__':
    main()