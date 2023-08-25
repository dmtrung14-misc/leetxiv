import random

fortune_500=["3M","A-Mark Precious Metals","A.O. Smith","AAR","ABM Industries","ADT","AECOM","AES","AGCO","AMC Networks","AMN Healthcare Services","APA","APi Group","ARKO","ASGN","AT&T","ATI","AbbVie","Abbott Laboratories","Abercrombie & Fitch","Academy Sports and Outdoors","Acadia Healthcare","Activision Blizzard","Acuity Brands","Adobe","Advance Auto Parts","Advanced Micro Devices","Advantage Solutions","Aerojet Rocketdyne Holdings","Affiliated Managers Group","Aflac","Agilent Technologies","Air Lease","Air Products & Chemicals","Airbnb","Akamai Technologies","Alaska Air Group","Albemarle","Albertsons","Alcoa","Alexandria Real Estate Equities","Alexion Pharmaceuticals","Align Technology","Alleghany","Alliant Energy","Allison Transmission Holdings","Allstate","Ally Financial","Alphabet","Altice USA","Altria Group","Amazon","Amedisys","Ameren","American Airlines Group","American Axle & Manufacturing","American Eagle Outfitters","American Electric Power","American Equity Investment Life Holding","American Express","American Family Insurance Group","American Financial Group","American International Group","American National Group","American Tower","American Water Works","Americold Realty Trust","Ameriprise Financial","AmerisourceBergen","Ametek","Amgen","Amica Mutual Insurance","Amkor Technology","Amneal Pharmaceuticals","Amphenol","Analog Devices","Andersons","Antero Resources","Anywhere Real Estate","Apollo Global Management","Apple","Applied Industrial Technologies","Applied Materials","AptarGroup","Aramark","ArcBest","Archer Daniels Midland","Arconic","Arcosa","Arista Networks","Arrow Electronics","Arthur J. Gallagher","Asbury Automotive Group","Ashland","Assurant","Atlas Air Worldwide Holdings","Atmos Energy","Auto-Owners Insurance","AutoNation","AutoZone","Autodesk","Autoliv","Automatic Data Processing","AvalonBay Communities","Avantor","Avaya Holdings","Avery Dennison","Avient","Avis Budget Group","Avnet","B&G Foods","BGC Group","BJ's Wholesale Club","BOK Financial","BWX Technologies","Baker Hughes","Ball","Bank of America","Bank of New York Mellon","Bath & Body Works","Baxter International","Beacon Roofing Supply","Beazer Homes USA","Becton Dickinson","Bed Bath & Beyond","Belden","Benchmark Electronics","Berkshire Hathaway","Berry Global Group","Best Buy","Big Lots","Bio-Rad Laboratories","BioMarin Pharmaceutical","Biogen","BlackRock","Blackstone","Block","Bloomin' Brands","BlueLinx Holdings","Boeing","Boise Cascade","Booking Holdings","Booz Allen Hamilton Holding","BorgWarner","Boston Properties","Boston Scientific","Boyd Gaming","Bread Financial Holdings","BrightView Holdings","Brighthouse Financial","Brink's","Brinker International","Bristol-Myers Squibb","Broadcom","Broadridge Financial Solutions","Brookdale Senior Living","Brown & Brown","Brown-Forman","Bruker","Brunswick","Builders FirstSource","Burlington Stores","C.H. Robinson Worldwide","CACI International","CBRE Group","CDK Global","CDW","CF Industries Holdings","CHS","CIT Group","CME Group","CMS Energy","CNO Financial Group","CSX","CUNA Mutual Group","CVS Health","Cabot","Cadence Design Systems","Caesars Entertainment","Caleres","Calumet Specialty Products Partners","Campbell Soup","Camping World Holdings","Capital One Financial","CarMax","Cardinal Health","Carlisle","Carlyle Group","Carpenter Technology","Carrier Global","Carter's","Carvana","Casey&#8217;s General Stores","Catalent","Caterpillar","Cboe Global Markets","Celanese","Centene","CenterPoint Energy","Central Garden & Pet","Century Communities","Cerner","ChampionX","Charles River Laboratories International","Charles Schwab","Charter Communications","Cheesecake Factory","Chemed","Chemours","Cheniere Energy","Chesapeake Energy","Chevron","Chewy","Chipotle Mexican Grill","Church & Dwight","Ciena","Cigna","Cincinnati Financial","Cintas","Cisco Systems","Citigroup","Citizens Financial Group","Citrix Systems","Clean Harbors","Clear Channel Outdoor Holdings","Clearwater Paper","Cleveland-Cliffs","Clorox","Coca-Cola","Coca-Cola Consolidated","Cognizant Technology Solutions","Coherent","Colgate-Palmolive","Columbia Sportswear","Comcast","Comerica","Comfort Systems USA","CommScope Holding","Commercial Metals","Community Health Systems","Compass","Conagra Brands","Conduent","ConocoPhillips","Consolidated Edison","Constellation Brands","ContextLogic","Continental Resources","Cooper Cos.","Cooper Tire & Rubber","Cooper-Standard Holdings","Copart","Core-Mark Holding","CoreCivic","CoreLogic","Cornerstone Building Brands","Corning","Corteva","Costco Wholesale","Coty","Country Financial","Covanta Holding","Covetrus","Cracker Barrel Old Country Store","Crane NXT","Crestwood Equity Partners","Crown Castle","Crown Holdings","Cummins","Curtiss-Wright","D.R. Horton","DCP Midstream","DISH Network","DTE Energy","DXC Technology","DaVita","Dana","Danaher","Darden Restaurants","Darling Ingredients","Deckers Outdoor","Deere","Delek US Holdings","Dell Technologies","Delta Air Lines","Dentsply Sirona","Designer Brands","Devon Energy","DexCom","Diamondback Energy","Dick's Sporting Goods","Diebold Nixdorf","Digital Realty Trust","Dillard's","Discover Financial Services","Dollar General","Dollar Tree","Dominion Energy","Domino's Pizza","Domtar","Donaldson","DoorDash","Dover","Dow","Dropbox","DuPont","Duke Energy","Dycom Industries","E.W. Scripps","EMCOR Group","EOG Resources","EPAM Systems","EQT","Eastman Chemical","Echo Global Logistics","EchoStar","Ecolab","Edgewell Personal Care","Edison International","Edwards Lifesciences","Elanco Animal Health","Electronic Arts","Elevance Health","Eli Lilly","Emerson Electric","EnLink Midstream","Enable Midstream Partners","Encompass Health","Endeavor Group Holdings","EnerSys","Energizer Holdings","Energy Transfer","Enovis","Ensign Group","Entegris","Entergy","Enterprise Products Partners","Enviri","Envista Holdings","Equifax","Equinix","Equitable Holdings","Equity Residential","Erie Insurance Group","Estee Lauder","Euronet Worldwide","Evercore","Evergy","Eversource Energy","Exelon","Expedia Group","Expeditors Intl. of Washington","Exxon Mobil","F5","FM Global","FMC","FTI Consulting","Fannie Mae","Farmers Insurance Exchange","Fastenal","FedEx","Federated Mutual Insurance","Fidelity National Financial","Fidelity National Information Services","Fifth Third Bancorp","First American Financial","First Citizens BancShares","First Horizon","First Republic Bank","First Solar","FirstEnergy","Fiserv","Five Below","Flagstar Bancorp","Fleetcor Technologies","Floor & Decor Holdings","Flowers Foods","Flowserve","Fluor","Foot Locker","Ford Motor","Fortinet","Fortive","Fortune Brands Innovations","Fox","Franchise Group","Franklin Resources","Freddie Mac","Freeport-McMoRan","Frontier Communications","G-III Apparel Group","GEO Group","GMS","GameStop","Gannett","Gap","Garrett Motion","Gartner","Gen Digital","Generac Holdings","General Dynamics","General Electric","General Mills","General Motors","Genesis HealthCare","Genuine Parts","Genworth Financial","Gilead Sciences","Global Partners","Global Payments","Globe Life","GoDaddy","Goldman Sachs Group","Goodyear Tire & Rubber","Graham Holdings","Granite Construction","Graphic Packaging Holding","Gray Television","Graybar Electric","Green Plains","Greenbrier","Greif","Griffon","Grocery Outlet Holding","Group 1 Automotive","Guardian Life Ins. Co. of America","Guess","H&R Block","H.B. Fuller","HCA Healthcare","HF Sinclair","HNI","HP","Hain Celestial Group","Halliburton","Hanesbrands","Hanover Insurance Group","Harley-Davidson","Hartford Financial Services Group","Hasbro","Hawaiian Electric Industries","Healthpeak Properties","Henry Schein","Hershey","Hertz Global Holdings","Hess","Hewlett Packard Enterprise","Hexion","Hill-Rom Holdings","Hillenbrand","Hilltop Holdings","Hilton Worldwide Holdings","Hologic","Home Depot","Honeywell International","Hormel Foods","Hovnanian Enterprises","Howmet Aerospace","Hub Group","Hubbell","Humana","Huntington Bancshares","Huntington Ingalls Industries","Huntsman","Hyatt Hotels","Hyster-Yale Materials Handling","IAC","IBM","IDEX","IDEXX Laboratories","IQVIA Holdings","ITT","Icahn Enterprises","Illinois Tool Works","Illumina","Incyte","Ingersoll Rand","Ingles Markets","Ingredion","Insight Enterprises","Insperity","Intel","Interactive Brokers Group","Intercontinental Exchange","International Flavors & Fragrances","International Paper","Interpublic Group","Intuit","Intuitive Surgical","Iron Mountain","Itron","J.B. Hunt Transport Services","J.M. Smucker","JELD-WEN Holding","JPMorgan Chase","Jabil","Jacobs Solutions","Jefferies Financial Group","JetBlue Airways","Joann","Johnson & Johnson","Jones Financial (Edward Jones)","Jones Lang LaSalle","Juniper Networks","KB Home","KBR","KKR","KLA","Kansas City Southern","Kar Auction Services","Kellogg","Kelly Services","Kemper","Kennametal","Keurig Dr Pepper","KeyCorp","Keysight Technologies","Kimberly-Clark","Kinder Morgan","Kirby","Knight-Swift Transportation Holdings","Knights of Columbus","Kohl&#8217;s","Korn Ferry","Kraft Heinz","Kroger","L3Harris Technologies","LCI Industries","LGI Homes","LHC Group","LKQ","LPL Financial Holdings","Laboratory Corp. of America","Lam Research","Lamb Weston Holdings","Land O&#8217;Lakes","Landstar System","Las Vegas Sands","Laureate Education","Lear","Leggett & Platt","Leidos Holdings","Lennar","Lennox International","Levi Strauss","Liberty Media","Liberty Mutual Insurance Group","Light & Wonder","Lincoln Electric Holdings","Lincoln National","Lithia Motors","Live Nation Entertainment","Lockheed Martin","Loews","Louisiana-Pacific","Lowe's","Lululemon athletica","Lumen Technologies","Lyft","M&T Bank","M\/I Homes","MDC Holdings","MDU Resources Group","MGM Resorts International","MKS Instruments","MRC Global","MSC Industrial Direct","MYR Group","Macy's","Magellan Health","Magellan Midstream Partners","Mahwah Bergen Retail Group","ManTech International","ManpowerGroup","Marathon Oil","Marathon Petroleum","Markel","Marriott International","Marriott Vacations Worldwide","Marsh & McLennan","Martin Marietta Materials","MasTec","Masco","Massachusetts Mutual Life Insurance","Mastercard","Match Group","Matson","Mattel","Maxim Integrated Products","Maximus","McAfee","McCormick","McDonald's","McKesson","Medical Mutual of Ohio","Mednax","Merck","Mercury General","Meredith","Meritage Homes","Meritor","MetLife","Meta Platforms","Mettler-Toledo International","Michaels","Microchip Technology","Micron Technology","Microsoft","Middleby","MillerKnoll","Modine Manufacturing","Mohawk Industries","Molina Healthcare","Molson Coors Beverage","Mondelez International","Monster Beverage","Moody's","Moog","Morgan Stanley","Mosaic","Motorola Solutions","Mr. Cooper Group","Mueller Industries","Murphy Oil","Murphy USA","Mutual of Omaha Insurance","NCR","NGL Energy Partners","NLV Financial","NOV","NRG Energy","NVR","Nasdaq","Nationwide","Navient","Navistar International","NetApp","Netflix","New Jersey Resources","New York Life Insurance","NewMarket","Newell Brands","Newmark Group","Newmont","News Corp.","Nexstar Media Group","NextEra Energy","NiSource","Nike","Nordson","Nordstrom","Norfolk Southern","Northern Trust","Northrop Grumman","Northwestern Mutual","Nu Skin Enterprises","Nucor","Nvidia","O'Reilly Automotive","O-I Glass","ODP","OGE Energy","ON Semiconductor","Occidental Petroleum","Ohio National Mutual","Old Dominion Freight Line","Old Republic International","Olin","Omnicom Group","OneMain Holdings","Oneok","Opendoor Technologies","Option Care Health","Oracle","Oshkosh","Otis Worldwide","Overstock.com","Ovintiv","Owens & Minor","Owens Corning","PAE","PBF Energy","PC Connection","PENN Entertainment","PG&E","PNC Financial Services Group","PPD","PPG Industries","PPL","PRA Health Sciences","PROG Holdings","PVH","Paccar","Pacific Life","Packaging Corp. of America","Palo Alto Networks","Par Pacific Holdings","Paramount Global","Parker-Hannifin","Parsons","Patrick Industries","Patterson","PayPal Holdings","Paychex","Peabody Energy","Penn Mutual Life Insurance","PennyMac Financial Services","Penske Automotive Group","People's United Financial","PepsiCo","Performance Food Group","Perspecta","Petco Health and Wellness","Peter Kiewit Sons'","Pfizer","Philip Morris International","Phillips 66","Pinnacle West Capital","Pioneer Natural Resources","Pitney Bowes","Plains GP Holdings","Playtika Holding","Plexus","Polaris","Pool","Popular","Portland General Electric","Post Holdings","PriceSmart","Primerica","Primoris Services","Principal Financial","Procter & Gamble","Progressive","Prologis","Prudential Financial","Public Service Enterprise Group","Public Storage","Publix Super Markets","Puget Energy","PulteGroup","Qorvo","Quad\/Graphics","Qualcomm","Quanta Services","Quest Diagnostics","Qurate Retail","R.R. Donnelley & Sons","REV Group","RH","RPM International","RTX","Rackspace Technology","Ralph Lauren","Range Resources","Raymond James Financial","Regal Rexnord","Regeneron Pharmaceuticals","Regions Financial","Reinsurance Group of America","Reliance Steel & Aluminum","Renewable Energy Group","Republic Services","ResMed","Resideo Technologies","Resolute Forest Products","Revlon","Revvity","Rite Aid","Robert Half","Rocket Companies","Rockwell Automation","Rollins","Roper Technologies","Ross Stores","Rush Enterprises","Ryder System","Ryerson Holding","S&P Global","SBA Communications","SLM","SS&C Technologies Holdings","SVB Financial Group","Salesforce","Sally Beauty Holdings","Sanderson Farms","Sanmina","ScanSource","Schneider National","Science Applications International","Scotts Miracle-Gro","Seaboard","Seagen","Sealed Air","Securian Financial Group","Select Medical Holdings","Selective Insurance Group","Sempra","Sentry Insurance Group","Service Corp. International","ServiceNow","Sherwin-Williams","Silgan Holdings","Simon Property Group","Sinclair","SiteOne Landscape Supply","Skechers U.S.A.","SkyWest","Skyworks Solutions","Sleep Number","Snap","Snap-on","Sonic Automotive","Sonoco Products","Southern","Southwest Airlines","Southwest Gas Holdings","Southwestern Energy","SpartanNash","Spectrum Brands Holdings","Spire","Spirit AeroSystems Holdings","Splunk","Sprague Resources","Sprouts Farmers Market","Stanley Black & Decker","Starbucks","State Farm Insurance","State Street","Steel Dynamics","Steelcase","Stepan","Stericycle","Stewart Information Services","Stifel Financial","StoneX Group","Stryker","Summit Materials","Super Micro Computer","Surgery Partners","Synchrony Financial","Syneos Health","Synopsys","Synovus Financial","Sysco","T. Rowe Price","TCF Financial","TD Synnex","TEGNA","TIAA","TJX","TTEC Holdings","TTM Technologies","Take-Two Interactive Software","Tapestry","Targa Resources","Target","Taylor Morrison Home","Teledyne FLIR","Teledyne Technologies","Teleflex","Telephone & Data Systems","TelevisaUnivision","Tempur Sealy International","Tenet Healthcare","Tenneco","Teradyne","Terex","Terminix Global Holdings","Tesla","Tetra Tech","Texas Instruments","Texas Roadhouse","Textron","Thermo Fisher Scientific","Thor Industries","Thrivent Financial for Lutherans","Timken","Toll Brothers","TopBuild","Toro","Tractor Supply","TransDigm Group","TransUnion","Travel + Leisure","TravelCenters of America","Travelers","TreeHouse Foods","Tri Pointe Homes","TriNet Group","Trimble","Trinity Industries","Triple-S Management","Triumph Group","Truist Financial","Tutor Perini","Twitter","Tyson Foods","U-Haul Holding","U.S. Bancorp","UFP Industries","UGI","US Foods Holding","USAA","UWM Holdings","Uber Technologies","Ulta Beauty","Under Armour","Union Pacific","Unisys","United Airlines Holdings","United Natural Foods","United Parcel Service","United Rentals","United States Steel","UnitedHealth Group","Univar Solutions","Universal","Universal Health Services","Unum Group","Upbound Group","Urban Outfitters","VF","Vail Resorts","Valero Energy","Valhi","Valmont Industries","Valvoline","Varian Medical Systems","Ventas","Verisk Analytics","Veritiv","Verizon Communications","Vertex Pharmaceuticals","Vertiv Holdings","Viasat","Viatris","Virtu Financial","Visa","Vishay Intertechnology","Visteon","Vistra","Vontier","Voya Financial","Vulcan Materials","W.R. Berkley","W.W. Grainger","WEC Energy Group","WESCO International","Walgreens Boots Alliance","Walmart","Walt Disney","Warner Bros. Discovery","Warner Music Group","Waste Management","Waters","Watsco","Wayfair","Weis Markets","Wells Fargo","Welltower","Werner Enterprises","West Pharmaceutical Services","WestRock","Western & Southern Financial Group","Western Digital","Western Midstream Partners","Western Union","Westinghouse Air Brake Technologies","Westlake","Weyerhaeuser","Whirlpool","Williams","Williams-Sonoma","Windstream Holdings II","Winnebago Industries","Woodward","Workday","World Kinect","Worthington Industries","Wynn Resorts","XPO","Xcel Energy","Xerox Holdings","Xilinx","Xylem","Yellow","Yum Brands","Yum China Holdings","Zebra Technologies","Zillow Group","Zimmer Biomet Holdings","Zions Bancorp.","Zoetis","Zoom Video Communications","Zurn Water Solutions","Zynga","eBay","iHeartMedia","loanDepot"]

def fortune_teller():
    return random.choice(fortune_500)