import requests
import sys
import tabulate
import colorama


colorama.init(autoreset=True)

def format_price(value):
    try:
        return f"{value:,.2f}"
    except Exception:
        return "N/A"

def convert_usd_to_xau(usd_amount, xau_price_per_ounce):
    if xau_price_per_ounce <= 0:
        raise ValueError("Invalid XAU price")
    return usd_amount / xau_price_per_ounce

def build_table(rows, headers):
    return tabulate(rows, headers=headers, tablefmt="github")

def main() :
    print(f"{colorama.Fore.RED}According to what you want to track Choose the number : {colorama.Style.RESET_ALL} ")
    print(f"1 {colorama.Fore.YELLOW} Crypto Cryptocurrencies {colorama.Style.RESET_ALL} ")
    print(f"2 {colorama.Fore.YELLOW} Forex {colorama.Style.RESET_ALL} ")
    print(f"3 {colorama.Fore.YELLOW} Metals {colorama.Style.RESET_ALL}")
    Exite1 = print(f"4 {colorama.Fore.YELLOW} Exit {colorama.Style.RESET_ALL} ")
    number1 = input(f"{colorama.Fore.RED} Enter a number: {colorama.Style.RESET_ALL}")
    
    if number1 not in ["1" , "2" , "3" , "4"] :
        sys.exit(F"{colorama.Fore.RED} Please enter One of the represented nembers only {colorama.Style.RESET_ALL} ")

    elif number1 == "1" :
        print(f"1 {colorama.Fore.YELLOW} Bitcoin (Btc/Usd) {colorama.Style.RESET_ALL} ")

        print(f"2 {colorama.Fore.YELLOW} Ethereum (Eth/Usd) {colorama.Style.RESET_ALL} ")

        print(f"3 {colorama.Fore.YELLOW} Sol (Sol/Usd) {colorama.Style.RESET_ALL} ")

        print(f"4 {colorama.Fore.YELLOW} Top 5 By MarketCap {colorama.Style.RESET_ALL} ")

        print(f"5 {colorama.Fore.YELLOW} Top 10 By MarketCap {colorama.Style.RESET_ALL} ")

        print(f"6 {colorama.Fore.YELLOW} Top 25 By MarketCap {colorama.Style.RESET_ALL} ")

        Exite2 = print(f"7 {colorama.Fore.YELLOW} Exit {colorama.Style.RESET_ALL} ")

        number2 = input(f"{colorama.Fore.RED} Enter a number: {colorama.Style.RESET_ALL}")

        if number2 not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" ] :
            sys.exit(F"{colorama.Fore.RED} Please enter One of the represented nembers only {colorama.Style.RESET_ALL} ")

        elif int(number2) == 1 :
            print(cryptoprice(1))

        elif int(number2) == 2 :
            print(cryptoprice(2))

        elif int(number2) == 3 :
            print(cryptoprice(3))

        elif int(number2) == 4 :
            print(cryptoprice(4))
        
        elif int(number2) == 5 :
            print(cryptoprice(5))

        elif int(number2) == 6 :
            print(cryptoprice(6))
        
        elif int(number2) == 7 :
            print(cryptoprice(7))
    elif number1 == "2" :
        print(f"1 {colorama.Fore.YELLOW} US Dollar vs Euro (USDEUR) {colorama.Style.RESET_ALL} ")
        print(f"2 {colorama.Fore.YELLOW} US Dollar vs Pound Sterling (USDGBP) {colorama.Style.RESET_ALL} ")
        print(f"3 {colorama.Fore.YELLOW} US Dollar vs Candian Dollar  (USDCAD) {colorama.Style.RESET_ALL} ")
        print(f"4 {colorama.Fore.YELLOW} Exit {colorama.Style.RESET_ALL} ")
        number2 = input(f"{colorama.Fore.RED} Enter a number: {colorama.Style.RESET_ALL}")
        if number2 not in ["1" , "2" , "3" , "4"] :
            sys.exit(F"{colorama.Fore.RED} Please enter One of the represented nembers only {colorama.Style.RESET_ALL} ")
        elif int(number2) == 1 :
            print(forex(1))
        elif int(number2) == 2 :
            print(forex(2))
        elif int(number2) == 3 :
            print(forex(3))
    elif number1 == "3" :
        print(f"1 {colorama.Fore.YELLOW} Gold vs US Dollar (XAUUSD) {colorama.Style.RESET_ALL} ")
        print(f"2 {colorama.Fore.YELLOW} Silver vs US Dollar (XAGUSD) {colorama.Style.RESET_ALL} ")
        print(f"3 {colorama.Fore.YELLOW} Exit {colorama.Style.RESET_ALL} ")
        number2 = input(f"{colorama.Fore.RED} Enter a number: {colorama.Style.RESET_ALL}")
        if int(number2) == 1 :
            print(metals(1))
        elif int(number2) == 2 :
            print(metals(2))
        elif int(number2) == 3 :
            print(metals(3))
    elif int(number1) == 4 :
        sys.exit()

            
def cryptoprice(n) :
    url = "https://api.coingecko.com/api/v3/simple/price"
    url_top = "https://api.coingecko.com/api/v3/coins/markets"
    
    if n == 1 :
        params_btc = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_market_cap": "true"}
        response = requests.get(url, params=params_btc)
        data_btc = response.json()
        btc_price = data_btc["bitcoin"]["usd"]
        btc_market_cap = data_btc["bitcoin"]["usd_market_cap"]
        print(f"{colorama.Fore.YELLOW}Bitcoin Price : {btc_price}$ , Bitcoin Marketcap: {btc_market_cap}$ {colorama.Style.RESET_ALL} ")
        sys.exit()

    if n == 2 :
        params_eth = {
        "ids": "ethereum",
        "vs_currencies": "usd",
        "include_market_cap": "true"}
        response = requests.get(url, params=params_eth)
        data_eth = response.json()
        eth_price = data_eth["ethereum"]["usd"]
        eth_market_cap = data_eth["ethereum"]["usd_market_cap"]
        print(f"{colorama.Fore.YELLOW}Price : {eth_price}$ , Marketcap: {eth_market_cap}$ {colorama.Style.RESET_ALL} ")
        sys.exit()

    if n == 3 :
        params_sol = {
        "ids": "solana",
        "vs_currencies": "usd",
        "include_market_cap": "true"}
        response = requests.get(url, params=params_sol)
        data = response.json()
        sol_price = data["solana"]["usd"]
        sol_market_cap = data["solana"]["usd_market_cap"]
        print(f"{colorama.Fore.YELLOW}Price : {sol_price}$ , Marketcap: {sol_market_cap}${colorama.Style.RESET_ALL}")
        sys.exit()
    if n == 4 : 
        params_top5 = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 5,
        "page": 1,
        "sparkline": "false"}

        response = requests.get(url_top, params=params_top5)
        headers_top = ["Ranks" , "Name" , "Symbol" , "Price" , "MarketCap"]
        yellow = "\033[93m"
        reset = "\033[0m"
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
    
        else:
            top_5 = []
            data = response.json()
            print(type(data))   
            print(len(data))    
            for coin in data:
                top_5.append([coin["market_cap_rank"] ,
                        coin["name"],
                        coin["symbol"].upper(),
                        f"${coin['current_price']:,}",
                        f"${coin['market_cap']:,}"])

            print(yellow + tabulate.tabulate(top_5 ,  headers= headers_top , tablefmt="fancy_grid") + reset)
        sys.exit()
    if n == 5 :
        params_top10 = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"}

        response = requests.get(url_top, params=params_top10)
        headers_top = ["Ranks" , "Name" , "Symbol" , "Price" , "MarketCap"]
        yellow = "\033[93m"
        reset = "\033[0m"
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
    
        else:
            top_10 = []
            data = response.json()
            print(type(data))   
            print(len(data))    
            for coin in data:
                top_10.append([coin["market_cap_rank"] ,
                        coin["name"],
                        coin["symbol"].upper(),
                        f"${coin['current_price']:,}",
                        f"${coin['market_cap']:,}"
                        ])

        print(yellow + tabulate.tabulate(top_10 ,  headers= headers_top , tablefmt="fancy_grid") + reset)
        sys.exit()

    if  n == 6 :
        params_top25 = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 25,
        "page": 1,
        "sparkline": "false"}

        response = requests.get(url_top, params=params_top25)
        headers_top = ["Ranks" , "Name" , "Symbol" , "Price" , "MarketCap"]
        yellow = "\033[93m"
        reset = "\033[0m"
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
    
        else:
            top_25 = []
            data = response.json()
            print(type(data))   
            print(len(data))    
            for coin in data:
                top_25.append([coin["market_cap_rank"] ,
                       coin["name"],
                       coin["symbol"].upper(),
                       f"${coin['current_price']:,}",
                    f"${coin['market_cap']:,}"
                       ])

        print(yellow + tabulate.tabulate(top_25 ,  headers= headers_top , tablefmt="fancy_grid") + reset)
    sys.exit()
    if n == 7 :
        sys.exit()


def forex(n) :
    url = "https://api.fastforex.io/convert"
    if n == 1 :
        param_eur = {
    "from" : "USD" , 
    "to" : "EUR" ,
    "amount" : 1 ,
    "api_key" : "48cd0dbaae-e6378e6d6c-t3atnl"}
        response = requests.get(url , params= param_eur)
        data = response.json()
        eur = data["result"]["EUR"]
        print(f"{colorama.Fore.YELLOW}1 $ (US Dollar) = {eur}€ (Euro) {colorama.Style.RESET_ALL} ")
        sys.exit()
    elif n == 2 :
                param_gbp = {
            "from" : "USD" , 
            "to" : "GBP" ,
            "amount" : 1 ,
            "api_key" : "48cd0dbaae-e6378e6d6c-t3atnl" }
                response = requests.get(url , params= param_gbp)
                data = response.json()
                gbp = data["result"]["GBP"]
                print(f"{colorama.Fore.YELLOW}1 $ (US Dollar) = {gbp}£ (Pound Sterling) {colorama.Style.RESET_ALL} ")
                sys.exit()
    elif n == 3 :
            param_cad = {
        "from" : "USD" , 
        "to" : "CAD" ,
        "amount" : 1 ,
        "api_key" : "48cd0dbaae-e6378e6d6c-t3atnl"}
            response = requests.get(url , params= param_cad)
            data = response.json()
            cad = data["result"]["CAD"]
            print(f"{colorama.Fore.YELLOW}1 $ (US Dollar) = {cad}CA$ (Candian Dollar) {colorama.Style.RESET_ALL} ")
            sys.exit()
    elif n == 4 :
        sys.exit()


def metals(n):
    url_gold = "https://www.goldapi.io/api/XAU/USD"
    url_silver = "https://www.goldapi.io/api/XAG/USD"
    if n == 1 :
        headers_gold = {
    "x-access-token":"goldapi-rtxq4smg41d03w-io",
    "Content-Type":"application/json"}
        response = requests.get(url_gold , headers= headers_gold)
        data = response.json()
        gold = data["price"]
        print(f"{colorama.Fore.YELLOW}1 Ounce = {gold}$ (US Dollar)  {colorama.Style.RESET_ALL} ")
        sys.exit()
    elif n == 2 :
        headers_silver = {
    "x-access-token":"goldapi-rtxq4smg41d03w-io",
    "Content-Type":"application/json"}
        response = requests.get(url_silver , headers= headers_silver)
        data = response.json()
        silver = data["price"]
        print(f"{colorama.Fore.YELLOW}1 Ounce = {silver}$ (US Dollar)  {colorama.Style.RESET_ALL} ")
        sys.exit()
    elif n == 3 :
        sys.exit()




if __name__ == "__main__" :
    main()