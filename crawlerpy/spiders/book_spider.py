#                      .                    .                           
#                 :-:--=:-:::.             :=-**##*=:                   
#                  :=----------.         .-%@@@@@@@@@%:                 
#                 :-------------:        :@@@@@@@@@@@@%.                
#                :-=-----------==:       +@@@@@@@@@@@@@#                
#              .------------=------.     =@@@@@@@@@@@@@#                
#               :=-=-------===-=--      .+%@@@@@@@@@@@#=                
#                --=--------==-=-.       -*%@@@@@@@@@*-.                
#                   ::----===+-             .#%@@@@*.                   
#                      -+++=: .               :+##+                     
#                     -+=====.              .=%@@%%%#=                  
#                  :-----------:.        :+#%%%@@@@@%@%+-               
#                -----------------      -%%%%%@@@%@@%%@%%*              
#               .-==----------==--:     #%%%@%@@@@@@@@@@%%.             
#               :-=+----------*=---    =%%%@@%%@@@%%@@@%%%=             
#               ---=----------*----:  .#%%%@@%%@@@%@%@@%%%%             
#              :-===----------+=---=  -#%%%@@%%@%@%@%@@%%%%=            
#                --=----------=#==+.   ==+%@@%%@@@%@%@@*++.             
#                --=-----------*=---  :===#@@%%@@@%@%%%--=              
#                -==-----------++--=  ---:#@%@@@%%%@@@%--=              
#                -=------------=:--=. =-- %@%%%%%%@%%%@=-=              
#               .-+-------------.:---.--: %%%%%%%%@%%@@+==              
#               :-++*++++++*+***. --=+--  *###########**-=              
#               --*+++++++++*+++: :--*-: :------=------*-=              
#               =-*++++++++*+***- .--*-. :-------------+-=              
#              .--*+++=+*++*+***+ :==*=: -------=------===:             
#              :=+++++==+++*++**+ -*++=. -------+-------+=:             
#               -++++=+==**+++***  :-:   -------+-------+.              
#                -+++=++=****+**#        -------+=------=               
#                .++==*=---=*+**+        =------+*------=               
#                 ----=    :---=          ====-.::+====                 
#            :**#==---=:   ----= ..   .:::=--=+*%#*--=+***. .--:..      
#            .=+**#=--==   :=--=%@*:.-=+%%*--=: ::+=--+***+=#@%*-=-::.  
#                :+=--=. :::=--=:.-*#%*--=*---+-+**=--=--=+**+*=**%@%=  
#                  =--= .#%%=--=.  +*#%#= +---#%++#=---.+%@%+  .+++*+-  
#                  ====   .:+===:   -==+= :===*+: -==== .--:.      ..   
#                  =--=     ----:         .----   :=---                 
#                  ----     :---:         .=---   .=---                 
#                  ----     :---:         .=---    =---                 
#                  ---:     :---:         .=---    +---                 
#                  +##%.    =*##-         -%%#:    %%%#                 
#                 :@@@@-    #@@@+         %@@@*   :@@@%:                
#                 .====.    -++=:         =+==-    --==.                

# @milosnowcat

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# The `BookCrawling` class is a web crawler that extracts book titles, prices, and availability from a
# website.
class BookCrawling(CrawlSpider):
    name = "books"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )

    def parse_item(self, response):
        """
        The function parses information from a web page response and yields a dictionary with the title,
        price, and availability of an item.
        
        :param response: The `response` parameter is the HTTP response object returned by the web server
        after making a request. It contains the HTML content of the web page that we are scraping
        """
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("\n", "").strip()
        }
