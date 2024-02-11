import utility
import requests
import sys
import os
# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

def get_country_list():
    try:
        url='https://wise.com/rates/currencies'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        return response
    except Exception as e:
        return f"Network Error: {e}"    
def get_country_wise_price(listofcount):
    try:
        for i in listofcount:
            url='https://wise.com/rates/live?source=USD&target='+i
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
            }
            response = requests.get(url, headers=headers)
            print(response.json())
    except Exception as e:
        return f"Network Error: {e}"    

currency_data = {
    'AED': 'United Arab Emirates dirham',
    'AFN': 'Afghan afghani',
    'ALL': 'Albanian lek',
    'AMD': 'Armenian dram',
    'ANG': 'Netherlands Antillean guilder',
    'AOA': 'Angolan kwanza',
    'ARS': 'Argentine peso',
    'AUD': 'Australian dollar',
    'AWG': 'Aruban florin',
    'AZN': 'Azerbaijani manat',
    'BAM': 'Bosnia-Herzegovina Convertible mark',
    'BBD': 'Barbadian dollar',
    'BDT': 'Bangladeshi taka',
    'BGN': 'Bulgarian lev',
    'BHD': 'Bahraini dinar',
    'BIF': 'Burundian franc',
    'BMD': 'Bermudan dollar',
    'BND': 'Brunei dollar',
    'BOB': 'Bolivian boliviano',
    'BRL': 'Brazilian real',
    'BSD': 'Bahamian dollar',
    'BTN': 'Bhutanese ngultrum',
    'BWP': 'Botswanan pula',
    'BYN': 'Belarusian ruble',
    'BZD': 'Belize dollar',
    'CAD': 'Canadian dollar',
    'CDF': 'Congolese franc',
    'CHF': 'Swiss franc',
    'CLP': 'Chilean peso',
    'CNY': 'Chinese yuan',
    'COP': 'Colombian peso',
    'CRC': 'Costa Rican colón',
    'CUC': 'Cuban Convertible peso',
    'CUP': 'Cuban peso',
    'CVE': 'Cape Verdean escudo',
    'CZK': 'Czech Republic koruna',
    'DJF': 'Djiboutian franc',
    'DKK': 'Danish krone',
    'DOP': 'Dominican peso',
    'DZD': 'Algerian dinar',
    'EGP': 'Egyptian pound',
    'ERN': 'Eritrean nakfa',
    'ETB': 'Ethiopian birr',
    'EUR': 'Euro',
    'FJD': 'Fijian dollar',
    'FKP': 'Falkland Islands pound',
    'GBP': 'British pound sterling',
    'GEL': 'Georgian lari',
    'GGP': 'Guernsey pound',
    'GHS': 'Ghanaian cedi',
    'GIP': 'Gibraltar pound',
    'GMD': 'Gambian dalasi',
    'GNF': 'Guinean franc',
    'GTQ': 'Guatemalan quetzal',
    'GYD': 'Guyanaese dollar',
    'HKD': 'Hong Kong dollar',
    'HNL': 'Honduran lempira',
    'HRK': 'Croatian kuna',
    'HTG': 'Haitian gourde',
    'HUF': 'Hungarian forint',
    'IDR': 'Indonesian rupiah',
    'ILS': 'Israeli new sheqel',
    'IMP': 'Isle of Man pound',
    'INR': 'Indian rupee',
    'IQD': 'Iraqi dinar',
    'IRR': 'Iranian rial',
    'ISK': 'Icelandic króna',
    'JEP': 'Jersey pound',
    'JMD': 'Jamaican dollar',
    'JOD': 'Jordanian dinar',
    'JPY': 'Japanese yen',
    'KES': 'Kenyan shilling',
    'KGS': 'Kyrgystani som',
    'KHR': 'Cambodian riel',
    'KMF': 'Comorian franc',
    'KPW': 'North Korean won',
    'KRW': 'South Korean won',
    'KWD': 'Kuwaiti dinar',
    'KYD': 'Cayman Islands dollar',
    'KZT': 'Kazakhstani tenge',
    'LAK': 'Laotian kip',
    'LBP': 'Lebanese pound',
    'LKR': 'Sri Lankan rupee',
    'LRD': 'Liberian dollar',
    'LSL': 'Lesotho loti',
    'LYD': 'Libyan dinar',
    'MAD': 'Moroccan dirham',
    'MDL': 'Moldovan leu',
    'MGA': 'Malagasy ariary',
    'MKD': 'Macedonian denar',
    'MMK': 'Myanma kyat',
    'MNT': 'Mongolian tugrik',
    'MOP': 'Macanese pataca',
    'MRU': 'Mauritanian ouguiya',
    'MUR': 'Mauritian rupee',
    'MVR': 'Maldivian rufiyaa',
    'MWK': 'Malawian kwacha',
    'MXN': 'Mexican peso',
    'MYR': 'Malaysian ringgit',
    'MZN': 'Mozambican metical',
    'NAD': 'Namibian dollar',
    'NGN': 'Nigerian naira',
    'NIO': 'Nicaraguan córdoba',
    'NOK': 'Norwegian krone',
    'NPR': 'Nepalese rupee',
    'NZD': 'New Zealand dollar',
    'OMR': 'Omani rial',
    'PAB': 'Panamanian balboa',
    'PEN': 'Peruvian Nuevo sol',
    'PGK': 'Papua New Guinean kina',
    'PHP': 'Philippine peso',
    'PKR': 'Pakistani rupee',
    'PLN': 'Polish zloty',
    'PYG': 'Paraguayan guarani',
    'QAR': 'Qatari rial',
    'RON': 'Romanian leu',
    'RSD': 'Serbian dinar',
    'RUB': 'Russian ruble',
    'RWF': 'Rwandan franc',
    'SAR': 'Saudi riyal',
    'SBD': 'Solomon Islands dollar',
    'SCR': 'Seychellois rupee',
    'SDG': 'Sudanese pound',
    'SEK': 'Swedish krona',
    'SGD': 'Singapore dollar',
    'SHP': 'Saint Helena pound',
    'SLE': 'Sierra Leonean leone',
    'SLL': 'Sierra Leonean leone',
    'SOS': 'Somali shilling',
    'SRD': 'Surinamese dollar',
    'STN': 'São Tomé & Príncipe dobra',
    'SVC': 'Salvadoran colón',
    'SYP': 'Syrian pound',
    'SZL': 'Swazi lilangeni',
    'THB': 'Thai baht',
    'TJS': 'Tajikistani somoni',
    'TMT': 'Turkmenistani manat',
    'TND': 'Tunisian dinar',
    'TOP': 'Tongan paʻanga',
    'TTD': 'Trinidad and Tobago dollar',
    'TWD': 'New Taiwan dollar',
    'TZS': 'Tanzanian shilling',
    'UAH': 'Ukrainian hryvnia',
    'UGX': 'Ugandan shilling',
    'USD': 'US dollar',
    'UYU': 'Uruguayan peso',
    'UZS': 'Uzbekistan som',
    'VEF': 'Venezuelan bolívar(2008-2018)',
    'VES': 'Venezuelan bolívar',
    'VND': 'Vietnamese dong',
    'VUV': 'Vanuatu vatu',
    'WST': 'Samoan tala',
    'XAF': 'Central Africa CFA franc',
    'XCD': 'East Caribbean dollar',
    'XOF': 'West African CFA franc',
    'XPF': 'CFP franc',
    'YER': 'Yemeni rial',
    'ZAR': 'South African rand',
    'ZMW': 'Zambian kwacha',
    'ZWL': 'Zimbabwean Dollar (2009)'
}

if __name__ == "__main__":
    connection = utility.connect_to_database()
    # for currency_code, currency_name in currency_data.items():
    #     try:
    #         cursor = connection.cursor()
    #         # Use placeholders (?) in the SQL query and provide values as a tuple to cursor.execute()
    #         cursor.execute('''UPDATE countries 
    #                         SET country_lg_name = ? 
    #                         WHERE country_name = ?''', (currency_name, currency_code))
    #         connection.commit()
    #         cursor.close()  # Close cursor after each execution to release resources
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         print(f"Currency Code: {currency_code}, Currency Name: {currency_name}")
    # connection = utility.connect_to_database()
    # ##x=utility.create_countries_table()
    # result = get_country_list()
    # get_country_wise_price(result.json())
    # # if connection:
       
    # #     if result.status_code==200:
    # #         print(result.json())
    #         #c=utility.insert_countries(result.json())
    #         # folder = "flags"
    #         # currency_codes = ['AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'AWG', 'AZN', 'BAM', 'BBD', 'BIF', 'BMD', 'BOB', 'BSD', 'BTN', 'BYN', 'BZD', 'CDF', 'CUC', 'CUP', 'CVE', 'DJF', 'DZD', 'ERN', 'ETB', 'FKP', 'GGP', 'GIP', 'GMD', 'GNF', 'GYD', 'HTG', 'IQD', 'IRR', 'JEP', 'JOD', 'KGS', 'KHR', 'KMF', 'KPW', 'KYD', 'KZT', 'LBP', 'LRD', 'LYD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MVR', 'MWK', 'PGK', 'PYG', 'RSD', 'RWF', 'SBD', 'SCR', 'SDG', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STN', 'SYP', 'SZL', 'TJS', 'TND', 'TOP', 'TTD', 'UZS', 'VEF', 'VES', 'VUV', 'WST', 'XAF', 'XCD', 'XPF', 'YER', 'ZWL']
    #         # c=utility.download_country_flags(currency_codes, folder)
        # connection.close()
