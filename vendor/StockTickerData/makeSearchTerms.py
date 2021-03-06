import csv

stockDict = {

    'MIIIU': 'M III Acquisition Corp.',

    'ORC': 'Orchid Island Capital, Inc.',

    'GRBK': 'Green Brick Partners, Inc.',

    'GAS': 'AGL Resources, Inc.',

    'THG': 'The Hanover Insurance Group, Inc.',

    'USLM': 'United States Lime & Minerals, Inc.',

    'NSEC': 'National Security Group, Inc.',

    'AEO': 'American Eagle Outfitters, Inc.',

    'KINS': 'Kingstone Companies, Inc',

    'IDLB': 'PowerShares FTSE International Low Beta Equal Weight Portfolio',

    'EVI': 'EnviroStarm, Inc.',

    'SUI-A': 'Sun Communities, Inc.',

    'PRXL': 'PAREXEL International Corporation',

    'WABC': 'Westamerica Bancorporation',

    'IONS': 'Ionis Pharmaceuticals, Inc.',

    'WWAV': 'Whitewave Foods Company (The)',

    'DLTH': 'Duluth Holdings Inc.',

    'BLVD': 'Boulevard Acquisition Corp. II',

    'OMED': 'OncoMed Pharmaceuticals, Inc.',

    'BCOV': 'Brightcove Inc.',

    'CVGI': 'Commercial Vehicle Group, Inc.',

    'LSCC': 'Lattice Semiconductor Corporation',

    'TASR': 'TASER International, Inc.',

    'ICBK': 'County Bancorp, Inc.',

    'ECOM': 'ChannelAdvisor Corporation',

    'OHAI': 'OHA Investment Corporation',

    'MKL': 'Markel Corporation',

    'IPHI': 'Inphi Corporation',

    'KRNY': 'Kearny Financial',

    'CECO': 'Career Education Corporation',

    'CERS': 'Cerus Corporation',

    'BSMX': 'Grupo Financiero Santander Mexico S.A. B. de C.V.',

    'QNST': 'QuinStreet, Inc.',

    'CBSH': 'Commerce Bancshares, Inc.',

    'WPXP': 'WPX Energy, Inc.',

    'DTZ': 'DTE Energy Company',

    'LULU': 'lululemon athletica inc.',

    'ONP': 'Orient Paper, Inc.',

    'WPZ': 'Williams Partners LP',

    'QUOT': 'Quotient Technology Inc.',

    'CNBKA': 'Century Bancorp, Inc.',

    'FLML': 'Flamel Technologies S.A.',

    'EMZ': 'Entergy Mississippi, Inc.',

    'GOL': 'Gol Linhas Aereas Inteligentes S.A.',

    'TTF': 'Thai Fund, Inc. (The)',

    'CRC': 'California Resources Corporation',

    'RRD': 'R.R. Donnelley & Sons Company',

    'WIX': 'Wix.com Ltd.',

    'SQ': 'Square, Inc.',

    'EPIQ': 'EPIQ Systems, Inc.',

    'HTBK': 'Heritage Commerce Corp',

    'C-S': 'Citigroup Inc.',

    'GLUU': 'Glu Mobile Inc.',

    'QABA': 'First Trust NASDAQ ABA Community Bank Index Fund',

    'RLJ': 'RLJ Lodging Trust',

    'GNW': 'Genworth Financial Inc',

    'ENIA': 'Enersis Americas S.A.',

    'PCK': 'Pimco California Municipal Income Fund II',

    'GNCMA': 'General Communication, Inc.',

    'STT-C': 'State Street Corporation',

    'INSM': 'Insmed, Inc.',

    'RIG': 'Transocean Ltd.',

    'KFFB': 'Kentucky First Federal Bancorp',

    'TEL': 'TE Connectivity Ltd.',

    'YELP': 'Yelp Inc.',

    'SMMF': 'Summit Financial Group, Inc.',

    'LGCYO': 'Legacy Reserves LP',

    'CFD': 'Nuveen Diversified Commodity Fund',

    'QTEC': 'First Trust NASDAQ-100- Technology Index Fund',

    'SKT': 'Tanger Factory Outlet Centers, Inc.',

    'ADSK': 'Autodesk, Inc.',

    'CARO': 'Carolina Financial Corporation',

    'LLTC': 'Linear Technology Corporation',

    'BWG': 'Legg Mason BW Global Income Opportunities Fund Inc.',

    'UMBF': 'UMB Financial Corporation',

    'CPHC': 'Canterbury Park Holding Corporation',

    'SWX': 'Southwest Gas Corporation',

    'AMAT': 'Applied Materials, Inc.',

    'DFRG': 'Del Frisco\'s Restaurant Group, Inc.',

    'INTU': 'Intuit Inc.',

    'INN-B': 'Summit Hotel Properties, Inc.',

    'EIGR': 'Eiger BioPharmaceuticals, Inc.',

    'BLRX': 'BioLineRx Ltd.',

    'BNJ': 'BlackRock New Jersey Municipal Income Trust',

    'ALDR': 'Alder BioPharmaceuticals, Inc.',

    'CTSH': 'Cognizant Technology Solutions Corporation',

    'NLY-C': 'Annaly Capital Management Inc',

    'VRTU': 'Virtusa Corporation',

    'GPI': 'Group 1 Automotive, Inc.',

    'BXS': 'BancorpSouth, Inc.',

    'SSKN': 'Strata Skin Sciences, Inc.',

    'PZC': 'PIMCO California Municipal Income Fund III',

    'TORM': 'TOR Minerals International Inc',

    'NAN': 'Nuveen New York Dividend Advantage Municipal Fund',

    'SFBS': 'ServisFirst Bancshares, Inc.',

    'GIGM': 'GigaMedia Limited',

    'SAN-C': 'Banco Santander, S.A.',

    'EVG': 'Eaton Vance Short Diversified Income Fund',

    'EGI': 'Entree Gold Inc',

    'TMP': 'Tompkins Financial Corporation',

    'EDN': 'Empresa Distribuidora Y Comercializadora Norte S.A. (Edenor)',

    'NEOT': 'Neothetics, Inc.',

    'RY-T': 'Royal Bank Of Canada',

    'DHF': 'Dreyfus High Yield Strategies Fund',

    'GMT': 'GATX Corporation',

    'ICB': 'MS Income Securities, Inc.',

    'LGCY': 'Legacy Reserves LP',

    'AUY': 'Yamana Gold Inc.',

    'WYY': 'WidePoint Corporation',

    'UIS': 'Unisys Corporation',

    'DSKX': 'DS Healthcare Group, Inc.',

    'TROV': 'TrovaGene, Inc.',

    'TISI': 'Team, Inc.',

    'ENO': 'Entergy New Orleans, Inc.',

    'LANC': 'Lancaster Colony Corporation',

    'MSCA': 'Main Street Capital Corporation',

    'VIDI': 'Vident International Equity Fund',

    'WTFC': 'Wintrust Financial Corporation',

    'GCI': 'TEGNA Inc.',

    'AEZS': 'AEterna Zentaris Inc.',

    'RSTI': 'Rofin-Sinar Technologies, Inc.',

    'HRTX': 'Heron Therapeutics, Inc.  ',

    'MBCN': 'Middlefield Banc Corp.',

    'MSI': 'Motorola Solutions, Inc.',

    'RSO': 'Resource Capital Corp.',

    'ADUS': 'Addus HomeCare Corporation',

    'EVP': 'Eaton Vance Pennsylvania Municipal Income Trust',

    'LTS': 'Ladenburg Thalmann Financial Services Inc',

    'DSCI': 'Derma Sciences, Inc.',

    'TSBK': 'Timberland Bancorp, Inc.',

    'NMS': 'Nuveen Minnesota Municipal Income Fund',

    'ALGT': 'Allegiant Travel Company',

    'FDC': 'First Data Corporation',

    'TPH': 'TRI Pointe Group, Inc.',

    'FFHL': 'Fuwei Films (Holdings) Co., Ltd.',

    'MFC': 'Manulife Financial Corp',

    'JSYN': 'Jensyn Acquistion Corp.',

    'NEWTL': 'Newtek Business Services Corp.',

    'LVNTA': 'Liberty Interactive Corporation',

    'SEV': 'Sevcon, Inc.',

    'GNST': 'GenSight Biologics S.A.',

    'NTIC': 'Northern Technologies International Corporation',

    'CADT': 'DT Asia Investments Limited',

    'HLG': 'Hailiang Education Group Inc.',

    'VCRA': 'Vocera Communications, Inc.',

    'FSV': 'FirstService Corporation',

    'SHO': 'Sunstone Hotel Investors, Inc.',

    'HCN-J': 'Welltower Inc.',

    'LBAI': 'Lakeland Bancorp, Inc.',

    'CI': 'Cigna Corporation',

    'NXJ': 'Nuveen New Jersey Dividend Advantage Municipal Fund',

    'BNTC': 'Benitec Biopharma Limited',

    'MYL': 'Mylan N.V.',

    'HRMN': 'Harmony Merger Corp.',

    'VMW': 'Vmware, Inc.',

    'MOD': 'Modine Manufacturing Company',

    'OCX': 'OncoCyte Corporation',

    'GPM': 'Guggenheim Enhanced Equity Income Fund',

    'DLR-H': 'Digital Realty Trust, Inc.',

    'FN': 'Fabrinet',

    'BVN': 'Buenaventura Mining Company Inc.',

    'PFN': 'PIMCO Income Strategy Fund II',

    'NMY': 'Nuveen Maryland Premium Income Municipal Fund',

    'ORMP': 'Oramed Pharmaceuticals Inc.',

    'NOAH': 'Noah Holdings Ltd.',

    'SQNS': 'Sequans Communications S.A.',

    'CHMA': 'Chiasma, Inc.',

    'LGL': 'LGL Group, Inc. (The)',

    'FTHI': 'First Trust High Income ETF',

    'PGND': 'Press Ganey Holdings, Inc.',

    'CFFN': 'Capitol Federal Financial, Inc.',

    'BTA': 'BlackRock Long-Term Municipal Advantage Trust',

    'ICLR': 'ICON plc',

    'PACB': 'Pacific Biosciences of California, Inc.',

    'PAVMU': 'PAVmed Inc.',

    'UIHC': 'United Insurance Holdings Corp.',

    'BML-I': 'Bank of America Corporation',

    'NBIX': 'Neurocrine Biosciences, Inc.',

    'BKEP': 'Blueknight Energy Partners L.P., L.L.C.',

    'DHY': 'Credit Suisse High Yield Bond Fund',

    'EEML': 'iShares MSCI Emerging Markets Latin America Index Fund',

    'AMTG-A': 'Apollo Residential Mortgage, Inc.',

    'ADI': 'Analog Devices, Inc.',

    'COLL': 'Collegium Pharmaceutical, Inc.',

    'PFH': 'CABCO Series 2004-101 Trust',

    'SELF': 'Global Self Storage, Inc.',

    'PLXS': 'Plexus Corp.',

    'HWKN': 'Hawkins, Inc.',

    'AEY': 'ADDvantage Technologies Group, Inc.',

    'SQBG': 'Sequential Brands Group, Inc.',

    'CS': 'Credit Suisse Group',

    'BVXVW': 'BiondVax Pharmaceuticals Ltd.',

    'BA': 'Boeing Company (The)',

    'CALL': 'magicJack VocalTec Ltd',

    'OVLY': 'Oak Valley Bancorp (CA)',

    'SNX': 'Synnex Corporation',

    'IOC': 'InterOil Corporation',

    'PIH': '1347 Property Insurance Holdings, Inc.',

    'CUBI': 'Customers Bancorp, Inc',

    'ISF': 'ING Group, N.V.',

    'TFSCW': '1347 Capital Corp.',

    'KVHI': 'KVH Industries, Inc.',

    'NCR': 'NCR Corporation',

    'ASC': 'Ardmore Shipping Corporation',

    'AMX': 'America Movil, S.A.B. de C.V.',

    'CRZO': 'Carrizo Oil & Gas, Inc.',

    'AGIIL': 'Argo Group International Holdings, Ltd.',

    'AEG': 'Aegon NV',

    'CERU': 'Cerulean Pharma Inc.',

    'MNRK': 'Monarch Financial Holdings, Inc.',

    'ATNI': 'Atlantic Tele-Network, Inc.',

    'WPT': 'World Point Terminals, LP',

    'CHD': 'Church & Dwight Company, Inc.',

    'VET': 'Vermilion Energy Inc.',

    'RSO-B': 'Resource Capital Corp.',

    'AMTX': 'Aemetis, Inc',

    'CORR-A': 'CorEnergy Infrastructure Trust, Inc.',

    'ARLP': 'Alliance Resource Partners, L.P.',

    'GIG': 'GigPeak, Inc.',

    'SGY': 'Stone Energy Corporation',

    'FSIC': 'FS Investment Corporation',

    'HBMD': 'Howard Bancorp, Inc.',

    'DGRS': 'WisdomTree U.S. SmallCap Quality Dividend Growth Fund',

    'KMG': 'KMG Chemicals, Inc.',

    'ARI-A': 'Apollo Commercial Real Estate Finance',

    'ORN': 'Orion Group Holdings, Inc.',

    'DCIX': 'Diana Containerships Inc.',

    'INN': 'Summit Hotel Properties, Inc.',

    'GRUB': 'GrubHub Inc.',

    'SBGI': 'Sinclair Broadcast Group, Inc.',

    'UTF': 'Cohen & Steers Infrastructure Fund, Inc',

    'CHEF': 'The Chefs\' Warehouse, Inc.',

    'FBIZ': 'First Business Financial Services, Inc.',

    'PAACU': 'Pacific Special Acquisition Corp.',

    'DEA': 'Easterly Government Properties, Inc.',

    'RIV': 'RiverNorth Opportunities Fund, Inc.',

    'NYMT': 'New York Mortgage Trust, Inc.',

    'BHB': 'Bar Harbor Bankshares, Inc.',

    'CASY': 'Caseys General Stores, Inc.',

    'TAL': 'TAL International Group, Inc.',

    'UEPS': 'Net 1 UEPS Technologies, Inc.',

    'SHOR': 'ShoreTel, Inc.',

    'STK': 'Columbia Seligman Premium Technology Growth Fund, Inc',

    'FDUS': 'Fidus Investment Corporation',

    'BDGE': 'Bridge Bancorp, Inc.',

    'CLMT': 'Calumet Specialty Products Partners, L.P.',

    'MET': 'MetLife, Inc.',

    'PLBC': 'Plumas Bancorp',

    'QVCB': 'Liberty Interactive Corporation',

    'CSWI': 'CSW Industrials, Inc.',

    'JKI': 'iShares Morningstar Mid-Cap ETF',

    'ZG': 'Zillow Group, Inc.',

    'GOODP': 'Gladstone Commercial Corporation',

    'RELX': 'RELX PLC',

    'FRGI': 'Fiesta Restaurant Group, Inc.',

    'PNTA': 'PennantPark Investment Corporation',

    'TUSA': 'First Trust Total US Market AlphaDEX ETF',

    'MIME': 'Mimecast Limited',

    'WNS': 'WNS (Holdings) Limited',

    'PEGI': 'Pattern Energy Group Inc.',

    'CLCD': 'CoLucid Pharmaceuticals, Inc.',

    'PJH': 'Prudential Financial, Inc.',

    'QTS': 'QTS Realty Trust, Inc.',

    'NGLS-A': 'Targa Resources Partners LP',

    'SRG': 'Seritage Growth Properties',

    'HBI': 'Hanesbrands Inc.',

    'FULLL': 'Full Circle Capital Corporation',

    'TPX': 'Tempur Sealy International, Inc.',

    'FCX': 'Freeport-McMoran, Inc.',

    'TRU': 'TransUnion',

    'CVA': 'Covanta Holding Corporation',

    'JOBS': '51job, Inc.',

    'ARRY': 'Array BioPharma Inc.',

    'SXCP': 'SunCoke Energy Partners, L.P.',

    'SIEN': 'Sientra, Inc.',

    'KMT': 'Kennametal Inc.',

    'PICO': 'PICO Holdings Inc.',

    'ETV': 'Eaton Vance Corporation',

    'PTXP': 'PennTex Midstream Partners, LP',

    'FICO': 'Fair Isaac Corporation',

    'OLBK': 'Old Line Bancshares, Inc.',

    'GRC': 'Gorman-Rupp Company (The)',

    'SBCF': 'Seacoast Banking Corporation of Florida',

    'QUAD': 'Quad Graphics, Inc',

    'AE': 'Adams Resources & Energy, Inc.',

    'SBSA': 'Spanish Broadcasting System, Inc.',

    'BHAC': 'Barington/Hilco Acquisition Corp.',

    'ZBK': 'Zions Bancorporation',

    'RIGP': 'Transocean Partners LLC',

    'KUTV': 'Ku6 Media Co., Ltd.',

    'RBPAA': 'Royal Bancshares of Pennsylvania, Inc.',

    'GMLP': 'Golar LNG Partners LP',

    'TLGT': 'Teligent, Inc.',

    'ROCK': 'Gibraltar Industries, Inc.',

    'EVER-A': 'EverBank Financial Corp.',

    'RMAX': 'RE/MAX Holdings, Inc.',

    'ROX': 'Castle Brands, Inc.',

    'KTOS': 'Kratos Defense & Security Solutions, Inc.',

    'CBAK': 'China BAK Battery, Inc.',

    'GXP-A': 'Great Plains Energy Inc',

    'KMPR': 'Kemper Corporation',

    'AMPH': 'Amphastar Pharmaceuticals, Inc.',

    'AFL': 'Aflac Incorporated',

    'GLBL': 'TerraForm Global, Inc.',

    'NXRT': 'NexPoint Residential Trust, Inc.',

    'VAL': 'Valspar Corporation (The)',

    'NCS': 'NCI Building Systems, Inc.',

    'GASS': 'StealthGas, Inc.',

    'SYKE': 'Sykes Enterprises, Incorporated',

    'SU': 'Suncor Energy  Inc.',

    'HQL': 'Tekla Life Sciences Investors',

    'JNJ': 'Johnson & Johnson',

    'BBG': 'Bill Barrett Corporation',

    'ANAT': 'American National Insurance Company',

    'TPRE': 'Third Point Reinsurance Ltd.',

    'BLE': 'BlackRock Municipal Income Trust II',

    'MHO-A': 'M/I Homes, Inc.',

    'TSE': 'Trinseo S.A.',

    'CSF': 'Victory CEMP US Discovery Enhanced Volatility Wtd Index ETF',

    'GAM': 'General American Investors, Inc.',

    'OPY': 'Oppenheimer Holdings, Inc.',

    'COT': 'Cott Corporation',

    'FTAI': 'Fortress Transportation and Infrastructure Investors LLC',

    'PLX': 'Protalix BioTherapeutics, Inc.',

    'ENDP': 'Endo International plc',

    'ABAC': 'Aoxin Tianli Group, Inc.',

    'SCHW-B': 'The Charles Schwab Corporation',

    'CVR': 'Chicago Rivet & Machine Co.',

    'PLUS': 'ePlus inc.',

    'DTLK': 'Datalink Corporation',

    'HFBL': 'Home Federal Bancorp, Inc. of Louisiana',

    'SKYS': 'Sky Solar Holdings, Ltd.',

    'HIMX': 'Himax Technologies, Inc.',

    'HUSI-H.CL': 'HSBC USA, Inc.',

    'STC': 'Stewart Information Services Corporation',

    'VSH': 'Vishay Intertechnology, Inc.',

    'MSFG': 'MainSource Financial Group, Inc.',

    'ELA': 'Entergy Louisiana, Inc.',

    'AZO': 'AutoZone, Inc.',

    'ETSY': 'Etsy, Inc.',

    'HOLI': 'Hollysys Automation Technologies, Ltd.',

    'LPSB': 'LaPorte Bancorp, Inc.',

    'ARLZ': 'Aralez Pharmaceuticals Inc.',

    'GNRT': 'Gener8 Maritime, Inc.',

    'AXTA': 'Axalta Coating Systems Ltd.',

    'CLH': 'Clean Harbors, Inc.',

    'BNED': 'Barnes & Noble Education, Inc',

    'CERC': 'Cerecor Inc.',

    'SBRAP': 'Sabra Healthcare REIT, Inc.',

    'GLU': 'The Gabelli Global Utility and Income Trust',

    'EMG': 'Emergent Capital, Inc.',

    'CSCD': 'Cascade Microtech, Inc.',

    'BPOPN': 'Popular, Inc.',

    'YOD': 'You On Demand Holdings, Inc.',

    'FELP': 'Foresight Energy LP',

    'PPX': 'PPL Capital Funding, Inc.',

    'TBBK': 'The Bancorp, Inc.',

    'MRLN': 'Marlin Business Services Corp.',

    'PBBI': 'PB Bancorp, Inc.',

    'MGYR': 'Magyar Bancorp, Inc.',

    'Z': 'Zillow Group, Inc.',

    'ONVI': 'Onvia, Inc.',

    'C-C': 'Citigroup Inc.',

    'XLNX': 'Xilinx, Inc.',

    'ECA': 'Encana Corporation',

    'RWLK': 'ReWalk Robotics Ltd',

    'RENN': 'Renren Inc.',

    'MCUR': 'MACROCURE LTD.',

    'HTA': 'Healthcare Trust of America, Inc.',

    'WMGIZ': 'Wright Medical Group N.V.',

    'WVE': 'WAVE Life Sciences Ltd.',

    'CHCI': 'Comstock Holding Companies, Inc.',

    'NLSN': 'Nielsen N.V.',

    'NR': 'Newpark Resources, Inc.',

    'GGP-A': 'General Growth Properties, Inc.',

    'FEP': 'First Trust Europe AlphaDEX Fund',

    'CO': 'China Cord Blood Corporation',

    'AHT-A': 'Ashford Hospitality Trust Inc',

    'ABRN': 'Arbor Realty Trust',

    'LMRK': 'Landmark Infrastructure Partners LP',

    'FGBI': 'First Guaranty Bancshares, Inc.',

    'JOB': 'General Employment Enterprises, Inc.',

    'SCWX': 'SecureWorks Corp.',

    'STX': 'Seagate Technology PLC',

    'AIV-Z': 'Apartment Investment and Management Company',

    'FNWB': 'First Northwest Bancorp',

    'EVTC': 'Evertec, Inc.',

    'TAP': 'Molson Coors Brewing  Company',

    'SEAC': 'SeaChange International, Inc.',

    'AMRI': 'Albany Molecular Research, Inc.',

    'CZWI': 'Citizens Community Bancorp, Inc.',

    'OZRK': 'Bank of the Ozarks',

    'PMTS': 'CPI Card Group Inc.',

    'NX': 'Quanex Building Products Corporation',

    'DGRW': 'WisdomTree U.S. Quality Dividend Growth Fund',

    'DXPE': 'DXP Enterprises, Inc.',

    'MGN': 'Mines Management, Inc.',

    'JPM.WS': 'J P Morgan Chase & Co',

    'NLS': 'Nautilus Group, Inc. (The)',

    'MTP': 'Midatech Pharma PLC',

    'LVNTB': 'Liberty Interactive Corporation',

    'ECL': 'Ecolab Inc.',

    'ERS': 'Empire Resources, Inc.',

    'BXP': 'Boston Properties, Inc.',

    'FMB': 'First Trust Managed Municipal ETF',

    'SYY': 'Sysco Corporation',

    'TY': 'Tri Continental Corporation',

    'WEYS': 'Weyco Group, Inc.',

    'ECTE': 'Echo Therapeutics, Inc.',

    'USNA': 'USANA Health Sciences, Inc.',

    'RBCN': 'Rubicon Technology, Inc.',

    'HIFR': 'InfraREIT, Inc.',

    'QLYS': 'Qualys, Inc.',

    'BCOM': 'B Communications Ltd.',

    'GF': 'New Germany Fund, Inc. (The)',

    'REXX': 'Rex Energy Corporation',

    'TTOO': 'T2 Biosystems, Inc.',

    'RNN': 'Rexahn Pharmaceuticals, Inc.',

    'NAV-D': 'Navistar International Corporation',

    'HCOM': 'Hawaiian Telcom Holdco, Inc.',

    'RITT': 'RIT Technologies Ltd.',

    'NRP': 'Natural Resource Partners LP',

    'CBO': 'CBO (Listing Market - NYSE - Networks A/E)',

    'SKIS': 'Peak Resorts, Inc.',

    'URI': 'United Rentals, Inc.',

    'RAIL': 'Freightcar America, Inc.',

    'TSI': 'TCW Strategic Income Fund, Inc.',

    'VNO-K': 'Vornado Realty Trust',

    'ENTG': 'Entegris, Inc.',

    'AINC': 'Ashford Inc.',

    'MXC': 'Mexco Energy Corporation',

    'AGRX': 'Agile Therapeutics, Inc.',

    'HDB': 'HDFC Bank Limited',

    'DK': 'Delek US Holdings, Inc.',

    'BDL': 'Flanigan\'s Enterprises, Inc.',

    'AMRK': 'A-Mark Precious Metals, Inc.',

    'EPAM': 'EPAM Systems, Inc.',

    'HDS': 'HD Supply Holdings, Inc.',

    'IM': 'Ingram Micro Inc.',

    'INOV': 'Inovalon Holdings, Inc.',

    'BSET': 'Bassett Furniture Industries, Incorporated',

    'FCAM': 'Fiat Chrysler Automobiles N.V.',

    'PCG-I': 'Pacific Gas & Electric Co.',

    'BAC.WS.A': 'Bank of America Corporation',

    'UAN': 'CVR Partners, LP',

    'WHLM': 'Wilhelmina International, Inc.',

    'PXS': 'Pyxis Tankers Inc.',

    'RCKY': 'Rocky Brands, Inc.',

    'PSCI': 'PowerShares S&P SmallCap Industrials Portfolio',

    'GPIC': 'Gaming Partners International Corporation',

    'CRMD': 'CorMedix Inc',

    'TEDU': 'Tarena International, Inc.',

    'TRNO-A': 'Terreno Realty Corporation',

    'HGG': 'HHGregg, Inc.',

    'RLGY': 'Realogy Holdings Corp.',

    'TMK': 'Torchmark Corporation',

    'LNT': 'Alliant Energy Corporation',

    'LENS': 'Presbia PLC',

    'BITA': 'Bitauto Holdings Limited',

    'PWOD': 'Penns Woods Bancorp, Inc.',

    'BYD': 'Boyd Gaming Corporation',

    'MDLY': 'Medley Management Inc.',

    'NVTR': 'Nuvectra Corporation',

    'EQIX': 'Equinix, Inc.',

    'INZ': 'ING Group, N.V.',

    'NQ': 'NQ Mobile Inc.',

    'MO': 'Altria Group',

    'DSX': 'Diana Shipping inc.',

    'CVV': 'CVD Equipment Corporation',

    'ENLK': 'EnLink Midstream Partners, LP',

    'CA': 'CA Inc.',

    'LMFA': 'LM Funding America, Inc.',

    'SYBT': 'Stock Yards Bancorp, Inc.',

    'INTX': 'Intersections, Inc.',

    'PIM': 'Putnam Master Intermediate Income Trust',

    'SBBP': 'Strongbridge Biopharma plc',

    'RSE': 'Rouse Properties, Inc.',

    'SHOP': 'Shopify Inc.',

    'AMP': 'AMERIPRISE FINANCIAL SERVICES, INC.',

    'NAK': 'Northern Dynasty Minerals, Ltd.',

    'VGR': 'Vector Group Ltd.',

    'EXTR': 'Extreme Networks, Inc.',

    'JMPC': 'JMP Group LLC',

    'VNRX': 'VolitionRX Limited',

    'PHIIK': 'PHI, Inc.',

    'WIN': 'Windstream Holdings, Inc.',

    'NVS': 'Novartis AG',

    'GM.WS.A': 'General Motors Company',

    'IVAC': 'Intevac, Inc.',

    'NVEE': 'NV5 Global, Inc.',

    'FE': 'FirstEnergy Corporation',

    'RMT': 'Royce Micro-Cap Trust, Inc.',

    'NAII': 'Natural Alternatives International, Inc.',

    'FRED': 'Fred\'s, Inc.',

    'CPS': 'Cooper-Standard Holdings Inc.',

    'TVIX': 'region',

    'VMBS': 'Vanguard Mortgage-Backed Securities ETF',

    'YUME': 'YuMe, Inc.',

    'MTDR': 'Matador Resources Company',

    'FSC': 'Fifth Street Finance Corp.',

    'RLJE': 'RLJ Entertainment, Inc.',

    'NTEC': 'Intec Pharma Ltd.',

    'MDRX': 'Allscripts Healthcare Solutions, Inc.',

    'ALJ': 'Alon USA Energy, Inc.',

    'CHRS': 'Coherus BioSciences, Inc.',

    'FCH-A': 'FelCor Lodging Trust Incorporated',

    'CCOI': 'Cogent Communications Holdings, Inc.',

    'VLTC': 'Voltari Corporation',

    'VGSH': 'Vanguard Short-Term Government ETF',

    'PB': 'Prosperity Bancshares, Inc.',

    'SAFT': 'Safety Insurance Group, Inc.',

    'ARR-A': 'ARMOUR Residential REIT, Inc.',

    'RDN': 'Radian Group Inc.',

    'MWR': 'Morgan Stanley',

    'SANW': 'S&W Seed Company',

    'MEP': 'Midcoast Energy Partners, L.P.',

    'RPAI': 'Retail Properties of America, Inc.',

    'LPT': 'Liberty Property Trust',

    'EZT': 'Entergy Texas Inc',

    'PNI': 'Pimco New York Municipal Income Fund II',

    'CLBS': 'Caladrius Biosciences, Inc.',

    'PCYG': 'Park City Group, Inc.',

    'PLXP': 'PLx Pharma Inc.',

    'JRI': 'Nuveen Real Asset Income and Growth Fund',

    'LL': 'Lumber Liquidators Holdings, Inc',

    'RUN': 'Sunrun Inc.',

    'CBU': 'Community Bank System, Inc.',

    'XON': 'Intrexon Corporation',

    'PPSI': 'Pioneer Power Solutions, Inc.',

    'HRMNW': 'Harmony Merger Corp.',

    'VLRS': 'Controladora Vuela Compania de Aviacion, S.A.B. de C.V.',

    'GLO': 'Clough Global Opportunities Fund',

    'PLKI': 'Popeyes Louisiana Kitchen, Inc.',

    'FNLC': 'First Bancorp, Inc (ME)',

    'BNTCW': 'Benitec Biopharma Limited',

    'CYRN': 'CYREN Ltd.',

    'RPTP': 'Raptor Pharmaceutical Corp.',

    'BDR': 'Blonder Tongue Laboratories, Inc.',

    'CNXR': 'Connecture, Inc.',

    'FNTCU': 'FinTech Acquisition Corp.',

    'ABUS': 'Arbutus Biopharma Corporation',

    'LEDS': 'SemiLEDS Corporation',

    'LMRKP': 'Landmark Infrastructure Partners LP',

    'MBLY': 'Mobileye N.V.',

    'WTBA': 'West Bancorporation',

    'NPD': 'China Nepstar Chain Drugstore Ltd',

    'MKTX': 'MarketAxess Holdings, Inc.',

    'NWBO': 'Northwest Biotherapeutics, Inc.',

    'GLDC': 'Golden Enterprises, Inc.',

    'FLDM': 'Fluidigm Corporation',

    'PYS': 'PPlus Trust',

    'TAIT': 'Taitron Components Incorporated',

    'MGI': 'Moneygram International, Inc.',

    'EBIO': 'Eleven Biotherapeutics, Inc.',

    'MXWL': 'Maxwell Technologies, Inc.',

    'NCT-D': 'Newcastle Investment Corporation',

    'CYAD': 'Celyad SA',

    'SWIR': 'Sierra Wireless, Inc.',

    'GWW': 'W.W. Grainger, Inc.',

    'SA': 'Seabridge Gold, Inc.',

    'KTEC': 'Key Technology, Inc.',

    'TCS': 'Container Store (The)',

    'MAV': 'Pioneer Municipal High Income Advantage Trust',

    'JMPB': 'JMP Group LLC',

    'PRE-E': 'PartnerRe Ltd.',

    'NWFL': 'Norwood Financial Corp.',

    'RAS-C': 'RAIT Financial Trust',

    'SKYY': 'First Trust ISE Cloud Computing Index Fund',

    'PEGA': 'Pegasystems Inc.',

    'TRVN': 'Trevena, Inc.',

    'NURO': 'NeuroMetrix, Inc.',

    'WCG': 'WellCare Health Plans, Inc.',

    'ANF': 'Abercrombie & Fitch Company',

    'GBAB': 'Guggenheim Build America Bonds Managed Duration Trust',

    'STL': 'Sterling Bancorp',

    'ARES': 'Ares Management L.P.',

    'VYGR': 'Voyager Therapeutics, Inc.',

    'SCLN': 'SciClone Pharmaceuticals, Inc.',

    'NKE': 'Nike, Inc.',

    'ACN': 'Accenture plc',

    'LNGR': 'Global X Longevity Thematic ETF',

    'NK': 'NantKwest, Inc.',

    'TWMC': 'Trans World Entertainment Corp.',

    'VNRAP': 'Vanguard Natural Resources LLC',

    'SPH': 'Suburban Propane Partners, L.P.',

    'MT': 'ArcelorMittal',

    'TTNP': 'Titan Pharmaceuticals, Inc.',

    'HZN': 'Horizon Global Corporation',

    'ANIP': 'ANI Pharmaceuticals, Inc.',

    'MDSY': 'ModSys International Ltd.',

    'NXEOW': 'Nexeo Solutions, Inc.',

    'NRF-D': 'Northstar Realty Finance Corp.',

    'VBF': 'Invesco Bond Fund',

    'CAH': 'Cardinal Health, Inc.',

    'UNAM': 'Unico American Corporation',

    'GILD': 'Gilead Sciences, Inc.',

    'NXEO': 'Nexeo Solutions, Inc.',

    'ATVI': 'Activision Blizzard, Inc',

    'UMH-A': 'UMH Properties, Inc.',

    'VXUS': 'Vanguard Total International Stock ETF',

    'BK-C': 'Bank Of New York Mellon Corporation (The)',

    'CE': 'Celanese Corporation',

    'SLW': 'Silver Wheaton Corp',

    'SPG-J': 'Simon Property Group, Inc.',

    'NBR': 'Nabors Industries Ltd.',

    'TRUE': 'TrueCar, Inc.',

    'IMPV': 'Imperva, Inc.',

    'VA': 'Virgin America Inc.',

    'MGM': 'MGM Resorts International',

    'TEN': 'Tenneco Inc.',

    'CLDX': 'Celldex Therapeutics, Inc.',

    'EXPD': 'Expeditors International of Washington, Inc.',

    'TBPH': 'Theravance Biopharma, Inc.',

    'BFO': 'Blackrock Florida Municipal 2020 Term Trust',

    'BFS': 'Saul Centers, Inc.',

    'PBF': 'PBF Energy Inc.',

    'CLRBZ': 'Cellectar Biosciences, Inc.',

    'MGPI': 'MGP Ingredients, Inc.',

    'AIRT': 'Air T, Inc.',

    'TCO-J': 'Taubman Centers, Inc.',

    'MLAB': 'Mesa Laboratories, Inc.',

    'CTIB': 'CTI Industries Corporation',

    'CISG': 'CNinsure Inc.',

    'MTB-': 'M&T Bank Corporation',

    'EBTC': 'Enterprise Bancorp Inc',

    'AKP': 'Alliance California Municipal Income Fund Inc',

    'MKC': 'McCormick & Company, Incorporated',

    'RXN': 'Rexnord Corporation',

    'EQBK': 'Equity Bancshares, Inc.',

    'CC': 'Chemours Company (The)',

    'AFA': 'American Financial Group, Inc.',

    'QLIK': 'Qlik Technologies Inc.',

    'EML': 'Eastern Company (The)',

    'PSCU': 'PowerShares S&P SmallCap Utilities Portfolio',

    'PVH': 'PVH Corp.',

    'NEP': 'NextEra Energy Partners, LP',

    'GPC': 'Genuine Parts Company',

    'EGF': 'Blackrock Enhanced Government Fund, Inc',

    'UA': 'Under Armour, Inc.',

    'CKH': 'SEACOR Holdings, Inc.',

    'NUS': 'Nu Skin Enterprises, Inc.',

    'HTH': 'Hilltop Holdings Inc.',

    'FLL': 'Full House Resorts, Inc.',

    'AAN': 'Aaron\'s,  Inc.',

    'ELON': 'Echelon Corporation',

    'AKO.B': 'Embotelladora Andina S.A.',

    'CENT': 'Central Garden & Pet Company',

    'ARMK': 'Aramark',

    'ASYS': 'Amtech Systems, Inc.',

    'TTEC': 'TeleTech Holdings, Inc.',

    'HTD': 'John Hancock Tax Advantaged Dividend Income Fund',

    'EV': 'Eaton Vance Corporation',

    'DGII': 'Digi International Inc.',

    'TRCH': 'Torchlight Energy Resources, Inc.',

    'SPIL': 'Siliconware Precision Industries Company, Ltd.',

    'VRNT': 'Verint Systems Inc.',

    'CHKE': 'Cherokee Inc.',

    'TOT': 'TotalFinaElf, S.A.',

    'UTI': 'Universal Technical Institute Inc',

    'NLST': 'Netlist, Inc.',

    'GTN': 'Gray Television, Inc.',

    'CHDN': 'Churchill Downs, Incorporated',

    'ALP-O': 'Alabama Power Company',

    'AFSI-E': 'AmTrust Financial Services, Inc.',

    'SBOT': 'Stellar Biotechnologies, Inc.',

    'YHOO': 'Yahoo! Inc.',

    'BGCP': 'BGC Partners, Inc.',

    'JIVE': 'Jive Software, Inc.',

    'REGN': 'Regeneron Pharmaceuticals, Inc.',

    'DNOW': 'NOW Inc.',

    'OSG': 'Overseas Shipholding Group, Inc.',

    'ADRD': 'BLDRS Developed Markets 100 ADR Index Fund',

    'CLSD': 'Clearside Biomedical, Inc.',

    'CTQ': 'Qwest Corporation',

    'BHI': 'Baker Hughes Incorporated',

    'STAR-D': 'iStar Financial Inc.',

    'PFGC': 'Performance Food Group Company',

    'JBT': 'John Bean Technologies Corporation',

    'AMCX': 'AMC Networks Inc.',

    'SPKE': 'Spark Energy, Inc.',

    'MNR-A': 'Monmouth Real Estate Investment Corporation',

    'MXF': 'Mexico Fund, Inc. (The)',

    'PSET': 'Principal Price Setters Index ETF',

    'BTN': 'Ballantyne Strong, Inc',

    'KOPN': 'Kopin Corporation',

    'AROC': 'Archrock, Inc.',

    'FSS': 'Federal Signal Corporation',

    'ALKS': 'Alkermes plc',

    'ACW': 'Accuride Corporation New',

    'PLCE': 'Children\'s Place, Inc. (The)',

    'SXL': 'Sunoco Logistics Partners LP',

    'AEHR': 'Aehr Test Systems',

    'MICTW': 'Micronet Enertec Technologies, Inc.',

    'LTRPB': 'Liberty TripAdvisor Holdings, Inc.',

    'WY-A': 'Weyerhaeuser Company',

    'TSEM': 'Tower Semiconductor Ltd.',

    'PBT': 'Permian Basin Royalty Trust',

    'ENH': 'Endurance Specialty Holdings Ltd',

    'TCAP': 'Triangle Capital Corporation',

    'MGA': 'Magna International, Inc.',

    'FYC': 'First Trust Small Cap Growth AlphaDEX Fund',

    'KNX': 'Knight Transportation, Inc.',

    'IRG': 'Ignite Restaurant Group, Inc.',

    'VCEL': 'Vericel Corporation',

    'PTCT': 'PTC Therapeutics, Inc.',

    'BRG-A': 'Bluerock Residential Growth REIT, Inc.',

    'APT': 'Alpha Pro Tech, Ltd.',

    'FEI': 'First Trust MLP and Energy Income Fund',

    'GXP-E': 'Great Plains Energy Inc',

    'KATE': 'Kate Spade & Company',

    'CSV': 'Carriage Services, Inc.',

    'ADMS': 'Adamas Pharmaceuticals, Inc.',

    'STAG-B': 'Stag Industrial, Inc.',

    'ENTL': 'Entellus Medical, Inc.',

    'DXYN': 'The Dixie Group, Inc.',

    'WNRL': 'Western Refining Logistics, LP',

    'PKO': 'Pimco Income Opportunity Fund',

    'NBCP': 'NB Capital Acquisition Corp.',

    'LYTS': 'LSI Industries Inc.',

    'TTEK': 'Tetra Tech, Inc.',

    'DKS': 'Dick\'s Sporting Goods Inc',

    'TACOW': 'Del Taco Restaurants, Inc.',

    'CHMT': 'Chemtura Corp.',

    'AGD': 'Alpine Global Dynamic Dividend Fund',

    'PNF': 'PIMCO New York Municipal Income Fund',

    'UCBA': 'United Community Bancorp',

    'PODD': 'Insulet Corporation',

    'AP': 'Ampco-Pittsburgh Corporation',

    'AKR': 'Acadia Realty Trust',

    'CVG': 'Convergys Corporation',

    'CSBK': 'Clifton Bancorp Inc.',

    'UMH-B': 'UMH Properties, Inc.',

    'VZA': 'Verizon Communications Inc.',

    'FF': 'FutureFuel Corp.',

    'UTHR': 'United Therapeutics Corporation',

    'KNDI': 'Kandi Technologies Group, Inc.',

    'CEN': 'Center Coast MLP & Infrastructure Fund',

    'HYB': 'New America High Income Fund, Inc. (The)',

    'FTCS': 'First Trust Capital Strength ETF',

    'TLLP': 'Tesoro Logistics LP',

    'CMP': 'Compass Minerals International, Inc.',

    'MFINL': 'Medallion Financial Corp.',

    'BEAV': 'B/E Aerospace, Inc.',

    'RMP': 'Rice Midstream Partners LP',

    'DLR-E': 'Digital Realty Trust, Inc.',

    'ANET': 'Arista Networks, Inc.',

    'DHIL': 'Diamond Hill Investment Group, Inc.',

    'CVT': 'CVENT, INC.',

    'EACQ': 'Easterly Acquisition Corp.',

    'AMSF': 'AMERISAFE, Inc.',

    'MELI': 'MercadoLibre, Inc.',

    'IMOS': 'ChipMOS TECHNOLOGIES (Bermuda) LTD.',

    'NFEC': 'NF Energy Saving Corporation',

    'MSLI': 'Merus Labs International Inc.',

    'DHG': 'DWS High Income Opportunities Fund, Inc.',

    'GOLD': 'Randgold Resources Limited',

    'CUTR': 'Cutera, Inc.',

    'CASH': 'Meta Financial Group, Inc.',

    'PEP': 'Pepsico, Inc.',

    'REIS': 'Reis, Inc',

    'BWXT': 'BWX Technologies, Inc.',

    'MAC': 'Macerich Company (The)',

    'ECCA': 'Eagle Point Credit Company Inc.',

    'CLS': 'Celestica, Inc.',

    'MORE          ': 'Monogram Residential Trust, Inc.',

    'DAIO': 'Data I/O Corporation',

    'AEPI': 'AEP Industries Inc.',

    'RYAAY': 'Ryanair Holdings plc',

    'AEL': 'American Equity Investment Life Holding Company',

    'CHK-D': 'Chesapeake Energy Corporation',

    'APAM': 'Artisan Partners Asset Management Inc.',

    'LOXO': 'Loxo Oncology, Inc.',

    'BOXC': 'Brookfield Canada Office Properties',

    'HRL': 'Hormel Foods Corporation',

    'DRAD': 'Digirad Corporation',

    'BSPM': 'Biostar Pharmaceuticals, Inc.',

    'CIR': 'CIRCOR International, Inc.',

    'CET': 'Central Securities Corporation',

    'L': 'Loews Corporation',

    'PFBX': 'Peoples Financial Corporation',

    'IPCC': 'Infinity Property and Casualty Corporation',

    'DD-A': 'E.I. du Pont de Nemours and Company',

    'OGEN': 'Oragenics, Inc.',

    'XBIT': 'XBiotech Inc.',

    'RYI': 'Ryerson Holding Corporation',

    'BRK.A': 'Berkshire Hathaway Inc.',

    'WINT': 'Windtree Therapeutics, Inc.',

    'GIMO': 'Gigamon Inc.',

    'TRI': 'Thomson Reuters Corp',

    'XELB': 'Xcel Brands, Inc',

    'BSAC': 'Banco Santander Chile',

    'COF-C': 'Capital One Financial Corporation',

    'HSC': 'Harsco Corporation',

    'FBSS': 'Fauquier Bankshares, Inc.',

    'CAB': 'Cabela\'s Inc',

    'GOF': 'Guggenheim Strategic Opportunities Fund',

    'NRT': 'North European Oil Royality Trust',

    'ANFI': 'Amira Nature Foods Ltd',

    'LNC': 'Lincoln National Corporation',

    'COF.WS': 'Capital One Financial Corporation',

    'VLO': 'Valero Energy Corporation',

    'STRA': 'Strayer Education, Inc.',

    'NC': 'NACCO Industries, Inc.',

    'HPQ': 'HP Inc.',

    'DYN.WS': 'Dynegy Inc.',

    'ZLTQ': 'ZELTIQ Aesthetics, Inc.',

    'GIM': 'Templeton Global Income Fund, Inc.',

    'BNFT': 'Benefitfocus, Inc.',

    'LFVN': 'Lifevantage Corporation',

    'COF': 'Capital One Financial Corporation',

    'CTO': 'Consolidated-Tomoka Land Co.',

    'BSTC': 'BioSpecifics Technologies Corp',

    'PZRX': 'PhaseRx, Inc.',

    'PFNX': 'Pfenex Inc.',

    'ASG': 'Liberty All-Star Growth Fund, Inc.',

    'WFC-Q': 'Wells Fargo & Company',

    'ASB.WS': 'Associated Banc-Corp',

    'GWR': 'Genesee & Wyoming, Inc.',

    'JONE': 'Jones Energy, Inc.',

    'DSPG': 'DSP Group, Inc.',

    'DXPS': 'WisdomTree United Kingdom Hedged Equity Fund',

    'DMD': 'Demand Media Inc.',

    'GNRX': 'VanEck Vectors Generic Drugs ETF',

    'CFA': 'Victory CEMP US 500 Volatility Wtd Index ETF',

    'GWRS': 'Global Water Resources, Inc.',

    'VTWG': 'Vanguard Russell 2000 Growth ETF',

    'CNCR': 'Loncar Cancer Immunotherapy ETF',

    'ASET': 'FlexShares Real Assets Allocation Index Fund',

    'CLIR': 'ClearSign Combustion Corporation',

    'WDC': 'Western Digital Corporation',

    'ARNA': 'Arena Pharmaceuticals, Inc.',

    'UPIP': 'Unwired Planet, Inc.',

    'EAC           ': 'Erickson Incorporated',

    'AAWW': 'Atlas Air Worldwide Holdings',

    'ABR-A': 'Arbor Realty Trust',

    'QSR': 'Restaurant Brands International Inc.',

    'BTZ': 'BlackRock Credit Allocation Income Trust',

    'CAPNW': 'Capnia, Inc.',

    'VNR': 'Vanguard Natural Resources LLC',

    'CELGZ': 'Celgene Corporation',

    'INUV': 'Inuvo, Inc',

    'LBTYK': 'Liberty Global plc',

    'PZZA': 'Papa John\'S International, Inc.',

    'NEM': 'Newmont Mining Corporation',

    'PED': 'Pedevco Corp.',

    'EVY': 'Eaton Vance New York Municipal Income Trust',

    'AIZ': 'Assurant, Inc.',

    'COG': 'Cabot Oil & Gas Corporation',

    'CSAL': 'Communications Sales & Leasing,Inc.',

    'EXAM': 'ExamWorks Group, Inc.',

    'NMRX': 'Numerex Corp.',

    'SIMO': 'Silicon Motion Technology Corporation',

    'BCX': 'BlackRock Resources',

    'TAX': 'Liberty Tax, Inc.',

    'IVC': 'Invacare Corporation',

    'MMV': 'Eaton Vance Massachusetts Municipal Income Trust',

    'HIL': 'Hill International, Inc.',

    'WSTC': 'West Corporation',

    'FAB': 'First Trust Multi Cap Value AlphaDEX Fund',

    'WLL': 'Whiting Petroleum Corporation',

    'DX': 'Dynex Capital, Inc.',

    'DSXN': 'Diana Shipping inc.',

    'RVLT': 'Revolution Lighting Technologies, Inc.',

    'TI': 'Telecom Italia S.P.A.',

    'ARTW': 'Art\'s-Way Manufacturing Co., Inc.',

    'EQGP': 'EQT GP Holdings, LP',

    'BLPH': 'Bellerophon Therapeutics, Inc.',

    'NSTG': 'NanoString Technologies, Inc.',

    'CJES': 'C&J Energy Services, Ltd.',

    'CAMP': 'CalAmp Corp.',

    'AIA': 'iShares Asia 50 ETF',

    'GLP': 'Global Partners LP',

    'VTVT': 'vTv Therapeutics Inc.',

    'PFG': 'Principal Financial Group Inc',

    'GIS': 'General Mills, Inc.',

    'PRZM': 'Prism Technologies Group, Inc.',

    'TFSC': '1347 Capital Corp.',

    'TRMR': 'Tremor Video, Inc.',

    'DTE': 'DTE Energy Company',

    'ICON': 'Iconix Brand Group, Inc.',

    'AHGP': 'Alliance Holdings GP, L.P.',

    'NAD': 'Nuveen Dividend Advantage Municipal Fund',

    'GRSHU': 'Gores Holdings, Inc.',

    'HRS': 'Harris Corporation',

    'PBIB': 'Porter Bancorp, Inc.',

    'DEX': 'Delaware Enhanced Global Dividend',

    'EOD': 'Wells Fargo Global Dividend Opportunity Fund',

    'DTF': 'Duff & Phelps Utilities Tax-Free Income, Inc.',

    'BMLA': 'BullMark LatAm Select Leaders ETF',

    'EVRI': 'Everi Holdings Inc.',

    'USAC': 'USA Compression Partners, LP',

    'PAGG': 'PowerShares Global Agriculture Portfolio',

    'TWI': 'Titan International, Inc.',

    'ROIA': 'Radio One, Inc.',

    'HYI': 'Western Asset High Yield Defined Opportunity Fund Inc.',

    'ISRL': 'Isramco, Inc.',

    'BLOX': 'Infoblox Inc.',

    'PSB-T': 'PS Business Parks, Inc.',

    'QRHC': 'Quest Resource Holding Corporation.',

    'NCT-C': 'Newcastle Investment Corporation',

    'CVM.WS': 'Cel-Sci Corporation',

    'MDCO': 'The Medicines Company',

    'AGO-B': 'Assured Guaranty Ltd.',

    'HMLP': 'Hoegh LNG Partners LP',

    'EFUT': 'eFuture Holding Inc.',

    'XOM': 'Exxon Mobil Corporation',

    'MRCY': 'Mercury Systems Inc',

    'JRS': 'Nuveen Real Estate Fund',

    'NPF': 'Nuveen Premier Municipal Income Fund, Inc.',

    'DERM': 'Dermira, Inc.',

    'BLVDW': 'Boulevard Acquisition Corp. II',

    'BML-L': 'Bank of America Corporation',

    'MBLX': 'Metabolix, Inc.',

    'EVOK': 'Evoke Pharma, Inc.',

    'NTC': 'Nuveen Connecticut Premium Income Municipal Fund',

    'SHEN': 'Shenandoah Telecommunications Co',

    'HBCP': 'Home Bancorp, Inc.',

    'MNR': 'Monmouth Real Estate Investment Corporation',

    'PSCC': 'PowerShares S&P SmallCap Consumer Staples Portfolio',

    'ECAC': 'E-compass Acquisition Corp.',

    'CMPR': 'Cimpress N.V',

    'CENTA': 'Central Garden & Pet Company',

    'RCS': 'PIMCO Strategic Income Fund, Inc.',

    'FIZZ': 'National Beverage Corp.',

    'JJSF': 'J & J Snack Foods Corp.',

    'IBO': 'IBO (Listing Market - NYSE Amex Network B F)',

    'POOL': 'Pool Corporation',

    'IMI': 'Intermolecular, Inc.',

    'HA': 'Hawaiian Holdings, Inc.',

    'AXTI': 'AXT Inc',

    'LGCYP': 'Legacy Reserves LP',

    'FEYE': 'FireEye, Inc.',

    'CNV': 'Cnova N.V.',

    'VLY.WS': 'Valley National Bancorp',

    'ALSN': 'Allison Transmission Holdings, Inc.',

    'BMCH': 'BMC Stock Holdings, Inc.',

    'FAX': 'Aberdeen Asia-Pacific Income Fund Inc',

    'PZG': 'Paramount Gold Nevada Corp.',

    'NEE-H': 'NextEra Energy, Inc.',

    'PLUG': 'Plug Power, Inc.',

    'CMA.WS': 'Comerica Incorporated',

    'RAVN': 'Raven Industries, Inc.',

    'GRVY': 'GRAVITY Co., Ltd.',

    'VKTX': 'Viking Therapeutics, Inc.',

    'SCHW-C': 'The Charles Schwab Corporation',

    'CBSHP': 'Commerce Bancshares, Inc.',

    'HMY': 'Harmony Gold Mining Company Limited',

    'SCQ': 'Stellus Capital Investment Corporation',

    'STXS': 'Stereotaxis, Inc.',

    'GEVO': 'Gevo, Inc.',

    'MWW': 'Monster Worldwide, Inc.',

    'EEFT': 'Euronet Worldwide, Inc.',

    'BABY': 'Natus Medical Incorporated',

    'ENRJ-': 'EnerJex Resources, Inc.',

    'NFG': 'National Fuel Gas Company',

    'CWCO': 'Consolidated Water Co. Ltd.',

    'BNCN': 'BNC Bancorp',

    'GLNG': 'Golar LNG Limited',

    'ACOR': 'Acorda Therapeutics, Inc.',

    'GAB-J': 'Gabelli Equity Trust, Inc. (The)',

    'FOXA': 'Twenty-First Century Fox, Inc.',

    'ADGE': 'American DG Energy Inc.',

    'LIND': 'Lindblad Expeditions Holdings Inc.',

    'WGBS': 'WaferGen Bio-systems, Inc.',

    'AGEN': 'Agenus Inc.',

    'ESS': 'Essex Property Trust, Inc.',

    'ESXB': 'Community Bankers Trust Corporation.',

    'FOR': 'Forestar Group Inc',

    'PSB-V': 'PS Business Parks, Inc.',

    'HBANP': 'Huntington Bancshares Incorporated',

    'OCC': 'Optical Cable Corporation',

    'IGR': 'CBRE Clarion Global Real Estate Income Fund',

    'ACY': 'AeroCentury Corp.',

    'VCF': 'Delaware Investments Colorado Municipal Income Fund, Inc',

    'ACET': 'Aceto Corporation',

    'RPD': 'Rapid7, Inc.',

    'INOD': 'Innodata Inc.',

    'FDS': 'FactSet Research Systems Inc.',

    'FPL': 'First Trust New Opportunities MLP & Energy Fund',

    'FEMB': 'First Trust Emerging Markets Local Currency Bond ETF',

    'HT-D': 'Hersha Hospitality Trust',

    'FTI': 'FMC Technologies, Inc.',

    'PRE-G': 'PartnerRe Ltd.',

    'ROST': 'Ross Stores, Inc.',

    'MSA': 'MSA Safety Incorporporated',

    'KSU': 'Kansas City Southern',

    'SEMG': 'Semgroup Corporation',

    'VHI': 'Valhi, Inc.',

    'XTLB': 'XTL Biopharmaceuticals Ltd.',

    'NEV': 'Nuveen Enhanced Municipal Value Fund',

    'CAA': 'CalAtlantic Group, Inc.',

    'SCE-K': 'Southern California Edison Company',

    'IDA': 'IDACORP, Inc.',

    'FCNCA': 'First Citizens BancShares, Inc.',

    'UDBI': 'Legg Mason US Diversified Core ETF',

    'BME': 'Blackrock Health Sciences Trust',

    'ACCO': 'Acco Brands Corporation',

    'AUPH': 'Aurinia Pharmaceuticals Inc',

    'HIW': 'Highwoods Properties, Inc.',

    'NRO': 'Neuberger Berman Real Estate Securities Income Fund, Inc.',

    'HPJ': 'Highpower International Inc',

    'ZOES': 'Zoe\'s Kitchen, Inc.',

    'PCMI': 'PCM, Inc.',

    'AMC': 'AMC Entertainment Holdings, Inc.',

    'CUR': 'Neuralstem, Inc.',

    'PCG': 'Pacific Gas & Electric Co.',

    'KTWO': 'K2M Group Holdings, Inc.',

    'XTLY': 'Xactly Corporation',

    'STAR-G': 'iStar Financial Inc.',

    'VWR': 'VWR Corporation',

    'WTW': 'Weight Watchers International Inc',

    'MAMS': 'MAM Software Group, Inc.',

    'BPOPM': 'Popular, Inc.',

    'WFT': 'Weatherford International plc',

    'RICK': 'RCI Hospitality Holdings, Inc.',

    'EAGL': 'Double Eagle Acquisition Corp.',

    'PGC': 'Peapack-Gladstone Financial Corporation',

    'SM': 'SM Energy Company',

    'GSB': 'GlobalSCAPE, Inc.',

    'PFS': 'Provident Financial Services, Inc',

    'KS': 'KapStone Paper and Packaging Corporation',

    'PCCC': 'PC Connection, Inc.',

    'EXEL': 'Exelixis, Inc.',

    'INFI': 'Infinity Pharmaceuticals, Inc.',

    'FCE.B': 'Forest City Realty Trust, Inc.',

    'PSA-B': 'Public Storage',

    'LTS-A': 'Ladenburg Thalmann Financial Services Inc',

    'BRX': 'Brixmor Property Group Inc.',

    'DLPH': 'Delphi Automotive plc',

    'SLRC': 'Solar Capital Ltd.',

    'EOT': 'Eaton Vance Municipal Income Trust',

    'BLDR': 'Builders FirstSource, Inc.',

    'CHU': 'China Unicom (Hong Kong) Ltd',

    'AVA': 'Avista Corporation',

    'RGT': 'Royce Global Value Trust, Inc.',

    'PFO': 'Flaherty & Crumrine Preferred Income Opportunity Fund Inc',

    'SGRY': 'Surgery Partners, Inc.',

    'VVI': 'Viad Corp',

    'LFL': 'LATAM Airlines Group S.A.',

    'KMM': 'Scudder Multi-Market Income Trust',

    'IKGH': 'Iao Kun Group Holding Company Limited',

    'STB': 'Student Transportation Inc',

    'AMPE': 'Ampio Pharmaceuticals, Inc.',

    'AMSWA': 'American Software, Inc.',

    'DFP': 'Flaherty & Crumrine Dynamic Preferred and Income Fund Inc.',

    'CAT': 'Caterpillar, Inc.',

    'FARO': 'FARO Technologies, Inc.',

    'NDRM': 'NeuroDerm Ltd.',

    'CLNT': 'Cleantech Solutions International, Inc.',

    'SINA': 'Sina Corporation',

    'KRC': 'Kilroy Realty Corporation',

    'BAC-E': 'Bank of America Corporation',

    'FNHC': 'Federated National Holding Company',

    'CADTW': 'DT Asia Investments Limited',

    'ACRS': 'Aclaris Therapeutics, Inc.',

    'AGN': 'Allergan plc.',

    'UMH': 'UMH Properties, Inc.',

    'GGN-B': 'GAMCO Global Gold, Natural Reources & Income Trust ',

    'TNP-C': 'Tsakos Energy Navigation Ltd',

    'DTYL': 'region',

    'APLE': 'Apple Hospitality REIT, Inc.',

    'SENEB': 'Seneca Foods Corp.',

    'TJX': 'TJX Companies, Inc. (The)',

    'MTN': 'Vail Resorts, Inc.',

    'INDB': 'Independent Bank Corp.',

    'TCPC': 'TCP Capital Corp.',

    'WMS': 'Advanced Drainage Systems, Inc.',

    'BKFS': 'Black Knight Financial Services, Inc.',

    'BV': 'Bazaarvoice, Inc.',

    'AXSM': 'Axsome Therapeutics, Inc.',

    'VNO-I': 'Vornado Realty Trust',

    'TOO-A': 'Teekay Offshore Partners L.P.',

    'KHI': 'Scudder High Income Trust',

    'SBPH': 'Spring Bank Pharmaceuticals, Inc.',

    'EBF': 'Ennis, Inc.',

    'PDVW': 'pdvWireless, Inc.',

    'UBOH': 'United Bancshares, Inc.',

    'MKC.V': 'McCormick & Company, Incorporated',

    'MTSI': 'MACOM Technology Solutions Holdings, Inc.',

    'KLREU': 'KLR Energy Acquisition Corp.',

    'IIJI': 'Internet Initiative Japan, Inc.',

    'AEGR': 'Aegerion Pharmaceuticals, Inc.',

    'VII': 'Vicon Industries, Inc.',

    'GRA': 'W.R. Grace & Co.',

    'FBHS': 'Fortune Brands Home & Security, Inc.',

    'WWE': 'World Wrestling Entertainment, Inc.',

    'LEN': 'Lennar Corporation',

    'SAP': 'SAP SE',

    'ADRE': 'BLDRS Emerging Markets 50 ADR Index Fund',

    'BIOA': 'BioAmber Inc.',

    'JSYNU': 'Jensyn Acquistion Corp.',

    'WPCS': 'WPCS International Incorporated',

    'AMRC': 'Ameresco, Inc.',

    'CMRX': 'Chimerix, Inc.',

    'BML-H': 'Bank of America Corporation',

    'MHD': 'Blackrock MuniHoldings Fund, Inc.',

    'FLN': 'First Trust Latin America AlphaDEX Fund',

    'ISDR': 'Issuer Direct Corporation',

    'TTS': 'Tile Shop Hldgs, Inc.',

    'PLPC': 'Preformed Line Products Company',

    'KMPA': 'Kemper Corporation',

    'UBIO': 'Proshares UltraPro Nasdaq Biotechnology',

    'HE': 'Hawaiian Electric Industries, Inc.',

    'ASB-C': 'Associated Banc-Corp',

    'WOOF': 'VCA Inc. ',

    'DSU': 'Blackrock Debt Strategies Fund, Inc.',

    'HOMB': 'Home BancShares, Inc.',

    'TANO': 'TravelCenters of America LLC',

    'USLV': 'region',

    'FLT': 'FleetCor Technologies, Inc.',

    'IMN': 'Imation Corporation',

    'BGNE': 'BeiGene, Ltd.',

    'PRAN': 'Prana Biotechnology Ltd',

    'FPT': 'Federated Premier Intermediate Municipal Income Fund',

    'JCE': 'Nuveen Core Equity Alpha Fund',

    'PWE': 'Penn West Petroleum Ltd',

    'SONS': 'Sonus Networks, Inc.',

    'TAC': 'TransAlta Corporation',

    'CATM': 'Cardtronics, Inc.',

    'MSBF': 'MSB Financial Corp.',

    'MSB': 'Mesabi Trust',

    'NUE': 'Nucor Corporation',

    'JTD': 'Nuveen Tax-Advantaged Dividend Growth Fund',

    'LOGI': 'Logitech International S.A.',

    'SBH': 'Sally Beauty Holdings, Inc.',

    'CLSN': 'Celsion Corporation',

    'SRF': 'Cushing Energy Income Fund (The)',

    'SNDX': 'Syndax Pharmaceuticals, Inc.',

    'TMO': 'Thermo Fisher Scientific Inc',

    'REPH': 'Recro Pharma, Inc.',

    'MFNC': 'Mackinac Financial Corporation',

    'TFX': 'Teleflex Incorporated',

    'SOL': 'Renesola Ltd.',

    'SO': 'Southern Company (The)',

    'ENS': 'Enersys',

    'COR': 'CoreSite Realty Corporation',

    'SEP': 'Spectra Energy Partners, LP',

    'CAE': 'CAE Inc',

    'MBUU': 'Malibu Boats, Inc.',

    'CARV': 'Carver Bancorp, Inc.',

    'GV': 'Goldfield Corporation (The)',

    'KODK.WS': 'Eastman Kodak Company',

    'PSB': 'PS Business Parks, Inc.',

    'MPA': 'Blackrock MuniYield Pennsylvania Quality Fund',

    'ASB': 'Associated Banc-Corp',

    'PTEN': 'Patterson-UTI Energy, Inc.',

    'GLDD': 'Great Lakes Dredge & Dock Corporation',

    'LXP': 'Lexington Realty Trust',

    'HSON': 'Hudson Global, Inc.',

    'CNCO': 'Cencosud S.A.',

    'AMCO': 'Armco Metals Holdings, Inc.',

    'AGRO': 'Adecoagro S.A.',

    'DAL': 'Delta Air Lines, Inc.',

    'CDOR': 'Condor Hospitality Trust, Inc.',

    'BIOL': 'Biolase, Inc.',

    'CSH': 'Cash America International, Inc.',

    'BMRN': 'BioMarin Pharmaceutical Inc.',

    'CG': 'The Carlyle Group L.P.',

    'AMBC': 'Ambac Financial Group, Inc.',

    'STI-A': 'SunTrust Banks, Inc.',

    'CUO': 'Continental Materials Corporation',

    'BAS': 'Basic Energy Services, Inc.',

    'ZHNE': 'Zhone Technologies, Inc.',

    'KW': 'Kennedy-Wilson Holdings Inc.',

    'SYMC': 'Symantec Corporation',

    'ENT': 'Global Eagle Entertainment Inc.',

    'CCI-A': 'Crown Castle International Corporation',

    'BSM': 'Black Stone Minerals, L.P.',

    'PTNR': 'Partner Communications Company Ltd.',

    'MUA': 'Blackrock MuniAssets Fund, Inc.',

    'DHI': 'D.R. Horton, Inc.',

    'NXP': 'Nuveen Select Tax Free Income Portfolio',

    'MEN': 'Blackrock MuniEnhanced Fund, Inc.',

    'TRR': 'TRC Companies, Inc.',

    'ENIC': 'Enersis Chile S.A.',

    'ROG': 'Rogers Corporation',

    'CFBK': 'Central Federal Corporation',

    'STEM': 'StemCells, Inc.',

    'MELR': 'Melrose Bancorp, Inc.',

    'GIB': 'CGI Group, Inc.',

    'QQXT': 'First Trust NASDAQ-100 Ex-Technology Sector Index Fund',

    'ABBV': 'AbbVie Inc.',

    'IRDM': 'Iridium Communications Inc',

    'TKAI': 'Tokai Pharmaceuticals, Inc.',

    'NEE-Q': 'NextEra Energy, Inc.',

    'HEI.A': 'Heico Corporation',

    'IVR-B': 'INVESCO MORTGAGE CAPITAL INC',

    'RDVY': 'First Trust NASDAQ Rising Dividend Achievers ETF',

    'ACPW': 'Active Power, Inc.',

    'PBSK': 'Poage Bankshares, Inc.',

    'NEA': 'Nuveen AMT-Free Municipal Income Fund',

    'IBP': 'Installed Building Products, Inc.',

    'MRK': 'Merck & Company, Inc.',

    'PTC': 'PTC Inc.',

    'IGC': 'India Globalization Capital Inc.',

    'MUX': 'McEwen Mining Inc.',

    'ENZL': 'iShares MSCI New Zealand Capped ETF',

    'LPL': 'LG Display Co., Ltd.',

    'JPM-F': 'J P Morgan Chase & Co',

    'SYPR': 'Sypris Solutions, Inc.',

    'MBFI': 'MB Financial Inc.',

    'ABCB': 'Ameris Bancorp',

    'BMTC': 'Bryn Mawr Bank Corporation',

    'IIVI': 'II-VI Incorporated',

    'ALLT': 'Allot Communications Ltd.',

    'GVA': 'Granite Construction Incorporated',

    'FCPT': 'Four Corners Property Trust, Inc.',

    'PPHM': 'Peregrine Pharmaceuticals Inc.',

    'ICCC': 'ImmuCell Corporation',

    'NOV': 'National Oilwell Varco, Inc.',

    'RRGB': 'Red Robin Gourmet Burgers, Inc.',

    'MLNX': 'Mellanox Technologies, Ltd.',

    'GLMD': 'Galmed Pharmaceuticals Ltd.',

    'CRBP': 'Corbus Pharmaceuticals Holdings, Inc.',

    'VGI': 'Virtus Global Multi-Sector Income Fund',

    'NYT': 'New York Times Company (The)',

    'SSNC': 'SS&C Technologies Holdings, Inc.',

    'IRBT': 'iRobot Corporation',

    'KOOL': 'Cesca Therapeutics Inc.',

    'OTIV': 'On Track Innovations Ltd',

    'SFLY': 'Shutterfly, Inc.',

    'TXRH': 'Texas Roadhouse, Inc.',

    'HLT': 'Hilton Worldwide Holdings Inc.',

    'KIN': 'Kindred Biosciences, Inc.',

    'DHRM': 'Dehaier Medical Systems Limited',

    'RVNC': 'Revance Therapeutics, Inc.',

    'SON': 'Sonoco Products Company',

    'ESE': 'ESCO Technologies Inc.',

    'EGLE': 'Eagle Bulk Shipping Inc.',

    'SERV': 'ServiceMaster Global Holdings, Inc.',

    'NBO': 'Neuberger Berman New York Intermediate Municipal Fund Inc.',

    'CLC': 'CLARCOR Inc.',

    'UNM': 'Unum Group',

    'PSA-T': 'Public Storage',

    'LB': 'L Brands, Inc.',

    'MBI': 'MBIA, Inc.',

    'AMH-C': 'American Homes 4 Rent',

    'GNVC': 'GenVec, Inc.',

    'DE': 'Deere & Company',

    'VEEV': 'Veeva Systems Inc.',

    'WAT': 'Waters Corporation',

    'FFG': 'FBL Financial Group, Inc.',

    'SIM': 'Grupo Simec, S.A. de C.V.',

    'ASTC': 'Astrotech Corporation',

    'AVK': 'Advent Claymore Convertible Securities and Income Fund',

    'JPM-G': 'J P Morgan Chase & Co',

    'BKH': 'Black Hills Corporation',

    'ALB': 'Albemarle Corporation',

    'WFC-L': 'Wells Fargo & Company',

    'FTK': 'Flotek Industries, Inc.',

    'KKR-A': 'KKR & Co. L.P.',

    'EMXX': 'Eurasian Minerals Inc.',

    'CVS': 'CVS Health Corporation',

    'UNTY': 'Unity Bancorp, Inc.',

    'CSS': 'CSS Industries, Inc.',

    'CBK': 'Christopher & Banks Corporation',

    'CCP': 'Care Capital Properties, Inc.',

    'SRSC': 'Sears Canada Inc. ',

    'ALL-D': 'Allstate Corporation (The)',

    'EPM-A': 'Evolution Petroleum Corporation, Inc.',

    'HIE': 'Miller/Howard High Income Equity Fund',

    'AEH': 'Aegon NV',

    'COE': 'China Online Education Group',

    'VICR': 'Vicor Corporation',

    'MGU': 'Macquarie Global Infrastructure Total Return Fund Inc.',

    'USAK': 'USA Truck, Inc.',

    'VGM': 'Invesco Trust for Investment Grade Municipals',

    'PGRE': 'Paramount Group, Inc.',

    'GUT-C': 'Gabelli Utility Trust (The)',

    'GNL': 'Global Net Lease, Inc.',

    'LMAT': 'LeMaitre Vascular, Inc.',

    'MFV': 'MFS Special Value Trust',

    'PFK': 'Prudential Financial, Inc.',

    'SGA': 'Saga Communications, Inc.',

    'IR': 'Ingersoll-Rand plc (Ireland)',

    'EXCU': 'Exelon Corporation',

    'SRCLP': 'Stericycle, Inc.',

    'MOBI': 'Sky-mobi Limited',

    'COOL': 'Majesco Entertainment Company',

    'VONG': 'Vanguard Russell 1000 Growth ETF',

    'AMSG': 'Amsurg Corp.',

    'SNBC': 'Sun Bancorp, Inc.',

    'BWEN': 'Broadwind Energy, Inc.',

    'STRT': 'Strattec Security Corporation',

    'HF': 'HFF, Inc.',

    'BIP': 'Brookfield Infrastructure Partners LP',

    'JGW': 'J.G. Wentworth Company (The)',

    'BBT': 'BB&T Corporation',

    'TCFC': 'The Community Financial Corporation',

    'CTBI': 'Community Trust Bancorp, Inc.',

    'UFS': 'Domtar Corporation',

    'BMI': 'Badger Meter, Inc.',

    'BKEPP': 'Blueknight Energy Partners L.P., L.L.C.',

    'PRFZ': 'PowerShares FTSE RAFI US 1500 Small-Mid Portfolio',

    'SKOR': 'FlexShares Credit-Scored US Corporate Bond Index Fund',

    'EIV': 'Eaton Vance Municipal Bond Fund II',

    'LYG': 'Lloyds Banking Group Plc',

    'CENX': 'Century Aluminum Company',

    'NTGR': 'NETGEAR, Inc.',

    'RPM': 'RPM International Inc.',

    'EC': 'Ecopetrol S.A.',

    'HPF': 'John Hancock Pfd Income Fund II',

    'FISV': 'Fiserv, Inc.',

    'APRI': 'Apricus Biosciences, Inc',

    'HGT': 'Hugoton Royalty Trust',

    'HSBC-A': 'HSBC Holdings plc',

    'HUSI-G.CL': 'HSBC USA, Inc.',

    'HJV': 'MS Structured Asset Corp Saturns GE Cap Corp Series 2002-14',

    'UAE': 'iShares MSCI UAE Capped ETF',

    'RPT': 'Ramco-Gershenson Properties Trust',

    'ROIC': 'Retail Opportunity Investments Corp.',

    'ARCX': 'Arc Logistic Partners LP',

    'STON': 'StoneMor Partners L.P.',

    'JMP': 'JMP Group LLC',

    'CPRX': 'Catalyst Pharmaceuticals, Inc.',

    'AAXJ': 'iShares MSCI All Country Asia ex Japan Index Fund',

    'LPSN': 'LivePerson, Inc.',

    'AIMC': 'Altra Industrial Motion Corp.',

    'RENX': 'RELX N.V.',

    'RFT': 'RAIT Financial Trust',

    'MDVXW': 'Medovex Corp.',

    'DL': 'China Distance Education Holdings Limited',

    'PSXP': 'Phillips 66 Partners LP',

    'PEI-B': 'Pennsylvania Real Estate Investment Trust',

    'ACHC': 'Acadia Healthcare Company, Inc.',

    'CMLS': 'Cumulus Media Inc.',

    'NW-C': 'Natl Westminster Pfd',

    'EVER': 'EverBank Financial Corp.',

    'GAINO': 'Gladstone Investment Corporation',

    'DGI': 'DigitalGlobe, Inc',

    'AWR': 'American States Water Company',

    'LMNX': 'Luminex Corporation',

    'MTRX': 'Matrix Service Company',

    'GABC': 'German American Bancorp, Inc.',

    'BEP': 'Brookfield Renewable Partners L.P.',

    'CSTE': 'CaesarStone Sdot-Yam Ltd.',

    'MHE': 'BlackRock Massachusetts Tax-Exempt Trust',

    'USPH': 'U.S. Physical Therapy, Inc.',

    'BNK': 'C1 Financial, Inc.',

    'CXSE': 'WisdomTree China ex-State-Owned Enterprises Fund',

    'BPY': 'Brookfield Property Partners L.P.',

    'BBC': 'BioShares Biotechnology Clinical Trials Fund',

    'CGIX': 'Cancer Genetics, Inc.',

    'BAK': 'Braskem S.A.',

    'PLT': 'Plantronics, Inc.',

    'WHLR': 'Wheeler Real Estate Investment Trust, Inc.',

    'AMFW': 'Amec Plc Ord',

    'NVR': 'NVR, Inc.',

    'OCUL': 'Ocular Therapeutix, Inc.',

    'TU': 'TELUS Corporation',

    'NXTM': 'NxStage Medical, Inc.',

    'VRNS': 'Varonis Systems, Inc.',

    'NNDM': 'Nano Dimension Ltd.',

    'SUMR': 'Summer Infant, Inc.',

    'HL-B': 'Hecla Mining Company',

    'SVA': 'Sinovac Biotech, Ltd.',

    'FMER': 'FirstMerit Corporation',

    'RRM': 'RR Media Ltd.',

    'AMOT': 'Allied Motion Technologies, Inc.',

    'DWAT': 'Arrow DWA Tactical ETF',

    'XPL': 'Solitario Exploration & Royalty Corp',

    'NRE': 'NorthStar Realty Europe Corp.',

    'CMFN': 'CM Finance Inc',

    'LNC.WS': 'Lincoln National Corporation',

    'PRE-D': 'PartnerRe Ltd.',

    'SWHC': 'Smith & Wesson Holding Corporation',

    'GPIAU': 'GP Investments Acquisition Corp.',

    'CINF': 'Cincinnati Financial Corporation',

    'ALN': 'American Lorain Corporation',

    'MRVL': 'Marvell Technology Group Ltd.',

    'AUBN': 'Auburn National Bancorporation, Inc.',

    'NVDQ': 'Novadaq Technologies Inc',

    'HBM.WS': 'HudBay Minerals Inc',

    'CMRE-C': 'Costamare Inc.',

    'MMM': '3M Company',

    'VAC': 'Marriot Vacations Worldwide Corporation',

    'TCB-B': 'TCF Financial Corporation',

    'SPNC': 'The Spectranetics Corporation',

    'ALCO': 'Alico, Inc.',

    'UBSI': 'United Bankshares, Inc.',

    'COF-D': 'Capital One Financial Corporation',

    'CIX': 'CompX International Inc.',

    'AGZD': 'WisdomTree Barclays U.S. Aggregate Bond Zero Duration Fund',

    'BDE': 'Black Diamond, Inc.',

    'HBK': 'Hamilton Bancorp, Inc.',

    'UBCP': 'United Bancorp, Inc.',

    'PRGS': 'Progress Software Corporation',

    'GENE': 'Genetic Technologies Ltd',

    'CERE': 'Ceres, Inc.',

    'HAE': 'Haemonetics Corporation',

    'SUPV': 'Grupo Supervielle S.A.',

    'NIHD': 'NII Holdings, Inc.',

    'EMC': 'EMC Corporation',

    'JPS': 'Nuveen Quality Preferred Income Fund 2',

    'RSPP': 'RSP Permian, Inc.',

    'RRC': 'Range Resources Corporation',

    'EPR-C': 'EPR Properties',

    'SOHOM': 'Sotherly Hotels LP',

    'ARE': 'Alexandria Real Estate Equities, Inc.',

    'ADPT': 'Adeptus Health Inc.',

    'FYX': 'First Trust Small Cap Core AlphaDEX Fund',

    'LBF': 'Scudder Global High Income Fund, Inc.',

    'DXGE': 'WisdomTree Germany Hedged Equity Fund',

    'EXR': 'Extra Space Storage Inc',

    'PSIX': 'Power Solutions International, Inc.',

    'CCRN': 'Cross Country Healthcare, Inc.',

    'NRF-A': 'Northstar Realty Finance Corp.',

    'CTMX': 'CytomX Therapeutics, Inc.',

    'HTBI': 'HomeTrust Bancshares, Inc.',

    'D': 'Dominion Resources, Inc.',

    'PXLW': 'Pixelworks, Inc.',

    'CMU': 'Colonial Municipal Income Trust',

    'BVA': 'Cordia Bancorp Inc.',

    'PBCT': 'People\'s United Financial, Inc.',

    'ARP-E': 'Atlas Resource Partners, L.P.',

    'VTHR': 'Vanguard Russell 3000 ETF',

    'CNMD': 'CONMED Corporation',

    'PX': 'Praxair, Inc.',

    'FIF': 'First Trust Energy Infrastructure Fund',

    'GLU-A': 'The Gabelli Global Utility and Income Trust',

    'DIN': 'DineEquity, Inc',

    'TVIA': 'TerraVia Holdings, Inc.',

    'LGI': 'Lazard Global Total Return and Income Fund',

    'LEE': 'Lee Enterprises, Incorporated',

    'PENN': 'Penn National Gaming, Inc.',

    'NVET': 'Nexvet Biopharma plc',

    'CTRE': 'CareTrust REIT, Inc.',

    'GCV-B': 'Gabelli Convertible and Income Securities Fund, Inc. (The)',

    'TR': 'Tootsie Roll Industries, Inc.',

    'NATH': 'Nathan\'s Famous, Inc.',

    'CBI': 'Chicago Bridge & Iron Company N.V.',

    'ITC': 'ITC Holdings Corp.',

    'EFSC': 'Enterprise Financial Services Corporation',

    'PPS-A': 'Post Properties, Inc.',

    'ACTA': 'Actua Corporation',

    'OXBR': 'Oxbridge Re Holdings Limited',

    'WRB': 'W.R. Berkley Corporation',

    'GILT': 'Gilat Satellite Networks Ltd.',

    'GWPH': 'GW Pharmaceuticals Plc',

    'NE': 'Noble Corporation',

    'LCM': 'Advent/Claymore Enhanced Growth & Income Fund',

    'HMTV': 'Hemisphere Media Group, Inc.',

    'SCON': 'Superconductor Technologies Inc.',

    'ACRE': 'Ares Commercial Real Estate Corporation',

    'CLNE': 'Clean Energy Fuels Corp.',

    'GGACW': 'Garnero Group Acquisition Company',

    'SCZ': 'iShares MSCI EAFE Small-Cap ETF',

    'KODK': 'Eastman Kodak Company',

    'ADX': 'Adams Diversified Equity Fund, Inc.',

    'NTP': 'Nam Tai Property Inc.',

    'INS': 'Intelligent Systems Corporation',

    'HD': 'Home Depot, Inc. (The)',

    'TRUP': 'Trupanion, Inc.',

    'GRX': 'The Gabelli Healthcare & Wellness Trust',

    'MP-D': 'Mississippi Power Company',

    'ADMP': 'Adamis Pharmaceuticals Corporation',

    'WTI': 'W&T Offshore, Inc.',

    'DIS': 'Walt Disney Company (The)',

    'RFEU': 'First Trust RiverFront Dynamic Europe ETF',

    'CADTU': 'DT Asia Investments Limited',

    'VTWO': 'Vanguard Russell 2000 ETF',

    'UTSI': 'UTStarcom Holdings Corp',

    'XPO': 'XPO Logistics, Inc.',

    'WGA': 'AG&E Holdings, Inc.',

    'PSA': 'Public Storage',

    'CLACW': 'Capitol Acquisition Corp. III',

    'HSFC-B.CL': 'Household Finance Corp',

    'WSM': 'Williams-Sonoma, Inc.',

    'OSM': 'SLM Corporation',

    'JXSB': 'Jacksonville Bancorp Inc.',

    'RHT': 'Red Hat, Inc.',

    'GTT': 'GTT Communications, Inc.',

    'STZ.B': 'Constellation Brands Inc',

    'CRI': 'Carter\'s, Inc.',

    'MSON': 'MISONIX, Inc.',

    'LKQ': 'LKQ Corporation',

    'USDP': 'USD Partners LP',

    'TNGO': 'Tangoe, Inc.',

    'OLD': 'The Long-Term Care ETF',

    'MAPI': 'Mapi - Pharma Ltd.',

    'DEPO': 'Depomed, Inc.',

    'ALDW': 'Alon USA Partners, LP',

    'EPM': 'Evolution Petroleum Corporation, Inc.',

    'CAL': 'Caleres, Inc.',

    'CNET': 'ChinaNet Online Holdings, Inc.',

    'USAP': 'Universal Stainless & Alloy Products, Inc.',

    'CNC': 'Centene Corporation',

    'SPRT': 'support.com, Inc.',

    'CDNA': 'CareDx, Inc.',

    'JTPY': 'JetPay Corporation',

    'AFC': 'Ares Capital Corporation',

    'DGLY': 'Digital Ally, Inc.',

    'MAUI': 'AdvisorShares Market Adaptive Unconstrained Income ETF',

    'PVTD': 'PrivateBancorp, Inc.',

    'FDTS': 'First Trust Developed Markets ex-US Small Cap AlphaDEX Fund',

    'WERN': 'Werner Enterprises, Inc.',

    'TEP': 'Tallgrass Energy Partners, LP',

    'NAP': 'Navios Maritime Midstream Partners LP',

    'SJR': 'Shaw Communications Inc.',

    'CTHR': 'Charles & Colvard Ltd',

    'ITEK': 'Inotek Pharmaceuticals Corporation',

    'FNTCW': 'FinTech Acquisition Corp.',

    'MOFG': 'MidWestOne Financial Group, Inc.',

    'ABX': 'Barrick Gold Corporation',

    'TROW': 'T. Rowe Price Group, Inc.',

    'GTWN': 'Georgetown Bancorp, Inc.',

    'PACE': 'Pace Holdings Corp.',

    'LEJU': 'Leju Holdings Limited',

    'NM-G': 'Navios Maritime Holdings Inc.',

    'BBDO': 'Banco Bradesco Sa',

    'NIM': 'Nuveen Select Maturities Municipal Fund',

    'BX': 'The Blackstone Group L.P.',

    'BLH': 'Blackrock New York Municipal 2018 Term Trust',

    'SWM': 'Schweitzer-Mauduit International, Inc.',

    'SGYPW': 'Synergy Pharmaceuticals, Inc.',

    'USG': 'USG Corporation',

    'HWBK': 'Hawthorn Bancshares, Inc.',

    'HSIC': 'Henry Schein, Inc.',

    'STO': 'Statoil ASA',

    'DTQ': 'DTE Energy Company',

    'RSYS': 'RadiSys Corporation',

    'LNG': 'Cheniere Energy, Inc.',

    'IHG': 'Intercontinental Hotels Group',

    'EVHC': 'Envision Healthcare Holdings, Inc.',

    'KMI-A': 'Kinder Morgan, Inc.',

    'STT-G': 'State Street Corporation',

    'RESN': 'Resonant Inc.',

    'SONA': 'Southern National Bancorp of Virginia, Inc.',

    'LKFN': 'Lakeland Financial Corporation',

    'RF-B': 'Regions Financial Corporation',

    'BIF': 'USLIFE Income Fund, Inc.',

    'GS-I': 'Goldman Sachs Group, Inc. (The)',

    'MON': 'Monsanto Company',

    'VTGN': 'VistaGen Therapeutics, Inc.',

    'SEB': 'Seaboard Corporation',

    'PL-C': 'Protective Life Corporation',

    'SKM': 'SK Telecom Co., Ltd.',

    'EZPW': 'EZCORP, Inc.',

    'CBF': 'Capital Bank Financial Corp.',

    'CROX': 'Crocs, Inc.',

    'RBC': 'Regal Beloit Corporation',

    'ARCO': 'Arcos Dorados Holdings Inc.',

    'TANP': 'TravelCenters of America LLC',

    'ZB-F': 'Zions Bancorporation',

    'WLDN': 'Willdan Group, Inc.',

    'MHGC': 'Morgans Hotel Group Co.',

    'NORD': 'Nord Anglia Education, Inc.',

    'REG-G': 'Regency Centers Corporation',

    'ARP-D': 'Atlas Resource Partners, L.P.',

    'FOLD': 'Amicus Therapeutics, Inc.',

    'AXLL': 'Axiall Corporation',

    'HMN': 'Horace Mann Educators Corporation',

    'GAIN': 'Gladstone Investment Corporation',

    'FNCX': 'Function(x) Inc.',

    'UNFI': 'United Natural Foods, Inc.',

    'WBMD': 'WebMD Health Corp',

    'BONT': 'The Bon-Ton Stores, Inc.',

    'FSBW': 'FS Bancorp, Inc.',

    'LEG': 'Leggett & Platt, Incorporated',

    'BHV': 'BlackRock Virginia Municipal Bond Trust',

    'MRCC': 'Monroe Capital Corporation',

    'CSBR': 'Champions Oncology, Inc.',

    'CDL': 'Victory CEMP US Large Cap High Div Volatility Wtd Index ETF',

    'FCFS': 'First Cash Financial Services, Inc.',

    'MTD': 'Mettler-Toledo International, Inc.',

    'COLM': 'Columbia Sportswear Company',

    'INVE': 'Identiv, Inc.',

    'APOL': 'Apollo Education Group, Inc.',

    'XENE': 'Xenon Pharmaceuticals Inc.',

    'ESIO': 'Electro Scientific Industries, Inc.',

    'PSA-X': 'Public Storage',

    'CHSCN': 'CHS Inc',

    'KRC-G': 'Kilroy Realty Corporation',

    'RLOC': 'ReachLocal, Inc.',

    'KGJI': 'Kingold Jewelry Inc.',

    'QADB': 'QAD Inc.',

    'DOW': 'Dow Chemical Company (The)',

    'UNXL': 'Uni-Pixel, Inc.',

    'EURN': 'Euronav NV',

    'IQI': 'Invesco Quality Municipal Income Trust',

    'ATI': 'Allegheny Technologies Incorporated',

    'TEO': 'Telecom Argentina Stet - France Telecom S.A.',

    'EVF': 'Eaton Vance Senior Income Trust',

    'JRO': 'Nuveen Floating Rate Income Opportuntiy Fund',

    'DDT': 'Dillard\'s, Inc.',

    'VEC': 'Vectrus, Inc.',

    'KBAL': 'Kimball International, Inc.',

    'AIG.WS': 'American International Group, Inc.',

    'GLRE': 'Greenlight Reinsurance, Ltd.',

    'SF': 'Stifel Financial Corporation',

    'JOUT': 'Johnson Outdoors Inc.',

    'AMCN': 'AirMedia Group Inc',

    'FFA': 'First Trust',

    'IPCI': 'Intellipharmaceutics International Inc.',

    'ABEO': 'Abeona Therapeutics Inc.',

    'WFC-V': 'Wells Fargo & Company',

    'THO': 'Thor Industries, Inc.',

    'NRF': 'Northstar Realty Finance Corp.',

    'X': 'United States Steel Corporation',

    'CPPL': 'Columbia Pipeline Partners LP',

    'DFT-B.CL': 'Dupont Fabros Technology, Inc.',

    'BSE': 'Blackrock New York Municipal Income Quality Trust',

    'OZM': 'Och-Ziff Capital Management Group LLC',

    'REN           ': 'Resolute Energy Corporation',

    'SCX': 'L.S. Starrett Company (The)',

    'LQDT': 'Liquidity Services, Inc.',

    'OMCL': 'Omnicell, Inc.',

    'CTAS': 'Cintas Corporation',

    'YUMA-A': 'Yuma Energy, Inc.',

    'FNB': 'F.N.B. Corporation',

    'STAR-E': 'iStar Financial Inc.',

    'KAR': 'KAR Auction Services, Inc',

    'FORTY': 'Formula Systems (1985) Ltd.',

    'MIE': 'Cohen & Steers MLP Income and Energy Opportunity Fund, Inc.',

    'FDIV': 'First Trust Strategic Income ETF',

    'PBR.A': 'Petroleo Brasileiro S.A.- Petrobras',

    'NML': 'Neuberger Berman MLP Income Fund Inc.',

    'GGG': 'Graco Inc.',

    'ALV': 'Autoliv, Inc.',

    'ZPIN': 'Zhaopin Limited',

    'GFY': 'Western Asset Variable Rate Strategic Fund Inc.',

    'NSYS': 'Nortech Systems Incorporated',

    'MGF': 'MFS Government Markets Income Trust',

    'HALL': 'Hallmark Financial Services, Inc.',

    'DPM': 'DCP Midstream Partners, LP',

    'SB-D': 'Safe Bulkers, Inc',

    'CACC': 'Credit Acceptance Corporation',

    'RDCM': 'Radcom Ltd.',

    'ORPN': 'Bio Blast Pharma Ltd.',

    'CMRE': 'Costamare Inc.',

    'DSW': 'DSW Inc.',

    'GFNCP': 'General Finance Corporation',

    'QTNT': 'Quotient Limited',

    'VDSI': 'VASCO Data Security International, Inc.',

    'BAC.WS.B': 'Bank of America Corporation',

    'PM': 'Philip Morris International Inc',

    'BSRR': 'Sierra Bancorp',

    'MBRX': 'Moleculin Biotech, Inc.',

    'JPM-H': 'J P Morgan Chase & Co',

    'MPAA': 'Motorcar Parts of America, Inc.',

    'SFS': 'Smart',

    'MLNK': 'ModusLink Global Solutions, Inc',

    'FSB': 'Franklin Financial Network, Inc.',

    'EVJ': 'Eaton Vance New Jersey Municipal Income Trust',

    'GCTS': 'GCT Semiconductor, Inc.',

    'HIG': 'Hartford Financial Services Group, Inc. (The)',

    'XRDC': 'Crossroads Capital, Inc.',

    'CVLT': 'CommVault Systems, Inc.',

    'DSE': 'Duff & Phelps Select Energy MLP Fund Inc.',

    'SAIC': 'SCIENCE APPLICATIONS INTERNATIONAL CORPORATION',

    'SPAN': 'Span-America Medical Systems, Inc.',

    'CTY': 'Qwest Corporation',

    'ISIL': 'Intersil Corporation',

    'MAIN': 'Main Street Capital Corporation',

    'RCI': 'Rogers Communication, Inc.',

    'BOFI': 'BofI Holding, Inc.',

    'MSBI': 'Midland States Bancorp, Inc.',

    'AUMAW': 'AR Capital Acquisition Corp.',

    'TGI': 'Triumph Group, Inc.',

    'TAPR': 'region',

    'MYE': 'Myers Industries, Inc.',

    'KIRK': 'Kirkland\'s, Inc.',

    'FHN': 'First Horizon National Corporation',

    'DST': 'DST Systems, Inc.',

    'DAC': 'Danaos Corporation',

    'BNDX': 'Vanguard Total International Bond ETF',

    'WWW': 'Wolverine World Wide, Inc.',

    'NWE': 'NorthWestern Corporation',

    'PSEC': 'Prospect Capital Corporation',

    'PSG': 'Performance Sports Group Ltd',

    'FISI': 'Financial Institutions, Inc.',

    'NLNK': 'NewLink Genetics Corporation',

    'PAM': 'Pampa Energia S.A.',

    'LHO-J': 'LaSalle Hotel Properties',

    'AFSI-B': 'AmTrust Financial Services, Inc.',

    'CAI': 'CAI International, Inc.',

    'SKUL': 'Skullcandy, Inc.',

    'MOS': 'Mosaic Company (The)',

    'FLAG': 'WeatherStorm Forensic Accounting Long Short ETF',

    'IBKC': 'IBERIABANK Corporation',

    'CGNT': 'Cogentix Medical, Inc.',

    'CSWC': 'Capital Southwest Corporation',

    'AJX': 'Great Ajax Corp.',

    'EDR': 'Education Realty Trust Inc.',

    'PSA-V': 'Public Storage',

    'PTLA': 'Portola Pharmaceuticals, Inc.',

    'ISP': 'ING Group, N.V.',

    'FSP': 'Franklin Street Properties Corp.',

    'INTT': 'inTest Corporation',

    'WU': 'Western Union Company (The)',

    'SDR': 'SandRidge Mississippian Trust II',

    'ACAD': 'ACADIA Pharmaceuticals Inc.',

    'HVT': 'Haverty Furniture Companies, Inc.',

    'ELEC': 'Electrum Special Acquisition Corporation',

    'BBH': 'VanEck Vectors Biotech ETF',

    'WTS': 'Watts Water Technologies, Inc.',

    'VLGEA': 'Village Super Market, Inc.',

    'DPRX': 'Dipexium Pharmaceuticals, Inc.',

    'NJV': 'Nuveen New Jersey Municipal Value Fund',

    'GPACW': 'Global Partner Acquisition Corp.',

    'FLXS': 'Flexsteel Industries, Inc.',

    'NQM': 'Nuveen Investment Quality Municipal Fund, Inc.',

    'GMAN': 'Gordmans Stores, Inc.',

    'OXY': 'Occidental Petroleum Corporation',

    'EA': 'Electronic Arts Inc.',

    'DEL': 'Deltic Timber Corporation',

    'BCLI': 'Brainstorm Cell Therapeutics Inc.',

    'PSB-U': 'PS Business Parks, Inc.',

    'DPW': 'Digital Power Corporation',

    'FEN': 'First Trust Energy Income and Growth Fund',

    'HTGZ': 'Hercules Capital, Inc.',

    'XRX': 'Xerox Corporation',

    'USFD': 'US Foods Holding Corp.',

    'MORN': 'Morningstar, Inc.',

    'LYB': 'LyondellBasell Industries NV',

    'GE': 'General Electric Company',

    'LSXMB': 'Liberty Media Corporation',

    'LPG': 'Dorian LPG Ltd.',

    'CFRX': 'ContraFect Corporation',

    'LPNT': 'LifePoint Health, Inc.',

    'REGI': 'Renewable Energy Group, Inc.',

    'CRDT': 'WisdomTree Strategic Corporate Bond Fund',

    'IFV': 'First Trust Dorsey Wright International Focus 5 ETF',

    'AGCO': 'AGCO Corporation',

    'TDY': 'Teledyne Technologies Incorporated',

    'HFBC': 'HopFed Bancorp, Inc.',

    'PHX': 'Panhandle Royalty Company',

    'BLMT': 'BSB Bancorp, Inc.',

    'KERX': 'Keryx Biopharmaceuticals, Inc.',

    'MRNS': 'Marinus Pharmaceuticals, Inc.',

    'PBIP': 'Prudential Bancorp, Inc.',

    'FTAG': 'First Trust Indxx Global Agriculture ETF',

    'INTG': 'The Intergroup Corporation',

    'CCL': 'Carnival Corporation',

    'WPRT': 'Westport Fuel Systems Inc',

    'NWBOW': 'Northwest Biotherapeutics, Inc.',

    'DAKP': 'Dakota Plains Holdings, Inc.',

    'KFN-': 'KKR Financial Holdings LLC',

    'OFG-A': 'OFG Bancorp',

    'BANC-C': 'Banc of California, Inc.',

    'ABT': 'Abbott Laboratories',

    'HDSN': 'Hudson Technologies, Inc.',

    'RNVAW': 'Rennova Health, Inc.',

    'RAI': 'Reynolds American Inc',

    'SGRP': 'SPAR Group, Inc.',

    'ACIW': 'ACI Worldwide, Inc.',

    'SRVA': 'SIRVA, Inc.',

    'PSX': 'Phillips 66',

    'IKNX': 'Ikonics Corporation',

    'XOMA': 'XOMA Corporation',

    'SXI': 'Standex International Corporation',

    'MTLS': 'Materialise NV',

    'WAIR': 'Wesco Aircraft Holdings, Inc.',

    'GSBC': 'Great Southern Bancorp, Inc.',

    'PNC': 'PNC Financial Services Group, Inc. (The)',

    'FWP': 'Forward Pharma A/S',

    'FFIC': 'Flushing Financial Corporation',

    'EDAP': 'EDAP TMS S.A.',

    'GBSN': 'Great Basin Scientific, Inc.',

    'DO': 'Diamond Offshore Drilling, Inc.',

    'VG': 'Vonage Holdings Corp.',

    'ZAGG': 'ZAGG Inc',

    'AA': 'Alcoa Inc.',

    'LVLT': 'Level 3 Communications, Inc.',

    'BHE': 'Benchmark Electronics, Inc.',

    'DLR': 'Digital Realty Trust, Inc.',

    'RATE': 'Bankrate, Inc.',

    'DRAM': 'Dataram Corporation',

    'MERC': 'Mercer International Inc.',

    'XNCR': 'Xencor, Inc.',

    'APPY': 'Venaxis, Inc.',

    'GAM-B': 'General American Investors, Inc.',

    'SOHOL': 'Sotherly Hotels LP',

    'CSX': 'CSX Corporation',

    'APC': 'Anadarko Petroleum Corporation',

    'CBS.A': 'CBS Corporation',

    'NYMTP': 'New York Mortgage Trust, Inc.',

    'BRID': 'Bridgford Foods Corporation',

    'COR-A': 'CoreSite Realty Corporation',

    'EFR': 'Eaton Vance Senior Floating-Rate Fund',

    'ARII': 'American Railcar Industries, Inc.',

    'CNSL': 'Consolidated Communications Holdings, Inc.',

    'GDV': 'Gabelli Dividend',

    'EAE': 'Entergy Arkansas, Inc.',

    'IDRA': 'Idera Pharmaceuticals, Inc.',

    'KRNT': 'Kornit Digital Ltd.',

    'PAA': 'Plains All American Pipeline, L.P.',

    'UREE': 'U.S. Rare Earths, Inc.',

    'TAST': 'Carrols Restaurant Group, Inc.',

    'GER': 'Goldman Sachs MLP Energy Renaissance Fund',

    'OCLSW': 'Oculus Innovative Sciences, Inc.',

    'HLS.WS': 'HealthSouth Corporation',

    'SMED': 'Sharps Compliance Corp',

    'POST': 'Post Holdings, Inc.',

    'NNC': 'Nuveen North Carolina Premium Income Municipal Fund',

    'RST': 'Rosetta Stone',

    'WFC-P': 'Wells Fargo & Company',

    'KSS': 'Kohl\'s Corporation',

    'RE': 'Everest Re Group, Ltd.',

    'EGLT': 'Egalet Corporation',

    'NRCIA': 'National Research Corporation',

    'BGT': 'Blackrock Global',

    'CXP': 'Columbia Property Trust, Inc.',

    'TTWO': 'Take-Two Interactive Software, Inc.',

    'GLOG-A': 'GasLog LP.',

    'SMG': 'Scotts Miracle-Gro Company (The)',

    'TATT': 'TAT Technologies Ltd.',

    'STS': 'Supreme Industries, Inc.',

    'AIII': 'ACRE Realty Investors, Inc.',

    'FCA': 'First Trust China AlphaDEX Fund',

    'PCG-A': 'Pacific Gas & Electric Co.',

    'RIF': 'RMR Real Estate Income Fund',

    'ZTR': 'Zweig Total Return Fund, Inc. (The)',

    'DWA': 'Dreamworks Animation SKG, Inc.',

    'FT': 'Franklin Universal Trust',

    'CID': 'Victory CEMP International High Div Volatility Wtd Index ETF',

    'RBA': 'Ritchie Bros. Auctioneers Incorporated',

    'XTNT': 'Xtant Medical Holdings, Inc.',

    'GLW': 'Corning Incorporated',

    'ARCI': 'Appliance Recycling Centers of America, Inc.',

    'TSO': 'Tesoro Corporation',

    'FCBC': 'First Community Bancshares, Inc.',

    'NSPR': 'InspireMD, Inc.',

    'FCTY': '1st Century Bancshares, Inc',

    'DAX': 'Recon Capital DAX Germany ETF',

    'USBI': 'United Security Bancshares, Inc.',

    'CNLMW': 'CB Pharma Acquisition Corp.',

    'NAKD': 'Naked Brand Group Inc.',

    'HCACU': 'Hennessy Capital Acquisition Corp. II',

    'CMG': 'Chipotle Mexican Grill, Inc.',

    'CEF': 'Central Fund of Canada Limited',

    'EUFN': 'iShares MSCI Europe Financials Sector Index Fund',

    'DTEA': 'DAVIDsTEA Inc.',

    'OVBC': 'Ohio Valley Banc Corp.',

    'DX-A': 'Dynex Capital, Inc.',

    'ODC': 'Oil-Dri Corporation Of America',

    'TMST': 'Timken Steel Corporation',

    'JPW': 'Nuveen Flexible Investment Income Fund',

    'RTRX': 'Retrophin, Inc.',

    'MFA': 'MFA Financial, Inc.',

    'PVTB': 'PrivateBancorp, Inc.',

    'MGT': 'MGT Capital Investments Inc',

    'FATE': 'Fate Therapeutics, Inc.',

    'VEDL': 'Vedanta  Limited',

    'OTEX': 'Open Text Corporation',

    'ESPR': 'Esperion Therapeutics, Inc.',

    'BLW': 'Citigroup Inc.',

    'CABO': 'Cable One, Inc.',

    'HCP': 'HCP, Inc.',

    'AKG': 'Asanko Gold Inc.',

    'ACAS': 'American Capital, Ltd.',

    'THW': 'Tekla World Healthcare Fund',

    'TDIV': 'First Trust NASDAQ Technology Dividend Index Fund',

    'HCLP': 'Hi-Crush Partners LP',

    'FAC': 'First Acceptance Corporation',

    'MTSC': 'MTS Systems Corporation',

    'PSCD': 'PowerShares S&P SmallCap Consumer Discretionary Portfolio',

    'ARWAR': 'Arowana Inc.',

    'CBMX': 'CombiMatrix Corporation',

    'NCMI': 'National CineMedia, Inc.',

    'IBOC': 'International Bancshares Corporation',

    'CIZN': 'Citizens Holding Company',

    'PFSW': 'PFSweb, Inc.',

    'FCS': 'Fairchild Semiconductor International, Inc.',

    'USLB': 'PowerShares Russell 1000 Low Beta Equal Weight Portfolio',

    'IFEU': 'iShares FTSE EPRA/NAREIT Europe Index Fund',

    'PDLI': 'PDL BioPharma, Inc.',

    'MPLX': 'MPLX LP',

    'TEAM': 'Atlassian Corporation Plc',

    'KEM': 'Kemet Corporation',

    'BANC': 'Banc of California, Inc.',

    'SJW': 'SJW Corporation',

    'VECO': 'Veeco Instruments Inc.',

    'APLP': 'Archrock Partners, L.P.',

    'RES': 'RPC, Inc.',

    'ZB-G': 'Zions Bancorporation',

    'PTIE': 'Pain Therapeutics',

    'MCRB': 'Seres Therapeutics, Inc.',

    'RRMS': 'Rose Rock Midstream, L.P.',

    'FET': 'Forum Energy Technologies, Inc.',

    'OXGN': 'OXiGENE, Inc.',

    'OGS': 'ONE Gas, Inc.',

    'CBM': 'Cambrex Corporation',

    'CEMI': 'Chembio Diagnostics, Inc.',

    'GALE': 'Galena Biopharma, Inc.',

    'AMT': 'American Tower Corporation (REIT)',

    'ESD': 'Western Asset Emerging Markets Debt Fund Inc',

    'NAVG': 'The Navigators Group, Inc.',

    'KWN': 'Kennedy-Wilson Holdings Inc.',

    'ABM': 'ABM Industries Incorporated',

    'NZH': 'Nuveen California Dividend Advantage Municipal Fund 3',

    'REXR': 'Rexford Industrial Realty, Inc.',

    'HAR': 'Harman International Industries, Incorporated',

    'AVT': 'Avnet, Inc.',

    'FNGN': 'Financial Engines, Inc.',

    'CSGS': 'CSG Systems International, Inc.',

    'IDTI': 'Integrated Device Technology, Inc.',

    'TY-': 'Tri Continental Corporation',

    'ADXS': 'Advaxis, Inc.',

    'CLNY': 'Colony Capital, Inc',

    'KORS': 'Michael Kors Holdings Limited',

    'SAMG': 'Silvercrest Asset Management Group Inc.',

    'FCFP': 'First Community Financial Partners, Inc.',

    'JCOM': 'j2 Global, Inc.',

    'GHC': 'Graham Holdings Company',

    'SPGI': 'S&P Global Inc.',

    'DTSI': 'DTS, Inc.',

    'WEB': 'Web.com Group, Inc.',

    'INT': 'World Fuel Services Corporation',

    'SBAC': 'SBA Communications Corporation',

    'LAWS': 'Lawson Products, Inc.',

    'HON': 'Honeywell International Inc.',

    'BATRK': 'Liberty Media Corporation',

    'EXAC': 'Exactech, Inc.',

    'LND': 'Brasilagro Cia Brasileira De Propriedades Agricolas',

    'ROYT': 'Pacific Coast Oil Trust',

    'WGL': 'WGL Holdings Inc',

    'NTL': 'Nortel Inversora SA',

    'ATNM': 'Actinium Pharmaceuticals, Inc.',

    'GLT': 'Glatfelter',

    'LUV': 'Southwest Airlines Company',

    'RHI': 'Robert Half International Inc.',

    'OPGNW': 'OpGen, Inc.',

    'THST': 'Truett-Hurst, Inc.',

    'AM': 'Antero Midstream Partners LP',

    'AEM': 'Agnico Eagle Mines Limited',

    'ESND': 'Essendant Inc.',

    'HTM': 'U.S. Geothermal Inc.',

    'IGOV': 'iShares S&P/Citigroup International Treasury Bond Fund',

    'LXFR': 'Luxfer Holdings PLC',

    'CRME': 'Cardiome Pharma Corporation',

    'HCJ': 'HCI Group, Inc.',

    'WIW': 'Western Asset/Claymore U.S Treasury Inflation Prot Secs Fd 2',

    'CNA': 'CNA Financial Corporation',

    'ECACR': 'E-compass Acquisition Corp.',

    'WLTW': 'Willis Towers Watson Public Limited Company',

    'GRSH': 'Gores Holdings, Inc.',

    'GSAT': 'Globalstar, Inc.',

    'GROW': 'U.S. Global Investors, Inc.',

    'KFS': 'Kingsway Financial Services, Inc.',

    'IMKTA': 'Ingles Markets, Incorporated',

    'ROK': 'Rockwell Automation, Inc.',

    'AITP': 'Advanced Inhalation Therapies (AIT) Ltd.',

    'ATAX': 'America First Multifamily Investors, L.P.',

    'SWK': 'Stanley Black & Decker, Inc.',

    'WEC': 'WEC Energy Group, Inc.',

    'EVDY': 'Everyday Health, Inc.',

    'CGEN': 'Compugen Ltd.',

    'WRB-C': 'W.R. Berkley Corporation',

    'LEU': 'Centrus Energy Corp.',

    'HI': 'Hillenbrand Inc',

    'KMB': 'Kimberly-Clark Corporation',

    'FNB-E': 'F.N.B. Corporation',

    'CLCT': 'Collectors Universe, Inc.',

    'DCOM': 'Dime Community Bancshares, Inc.',

    'DRYS': 'DryShips Inc.',

    'CAC': 'Camden National Corporation',

    'NCZ': 'AllianzGI Convertible & Income Fund II',

    'BNSO': 'Bonso Electronics International, Inc.',

    'N': 'Netsuite Inc',

    'CNQ': 'Canadian Natural Resources Limited',

    'VBIV': 'VBI Vaccines, Inc.',

    'MMD': 'MainStay DefinedTerm Municipal Opportunities Fund',

    'MTB': 'M&T Bank Corporation',

    'MUJ': 'Blackrock MuniHoldings New Jersey Insured Fund, Inc.',

    'FITS': 'The Health and Fitness ETF',

    'FCO': 'Aberdeen Global Income Fund, Inc.',

    'ATSG': 'Air Transport Services Group, Inc',

    'GYC': 'Corporate Asset Backed Corp CABCO',

    'BHL': 'Blackrock Defined Opportunity Credit Trust',

    'WEBK': 'Wellesley Bancorp, Inc.',

    'ACWI': 'iShares MSCI ACWI Index Fund',

    'BPFH': 'Boston Private Financial Holdings, Inc.',

    'CECE': 'CECO Environmental Corp.',

    'CLRO': 'ClearOne, Inc.',

    'CCRC': 'China Customer Relations Centers, Inc.',

    'USMD': 'USMD Holdings, Inc.',

    'ONCS': 'OncoSec Medical Incorporated',

    'CIF': 'Colonial Intermediate High Income Fund',

    'ALX': 'Alexander\'s, Inc.',

    'NCBS': 'Nicolet Bankshares Inc.',

    'DRWI': 'DragonWave Inc',

    'ISLE': 'Isle of Capri Casinos, Inc.',

    'TOL': 'Toll Brothers Inc.',

    'NCA': 'Nuveen California Municipal Value Fund, Inc.',

    'TSLA': 'Tesla Motors, Inc.',

    'CRS': 'Carpenter Technology Corporation',

    'WUBA': '58.com Inc.',

    'VGLT': 'Vanguard Long-Term Government Bond ETF',

    'NQP': 'Nuveen Pennsylvania Investment Quality Municipal Fund, Inc.',

    'EPRS': 'EPIRUS Biopharmaceuticals, Inc.',

    'TYC': 'Tyco International plc',

    'ISD': 'Prudential Short Duration High Yield Fund, Inc.',

    'EL': 'Estee Lauder Companies, Inc. (The)',

    'VMI': 'Valmont Industries, Inc.',

    'IZEA': 'IZEA Inc.',

    'CSIQ': 'Canadian Solar Inc.',

    'CBB-B': 'Cincinnati Bell Inc',

    'MLSS': 'Milestone Scientific, Inc.',

    'DNBF': 'DNB Financial Corp',

    'NKTR': 'Nektar Therapeutics',

    'CYHHZ': 'Community Health Systems, Inc.',

    'IAF': 'Aberdeen Australia Equity Fund Inc',

    'JAX': 'J. Alexander\'s Holdings, Inc.',

    'DMLP': 'Dorchester Minerals, L.P.',

    'DANG': 'E-Commerce China Dangdang Inc.',

    'DISH': 'DISH Network Corporation',

    'AGNC': 'American Capital Agency Corp.',

    'FLEX': 'Flextronics International Ltd.',

    'MRVC': 'MRV Communications, Inc.',

    'BKCC': 'BlackRock Capital Investment Corporation',

    'RAX': 'Rackspace Hosting, Inc',

    'SRE': 'Sempra Energy',

    'TSU': 'TIM Participacoes S.A.',

    'HLTH': 'Nobilis Health Corp.',

    'VTWV': 'Vanguard Russell 2000 Value ETF',

    'PRIM': 'Primoris Services Corporation',

    'MXPT': 'MaxPoint Interactive, Inc.',

    'AGM-A': 'Federal Agricultural Mortgage Corporation',

    'RVSB': 'Riverview Bancorp Inc',

    'VIIX': 'region',

    'AMSC': 'American Superconductor Corporation',

    'AZZ': 'AZZ Inc.',

    'JAKK': 'JAKKS Pacific, Inc.',

    'CWST': 'Casella Waste Systems, Inc.',

    'DGICA': 'Donegal Group, Inc.',

    'MIN': 'MFS Intermediate Income Trust',

    'CMCSA': 'Comcast Corporation',

    'LINK': 'Interlink Electronics, Inc.',

    'DXR': 'Daxor Corporation',

    'IFF': 'Internationa Flavors & Fragrances, Inc.',

    'BAH': 'Booz Allen Hamilton Holding Corporation',

    'HNP': 'Huaneng Power International, Inc.',

    'HELE': 'Helen of Troy Limited',

    'SUNS': 'Solar Senior Capital Ltd.',

    'MASI': 'Masimo Corporation',

    'MCN': 'Madison Covered Call & Equity Strategy Fund',

    'VMEM': 'Violin Memory, Inc.',

    'AMH-B': 'American Homes 4 Rent',

    'RCII': 'Rent-A-Center Inc.',

    'HIO': 'Western Asset High Income Opportunity Fund, Inc.',

    'KSM': 'Scudder Strategic Municiple Income Trust',

    'PW-A': 'Power REIT',

    'WFBI': 'WashingtonFirst Bankshares Inc',

    'IDE': 'Voya Infrastructure, Industrials and Materials Fund',

    'AXE': 'Anixter International Inc.',

    'TOO-B': 'Teekay Offshore Partners L.P.',

    'HMPR': 'Hampton Roads Bankshares Inc',

    'BHACW': 'Barington/Hilco Acquisition Corp.',

    'FGEN': 'FibroGen, Inc',

    'FNJN': 'Finjan Holdings, Inc.',

    'STV': 'China Digital TV Holding Co., Ltd.',

    'AT': 'Atlantic Power Corporation',

    'PMBC': 'Pacific Mercantile Bancorp',

    'DYN-A': 'Dynegy Inc.',

    'SYNT': 'Syntel, Inc.',

    'INGN': 'Inogen, Inc',

    'JNS': 'Janus Capital Group, Inc',

    'TFSL': 'TFS Financial Corporation',

    'MOG.B': 'Moog Inc.',

    'FIVE': 'Five Below, Inc.',

    'IEC': 'IEC Electronics Corp.',

    'ITIC': 'Investors Title Company',

    'CLLS': 'Cellectis S.A.',

    'PLNT': 'Planet Fitness, Inc.',

    'Q': 'Quintiles Transitional Holdings Inc.',

    'CCD': 'Calamos Dynamic Convertible & Income Fund',

    'RMBS': 'Rambus, Inc.',

    'FRC-F': 'FIRST REPUBLIC BANK',

    'SBRA': 'Sabra Healthcare REIT, Inc.',

    'NEWM': 'New Media Investment Group Inc.',

    'PCLN': 'The Priceline Group Inc. ',

    'EAT': 'Brinker International, Inc.',

    'INNL': 'Innocoll Holdings',

    'FHY': 'First Trust Strategic High Income Fund II',

    'ERI': 'Eldorado Resorts, Inc.',

    'SBI': 'Western Asset Intermediate Muni Fund Inc',

    'EXPO': 'Exponent, Inc.',

    'STAG': 'Stag Industrial, Inc.',

    'ACV': 'AllianzGI Diversified Income & Convertible Fund',

    'VMO': 'Invesco Municipal Opportunity Trust',

    'JFR': 'Nuveen Floating Rate Income Fund',

    'SPCB': 'SuperCom, Ltd.',

    'ABG': 'Asbury Automotive Group Inc',

    'CQH': 'Cheniere Energy Partners LP Holdings, LLC',

    'RDHL': 'Redhill Biopharma Ltd.',

    'BP': 'BP p.l.c.',

    'SAH': 'Sonic Automotive, Inc.',

    'MGEE': 'MGE Energy Inc.',

    'EPC': 'Energizer Holdings, Inc.',

    'WFC.WS': 'Wells Fargo & Company',

    'AFT': 'Apollo Senior Floating Rate Fund Inc.',

    'CMC': 'Commercial Metals Company',

    'FKU': 'First Trust United Kingdom AlphaDEX Fund',

    'SYX': 'Systemax Inc.',

    'AREX': 'Approach Resources Inc.',

    'BIO': 'Bio-Rad Laboratories, Inc.',

    'TRCO': 'Tribune Media Company',

    'PCN': 'Pimco Corporate & Income Stategy Fund',

    'APF': 'Morgan Stanley Asia-Pacific Fund, Inc.',

    'EOCC': 'Empresa Nacional de Electricidad S.A.',

    'UTEK': 'Ultratech, Inc.',

    'SNSS': 'Sunesis Pharmaceuticals, Inc.',

    'MVT': 'Blackrock MuniVest Fund II, Inc.',

    'EPR-E': 'EPR Properties',

    'OFS': 'OFS Capital Corporation',

    'ABCD': 'Cambium Learning Group, Inc.',

    'SPU': 'SkyPeople Fruit Juice, Inc.',

    'PDBC': 'PowerShares DB Optimum Yield Diversified Commodity Strategy Po',

    'ETG': 'Eaton Vance Tax-Advantaged Global Dividend Income Fund',

    'RBS-L': 'Royal Bank Scotland plc (The)',

    'JRVR': 'James River Group Holdings, Ltd.',

    'TAYD': 'Taylor Devices, Inc.',

    'AWX': 'Avalon Holdings Corporation',

    'DOC': 'Physicians Realty Trust',

    'FBMS': 'The First Bancshares, Inc.',

    'BATRR': 'Liberty Media Corporation',

    'GD': 'General Dynamics Corporation',

    'SPLK': 'Splunk Inc.',

    'NWLI': 'National Western Life Group, Inc.',

    'GOODM': 'Gladstone Commercial Corporation',

    'CRTO': 'Criteo S.A.',

    'PRFT': 'Perficient, Inc.',

    'CLMS': 'Calamos Asset Management, Inc.',

    'JPEP': 'JP Energy Partners LP',

    'CGA': 'China Green Agriculture, Inc.',

    'BXE': 'Bellatrix Exploration Ltd',

    'BERY': 'BPC Acquisition Corp',

    'AIRI': 'Air Industries Group',

    'PFE': 'Pfizer, Inc.',

    'SBFG': 'SB Financial Group, Inc.',

    'PAGP': 'Plains Group Holdings, L.P.',

    'ZGNX': 'Zogenix, Inc.',

    'EVLMC': 'Eaton Vance NextShares Trust II',

    'GDL-B': 'The GDL Fund',

    'SWC': 'Stillwater Mining Company',

    'AXR': 'AMREP Corporation',

    'PTI': 'Proteostasis Therapeutics, Inc.',

    'HDP': 'Hortonworks, Inc.',

    'MTGEP': 'American Capital Mortgage Investment Corp.',

    'NRF-B': 'Northstar Realty Finance Corp.',

    'BDJ': 'Blackrock Enhanced Equity Dividend Trust',

    'FEIC': 'FEI Company',

    'APDN': 'Applied DNA Sciences Inc',

    'FRPT': 'Freshpet, Inc.',

    'REI': 'Ring Energy, Inc.',

    'SNE': 'Sony Corp Ord',

    'LINC': 'Lincoln Educational Services Corporation',

    'NBH': 'Neuberger Berman Intermediate Municipal Fund Inc.',

    'AA-B': 'Alcoa Inc.',

    'FALC': 'FalconStor Software, Inc.',

    'EXP': 'Eagle Materials Inc',

    'NBW': 'Neuberger Berman California Intermediate Municipal Fund Inc.',

    'MKTO': 'Marketo, Inc.',

    'ERJ': 'Embraer-Empresa Brasileira de Aeronautica',

    'GDO': 'Western Asset Global Corporate Defined Opportunity Fund Inc.',

    'AKTX': 'Akari Therapeutics Plc',

    'EVT': 'Eaton Vance Tax Advantaged Dividend Income Fund',

    'ITRN': 'Ituran Location and Control Ltd.',

    'WBS-E': 'Webster Financial Corporation',

    'EXK': 'Endeavour Silver Corporation',

    'ELU': 'Entergy Louisiana, Inc.',

    'GK': 'G&K Services, Inc.',

    'IMS': 'IMS Health Holdings, Inc.',

    'STI.WS.B': 'SunTrust Banks, Inc.',

    'URRE': 'Uranium Resources, Inc.',

    'INXN': 'InterXion Holding N.V.',

    'FIVN': 'Five9, Inc.',

    'SNHO': 'Senior Housing Properties Trust',

    'INSY': 'Insys Therapeutics, Inc.',

    'DDR-K': 'DDR Corp.',

    'UBS': 'UBS AG',

    'GEN           ': 'Genesis Healthcare, Inc.',

    'BBT-F': 'BB&T Corporation',

    'RDY': 'Dr. Reddy\'s Laboratories Ltd',

    'FRBA': 'First Bank',

    'HMST': 'HomeStreet, Inc.',

    'CEM': 'ClearBridge Energy MLP Fund Inc.',

    'AFSI-D': 'AmTrust Financial Services, Inc.',

    'JBLU': 'JetBlue Airways Corporation',

    'AMH': 'American Homes 4 Rent',

    'MPV': 'Babson Capital Participation Investors',

    'KTN': 'Lehman ABS Corporation',

    'JGV': 'Nuveen Global Equity Income Fund ',

    'DXCM': 'DexCom, Inc.',

    'EXPR': 'Express, Inc.',

    'IPDN': 'Professional Diversity Network, Inc.',

    'ATRC': 'AtriCure, Inc.',

    'AKAM': 'Akamai Technologies, Inc.',

    'HMHC': 'Houghton Mifflin Harcourt Company',

    'ENH-C': 'Endurance Specialty Holdings Ltd',

    'PEB': 'Pebblebrook Hotel Trust',

    'RVP': 'Retractable Technologies, Inc.',

    'TUBE': 'TubeMogul, Inc.',

    'GENC': 'Gencor Industries Inc.',

    'CIFC': 'CIFC LLC',

    'AKS': 'AK Steel Holding Corporation',

    'GPRE': 'Green Plains, Inc.',

    'IBUY': 'Amplify Online Retail ETF',

    'MTL': 'Mechel OAO',

    'HBHCL': 'Hancock Holding Company',

    'SSS': 'Sovran Self Storage, Inc.',

    'HMG': 'HMG/Courtland Properties, Inc.',

    'EFT': 'Eaton Vance Floating Rate Income Trust',

    'SREV': 'ServiceSource International, Inc.',

    'NRK': 'Nuveen New York AMT-Free Municipal Income Fund',

    'EVSTC': 'Eaton Vance NextShares Trust',

    'BOKF': 'BOK Financial Corporation',

    'IPXL': 'Impax Laboratories, Inc.',

    'MTH': 'Meritage Corporation',

    'MCX': 'Medley Capital Corporation',

    'NAC': 'Nuveen California Dividend Advantage Municipal Fund',

    'KTOV': 'Kitov Pharamceuticals Holdings Ltd.',

    'CTR': 'ClearBridge Energy MLP Total Return Fund Inc.',

    'REV': 'Revlon, Inc.',

    'BAM$': 'Brookfield Asset Management Inc',

    'HABT': 'The Habit Restaurants, Inc.',

    'EBMT': 'Eagle Bancorp Montana, Inc.',

    'PAH': 'Platform Specialty Products Corporation',

    'RMGN': 'RMG Networks Holding Corporation',

    'HEAR': 'Turtle Beach Corporation',

    'LNKD': 'LinkedIn Corporation',

    'ELECW': 'Electrum Special Acquisition Corporation',

    'BCS-D': 'Barclays PLC',

    'MYGN': 'Myriad Genetics, Inc.',

    'EVR': 'Evercore Partners Inc',

    'AQMS': 'Aqua Metals, Inc.',

    'NKSH': 'National Bankshares, Inc.',

    'MRKT': 'Markit Ltd.',

    'TUP': 'Tupperware Brands Corporation',

    'COMM': 'CommScope Holding Company, Inc.',

    'BCS': 'Barclays PLC',

    'EQY': 'Equity One, Inc.',

    'OIIM': 'O2Micro International Limited',

    'DSL': 'DoubleLine Income Solutions Fund',

    'NIQ': 'Nuveenn Intermediate Duration Quality Municipal Term Fund',

    'ADXSW': 'Advaxis, Inc.',

    'MDVN': 'Medivation, Inc.',

    'ODFL': 'Old Dominion Freight Line, Inc.',

    'SGF': 'Aberdeen Singapore Fund, Inc.',

    'CHT': 'Chunghwa Telecom Co., Ltd.',

    'BXP-B': 'Boston Properties, Inc.',

    'AWK': 'American Water Works',

    'WYN': 'Wyndham Worldwide Corp',

    'MDGN': 'Medgenics, Inc.',

    'TRQ': 'Turquoise Hill Resources Ltd.',

    'AXS-C': 'Axis Capital Holdings Limited',

    'GRX-A': 'The Gabelli Healthcare & Wellness Trust',

    'SCG': 'Scana Corporation',

    'BML-G': 'Bank of America Corporation',

    'SAN': 'Banco Santander, S.A.',

    'CHEK': 'Check-Cap Ltd.',

    'AGM-C': 'Federal Agricultural Mortgage Corporation',

    'RZA': 'Reinsurance Group of America, Incorporated',

    'AET': 'Aetna Inc.',

    'KTF': 'Scudder Municiple Income Trust',

    'SATS': 'EchoStar Corporation',

    'WHF': 'WhiteHorse Finance, Inc.',

    'PBHC': 'Pathfinder Bancorp, Inc.',

    'VSI': 'Vitamin Shoppe, Inc',

    'DOOR': 'Masonite International Corporation',

    'NMIH': 'NMI Holdings Inc',

    'XXIA': 'Ixia',

    'PEI-A': 'Pennsylvania Real Estate Investment Trust',

    'EBSB': 'Meridian Bancorp, Inc.',

    'ERIE': 'Erie Indemnity Company',

    'DWIN': 'PowerShares DWA Tactical Multi-Asset Income Portfolio',

    'TLP': 'Transmontaigne Partners L.P.',

    'PKOH': 'Park-Ohio Holdings Corp.',

    'CMCT': 'CIM Commercial Trust Corporation',

    'FBRC': 'FBR & Co',

    'PNC.WS': 'PNC Financial Services Group, Inc. (The)',

    'OOMA': 'Ooma, Inc.',

    'ANIK': 'Anika Therapeutics Inc.',

    'ERC': 'Wells Fargo Multi-Sector Income Fund',

    'JBK': 'Lehman ABS Corporation',

    'CCFI': 'Community Choice Financial Inc.',

    'BMY': 'Bristol-Myers Squibb Company',

    'JMLP': 'Nuveen All Cap Energy MLP Opportunities Fund',

    'EMAN': 'eMagin Corporation',

    'UTX': 'United Technologies Corporation',

    'BAM': 'Brookfield Asset Management Inc',

    'ESTE': 'Earthstone Energy, Inc.',

    'HSNI': 'HSN, Inc.',

    'VTN': 'Invesco Trust  for Investment Grade New York Municipal',

    'POT': 'Potash Corporation of Saskatchewan Inc.',

    'BGCA': 'BGC Partners, Inc.',

    'MITT-A': 'AG Mortgage Investment Trust, Inc.',

    'BHP': 'BHP Billiton Limited',

    'CETC': 'Hongli Clean Energy Technologies Corp.',

    'PACD': 'Pacific Drilling S.A.',

    'CAPL': 'CrossAmerica Partners LP',

    'CUK': 'Carnival Corporation',

    'FTF': 'Franklin Limited Duration Income Trust',

    'DIT': 'AMCON Distributing Company',

    'PII': 'Polaris Industries Inc.',

    'SAN-I': 'Banco Santander, S.A.',

    'LOR': 'Lazard World Dividend & Income Fund, Inc.',

    'LRCX': 'Lam Research Corporation',

    'HTGC': 'Hercules Capital, Inc.',

    'AMEH': 'Apollo Medical Holdings, Inc.',

    'JMT': 'Nuven Mortgage Opportunity Term Fund 2',

    'LPX': 'Louisiana-Pacific Corporation',

    'DTUS': 'region',

    'VRSN': 'VeriSign, Inc.',

    'CPE-A': 'Callon Petroleum Company',

    'FH': 'FORM Holdings Corp.',

    'RKDA': 'Arcadia Biosciences, Inc.',

    'WSO': 'Watsco, Inc.',

    'PG': 'Procter & Gamble Company (The)',

    'MTEX': 'Mannatech, Incorporated',

    'EFC': 'Ellington Financial LLC',

    'JVA': 'Coffee Holding Co., Inc.',

    'XIV': 'region',

    'CAFD': '8point3 Energy Partners LP',

    'ANDAR': 'Andina Acquisition Corp. II',

    'MSEX': 'Middlesex Water Company',

    'TOWR': 'Tower International, Inc.',

    'FUND': 'Sprott Focus Trust, Inc.',

    'FDML': 'Federal-Mogul Holdings Corporation',

    'FTD': 'FTD Companies, Inc.',

    'CETV': 'Central European Media Enterprises Ltd.',

    'ARWAW': 'Arowana Inc.',

    'MKSI': 'MKS Instruments, Inc.',

    'XKE': 'Lehman ABS Corporation',

    'DVA': 'DaVita healthCare Partners Inc.',

    'NGS': 'Natural Gas Services Group, Inc.',

    'INVA': 'Innoviva, Inc.',

    'PANW': 'Palo Alto Networks, Inc.',

    'MAT': 'Mattel, Inc.',

    'BGY': 'BLACKROCK INTERNATIONAL, LTD.',

    'PNRG': 'PrimeEnergy Corporation',

    'ATTU': 'Attunity Ltd.',

    'WIT': 'Wipro Limited',

    'VUSE': 'Vident Core US Equity ETF',

    'PKY': 'Parkway Properties, Inc.',

    'HT-C': 'Hersha Hospitality Trust',

    'DFVL': 'region',

    'ESSA': 'ESSA Bancorp, Inc.',

    'MODN': 'Model N, Inc.',

    'TKR': 'Timken Company (The)',

    'NMT': 'Nuveen Massachusetts Premium Income Municipal Fund',

    'SWKS': 'Skyworks Solutions, Inc.',

    'CUB': 'Cubic Corporation',

    'ARES-A': 'Ares Management L.P.',

    'SOFO': 'Sonic Foundry, Inc.',

    'PDFS': 'PDF Solutions, Inc.',

    'GAIA': 'Gaiam, Inc.',

    'HIG.WS': 'Hartford Financial Services Group, Inc. (The)',

    'LEI': 'Lucas Energy, Inc.',

    'SMCP': 'AlphaMark Actively Managed Small Cap ETF',

    'PRK': 'Park National Corporation',

    'LEN.B': 'Lennar Corporation',

    'CUBA': 'The Herzfeld Caribbean Basin Fund, Inc.',

    'PME': 'Pingtan Marine Enterprise Ltd.',

    'HUBS': 'HubSpot, Inc.',

    'CPG': 'Crescent Point Energy Corporation',

    'AME': 'AMTEK, Inc.',

    'VZ': 'Verizon Communications Inc.',

    'MDU': 'MDU Resources Group, Inc.',

    'WNR': 'Western Refining, Inc.',

    'CBRL': 'Cracker Barrel Old Country Store, Inc.',

    'ESGR': 'Enstar Group Limited',

    'AINV': 'Apollo Investment Corporation',

    'AST.WS': 'Asterias Biotherapeutics, Inc.',

    'SOJA': 'Southern Company (The)',

    'PEB-C': 'Pebblebrook Hotel Trust',

    'PDEX': 'Pro-Dex, Inc.',

    'CEB': 'CEB Inc.',

    'RGS': 'Regis Corporation',

    'CDXC': 'ChromaDex Corporation',

    'CME': 'CME Group Inc.',

    'STRL': 'Sterling Construction Company Inc',

    'ORM': 'Owens Realty Mortgage, Inc.',

    'QRVO': 'Qorvo, Inc.',

    'HPI': 'John Hancock Preferred Income Fund',

    'NP': 'Neenah Paper, Inc.',

    'CYTX': 'Cytori Therapeutics Inc',

    'SRCE': '1st Source Corporation',

    'EQC': 'Equity Commonwealth',

    'HTWR': 'Heartware International, Inc.',

    'NTAP': 'NetApp, Inc.',

    'JAGX': 'Jaguar Animal Health, Inc.',

    'MQY': 'Blackrock MuniYield Quality Fund, Inc.',

    'EPR': 'EPR Properties',

    'VOYA': 'Voya Financial, Inc.',

    'JOE': 'St. Joe Company (The)',

    'UWN': 'Nevada Gold & Casinos, Inc.',

    'BFIT': 'Global X Health & Wellness Thematic ETF',

    'GEF': 'Greif Bros. Corporation',

    'LAND': 'Gladstone Land Corporation',

    'SMLP': 'Summit Midstream Partners, LP',

    'SAND          ': 'Sandstorm Gold Ltd',

    'BOJA': 'Bojangles\', Inc.',

    'TLK': 'PT Telekomunikasi Indonesia, Tbk',

    'MTSL': 'MER Telemanagement Solutions Ltd.',

    'FOF': 'Cohen & Steers Closed-End Opportunity Fund, Inc.',

    'TMK-C': 'Torchmark Corporation',

    'SNN': 'Smith & Nephew SNATS, Inc.',

    'RF': 'Regions Financial Corporation',

    'BUR': 'Burcon Nutrascience Corp',

    'PRPH': 'ProPhase Labs, Inc.',

    'FL': 'Foot Locker, Inc.',

    'NLY-A': 'Annaly Capital Management Inc',

    'MNDO': 'MIND C.T.I. Ltd.',

    'BKU': 'BankUnited, Inc.',

    'BFK': 'BlackRock Municipal Income Trust',

    'BVXV': 'BiondVax Pharmaceuticals Ltd.',

    'MTG': 'MGIC Investment Corporation',

    'NID': 'Nuveen Intermediate Duration Municipal Term Fund',

    'LUNA': 'Luna Innovations Incorporated',

    'MPC': 'Marathon Petroleum Corporation',

    'CXW': 'Corrections Corporation of America',

    'NEE-C': 'NextEra Energy, Inc.',

    'ESRT': 'Empire State Realty Trust, Inc.',

    'ITCI': 'Intra-Cellular Therapies Inc.',

    'OFLX': 'Omega Flex, Inc.',

    'BBRY': 'BlackBerry Limited',

    'MHO': 'M/I Homes, Inc.',

    'JACK': 'Jack In The Box Inc.',

    'HIBB': 'Hibbett Sports, Inc.',

    'TRP': 'TransCanada Corporation',

    'CHTR': 'Charter Communications, Inc.',

    'NSL': 'Nuveen Senior Income Fund',

    'FRME': 'First Merchants Corporation',

    'CACI': 'CACI International, Inc.',

    'QCOM': 'QUALCOMM Incorporated',

    'OSK': 'Oshkosh Corporation',

    'BRS': 'Bristow Group Inc',

    'DRNA': 'Dicerna Pharmaceuticals, Inc.',

    'DGRE': 'WisdomTree Emerging Markets Quality Dividend Growth Fund',

    'BTT': 'BlackRock Municipal Target Term Trust Inc. (The)',

    'CL': 'Colgate-Palmolive Company',

    'AXDX': 'Accelerate Diagnostics, Inc.',

    'BR': 'Broadridge Financial Solutions, Inc.',

    'SSRG': 'Symmetry Surgical Inc.',

    'JW.B': 'John Wiley & Sons, Inc.',

    'STLD': 'Steel Dynamics, Inc.',

    'WMIH': 'WMIH Corp.',

    'MUE': 'Blackrock MuniHoldings Quality Fund II, Inc.',

    'MFO': 'MFA Financial, Inc.',

    'GJT': 'Synthetic Fixed-Income Securities, Inc.',

    'KANG': 'iKang Healthcare Group, Inc.',

    'TBK': 'Triumph Bancorp, Inc.',

    'FAST': 'Fastenal Company',

    'BIT': 'BlackRock Multi-Sector Income Trust',

    'IVTY': 'Invuity, Inc.',

    'ALLE': 'Allegion plc',

    'TTPH': 'Tetraphase Pharmaceuticals, Inc.',

    'ELLO': 'Ellomay Capital Ltd.',

    'PSA-S': 'Public Storage',

    'NRIM': 'Northrim BanCorp Inc',

    'CCE': 'Coca-Cola European Partners plc',

    'COHU': 'Cohu, Inc.',

    'UNH': 'UnitedHealth Group Incorporated',

    'EEQ': 'Enbridge Energy Management LLC',

    'TRK': 'Speedway Motorsports, Inc.',

    'CYBR': 'CyberArk Software Ltd.',

    'CHW': 'Calamos Global Dynamic Income Fund',

    'VER': 'VEREIT Inc.',

    'SBSI': 'Southside Bancshares, Inc.',

    'ARKR': 'Ark Restaurants Corp.',

    'KR': 'Kroger Company (The)',

    'ZDGE': 'Zedge, Inc.',

    'GNE-A': 'Genie Energy Ltd.',

    'CPF': 'CPB Inc.',

    'PSCT': 'PowerShares S&P SmallCap Information Technology Portfolio',

    'CUBS': 'Customers Bancorp, Inc',

    'QLC': 'FlexShares US Quality Large Cap Index Fund',

    'PUK-A': 'Prudential Public Limited Company',

    'LTC': 'LTC Properties, Inc.',

    'TCO': 'Taubman Centers, Inc.',

    'PLAY': 'Dave & Buster\'s Entertainment, Inc.',

    'CVI': 'CVR Energy Inc.',

    'IPAS': 'iPass Inc.',

    'FDT': 'First Trust Developed Markets Ex-US AlphaDEX Fund',

    'PIY': 'Merrill Lynch Depositor, Inc.',

    'TENX': 'Tenax Therapeutics, Inc.',

    'BIOA.WS': 'BioAmber Inc.',

    'OMAB': 'Grupo Aeroportuario del Centro Norte S.A.B. de C.V.',

    'GLOG': 'GasLog LP.',

    'NVCN': 'Neovasc Inc.',

    'CAJ': 'Canon, Inc.',

    'ETB': 'Eaton Vance Tax-Managed Buy-Write Income Fund',

    'TDJ': 'Telephone and Data Systems, Inc.',

    'HHS': 'Harte-Hanks, Inc.',

    'YIN': 'Yintech Investment Holdings Limited',

    'MTU': 'Mitsubishi UFJ Financial Group Inc',

    'BBCN': 'BBCN Bancorp, Inc.',

    'SSB': 'South State Corporation',

    'PWX': 'Providence and Worcester Railroad Company',

    'FRC-G': 'FIRST REPUBLIC BANK',

    'KOP': 'Koppers Holdings Inc.',

    'RITTW': 'RIT Technologies Ltd.',

    'ITI': 'Iteris, Inc.',

    'HEP': 'Holly Energy Partners, L.P.',

    'GBNK': 'Guaranty Bancorp',

    'MTOR': 'Meritor, Inc.',

    'MOKO': 'Moko Social Media Ltd.',

    'TNDM': 'Tandem Diabetes Care, Inc.',

    'DDD': '3D Systems Corporation',

    'VTIP': 'Vanguard Short-Term Inflation-Protected Securities Index Fund',

    'WBAI': '500.com Limited',

    'FFC': 'Flaherty & Crumrine Preferred Securities Income Fund Inc',

    'SFUN': 'SouFun Holdings Limited',

    'RY': 'Royal Bank Of Canada',

    'CUBE-A': 'CubeSmart',

    'FIG': 'Fortress Investment Group LLC',

    'CRVS': 'Corvus Pharmaceuticals, Inc.',

    'WYNN': 'Wynn Resorts, Limited',

    'MFRM': 'Mattress Firm Holding Corp.',

    'LBTYA': 'Liberty Global plc',

    'KF': 'Korea Fund, Inc. (The)',

    'VXUP': 'AccuShares Spot CBOE VIX Up Shares',

    'OIBR.C': 'Oi S.A.',

    'TSQ': 'Townsquare Media, Inc.',

    'PNK': 'Pinnacle Entertainment, Inc.',

    'ZTS': 'Zoetis Inc.',

    'CNIT': 'China Information Technology, Inc.',

    'YUMA': 'Yuma Energy, Inc.',

    'PNC-P': 'PNC Financial Services Group, Inc. (The)',

    'NICE': 'NICE-Systems Limited',

    'INFU': 'InfuSystems Holdings, Inc.',

    'HAL': 'Halliburton Company',

    'DRE': 'Duke Realty Corporation',

    'YDIV': 'First Trust International Multi-Asset Diversified Income Index',

    'BOOM': 'Dynamic Materials Corporation',

    'CFFI': 'C&F Financial Corporation',

    'SSW': 'Seaspan Corporation',

    'GARS': 'Garrison Capital Inc.',

    'MVG': 'Mag Silver Corporation',

    'RSG': 'Republic Services, Inc.',

    'YPF': 'YPF Sociedad Anonima',

    'UPLD': 'Upland Software, Inc.',

    'RFAP': 'First Trust RiverFront Dynamic Asia Pacific ETF',

    'CYD': 'China Yuchai International Limited',

    'FCVT': 'First Trust SSI Strategic Convertible Securities ETF',

    'SONC': 'Sonic Corp.',

    'PVCT': 'Provectus Biopharmaceuticals, Inc.',

    'TOWN': 'Towne Bank',

    'ADC': 'Agree Realty Corporation',

    'JPM-D': 'J P Morgan Chase & Co',

    'LAD': 'Lithia Motors, Inc.',

    'ARW': 'Arrow Electronics, Inc.',

    'SNDE': 'Sundance Energy Australia Limited',

    'IRIX': 'IRIDEX Corporation',

    'FGL': 'Fidelity and Guaranty Life',

    'CLVS': 'Clovis Oncology, Inc.',

    'MRIN': 'Marin Software Incorporated',

    'IMPR': 'Imprivata, Inc.',

    'ATKR': 'Atkore International Group Inc.',

    'IDSA': 'Industrial Services of America, Inc.',

    'CGG': 'CGG',

    'DRRX': 'Durect Corporation',

    'MGH': 'Minco Gold Corporation',

    'QHC': 'Quorum Health Corporation',

    'SRV': 'The Cushing MLP Total Return Fund',

    'AGND': 'WisdomTree Barclays U.S. Aggregate Bond Negative Duration Fund',

    'SCD': 'LMP Capital and Income Fund Inc.',

    'ZIV': 'region',

    'ALLY-A': 'Ally Financial Inc.',

    'GWRE': 'Guidewire Software, Inc.',

    'BIOS': 'BioScrip, Inc.',

    'VKI': 'Invesco Advantage Municipal Income Trust II',

    'SGBK': 'Stonegate Bank',

    'ZEN': 'Zendesk, Inc.',

    'COHR': 'Coherent, Inc.',

    'JBN': 'Select Asset Inc.',

    'ETW': 'Eaton Vance Corporation',

    'HZO': 'MarineMax, Inc.',

    'BKN': 'BlackRock Investment Quality Municipal Trust Inc. (The)',

    'MPCT': 'iShares Sustainable MSCI Global Impact ETF',

    'RPAI-A': 'Retail Properties of America, Inc.',

    'UHT': 'Universal Health Realty Income Trust',

    'KONE': 'Kingtone Wirelessinfo Solution Holding Ltd',

    'GXP-D': 'Great Plains Energy Inc',

    'ELNK': 'EarthLink Holdings Corp.',

    'CLUB': 'Town Sports International Holdings, Inc.',

    'AN': 'AutoNation, Inc.',

    'NOW': 'ServiceNow, Inc.',

    'ALOG': 'Analogic Corporation',

    'BKJ': 'Bancorp of New Jersey, Inc',

    'ELJ': 'Entergy Louisiana, Inc.',

    'VRAY': 'ViewRay, Inc.',

    'KRC-H': 'Kilroy Realty Corporation',

    'MIFI': 'Novatel Wireless, Inc.',

    'WBC': 'Wabco Holdings Inc.',

    'VTAE': 'Vitae Pharmaceuticals, Inc.',

    'ETRM': 'EnteroMedics Inc.',

    'HLIT': 'Harmonic Inc.',

    'CTX': 'Qwest Corporation',

    'SELB': 'Selecta Biosciences, Inc.',

    'FOMX': 'Foamix Pharmaceuticals Ltd.',

    'BEN': 'Franklin Resources, Inc.',

    'IF': 'Aberdeen Indonesia Fund, Inc.',

    'CASS': 'Cass Information Systems, Inc',

    'COYN': 'COPsync, Inc.',

    'NVAX': 'Novavax, Inc.',

    'EGHT': '8x8 Inc',

    'HSBC': 'HSBC Holdings plc',

    'MITT': 'AG Mortgage Investment Trust, Inc.',

    'MTBC': 'Medical Transcription Billing, Corp.',

    'BKSC': 'Bank of South Carolina Corp.',

    'UTG': 'Reaves Utility Income Fund',

    'IMDZ': 'Immune Design Corp.',

    'ASPN': 'Aspen Aerogels, Inc.',

    'LODE': 'Comstock Mining, Inc.',

    'MER-P': 'Merrill Lynch & Co., Inc.',

    'IHC': 'Independence Holding Company',

    'IBKR': 'Interactive Brokers Group, Inc.',

    'FMI': 'Foundation Medicine, Inc.',

    'EVAR': 'Lombard Medical, Inc.',

    'ABEV': 'Ambev S.A.',

    'AYA': 'Amaya Inc.',

    'CHI': 'Calamos Convertible Opportunities and Income Fund',

    'SCM': 'Stellus Capital Investment Corporation',

    'HFC': 'HollyFrontier Corporation',

    'JOY': 'Joy Global Inc.',

    'PRMW': 'Primo Water Corporation',

    'BAC-W': 'Bank of America Corporation',

    'XEC': 'Cimarex Energy Co',

    'P': 'Pandora Media, Inc.',

    'TTC': 'Toro Company (The)',

    'EXD': 'Eaton Vance Tax-Advantaged Bond',

    'NCOM': 'National Commerce Corporation',

    'TFSCR': '1347 Capital Corp.',

    'MLP': 'Maui Land & Pineapple Company, Inc.',

    'BLUE': 'bluebird bio, Inc.',

    'IXYS': 'IXYS Corporation',

    'ELB': 'Entergy Louisiana, Inc.',

    'NHF': 'NexPoint Credit Stategies Fund',

    'MS-I': 'Morgan Stanley',

    'UMPQ': 'Umpqua Holdings Corporation',

    'VCSH': 'Vanguard Short-Term Corporate Bond ETF',

    'EMJ': 'Eaton Vance New Jersey Municipal Bond Fund',

    'XPLR': 'Xplore Technologies Corp',

    'CYTR': 'CytRx Corporation',

    'VIVO': 'Meridian Bioscience Inc.',

    'PNTR': 'Pointer Telocation Ltd.',

    'WWD': 'Woodward, Inc.',

    'CPAH': 'CounterPath Corporation',

    'PVG': 'Pretium Resources, Inc.',

    'IRT': 'Independence Realty Trust, Inc.',

    'FLO': 'Flowers Foods, Inc.',

    'AHL': 'Aspen Insurance Holdings Limited',

    'MFG': 'Mizuho Financial Group, Inc.',

    'DPZ': 'Domino\'s Pizza Inc',

    'NUV': 'Nuveen AMT-Free Municipal Value Fund',

    'GEL': 'Genesis Energy, L.P.',

    'HWAY': 'Healthways, Inc.',

    'RLI': 'RLI Corp.',

    'GRFS': 'Grifols, S.A.',

    'NMFC': 'New Mountain Finance Corporation',

    'BSFT': 'BroadSoft, Inc.',

    'STI-E': 'SunTrust Banks, Inc.',

    'CNK': 'Cinemark Holdings Inc',

    'BLIN          ': 'Bridgeline Digital, Inc.',

    'SHLM': 'A. Schulman, Inc.',

    'IDI': 'IDI, Inc.',

    'AL': 'Air Lease Corporation',

    'SPWH': 'Sportsman\'s Warehouse Holdings, Inc.',

    'STT-E': 'State Street Corporation',

    'AGO-E': 'Assured Guaranty Ltd.',

    'LUB': 'Luby\'s, Inc.',

    'GLBZ': 'Glen Burnie Bancorp',

    'NCLH': 'Norwegian Cruise Line Holdings Ltd.',

    'FRC-A': 'FIRST REPUBLIC BANK',

    'ESES': 'Eco-Stim Energy Solutions, Inc.',

    'ANGI': 'Angie\'s List, Inc.',

    'ELS-C': 'Equity Lifestyle Properties, Inc.',

    'DLNG-A': 'Dynagas LNG Partners LP',

    'NDSN': 'Nordson Corporation',

    'SHLX': 'Shell Midstream Partners, L.P.',

    'NHC': 'National HealthCare Corporation',

    'HST': 'Host Hotels & Resorts, Inc.',

    'BTO': 'John Hancock Financial Opportunities Fund',

    'CEVA': 'CEVA, Inc.',

    'IBIO': 'iBio, Inc.',

    'AIQ': 'Alliance HealthCare Services, Inc.',

    'CBT': 'Cabot Corporation',

    'CST': 'CST Brands, Inc.',

    'COYNW': 'COPsync, Inc.',

    'KYO': 'Kyocera Corporation',

    'OAKS': 'Five Oaks Investment Corp.',

    'TCO-K': 'Taubman Centers, Inc.',

    'NNN': 'National Retail Properties',

    'JAZZ': 'Jazz Pharmaceuticals plc',

    'GCAP': 'GAIN Capital Holdings, Inc.',

    'FCCO': 'First Community Corporation',

    'EFF': 'Eaton vance Floating-Rate Income Plus Fund',

    'OMN': 'OMNOVA Solutions Inc.',

    'ACLS': 'Axcelis Technologies, Inc.',

    'LOW': 'Lowe\'s Companies, Inc.',

    'IART': 'Integra LifeSciences Holdings Corporation',

    'CHMI': 'Cherry Hill Mortgage Investment Corporation',

    'GAINN': 'Gladstone Investment Corporation',

    'JDD': 'Nuveen Diversified Dividend and Income Fund',

    'NM': 'Navios Maritime Holdings Inc.',

    'AERI': 'Aerie Pharmaceuticals, Inc.',

    'TZOO': 'Travelzoo Inc.',

    'C-K': 'Citigroup Inc.',

    'NEFF': 'Neff Corporation',

    'SNHY': 'Sun Hydraulics Corporation',

    'PPS': 'Post Properties, Inc.',

    'OME': 'Omega Protein Corporation',

    'EQT': 'EQT Corporation',

    'VSEC': 'VSE Corporation',

    'STJ': 'St. Jude Medical, Inc.',

    'SNOW': 'Intrawest Resorts Holdings, Inc.',

    'OFG-D': 'OFG Bancorp',

    'CLAC': 'Capitol Acquisition Corp. III',

    'SYT': 'Syngenta AG',

    'ZN': 'Zion Oil & Gas Inc',

    'VISN': 'VisionChina Media, Inc.',

    'VRTB': 'Vestin Realty Mortgage II, Inc.',

    'PRSC': 'The Providence Service Corporation',

    'CNXC': 'CNX Coal Resources LP',

    'CCS': 'Century Communities, Inc.',

    'YY': 'YY Inc.',

    'QBAK': 'Qualstar Corporation',

    'PNRA': 'Panera Bread Company',

    'TILE': 'Interface, Inc.',

    'DCM': 'NTT DOCOMO, Inc',

    'TSRO': 'TESARO, Inc.',

    'LAZ': 'Lazard Ltd.',

    'CWBC': 'Community West Bancshares',

    'NTG': 'Tortoise MLP Fund, Inc.',

    'HIIQ': 'Health Insurance Innovations, Inc.',

    'OGXI': 'OncoGenex Pharmaceuticals Inc.',

    'THC': 'Tenet Healthcare Corporation',

    'GSI': 'General Steel Holdings, Inc.',

    'CHEKW': 'Check-Cap Ltd.',

    'JBHT': 'J.B. Hunt Transport Services, Inc.',

    'WSBC': 'WesBanco, Inc.',

    'STML': 'Stemline Therapeutics, Inc.',

    'MCR': 'MFS Charter Income Trust',

    'STR': 'Questar Corporation',

    'HBANO': 'Huntington Bancshares Incorporated',

    'GCVRZ': 'Sanofi',

    'APA': 'Apache Corporation',

    'GYB': 'CABCO Series 2004-101 Trust',

    'EQM': 'EQT Midstream Partners, LP',

    'HTGX': 'Hercules Capital, Inc.',

    'ZAYO': 'Zayo Group Holdings, Inc.',

    'NNN-D': 'National Retail Properties',

    'RZB': 'Reinsurance Group of America, Incorporated',

    'PNX': 'Phoenix Companies, Inc. (The)',

    'SGNT': 'Sagent Pharmaceuticals, Inc.',

    'WK': 'Workiva Inc.',

    'FV': 'First Trust Dorsey Wright Focus 5 ETF',

    'ACP': 'Avenue Income Credit Strategies Fund',

    'BLKB': 'Blackbaud, Inc.',

    'NAUH': 'National American University Holdings, Inc.',

    'SCE-H': 'Southern California Edison Company',

    'PAC': 'Grupo Aeroportuario Del Pacifico, S.A. de C.V.',

    'VLY-A': 'Valley National Bancorp',

    'AED': 'Aegon NV',

    'KLXI': 'KLX Inc.',

    'ENB': 'Enbridge Inc',

    'ORA': 'Ormat Technologies, Inc.',

    'GGAC': 'Garnero Group Acquisition Company',

    'AVAV': 'AeroVironment, Inc.',

    'MHLD': 'Maiden Holdings, Ltd.',

    'KEP': 'Korea Electric Power Corporation',

    'USCR': 'U S Concrete, Inc.',

    'ASM': 'Avino Silver',

    'CFR-A': 'Cullen/Frost Bankers, Inc.',

    'AMWD': 'American Woodmark Corporation',

    'VCYT': 'Veracyte, Inc.',

    'COP': 'ConocoPhillips',

    'MHN': 'Blackrock MuniHoldings New York Quality Fund, Inc.',

    'HQCL': 'Hanwha Q CELLS Co., Ltd. ',

    'OIS': 'Oil States International, Inc.',

    'PHF': 'Pacholder High Yield Fund, Inc.',

    'FGP': 'Ferrellgas Partners, L.P.',

    'AUDC': 'AudioCodes Ltd.',

    'QIWI': 'QIWI plc',

    'CLBH': 'Carolina Bank Holdings Inc.',

    'AMID': 'American Midstream Partners, LP',

    'KAP': 'KCAP Financial, Inc.',

    'UZA': 'United States Cellular Corporation',

    'SBLKL': 'Star Bulk Carriers Corp.',

    'PRTA': 'Prothena Corporation plc',

    'BAA': 'BANRO CORPORATION',

    'HASI': 'Hannon Armstrong Sustainable Infrastructure Capital, Inc.',

    'WVVIP': 'Willamette Valley Vineyards, Inc.',

    'CCA': 'MFS California Insured Municipal Trust',

    'LADR': 'Ladder Capital Corp',

    'ATEC': 'Alphatec Holdings, Inc.',

    'KMF': 'Kayne Anderson Midstream Energy Fund, Inc',

    'UAM': 'Universal American Corp.',

    'VRX': 'Valeant Pharmaceuticals International, Inc.',

    'ITEQ': 'BlueStar TA-BIGITech Israel Technology ETF',

    'RLGT': 'Radiant Logistics, Inc.',

    'MARPS': 'Marine Petroleum Trust',

    'CSI': 'Cutwater Select Income Fund',

    'HGH': 'Hartford Financial Services Group, Inc. (The)',

    'SHOO': 'Steven Madden, Ltd.',

    'MEG': 'Media General, Inc.',

    'MOMO': 'Momo Inc.',

    'LJPC': 'La Jolla Pharmaceutical Company',

    'RF-A': 'Regions Financial Corporation',

    'CHCT': 'Community Healthcare Trust Incorporated',

    'CPRT': 'Copart, Inc.',

    'CMRE-D': 'Costamare Inc.',

    'CSGP': 'CoStar Group, Inc.',

    'COWNL': 'Cowen Group, Inc.',

    'FHCO': 'Female Health Company (The)',

    'CPE': 'Callon Petroleum Company',

    'BIB': 'ProShares Ultra Nasdaq Biotechnology',

    'OSTK': 'Overstock.com, Inc.',

    'NGVT': 'Ingevity Corporation',

    'XGTIW': 'XG Technology, Inc',

    'OSN': 'Ossen Innovation Co., Ltd.',

    'KLAC': 'KLA-Tencor Corporation',

    'DLBL': 'region',

    'EBAY': 'eBay Inc.',

    'ABE           ': 'Aberdeen Emerging Markets Smaller Company Opportunities Fund I',

    'KMPH': 'KemPharm, Inc.',

    'VOC': 'VOC Energy Trust',

    'PKI': 'PerkinElmer, Inc.',

    'ALQA': 'Alliqua BioMedical, Inc.',

    'MLR': 'Miller Industries, Inc.',

    'EACQW': 'Easterly Acquisition Corp.',

    'BKHU': 'Black Hills Corporation',

    'ZBRA': 'Zebra Technologies Corporation',

    'NGD': 'NEW GOLD INC.',

    'VNRBP': 'Vanguard Natural Resources LLC',

    'MOG.A': 'Moog Inc.',

    'CCMP': 'Cabot Microelectronics Corporation',

    'APU': 'AmeriGas Partners, L.P.',

    'SNC': 'State National Companies, Inc.',

    'APIC': 'Apigee Corporation',

    'FPRX': 'Five Prime Therapeutics, Inc.',

    'PHII': 'PHI, Inc.',

    'BPL': 'Buckeye Partners L.P.',

    'ZX': 'China Zenix Auto International Limited',

    'FOE': 'Ferro Corporation',

    'TSCO': 'Tractor Supply Company',

    'CHA': 'China Telecom Corp Ltd',

    'PRTY': 'Party City Holdco Inc.',

    'PUMP': 'Asante Solutions, Inc.',

    'ZYNE': 'Zynerba Pharmaceuticals, Inc.',

    'CRCM': 'Care.com, Inc.',

    'IFON': 'InfoSonics Corp',

    'NATI': 'National Instruments Corporation',

    'R': 'Ryder System, Inc.',

    'TSRA': 'Tessera Technologies, Inc.',

    'PNR': 'Pentair plc.',

    'UNB': 'Union Bankshares, Inc.',

    'TBIO': 'Transgenomic, Inc.',

    'CTSO': 'Cytosorbents Corporation',

    'PFPT': 'Proofpoint, Inc.',

    'NYMX': 'Nymox Pharmaceutical Corporation',

    'ICA': 'Empresas Ica Soc Contrladora',

    'ULTI': 'The Ultimate Software Group, Inc.',

    'CART': 'Carolina Trust Bank',

    'YRD': 'Yirendai Ltd.',

    'IROQ': 'IF Bancorp, Inc.',

    'FGM': 'First Trust Germany AlphaDEX Fund',

    'CIK': 'Credit Suisse Asset Management Income Fund, Inc.',

    'BYBK': 'Bay Bancorp, Inc.',

    'LIME': 'Lime Energy Co.',

    'FFKT': 'Farmers Capital Bank Corporation',

    'LGND': 'Ligand Pharmaceuticals Incorporated',

    'NDAQ': 'Nasdaq, Inc.',

    'HVT.A': 'Haverty Furniture Companies, Inc.',

    'SAN-B': 'Banco Santander, S.A.',

    'HNW': 'Pioneer Diversified High Income Trust',

    'ULTA': 'Ulta Salon, Cosmetics & Fragrance, Inc.',

    'SLQD': 'iShares 0-5 Year Investment Grade Corporate Bond ETF',

    'CUBI-C': 'Customers Bancorp, Inc',

    'EAGLU': 'Double Eagle Acquisition Corp.',

    'DWTR': 'PowerShares DWA Tactical Sector Rotation Portfolio',

    'KYE': 'Kayne Anderson Energy Total Return Fund, Inc.',

    'WAGE': 'WageWorks, Inc.',

    'BEL': 'Belmond Ltd.',

    'MTGE': 'American Capital Mortgage Investment Corp.',

    'PTSI': 'P.A.M. Transportation Services, Inc.',

    'RYAM': 'Rayonier Advanced Materials Inc.',

    'PSCE': 'PowerShares S&P SmallCap Energy Portfolio',

    'SE': 'Spectra Energy Corp',

    'FMD': 'First Marblehead Corporation (The)',

    'NTRA': 'Natera, Inc.',

    'EIG': 'Employers Holdings Inc',

    'PFBI': 'Premier Financial Bancorp, Inc.',

    'VNO-J': 'Vornado Realty Trust',

    'BREW': 'Craft Brew Alliance, Inc.',

    'OSHC': 'Ocean Shore Holding Co.',

    'SILC': 'Silicom Ltd',

    'RSO-A': 'Resource Capital Corp.',

    'PNM': 'PNM Resources, Inc. (Holding Co.)',

    'FSBK': 'First South Bancorp Inc',

    'NNN-E': 'National Retail Properties',

    'HBNC': 'Horizon Bancorp (IN)',

    'JRJR': 'JRjr33, Inc.',

    'SHI': 'SINOPEC Shangai Petrochemical Company, Ltd.',

    'MCS': 'Marcus Corporation (The)',

    'KT': 'KT Corporation',

    'BRKL': 'Brookline Bancorp, Inc.',

    'UNVR': 'Univar Inc.',

    'IDCC': 'InterDigital, Inc.',

    'HUBB': 'Hubbell Inc',

    'ENVA': 'Enova International, Inc.',

    'ROBO': 'ROBO Global Robotics and Automation Index ETF',

    'BUI': 'BlackRock Utility and Infrastructure Trust',

    'ECYT': 'Endocyte, Inc.',

    'TIVO': 'TiVo Inc.',

    'TDS': 'Telephone and Data Systems, Inc.',

    'AMG': 'Affiliated Managers Group, Inc.',

    'OMAM': 'OM Asset Management plc',

    'GS-B': 'Goldman Sachs Group, Inc. (The)',

    'LGIH': 'LGI Homes, Inc.',

    'LXK': 'Lexmark International, Inc.',

    'OASM': 'Oasmia Pharmaceutical AB',

    'ANTX': 'Anthem, Inc.',

    'MPEL': 'Melco Crown Entertainment Limited',

    'UVV': 'Universal Corporation',

    'WST': 'West Pharmaceutical Services, Inc.',

    'DY': 'Dycom Industries, Inc.',

    'GFI': 'Gold Fields Limited',

    'AOI': 'Alliance One International, Inc.',

    'GOOD': 'Gladstone Commercial Corporation',

    'GFF': 'Griffon Corporation',

    'DDR': 'DDR Corp.',

    'AGLE': 'Aeglea BioTherapeutics, Inc.',

    'BANF': 'BancFirst Corporation',

    'SCAI': 'Surgical Care Affiliates, Inc.',

    'OFG': 'OFG Bancorp',

    'SCSS': 'Select Comfort Corporation',

    'PES': 'Pioneer Energy Services Corp.',

    'FSTR': 'L.B. Foster Company',

    'ACFC': 'Atlantic Coast Financial Corporation',

    'DRII': 'Diamond Resorts International, Inc.',

    'CFX': 'Colfax Corporation',

    'OFC': 'Corporate Office Properties Trust',

    'WPG-I': 'WP Glimcher Inc.',

    'JHY': 'Nuveen High Income 2020 Target Term Fund',

    'NGVC': 'Natural Grocers by Vitamin Cottage, Inc.',

    'MNI': 'McClatchy Company (The)',

    'DISCB': 'Discovery Communications, Inc.',

    'IRMD': 'iRadimed Corporation',

    'SOV-C': 'Santander Holdings USA, Inc.',

    'BMS': 'Bemis Company, Inc.',

    'AVGR': 'Avinger, Inc.',

    'PTR': 'PetroChina Company Limited',

    'HNI': 'HNI Corporation',

    'CELP': 'Cypress Energy Partners, L.P.',

    'SNI': 'Scripps Networks Interactive, Inc',

    'FNFV': 'Fidelity National Financial, Inc.',

    'MOBL': 'MobileIron, Inc.',

    'SRCL': 'Stericycle, Inc.',

    'ESCA': 'Escalade, Incorporated',

    'HES': 'Hess Corporation',

    'MITL': 'Mitel Networks Corporation',

    'OCLS': 'Oculus Innovative Sciences, Inc.',

    'SEM': 'Select Medical Holdings Corporation',

    'XRM': 'Xerium Technologies, Inc.',

    'MH-C': 'Maiden Holdings, Ltd.',

    'ICLD': 'InterCloud Systems, Inc',

    'TLI': 'Western Asset Corporate Loan Fund Inc',

    'VALX': 'Validea Market Legends ETF',

    'BIG': 'Big Lots, Inc.',

    'RS': 'Reliance Steel & Aluminum Co.',

    'NFJ': 'AllianzGI NFJ Dividend, Interest & Premium Strategy Fund',

    'DOV': 'Dover Corporation',

    'EDU': 'New Oriental Education & Technology Group, Inc.',

    'TOPS': 'TOP Ships Inc.',

    'SPG': 'Simon Property Group, Inc.',

    'ERA': 'Era Group, Inc.',

    'PERF': 'Perfumania Holdings, Inc',

    'UGI': 'UGI Corporation',

    'CGO': 'Calamos Global Total Return Fund',

    'DMO': 'Western Asset Mortgage Defined Opportunity Fund Inc',

    'FPO': 'First Potomac Realty Trust',

    'CCK': 'Crown Holdings, Inc.',

    'OSUR': 'OraSure Technologies, Inc.',

    'PDCO': 'Patterson Companies, Inc.',

    'AMBCW': 'Ambac Financial Group, Inc.',

    'BWL.A': 'Bowl America, Inc.',

    'PLG': 'Platinum Group Metals Ltd.',

    'CBPX': 'Continental Building Products, Inc.',

    'NSAT': 'Norsat International Inc.',

    'PANL': 'Pangaea Logistics Solutions Ltd.',

    'PCTI': 'PC-Tel, Inc.',

    'IFMI': 'Institutional Financial Markets, Inc.',

    'PAR': 'PAR Technology Corporation',

    'SMIT': 'Schmitt Industries, Inc.',

    'DAR': 'Darling Ingredients Inc.',

    'TLN': 'Talen Energy Corporation',

    'CONG': 'congatec Holding AG',

    'FPXI': 'First Trust International IPO ETF',

    'BSF': 'Bear State Financial, Inc.',

    'GEOS': 'Geospace Technologies Corporation',

    'PUK': 'Prudential Public Limited Company',

    'ETH': 'Ethan Allen Interiors Inc.',

    'XXII': '22nd Century Group, Inc',

    'APWC': 'Asia Pacific Wire & Cable Corporation Limited',

    'CLA': 'Capitala Finance Corp.',

    'SYNL': 'Synalloy Corporation',

    'ABC': 'AmerisourceBergen Corporation (Holding Co)',

    'WINS': 'Wins Finance Holdings Inc.',

    'WM': 'Waste Management, Inc.',

    'EXA': 'Exa Corporation',

    'APH': 'Amphenol Corporation',

    'ELY': 'Callaway Golf Company',

    'MPSX': 'Multi Packaging Solutions International Limited',

    'NVTA': 'Invitae Corporation',

    'KGC': 'Kinross Gold Corporation',

    'BGG': 'Briggs & Stratton Corporation',

    'LIFE': 'aTyr Pharma, Inc.',

    'HBIO': 'Harvard Bioscience, Inc.',

    'FOXF': 'Fox Factory Holding Corp.',

    'HAS': 'Hasbro, Inc.',

    'NVFY': 'Nova Lifestyle, Inc',

    'PCH': 'Potlatch Corporation',

    'EAGLW': 'Double Eagle Acquisition Corp.',

    'TDG': 'Transdigm Group Incorporated',

    'OLED': 'Universal Display Corporation',

    'CIM': 'Chimera Investment Corporation',

    'TRIL': 'Trillium Therapeutics Inc.',

    'ALL-E': 'Allstate Corporation (The)',

    'PNC-Q': 'PNC Financial Services Group, Inc. (The)',

    'AMED': 'Amedisys Inc',

    'OTEL': 'Otelco Inc.',

    'GNMA': 'iShares GNMA Bond ETF',

    'MMS': 'Maximus, Inc.',

    'CCO': 'Clear Channel Outdoor Holdings, Inc.',

    'NCT-B': 'Newcastle Investment Corporation',

    'BLD': 'TopBuild Corp.',

    'NGHCP': 'National General Holdings Corp',

    'MFRI': 'MFRI, Inc.',

    'SJI': 'South Jersey Industries, Inc.',

    'ATHX': 'Athersys, Inc.',

    'BWA': 'BorgWarner Inc.',

    'INST': 'Instructure, Inc.',

    'KLDX': 'Klondex Mines Ltd.',

    'SSBI': 'Summit State Bank',

    'HHC': 'Howard Hughes Corporation (The)',

    'FXCM': 'FXCM Inc.',

    'TDA': 'Telephone and Data Systems, Inc.',

    'FAD': 'First Trust Multi Cap Growth AlphaDEX Fund',

    'UFI': 'Unifi, Inc.',

    'BGI': 'Birks Group Inc.',

    'CRD.A': 'Crawford & Company',

    'UQM': 'UQM TECHNOLOGIES INC',

    'STM': 'STMicroelectronics N.V.',

    'ASFI': 'Asta Funding, Inc.',

    'WAL': 'Western Alliance Bancorporation',

    'RGC': 'Regal Entertainment Group',

    'HNR': 'Harvest Natural Resources Inc',

    'CPAC': 'Cementos Pacasmayo S.A.A.',

    'JCS': 'Communications Systems, Inc.',

    'ONE           ': 'Higher One Holdings, Inc.',

    'TITN': 'Titan Machinery Inc.',

    'LM': 'Legg Mason, Inc.',

    'HLM-': 'Hillman Group Capital Trust',

    'DFVS': 'region',

    'JPM': 'J P Morgan Chase & Co',

    'IOTS': 'Adesto Technologies Corporation',

    'UUUU': 'Energy Fuels Inc',

    'GSS': 'Golden Star Resources, Ltd',

    'SMT': 'SMART Technologies Inc.',

    'TROVW': 'TrovaGene, Inc.',

    'AVP': 'Avon Products, Inc.',

    'SPB           ': 'Spectrum Brands Holdings, Inc.',

    'FTNT': 'Fortinet, Inc.',

    'PSB-S': 'PS Business Parks, Inc.',

    'NSM': 'Nationstar Mortgage Holdings Inc.',

    'CRTN': 'Cartesian, Inc.',

    'ITUB': 'Itau Unibanco Banco Holding SA',

    'DEI': 'Douglas Emmett, Inc.',

    'CB': 'D/B/A Chubb Limited New',

    'FKO': 'First Trust South Korea AlphaDEX Fund',

    'CVRS': 'Corindus Vascular Robotics, Inc.',

    'ARGS': 'Argos Therapeutics, Inc.',

    'IVR-A': 'Invesco Mortgage Capital Inc.',

    'RGLD': 'Royal Gold, Inc.',

    'AEE': 'Ameren Corporation',

    'CBLI': 'Cleveland BioLabs, Inc.',

    'PE': 'Parsley Energy, Inc.',

    'BBN': 'BalckRock Taxable Municipal Bond Trust',

    'BANFP': 'BancFirst Corporation',

    'MOH': 'Molina Healthcare Inc',

    'XONE': 'The ExOne Company',

    'EEA': 'European Equity Fund, Inc. (The)',

    'SRPT': 'Sarepta Therapeutics, Inc.',

    'MAB': 'Eaton Vance Massachusetts Municipal Bond Fund',

    'DG': 'Dollar General Corporation',

    'NVO': 'Novo Nordisk A/S',

    'HYND': 'WisdomTree BofA Merrill Lynch High Yield Bond Negative Duratio',

    'BABA': 'Alibaba Group Holding Limited',

    'IRCP': 'IRSA Propiedades Comerciales S.A.',

    'SBGL': 'Sibanye Gold Limited',

    'FMS': 'Fresenius Medical Care Corporation',

    'VMET': 'Viamet Pharmaceuticals Corp.',

    'CBMG': 'Cellular Biomedicine Group, Inc.',

    'PCQ': 'PIMCO California Municipal Income Fund',

    'ALIM': 'Alimera Sciences, Inc.',

    'TIF': 'Tiffany & Co.',

    'CDTX': 'Cidara Therapeutics, Inc.',

    'ADM': 'Archer-Daniels-Midland Company',

    'LORL': 'Loral Space and Communications, Inc.',

    'CSQ': 'Calamos Strategic Total Return Fund',

    'MCC': 'Medley Capital Corporation',

    'UGP': 'Ultrapar Participacoes S.A.',

    'FAAR': 'First Trust Alternative Absolute Return Strategy ETF',

    'LABL': 'Multi-Color Corporation',

    'TIK': 'Tel-Instrument Electronics Corp.',

    'BRKR': 'Bruker Corporation',

    'CSOD': 'Cornerstone OnDemand, Inc.',

    'APPF': 'AppFolio, Inc.',

    'GBLIZ': 'Global Indemnity plc',

    'HLS': 'HealthSouth Corporation',

    'DM': 'Dominion Midstream Partners, LP',

    'TRNO': 'Terreno Realty Corporation',

    'ARR-B': 'ARMOUR Residential REIT, Inc.',

    'OTIC': 'Otonomy, Inc.',

    'CFO': 'Victory CEMP US 500 Enhanced Volatility Wtd Index ETF',

    'FBR': 'Fibria Celulose S.A.',

    'AEMD': 'Aethlon Medical, Inc.',

    'VALU': 'Value Line, Inc.',

    'GUT-A': 'Gabelli Utility Trust (The)',

    'PNFP': 'Pinnacle Financial Partners, Inc.',

    'AVH': 'Avianca Holdings S.A.',

    'BIIB': 'Biogen Inc.',

    'TRXC': 'TransEnterix, Inc.',

    'KMI.WS': 'Kinder Morgan, Inc.',

    'MJCO': 'Majesco',

    'TGC': 'Tengasco, Inc.',

    'LTBR': 'Lightbridge Corporation',

    'CXDC': 'China XD Plastics Company Limited',

    'CVB': 'Lehman ABS Corporation',

    'SCE-G': 'Southern California Edison Company',

    'AUMN': 'Golden Minerals Company',

    'GGP': 'General Growth Properties, Inc.',

    'KEF': 'Korea Equity Fund, Inc.',

    'GDEN': 'Golden Entertainment, Inc.',

    'CTG': 'Computer Task Group, Incorporated',

    'EIX': 'Edison International',

    'CLI': 'Mack-Cali Realty Corporation',

    'TPUB': 'Tribune Publishing Company',

    'MCEP': 'Mid-Con Energy Partners, LP',

    'CEZ': 'Victory CEMP Emerging Market Volatility Wtd Index ETF',

    'ENJ': 'Entergy New Orleans, Inc.',

    'VSTM': 'Verastem, Inc.',

    'MFSF': 'MutualFirst Financial Inc.',

    'VASC': 'Vascular Solutions, Inc.',

    'FNSR': 'Finisar Corporation',

    'MBFIP': 'MB Financial Inc.',

    'SNA': 'Snap-On Incorporated',

    'CPHI': 'China Pharma Holdings, Inc.',

    'LQ': 'La Quinta Holdings Inc.',

    'LSBG': 'Lake Sunapee Bank Group',

    'CATO': 'Cato Corporation (The)',

    'PFLT': 'PennantPark Floating Rate Capital Ltd.',

    'MBT': 'Mobile TeleSystems OJSC',

    'FUN': 'Cedar Fair, L.P.',

    'MYF': 'Blackrock MuniYield Investment Fund',

    'MCBC': 'Macatawa Bank Corporation',

    'HUBG': 'Hub Group, Inc.',

    'SNMX': 'Senomyx, Inc.',

    'GNK': 'Genco Shipping & Trading Limited Warrants Expiring 12/31/2021 ',

    'PBFX': 'PBF Logistics LP',

    'CCIH': 'ChinaCache International Holdings Ltd.',

    'UBNT': 'Ubiquiti Networks, Inc.',

    'NHLD': 'National Holdings Corporation',

    'REG': 'Regency Centers Corporation',

    'VRTV': 'Veritiv Corporation',

    'MTR': 'Mesa Royalty Trust',

    'MILN': 'Global X Millennials Thematic ETF',

    'UTMD': 'Utah Medical Products, Inc.',

    'WF': 'Woori Bank',

    'COTY': 'Coty Inc.',

    'HALO': 'Halozyme Therapeutics, Inc.',

    'STAR          ': 'iStar Financial Inc.',

    'AZPN': 'Aspen Technology, Inc.',

    'NSPH': 'Nanosphere, Inc.',

    'NNBR': 'NN, Inc.',

    'OVAS': 'Ovascience Inc.',

    'OLP': 'One Liberty Properties, Inc.',

    'VLY': 'Valley National Bancorp',

    'CPN': 'Calpine Corporation',

    'TRMB': 'Trimble Navigation Limited',

    'FCB': 'FCB Financial Holdings, Inc.',

    'GSV': 'Gold Standard Ventures Corporation',

    'EJ': 'E-House (China) Holdings Limited',

    'PHD': 'Pioneer Floating Rate Trust',

    'STT-D': 'State Street Corporation',

    'DFBG': 'Differential Brands Group Inc.',

    'SALT': 'Scorpio Bulkers Inc.',

    'INTC': 'Intel Corporation',

    'GJR': 'Synthetic Fixed-Income Securities, Inc.',

    'BGB': 'Blackstone / GSO Strategic Credit Fund',

    'SSW-E': 'Seaspan Corporation',

    'CALD': 'Callidus Software, Inc.',

    'MRC': 'MRC Global Inc.',

    'IRS': 'IRSA Inversiones Y Representaciones S.A.',

    'GEF.B': 'Greif Bros. Corporation',

    'IIM': 'Invesco Value Municipal Income Trust',

    'ECR': 'Eclipse Resources Corporation',

    'BAP': 'Credicorp Ltd.',

    'AER': 'Aercap Holdings N.V.',

    'OII': 'Oceaneering International, Inc.',

    'BBY': 'Best Buy Co., Inc.',

    'GHDX': 'Genomic Health, Inc.',

    'BLX': 'Banco Latinoamericano de Comercio Exterior, S.A.',

    'EXAR': 'Exar Corporation',

    'AXS-D': 'Axis Capital Holdings Limited',

    'ALL-F': 'Allstate Corporation (The)',

    'RBS-T': 'Royal Bank Scotland plc (The)',

    'AEIS': 'Advanced Energy Industries, Inc.',

    'FRC-D': 'FIRST REPUBLIC BANK',

    'AHC': 'A.H. Belo Corporation',

    'LVHD': 'Legg Mason Low Volatility High Dividend ETF',

    'APOG': 'Apogee Enterprises, Inc.',

    'TIME': 'Time Inc.',

    'ACRX': 'AcelRx Pharmaceuticals, Inc.',

    'VBLT': 'Vascular Biogenics Ltd.',

    'COMT': 'iShares Commodities Select Strategy ETF',

    'SWH': 'Stanley Black & Decker, Inc.',

    'YPRO': 'AdvisorShares YieldPro ETF',

    'LDR': 'Landauer, Inc.',

    'DAN': 'Dana Holding Corporation',

    'TAP.A': 'Molson Coors Brewing  Company',

    'CRDS': 'Crossroads Systems, Inc.',

    'GMO': 'General Moly, Inc',

    'CBL': 'CBL & Associates Properties, Inc.',

    'MTZ': 'MasTec, Inc.',

    'AWRE': 'Aware, Inc.',

    'MD': 'Mednax, Inc',

    'SAJA': 'Sajan, Inc.',

    'SC': 'Santander Consumer USA Holdings Inc.',

    'JEQ': 'Aberdeen Japan Equity Fund, Inc. ',

    'MG': 'Mistras Group Inc',

    'RBS': 'Royal Bank Scotland plc (The)',

    'DLA': 'Delta Apparel, Inc.',

    'AFSI-A': 'AmTrust Financial Services, Inc.',

    'BFS-C': 'Saul Centers, Inc.',

    'EAA': 'Entergy Arkansas, Inc.',

    'TCB-C': 'TCF Financial Corporation',

    'PFL': 'PIMCO Income Strategy Fund',

    'ETAK': 'Elephant Talk Communications Corp.',

    'HW': 'Headwaters Incorporated',

    'LITB': 'LightInTheBox Holding Co., Ltd.',

    'GWB': 'Great Western Bancorp, Inc.',

    'AOSL': 'Alpha and Omega Semiconductor Limited',

    'NTX': 'Nuveen Texas Quality Income Municipal Fund',

    'TSM': 'Taiwan Semiconductor Manufacturing Company Ltd.',

    'NHI': 'National Health Investors, Inc.',

    'IX': 'Orix Corp Ads',

    'ISCA': 'International Speedway Corporation',

    'UDF': 'United Development Funding IV',

    'WDFC': 'WD-40 Company',

    'PMT': 'PennyMac Mortgage Investment Trust',

    'BBL': 'BHP Billiton plc',

    'DBL': 'DoubleLine Opportunistic Credit Fund',

    'LSXMK': 'Liberty Media Corporation',

    'DEG': 'Etablissements Delhaize Freres et Cie &quot;Le Lion&quot; S.A.',

    'NEWR': 'New Relic, Inc.',

    'NNY': 'Nuveen New York Municipal Value Fund, Inc.',

    'ISR': 'IsoRay, Inc.',

    'CRVL': 'CorVel Corp.',

    'WLK': 'Westlake Chemical Corporation',

    'ELTK': 'Eltek Ltd.',

    'THQ': 'Tekla Healthcare Opportunies Fund',

    'CTW': 'Qwest Corporation',

    'AVNW': 'Aviat Networks, Inc.',

    'MAA': 'Mid-America Apartment Communities, Inc.',

    'MCF': 'Contango Oil & Gas Company',

    'PBB': 'Prospect Capital Corporation',

    'CX': 'Cemex S.A.B. de C.V.',

    'CPLP': 'Capital Product Partners L.P.',

    'IMUC': 'ImmunoCellular Therapeutics, Ltd.',

    'CRNT': 'Ceragon Networks Ltd.',

    'DCT': 'DCT Industrial Trust Inc',

    'SPXX': 'Nuveen S&P 500 Dynamic Overwrite Fund',

    'VIVE': 'Viveve Medical, Inc.',

    'LECO': 'Lincoln Electric Holdings, Inc.',

    'FSFG': 'First Savings Financial Group, Inc.',

    'GWGH': 'GWG Holdings, Inc',

    'AEP': 'American Electric Power Company, Inc.',

    'GPN': 'Global Payments Inc.',

    'NUM': 'Nuveen Michigan Quality Income Municipal Fund',

    'TRTLU': 'Terrapin 3 Acquisition Corporation',

    'BRKS': 'Brooks Automation, Inc.',

    'TCBI': 'Texas Capital Bancshares, Inc.',

    'WVVI': 'Willamette Valley Vineyards, Inc.',

    'GCP': 'GCP Applied Technologies Inc.',

    'NDLS': 'Noodles & Company',

    'FCN': 'FTI Consulting, Inc.',

    'EVC': 'Entravision Communications Corporation',

    'FITBI': 'Fifth Third Bancorp',

    'MSL': 'MidSouth Bancorp',

    'SIGM': 'Sigma Designs, Inc.',

    'CYRXW': 'CryoPort, Inc.',

    'ALL-C': 'Allstate Corporation (The)',

    'SPPI': 'Spectrum Pharmaceuticals, Inc.',

    'MNTX': 'Manitex International, Inc.',

    'IGA': 'Voya Global Advantage and Premium Opportunity Fund',

    'RQI': 'Cohen & Steers Quality Income Realty Fund Inc',

    'ATTO': 'Atento S.A.',

    'RCG': 'RENN Fund, Inc.',

    'GLQ': 'Clough Global Equity Fund',

    'TESS': 'TESSCO Technologies Incorporated',

    'TGT': 'Target Corporation',

    'NSIT': 'Insight Enterprises, Inc.',

    'CAS': 'Castle (A.M.) & Co.',

    'SHLO': 'Shiloh Industries, Inc.',

    'SPAR': 'Spartan Motors, Inc.',

    'BBGI': 'Beasley Broadcast Group, Inc.',

    'MFLX': 'Multi-Fineline Electronix, Inc.',

    'NSP': 'Insperity, Inc.',

    'ASB-B': 'Associated Banc-Corp',

    'ARA': 'American Renal Associates Holdings, Inc',

    'ANDAW': 'Andina Acquisition Corp. II',

    'FR': 'First Industrial Realty Trust, Inc.',

    'BCV': 'Bancroft Fund Limited',

    'SPR': 'Spirit Aerosystems Holdings, Inc.',

    'MESO': 'Mesoblast Limited',

    'NYH': 'Eaton Vance New York Municipal Bond Fund II',

    'CRL': 'Charles River Laboratories International, Inc.',

    'EP-C': 'El Paso Corporation',

    'VDTH': 'Videocon d2h Limited',

    'SCE-J': 'Southern California Edison Company',

    'BZUN': 'Baozun Inc.',

    'MZOR': 'Mazor Robotics Ltd.',

    'SLCA': 'U.S. Silica Holdings, Inc.',

    'ULBI': 'Ultralife Corporation',

    'IRM': 'Iron Mountain Incorporated',

    'KYN-G': 'Kayne Anderson MLP Investment Company',

    'RGLS': 'Regulus Therapeutics Inc.',

    'AETI': 'American Electric Technologies, Inc.',

    'TMK-B': 'Torchmark Corporation',

    'SBNYW': 'Signature Bank',

    'PCF': 'Putnam High Income Bond Fund',

    'GDOT': 'Green Dot Corporation',

    'SMP': 'Standard Motor Products, Inc.',

    'ASR': 'Grupo Aeroportuario del Sureste, S.A. de C.V.',

    'LXU': 'Lsb Industries Inc.',

    'NEE': 'NextEra Energy, Inc.',

    'VFC': 'V.F. Corporation',

    'MYN': 'Blackrock MuniYield New York Quality Fund, Inc.',

    'ESP': 'Espey Mfg. & Electronics Corp.',

    'AGMX': 'AutoGenomics, Inc.',

    'HTLF': 'Heartland Financial USA, Inc.',

    'ISSC': 'Innovative Solutions and Support, Inc.',

    'JMU': 'Wowo Limited',

    'TIS': 'Orchids Paper Products Company',

    'CMO': 'Capstead Mortgage Corporation',

    'TSLF': 'THL Credit Senior Loan Fund',

    'WR': 'Westar Energy, Inc.',

    'DLBS': 'region',

    'CEMP': 'Cempra, Inc.',

    'MBVT': 'Merchants Bancshares, Inc.',

    'BFZ': 'BlackRock California Municipal Income Trust',

    'ELLI': 'Ellie Mae, Inc.',

    'LHO-H': 'LaSalle Hotel Properties',

    'CCF': 'Chase Corporation',

    'RETA': 'Reata Pharmaceuticals, Inc.',

    'DCA': 'Virtus Total Return Fund',

    'IMMR': 'Immersion Corporation',

    'PCG-B': 'Pacific Gas & Electric Co.',

    'IVZ': 'Invesco Plc',

    'PRLB': 'Proto Labs, Inc.',

    'WY': 'Weyerhaeuser Company',

    'AIF': 'Apollo Tactical Income Fund Inc.',

    'PRTK': 'Paratek Pharmaceuticals, Inc. ',

    'QQQX': 'Nuveen NASDAQ 100 Dynamic Overwrite Fund',

    'DPLO': 'Diplomat Pharmacy, Inc.',

    'CLM': 'Cornerstone Strategic Value Fund, Inc.',

    'ENRJ': 'EnerJex Resources, Inc.',

    'MDVX': 'Medovex Corp.',

    'OEC': 'Orion Engineered Carbons S.A',

    'VBND': 'Vident Core U.S. Bond Strategy Fund',

    'KLREW': 'KLR Energy Acquisition Corp.',

    'MRD': 'Memorial Resource Development Corp.',

    'GS-A': 'Goldman Sachs Group, Inc. (The)',

    'FCCY': '1st Constitution Bancorp (NJ)',

    'AGM': 'Federal Agricultural Mortgage Corporation',

    'LBRDA': 'Liberty Broadband Corporation',

    'PVBC': 'Provident Bancorp, Inc.',

    'SLG-I': 'SL Green Realty Corporation',

    'GEH': 'General Electric Capital Corporation',

    'BOXL': 'Boxlight Corporation',

    'AMZN': 'Amazon.com, Inc.',

    'ETO': 'Eaton Vance Tax-Advantage Global Dividend Opp',

    'PZE': 'Petrobras Argentina S.A.',

    'CAR': 'Avis Budget Group, Inc.',

    'CHY': 'Calamos Convertible and High Income Fund',

    'MENT': 'Mentor Graphics Corporation',

    'PAY': 'Verifone Systems, Inc.',

    'ASMB': 'Assembly Biosciences, Inc.',

    'WIFI': 'Boingo Wireless, Inc.',

    'GIGA': 'Giga-tronics Incorporated',

    'LILAK': 'Liberty Global plc',

    'JUNO': 'Juno Therapeutics, Inc.',

    'PEIX': 'Pacific Ethanol, Inc.',

    'STRM': 'Streamline Health Solutions, Inc.',

    'MGR': 'Affiliated Managers Group, Inc.',

    'BIO.B': 'Bio-Rad Laboratories, Inc.',

    'AGII': 'Argo Group International Holdings, Ltd.',

    'GUID': 'Guidance Software, Inc.',

    'DPG': 'Duff & Phelps Global Utility Income Fund Inc.',

    'DPS': 'Dr Pepper Snapple Group, Inc',

    'SMFG': 'Sumitomo Mitsui Financial Group Inc',

    'BGSF': 'BG Staffing Inc',

    'KPTI': 'Karyopharm Therapeutics Inc.',

    'FEMS': 'First Trust Emerging Markets Small Cap AlphaDEX Fund',

    'CTAA': 'Qwest Corporation',

    'CBA           ': 'ClearBridge American Energy MLP Fund Inc.',

    'TQQQ': 'ProShares UltraPro QQQ',

    'OXLCN': 'Oxford Lane Capital Corp.',

    'MHLDO': 'Maiden Holdings, Ltd.',

    'ARE-D': 'Alexandria Real Estate Equities, Inc.',

    'BVSN': 'BroadVision, Inc.',

    'GALTW': 'Galectin Therapeutics Inc.',

    'ASBB': 'ASB Bancorp, Inc.',

    'SGC': 'Superior Uniform Group, Inc.',

    'EXPE': 'Expedia, Inc.',

    'ARMH': 'ARM Holdings plc',

    'ACSF': 'American Capital Senior Floating, Ltd.',

    'CAW': 'CCA Industries, Inc.',

    'NYLD.A': 'NRG Yield, Inc.',

    'CORR': 'CorEnergy Infrastructure Trust, Inc.',

    'CSL': 'Carlisle Companies Incorporated',

    'NYRT': 'New York REIT, Inc.',

    'WINA': 'Winmark Corporation',

    'PMM': 'Putnam Managed Municipal Income Trust',

    'HSTM': 'HealthStream, Inc.',

    'KSU-': 'Kansas City Southern',

    'PFIN': 'P & F Industries, Inc.',

    'SDRL': 'Seadrill Limited',

    'YLCO': 'Global X Yieldco Index ETF',

    'PNBK': 'Patriot National Bancorp Inc.',

    'PMF': 'PIMCO Municipal Income Fund',

    'GLOB': 'Globant S.A.',

    'EBIX': 'Ebix, Inc.',

    'SNFCA': 'Security National Financial Corporation',

    'TSNU': 'Tyson Foods, Inc.',

    'KST': 'Scudder Strategic Income Trust',

    'STBA': 'S&T Bancorp, Inc.',

    'AMNB': 'American National Bankshares, Inc.',

    'FCSC': 'Fibrocell Science Inc',

    'MIND': 'Mitcham Industries, Inc.',

    'NEE-K': 'NextEra Energy, Inc.',

    'T': 'AT&T Inc.',

    'FRAN': 'Francesca\'s Holdings Corporation',

    'ATU': 'Actuant Corporation',

    'TUTT': 'Tuttle Tactical Management U.S. Core ETF',

    'OCFC': 'OceanFirst Financial Corp.',

    'CSU': 'Capital Senior Living Corporation',

    'BHACR': 'Barington/Hilco Acquisition Corp.',

    'DDC': 'Dominion Diamond Corporation',

    'ACTX': 'Global X Guru Activist ETF',

    'EOG': 'EOG Resources, Inc.',

    'SLMBP': 'SLM Corporation',

    'NXN': 'Nuveen Insured New York Select Tax-Free Income Portfolio',

    'ESSF': 'ETRE REIT, LLC',

    'PFIS': 'Peoples Financial Services Corp. ',

    'HSEB': 'HSBC Holdings plc',

    'GLDI': 'Credit Suisse AG',

    'NNVC': 'NanoViricides, Inc.',

    'GALT': 'Galectin Therapeutics Inc.',

    'C-L': 'Citigroup Inc.',

    'PIRS': 'Pieris Pharmaceuticals, Inc.',

    'AAT': 'American Assets Trust, Inc.',

    'SQI': 'SciQuest, Inc.',

    'UDR': 'United Dominion Realty Trust, Inc.',

    'ORI': 'Old Republic International Corporation',

    'OSBC': 'Old Second Bancorp, Inc.',

    'BBT-D': 'BB&T Corporation',

    'OLLI': 'Ollie\'s Bargain Outlet Holdings, Inc.',

    'OC': 'Owens Corning Inc',

    'RCON': 'Recon Technology, Ltd.',

    'SCOR': 'comScore, Inc.',

    'BATRA': 'Liberty Media Corporation',

    'CRR': 'Carbo Ceramics, Inc.',

    'DSWL': 'Deswell Industries, Inc.',

    'AVGO': 'Broadcom Limited',

    'VNET': '21Vianet Group, Inc.',

    'DXI': 'DXI Energy Inc.',

    'CVTI': 'Covenant Transportation Group, Inc.',

    'NVDA': 'NVIDIA Corporation',

    'ROSG': 'Rosetta Genomics Ltd.',

    'MRUS': 'Merus N.V.',

    'SCS': 'Steelcase Inc.',

    'TEGP': 'Tallgrass Energy GP, LP',

    'EEMA': 'iShares MSCI Emerging Markets Asia Index Fund',

    'GMED': 'Globus Medical, Inc.',

    'PJC': 'Piper Jaffray Companies',

    'LAKE': 'Lakeland Industries, Inc.',

    'ZFGN': 'Zafgen, Inc.',

    'OMEX': 'Odyssey Marine Exploration, Inc.',

    'SFNC': 'Simmons First National Corporation',

    'UN': 'Unilever NV',

    'BBP': 'BioShares Biotechnology Products Fund',

    'ABY': 'Atlantica Yield plc',

    'STLY': 'Stanley Furniture Company, Inc.',

    'ANDA': 'Andina Acquisition Corp. II',

    'SAIA': 'Saia, Inc.',

    'DQ': 'DAQO New Energy Corp.',

    'NRF-E': 'Northstar Realty Finance Corp.',

    'PHM': 'PulteGroup, Inc.',

    'MEOH': 'Methanex Corporation',

    'BGS': 'B&G Foods, Inc.',

    'NGHCZ': 'National General Holdings Corp',

    'NVMI': 'Nova Measuring Instruments Ltd.',

    'ELRC': 'Electro Rent Corporation',

    'ONEQ': 'Fidelity Nasdaq Composite Index Tracking Stock',

    'AAV': 'Advantage Oil & Gas Ltd',

    'SOHU': 'Sohu.com Inc.',

    'DBD': 'Diebold, Incorporated',

    'CVO': 'Cenveo Inc',

    'AA-': 'Alcoa Inc.',

    'ITUS': 'ITUS Corporation',

    'SLTB': 'Scorpio Bulkers Inc.',

    'CIDM': 'Cinedigm Corp',

    'USB-M': 'U.S. Bancorp',

    'VVC': 'Vectren Corporation',

    'INO': 'Inovio Pharmaceuticals, Inc.',

    'ADAP': 'Adaptimmune Therapeutics plc',

    'OHGI': 'One Horizon Group, Inc.',

    'VAR': 'Varian Medical Systems, Inc.',

    'CNX': 'CONSOL Energy Inc.',

    'INFN': 'Infinera Corporation',

    'MGCD': 'MGC Diagnostics Corporation',

    'PACEW': 'Pace Holdings Corp.',

    'KOS': 'Kosmos Energy Ltd.',

    'NKG': 'Nuveen Georgia Dividend Advantage Municipal Fund 2',

    'SSYS': 'Stratasys, Ltd.',

    'SVVC': 'Firsthand Technology Value Fund, Inc.',

    'FMK': 'First Trust Mega Cap AlphaDEX Fund',

    'CUBI-D': 'Customers Bancorp, Inc',

    'CBOE': 'CBOE Holdings, Inc.',

    'BTX': 'BioTime, Inc.',

    'NAV': 'Navistar International Corporation',

    'CALM': 'Cal-Maine Foods, Inc.',

    'SHW': 'Sherwin-Williams Company (The)',

    'TLYS': 'Tilly\'s, Inc.',

    'CIEN': 'Ciena Corporation',

    'ORBC': 'ORBCOMM Inc.',

    'APD': 'Air Products and Chemicals, Inc.',

    'BLVDU': 'Boulevard Acquisition Corp. II',

    'CFC-A': 'Countrywide Financial Corporation',

    'CF': 'CF Industries Holdings, Inc.',

    'OFED': 'Oconee Federal Financial Corp.',

    'BPMC': 'Blueprint Medicines Corporation',

    'MTRN': 'Materion Corporation',

    'AAU': 'Almaden Minerals, Ltd.',

    'GNCA': 'Genocea Biosciences, Inc.',

    'CVRR': 'CVR Refining, LP',

    'ENBL': 'Enable Midstream Partners, LP',

    'FANG': 'Diamondback Energy, Inc.',

    'SXE': 'Southcross Energy Partners, L.P.',

    'RMD': 'ResMed Inc.',

    'KE': 'Kimball Electronics, Inc.',

    'MCK': 'McKesson Corporation',

    'MY': 'China Ming Yang Wind Power Group Limited',

    'AU': 'AngloGold Ashanti Limited',

    'ASUR': 'Asure Software Inc',

    'HNNA': 'Hennessy Advisors, Inc.',

    'MFM': 'MFS Municipal Income Trust',

    'GLOW': 'Glowpoint, Inc.',

    'HTR': 'Brookfield Total Return Fund Inc.',

    'CVEO': 'Civeo Corporation',

    'CSA': 'Victory CEMP US Small Cap Volatility Wtd Index ETF',

    'MBTF': 'M B T Financial Corp',

    'SOCL': 'Global X Social Media Index ETF',

    'BIS': 'ProShares UltraShort Nasdaq Biotechnology',

    'SNV': 'Synovus Financial Corp.',

    'FMC': 'FMC Corporation',

    'OXBRW': 'Oxbridge Re Holdings Limited',

    'AAMC': 'Altisource Asset Management Corp',

    'FFBC': 'First Financial Bancorp.',

    'BOCH': 'Bank of Commerce Holdings (CA)',

    'NEOG': 'Neogen Corporation',

    'ABDC': 'Alcentra Capital Corp.',

    'OKSB': 'Southwest Bancorp, Inc.',

    'SANM': 'Sanmina Corporation',

    'RFTA': 'RAIT Financial Trust',

    'FORK': 'Fuling Global Inc.',

    'FRT': 'Federal Realty Investment Trust',

    'TVE': 'Tennessee Valley Authority',

    'CHSP-A': 'Chesapeake Lodging Trust',

    'HAYN': 'Haynes International, Inc.',

    'SCYX': 'SCYNEXIS, Inc.',

    'HCKT': 'The Hackett Group, Inc.',

    'ARE-E': 'Alexandria Real Estate Equities, Inc.',

    'EIGI': 'Endurance International Group Holdings, Inc.',

    'EGOV': 'NIC Inc.',

    'CEQP': 'Crestwood Equity Partners LP',

    'CYNO': 'Cynosure, Inc.',

    'SLGN': 'Silgan Holdings Inc.',

    'CSB': 'Victory CEMP US Small Cap High Div Volatility Wtd Index ETF',

    'GTXI': 'GTx, Inc.',

    'NILE': 'Blue Nile, Inc.',

    'CINR': 'Ciner Resources LP',

    'OPOF': 'Old Point Financial Corporation',

    'SSNI': 'Silver Spring Networks, Inc.',

    'CARA': 'Cara Therapeutics, Inc.',

    'OTG': 'OTG EXP, Inc.',

    'SPOK': 'Spok Holdings, Inc.',

    'NUAN': 'Nuance Communications, Inc.',

    'ALL-A': 'Allstate Corporation (The)',

    'BFAM': 'Bright Horizons Family Solutions Inc.',

    'TAHO': 'Tahoe Resources, Inc.',

    'INGR': 'Ingredion Incorporated',

    'UTL': 'UNITIL Corporation',

    'ZIONZ': 'Zions Bancorporation',

    'GST': 'Gastar Exploration Inc.',

    'RDEN': 'Elizabeth Arden, Inc.',

    'NSU': 'Nevsun Resources Ltd',

    'CCV': 'Comcast Corporation',

    'CPA': 'Copa Holdings, S.A.',

    'SLF': 'Sun Life Financial Inc.',

    'CUBN': 'Commerce Union Bancshares, Inc.',

    'CQP': 'Cheniere Energy Partners, LP',

    'GB': 'Greatbatch, Inc.',

    'SNH': 'Senior Housing Properties Trust',

    'CVM': 'Cel-Sci Corporation',

    'SENS': 'Senseonics Holdings, Inc.',

    'EVEP': 'EV Energy Partners, L.P.',

    'HWCC': 'Houston Wire & Cable Company',

    'CXRX': 'Concordia Healthcare Corp.',

    'PLOW': 'Douglas Dynamics, Inc.',

    'JPM-E': 'J P Morgan Chase & Co',

    'OHRP': 'Ohr Pharmaceuticals, Inc.',

    'EMR': 'Emerson Electric Company',

    'PBI-B': 'Pitney Bowes Inc.',

    'UPS': 'United Parcel Service, Inc.',

    'ON': 'ON Semiconductor Corporation',

    'ETJ': 'Eaton Vance Risk-Managed Diversified Equity Income Fund',

    'FONR': 'Fonar Corporation',

    'URG': 'Ur Energy Inc',

    'SSW-D': 'Seaspan Corporation',

    'JBL': 'Jabil Circuit, Inc.',

    'DDS': 'Dillard\'s, Inc.',

    'AFH': 'Atlas Financial Holdings, Inc.',

    'EVH': 'Evolent Health, Inc',

    'OXM': 'Oxford Industries, Inc.',

    'AJRD': 'Aerojet Rocketdyne Holdings, Inc. ',

    'GPT': 'Gramercy Property Trust',

    'JASNW': 'Jason Industries, Inc.',

    'CMRE-B': 'Costamare Inc.',

    'GGACR': 'Garnero Group Acquisition Company',

    'ANH-C': 'Anworth Mortgage Asset  Corporation',

    'FES': 'Forbes Energy Services Ltd',

    'SPTN': 'SpartanNash Company',

    'LEO': 'Dreyfus Strategic Municipals, Inc.',

    'EVO': 'Eaton Vance Ohio Municipal Income Trust',

    'PRE-F': 'PartnerRe Ltd.',

    'PNW': 'Pinnacle West Capital Corporation',

    'VIRC': 'Virco Manufacturing Corporation',

    'ACAT': 'Arctic Cat Inc.',

    'TREE': 'LendingTree, Inc.',

    'BDN': 'Brandywine Realty Trust',

    'BAF': 'BlackRock Income Investment Quality Trust',

    'MSP': 'Madison Strategic Sector Premium Fund',

    'CTS': 'CTS Corporation',

    'MYJ': 'Blackrock MuniYield New Jersey Fund, Inc.',

    'JRJC': 'China Finance Online Co. Limited',

    'KOF': 'Coca Cola Femsa S.A.B. de C.V.',

    'CGNX': 'Cognex Corporation',

    'AFGE': 'American Financial Group, Inc.',

    'SBLK': 'Star Bulk Carriers Corp.',

    'MBSD': 'FlexShares Disciplined Duration MBS Index Fund',

    'BRG': 'Bluerock Residential Growth REIT, Inc.',

    'LITE': 'Lumentum Holdings Inc.',

    'LOGM': 'LogMein, Inc.',

    'JSMD': 'Janus Small/Mid Cap Growth Alpha ETF',

    'EIO': 'Eaton Vance Ohio Municipal Bond Fund',

    'NMO': 'Nuveen Municipal Market Opportunity Fund, Inc.',

    'KND': 'Kindred Healthcare, Inc.',

    'ERIC': 'Ericsson',

    'IAC': 'IAC/InterActiveCorp',

    'TARO': 'Taro Pharmaceutical Industries Ltd.',

    'SRC': 'Spirit Realty Capital, Inc.',

    'SRAQ': 'Silver Run Acquisition Corporation',

    'IGT': 'International Game Technology',

    'IEX': 'IDEX Corporation',

    'AGIO': 'Agios Pharmaceuticals, Inc.',

    'WCC': 'WESCO International, Inc.',

    'BWLD': 'Buffalo Wild Wings, Inc.',

    'MCRI': 'Monarch Casino & Resort, Inc.',

    'EYEG': 'Eyegate Pharmaceuticals, Inc.',

    'TTM': 'Tata Motors Ltd',

    'BLCM': 'Bellicum Pharmaceuticals, Inc.',

    'CPHR': 'Cipher Pharmaceuticals Inc.',

    'VMM': 'Delaware Investments Minnesota Municipal Income Fund II, Inc.',

    'FSM': 'Fortuna Silver Mines Inc.',

    'LCUT': 'Lifetime Brands, Inc.',

    'DRH': 'Diamondrock Hospitality Company',

    'GBT': 'GLOBAL BLOOD THERAPEUTICS, INC.',

    'MCY': 'Mercury General Corporation',

    'MYC': 'Blackrock MuniYield California Fund, Inc.',

    'INN-A': 'Summit Hotel Properties, Inc.',

    'TVIZ': 'region',

    'CADC': 'China Advanced Construction Materials Group, Inc.',

    'BCEI': 'Bonanza Creek Energy, Inc.',

    'EMIF': 'iShares S&P Emerging Markets Infrastructure Index Fund',

    'SNHN': 'Senior Housing Properties Trust',

    'HOV': 'Hovnanian Enterprises Inc',

    'PERY': 'Perry Ellis International Inc.',

    'GSK': 'GlaxoSmithKline PLC',

    'MRTN': 'Marten Transport, Ltd.',

    'BBSI': 'Barrett Business Services, Inc.',

    'CSII': 'Cardiovascular Systems, Inc.',

    'ARCW': 'ARC Group Worldwide, Inc.',

    'TXMD': 'TherapeuticsMD, Inc.',

    'GRPN': 'Groupon, Inc.',

    'XCO': 'EXCO Resources NL',

    'SRDX': 'SurModics, Inc.',

    'CRD.B': 'Crawford & Company',

    'ARDM': 'Aradigm Corporation',

    'GES': 'Guess?, Inc.',

    'HURN': 'Huron Consulting Group Inc.',

    'COKE': 'Coca-Cola Bottling Co. Consolidated',

    'ETN': 'Eaton Corporation, PLC',

    'BLFS': 'BioLife Solutions, Inc.',

    'SNR': 'New Senior Investment Group Inc.',

    'AFI': 'Armstrong Flooring, Inc.',

    'LOV': 'Spark Networks, Inc.',

    'JPM-B': 'J P Morgan Chase & Co',

    'GUT': 'Gabelli Utility Trust (The)',

    'DFS': 'Discover Financial Services',

    'BOE': 'Blackrock Global',

    'TISA': 'Top Image Systems, Ltd.',

    'QCLN': 'First Trust NASDAQ Clean Edge Green Energy Index Fund',

    'CHKP': 'Check Point Software Technologies Ltd.',

    'SFN': 'Stifel Financial Corporation',

    'AIRR': 'First Trust RBA American Industrial Renaissance ETF',

    'ALXN': 'Alexion Pharmaceuticals, Inc.',

    'BSBR': 'Banco Santander Brasil SA',

    'IRWD': 'Ironwood Pharmaceuticals, Inc.',

    'SSW-C.CL': 'Seaspan Corporation',

    'YCB': 'Your Community Bankshares, Inc.',

    'GGACU': 'Garnero Group Acquisition Company',

    'SWN': 'Southwestern Energy Company',

    'RBS-R': 'Royal Bank Scotland plc (The)',

    'GBL': 'Gamco Investors, Inc.',

    'PEN': 'Penumbra, Inc.',

    'EYES': 'Second Sight Medical Products, Inc.',

    'MCI': 'Babson Capital Corporate Investors',

    'WGP': 'Western Gas Equity Partners, LP',

    'CIT': 'CIT Group Inc (DEL)',

    'BITE': 'The Restaurant ETF',

    'ACGL': 'Arch Capital Group Ltd.',

    'CBYL': 'Carbylan Therapeutics, Inc.',

    'CERN': 'Cerner Corporation',

    'DV': 'DeVry Education Group Inc.',

    'CYAN': 'Cyanotech Corporation',

    'BCE': 'BCE, Inc.',

    'HQY': 'HealthEquity, Inc.',

    'HNH': 'Handy & Harman Ltd.',

    'AGNCP': 'American Capital Agency Corp.',

    'WLH': 'Lyon William Homes',

    'GRAM': 'Grana y Montero S.A.A.',

    'PSCH': 'PowerShares S&P SmallCap Health Care Portfolio',

    'NVEC': 'NVE Corporation',

    'OPGN': 'OpGen, Inc.',

    'FAM': 'First Trust/Aberdeen Global Opportunity Income Fund',

    'SHO-F': 'Sunstone Hotel Investors, Inc.',

    'NAZ': 'Nuveen Arizona Premium Income Municipal Fund',

    'SOCB': 'Southcoast Financial Corporation',

    'CHKR': 'Chesapeake Granite Wash Trust',

    'MSCI': 'MSCI Inc',

    'FBNC': 'First Bancorp',

    'VMC': 'Vulcan Materials Company',

    'SNAK': 'Inventure Foods, Inc.',

    'I': 'Intelsat S.A.',

    'NPN': 'Nuveen Pennsylvania Municipal Value Fund',

    'VXDN': 'AccuShares Spot CBOE VIX Down Shares',

    'MNK': 'Mallinckrodt plc',

    'JSML': 'Janus Small Cap Growth Alpha ETF',

    'FULT': 'Fulton Financial Corporation',

    'MLHR': 'Herman Miller, Inc.',

    'CNFR': 'Conifer Holdings, Inc.',

    'MYOS': 'MYOS RENS Technology Inc.',

    'KRA': 'Kraton Performance Polymers, Inc',

    'SEDG': 'SolarEdge Technologies, Inc.',

    'TBNK': 'Territorial Bancorp Inc.',

    'PCI': 'PIMCO Dynamic Credit Income Fund',

    'DHX': 'DHI Group, Inc.',

    'LCNB': 'LCNB Corporation',

    'AVXL': 'Anavex Life Sciences Corp.',

    'ABAX': 'ABAXIS, Inc.',

    'BELFA': 'Bel Fuse Inc.',

    'ASH': 'Ashland Inc.',

    'CFGE': 'Calamos Focus Growth ETF',

    'ARQL': 'ArQule, Inc.',

    'ECACU': 'E-compass Acquisition Corp.',

    'AAON': 'AAON, Inc.',

    'BRC': 'Brady Corporation',

    'MHH': 'Mastech Holdings, Inc',

    'PFSI': 'PennyMac Financial Services, Inc.',

    'SSY': 'SunLink Health Systems, Inc.',

    'DLHC': 'DLH Holdings Corp.',

    'CARB': 'Carbonite, Inc.',

    'VSR': 'Versar, Inc.',

    'XGTI': 'XG Technology, Inc',

    'CRM': 'Salesforce.com Inc',

    'RVT': 'Royce Value Trust, Inc.',

    'IDN': 'Intellicheck Mobilisa, Inc.',

    'LPCN': 'Lipocine Inc.',

    'NQS': 'Nuveen Select Quality Municipal Fund, Inc.',

    'PSA-R': 'Public Storage',

    'ISIG': 'Insignia Systems, Inc.',

    'EMMS': 'Emmis Communications Corporation',

    'BLBD': 'Blue Bird Corporation',

    'BICK': 'First Trust BICK Index Fund',

    'MFT': 'Blackrock MuniYield Investment QualityFund',

    'CCC': 'Calgon Carbon Corporation',

    'SJM': 'J.M. Smucker Company (The)',

    'RAVE': 'Rave Restaurant Group, Inc.',

    'DMTX': 'Dimension Therapeutics, Inc.',

    'WMLP': 'Westmoreland Resource Partners, LP',

    'EME': 'EMCOR Group, Inc.',

    'FPP.WS': 'FieldPoint Petroleum Corporation',

    'MDR': 'McDermott International, Inc.',

    'GGZ-A': 'Gabelli Global Small and Mid Cap Value Trust (The)',

    'BT': 'BT Group plc',

    'NEE-P': 'NextEra Energy, Inc.',

    'TRTLW': 'Terrapin 3 Acquisition Corporation',

    'RRTS': 'Roadrunner Transportation Systems, Inc',

    'IMMU': 'Immunomedics, Inc.',

    'STAA': 'STAAR Surgical Company',

    'TEVA': 'Teva Pharmaceutical Industries Limited',

    'HP': 'Helmerich & Payne, Inc.',

    'GST-B': 'Gastar Exploration Inc.',

    'VTNR': 'Vertex Energy, Inc',

    'CHNR': 'China Natural Resources, Inc.',

    'MPB': 'Mid Penn Bancorp',

    'AFSI-C': 'AmTrust Financial Services, Inc.',

    'KYN-F': 'Kayne Anderson MLP Investment Company',

    'SP': 'SP Plus Corporation',

    'AEUA': 'Anadarko Petroleum Corporation',

    'STBZ': 'State Bank Financial Corporation.',

    'JHS': 'John Hancock Income Securities Trust',

    'AES': 'The AES Corporation',

    'AIY': 'Apollo Investment Corporation',

    'POL': 'PolyOne Corporation',

    'LDRI': 'PowerShares LadderRite 0-5 Year Corporate Bond Portfolio',

    'HOLX': 'Hologic, Inc.',

    'SAAS': 'inContact, Inc.',

    'RDWR': 'Radware Ltd.',

    'GRX-B': 'The Gabelli Healthcare & Wellness Trust',

    'COF-P': 'Capital One Financial Corporation',

    'GGE': 'Guggenheim Enhanced Equity Strategy Fund',

    'HMNF': 'HMN Financial, Inc.',

    'WMB': 'Williams Companies, Inc. (The)',

    'SHIP': 'Seanergy Maritime Holdings Corp',

    'GPE-A': 'Georgia Power Company',

    'GFNSL': 'General Finance Corporation',

    'NEOS': 'Neos Therapeutics, Inc.',

    'PRAA': 'PRA Group, Inc.',

    'GNRC': 'Generac Holdlings Inc.',

    'DOX': 'Amdocs Limited',

    'VTRB': 'Ventas Realty, Limited Partnership // Ventas Capital Corporati',

    'HCI': 'HCI Group, Inc.',

    'IPKW': 'PowerShares International BuyBack Achievers Portfolio',

    'BSX': 'Boston Scientific Corporation',

    'COO': 'Cooper Companies, Inc. (The)',

    'HRTG': 'Heritage Insurance Holdings, Inc.',

    'WAB': 'Westinghouse Air Brake Technologies Corporation',

    'CNYD': 'China Yida Holding, Co.',

    'AXS': 'Axis Capital Holdings Limited',

    'GOOGL': 'Alphabet Inc.',

    'POWI': 'Power Integrations, Inc.',

    'AMCC': 'Applied Micro Circuits Corporation',

    'ARDC': 'Ares Dynamic Credit Allocation Fund, Inc.',

    'UA.C': 'Under Armour, Inc.',

    'CRY': 'CryoLife, Inc.',

    'NCTY': 'The9 Limited',

    'AES-C': 'The AES Corporation',

    'LOCO': 'El Pollo Loco Holdings, Inc.',

    'INF': 'Brookfield Global Listed Infrastructure Income Fund',

    'GT': 'The Goodyear Tire & Rubber Company',

    'VONE': 'Vanguard Russell 1000 ETF',

    'TWOU': '2U, Inc.',

    'ENPH': 'Enphase Energy, Inc.',

    'CMN': 'Cantel Medical Corp.',

    'CWAY': 'Coastway Bancorp, Inc.',

    'TESO': 'Tesco Corporation',

    'AIV': 'Apartment Investment and Management Company',

    'VCIT': 'Vanguard Intermediate-Term Corporate Bond ETF',

    'TAOM': 'Taomee Holdings Limited',

    'DLR-F': 'Digital Realty Trust, Inc.',

    'O': 'Realty Income Corporation',

    'MNE': 'Blackrock Muni New York Intermediate Duration Fund Inc',

    'RGEN': 'Repligen Corporation',

    'XRS': 'TAL Education Group',

    'UCTT': 'Ultra Clean Holdings, Inc.',

    'EPZM': 'Epizyme, Inc.',

    'CLW': 'Clearwater Paper Corporation',

    'BTG': 'B2Gold Corp',

    'ALNY': 'Alnylam Pharmaceuticals, Inc.',

    'AMOV': 'America Movil, S.A.B. de C.V.',

    'SNTA': 'Synta Pharmaceuticals Corp.',

    'SIVB': 'SVB Financial Group',

    'BKS': 'Barnes & Noble, Inc.',

    'MXE': 'Mexico Equity and Income Fund, Inc. (The)',

    'TEAR': 'TearLab Corporation',

    'ONCE': 'Spark Therapeutics, Inc.',

    'PFD': 'Flaherty & Crumrine Preferred Income Fund Incorporated',

    'MIK': 'The Michaels Companies, Inc.',

    'LMCA': 'Liberty Media Corporation',

    'AKBA': 'Akebia Therapeutics, Inc.',

    'PDS': 'Precision Drilling Corporation',

    'GULF': 'WisdomTree Middle East Dividend Fund',

    'UNTD': 'United Online, Inc.',

    'NM-H': 'Navios Maritime Holdings Inc.',

    'MVCB': 'MVC Capital, Inc.',

    'ESL': 'Esterline Technologies Corporation',

    'ELMD': 'Electromed, Inc.',

    'EDI': 'Stone Harbor Emerging Markets Total Income Fund',

    'XHR': 'Xenia Hotels & Resorts, Inc.',

    'HTCH': 'Hutchinson Technology Incorporated',

    'CNNX': 'Cone Midstream Partners LP',

    'EXLS': 'ExlService Holdings, Inc.',

    'WEA': 'Western Asset Bond Fund',

    'AGC': 'Advent Claymore Convertible Securities and Income Fund II',

    'NEWS': 'NewStar Financial, Inc.',

    'TLMR': 'Talmer Bancorp, Inc.',

    'HYGS': 'Hydrogenics Corporation',

    'ICPT': 'Intercept Pharmaceuticals, Inc.',

    'KEN': 'Kenon Holdings Ltd.',

    'PJS': 'Preferred Plus Trust Ser QWS 2 Tr Ctf',

    'RBS-H': 'Royal Bank Scotland plc (The)',

    'OCN': 'Ocwen Financial Corporation',

    'BAC-A': 'Bank of America Corporation',

    'CBMXW': 'CombiMatrix Corporation',

    'TCPI': 'TCP International Holdings Ltd.',

    'LHO': 'LaSalle Hotel Properties',

    'CLRB': 'Cellectar Biosciences, Inc.',

    'TRX': 'Tanzanian Royalty Exploration Corporation',

    'TWTR': 'Twitter, Inc.',

    'GGN': 'GAMCO Global Gold, Natural Reources & Income Trust ',

    'AROW': 'Arrow Financial Corporation',

    'ANY': 'Sphere 3D Corp.',

    'CYBE': 'CyberOptics Corporation',

    'LMOS': 'Lumos Networks Corp.',

    'SIVBO': 'SVB Financial Group',

    'PKBK': 'Parke Bancorp, Inc.',

    'CNTF': 'China TechFaith Wireless Communication Technology Limited',

    'TLT': 'iShares 20+ Year Treasury Bond ETF',

    'MEET': 'MeetMe, Inc.',

    'SBW': 'Western Asset Worldwide Income Fund Inc.',

    'NTRSP': 'Northern Trust Corporation',

    'HR': 'Healthcare Realty Trust Incorporated',

    'USB-N': 'U.S. Bancorp',

    'WFC-R': 'Wells Fargo & Company',

    'PNQI': 'PowerShares Nasdaq Internet Portfolio',

    'NATL': 'National Interstate Corporation',

    'STPP': 'region',

    'AAAP': 'Advanced Accelerator Applications S.A.',

    'PN': 'Patriot National, Inc.',

    'TRMK': 'Trustmark Corporation',

    'ADHD': 'Alcobra Ltd.',

    'PSA-A': 'Public Storage',

    'CFCOU': 'CF Corporation',

    'SASR': 'Sandy Spring Bancorp, Inc.',

    'CFRXW': 'ContraFect Corporation',

    'SGU': 'Star Gas Partners, L.P.',

    'GTIM': 'Good Times Restaurants Inc.',

    'MSG': 'MSG Networks Inc.',

    'EIA': 'Eaton Vance California Municipal Bond Fund II',

    'RDI': 'Reading International Inc',

    'ZSAN': 'Zosano Pharma Corporation',

    'GCH': 'Aberdeen Greater China Fund, Inc.',

    'MYRG': 'MYR Group, Inc.',

    'PRE-H': 'PartnerRe Ltd.',

    'FCEL': 'FuelCell Energy, Inc.',

    'GPL': 'Great Panther Silver Limited',

    'AEB': 'Aegon NV',

    'BLJ': 'Blackrock New Jersey Municipal Bond Trust',

    'CHSCO': 'CHS Inc',

    'JYNT': 'The Joint Corp.',

    'PTN': 'Palatin Technologies, Inc.',

    'WPPGY': 'WPP plc',

    'VICL': 'Vical Incorporated',

    'BSL': 'Blackstone GSO Senior Floating Rate Term Fund',

    'CPIX': 'Cumberland Pharmaceuticals Inc.',

    'LGF': 'Lions Gate Entertainment Corporation',

    'BAC-C': 'Bank of America Corporation',

    'FLTX': 'Fleetmatics Group PLC',

    'CJJD': 'China Jo-Jo Drugstores, Inc.',

    'RBS-F': 'Royal Bank Scotland plc (The)',

    'AIR': 'AAR Corp.',

    'FINL': 'The Finish Line, Inc.',

    'WSTG': 'Wayside Technology Group, Inc.',

    'MMLP': 'Martin Midstream Partners L.P.',

    'IPAR': 'Inter Parfums, Inc.',

    'CYOU': 'Changyou.com Limited',

    'CATY': 'Cathay General Bancorp',

    'EBAYL': 'eBay Inc.',

    'MDLZ': 'Mondelez International, Inc.',

    'MNST': 'Monster Beverage Corporation',

    'COH': 'Coach, Inc.',

    'NCI': 'Navigant Consulting, Inc.',

    'PRI': 'Primerica, Inc.',

    'FOSL': 'Fossil Group, Inc.',

    'RRR': 'Red Rock Resorts, Inc.',

    'MRTX': 'Mirati Therapeutics, Inc.',

    'PSA-C': 'Public Storage',

    'VLP': 'Valero Energy Partners LP',

    'TREX': 'Trex Company, Inc.',

    'CFG': 'Citizens Financial Group, Inc.',

    'NFLX': 'Netflix, Inc.',

    'XNY': 'China Xiniya Fashion Limited',

    'TRC': 'Tejon Ranch Co',

    'RAS-B': 'RAIT Financial Trust',

    'TDW': 'Tidewater Inc.',

    'GPK': 'Graphic Packaging Holding Company',

    'LVS': 'Las Vegas Sands Corp.',

    'STI.WS.A': 'SunTrust Banks, Inc.',

    'NXEOU': 'Nexeo Solutions, Inc.',

    'BKT': 'BlackRock Income Trust Inc. (The)',

    'BGX': 'Blackstone GSO Long Short Credit Income Fund',

    'ICLN': 'iShares S&P Global Clean Energy Index Fund',

    'MAS': 'Masco Corporation',

    'INAP': 'Internap Corporation',

    'DCUC': 'Dominion Resources, Inc.',

    'PYPL': 'PayPal Holdings, Inc.',

    'IGD': 'Voya Global Equity Dividend and Premium Opportunity Fund',

    'INN-C': 'Summit Hotel Properties, Inc.',

    'CPSS': 'Consumer Portfolio Services, Inc.',

    'HYH': 'Halyard Health, Inc.',

    'DVD': 'Dover Motorsports, Inc.',

    'UTES': 'Reaves Utilities ETF',

    'SPHS': 'Sophiris Bio, Inc.',

    'TCCA': 'Triangle Capital Corporation',

    'AFW': 'American Financial Group, Inc.',

    'GFN': 'General Finance Corporation',

    'GDDY': 'GoDaddy Inc.',

    'WKHS': 'Workhorse Group, Inc.',

    'CTIC': 'CTI BioPharma Corp.',

    'ARC': 'ARC Document Solutions, Inc.',

    'DMRC': 'Digimarc Corporation',

    'GRMN': 'Garmin Ltd.',

    'CZNC': 'Citizens & Northern Corp',

    'FSCFL': 'Fifth Street Finance Corp.',

    'CHSCM': 'CHS Inc',

    'ONTX': 'Onconova Therapeutics, Inc.',

    'SWZ': 'Swiss Helvetia Fund, Inc. (The)',

    'ARAY': 'Accuray Incorporated',

    'LOPE': 'Grand Canyon Education, Inc.',

    'LBIX': 'Leading Brands Inc',

    'CRIS': 'Curis, Inc.',

    'DGICB': 'Donegal Group, Inc.',

    'ACIA': 'Acacia Communications, Inc.',

    'HAWK': 'Blackhawk Network Holdings, Inc.',

    'VR': 'Validus Holdings, Ltd.',

    'NTRS': 'Northern Trust Corporation',

    'BRO': 'Brown & Brown, Inc.',

    'AHT-D': 'Ashford Hospitality Trust Inc',

    'WRI': 'Weingarten Realty Investors',

    'PAYC': 'Paycom Software, Inc.',

    'WCIC': 'WCI Communities, Inc.',

    'EE': 'El Paso Electric Company',

    'FPP': 'FieldPoint Petroleum Corporation',

    'GLAD': 'Gladstone Capital Corporation',

    'OESX': 'Orion Energy Systems, Inc.',

    'MNKD': 'MannKind Corporation',

    'IGF': 'iShares Global Infrastructure ETF',

    'LNCE': 'Snyder\'s-Lance, Inc.',

    'CRMT': 'America\'s Car-Mart, Inc.',

    'UBP': 'Urstadt Biddle Properties Inc.',

    'SMBK': 'SmartFinancial, Inc.',

    'VOD': 'Vodafone Group Plc',

    'RDIB': 'Reading International Inc',

    'CRT': 'Cross Timbers Royalty Trust',

    'CCZ': 'Comcast Corporation',

    'AVXS': 'AveXis, Inc.',

    'OMER': 'Omeros Corporation',

    'PRO': 'PROS Holdings, Inc.',

    'RLGT-A': 'Radiant Logistics, Inc.',

    'FRSH': 'Papa Murphy\'s Holdings, Inc.',

    'OHI': 'Omega Healthcare Investors, Inc.',

    'GBX': 'Greenbrier Companies, Inc. (The)',

    'CIGI': 'Colliers International Group Inc. ',

    'FNTC': 'FinTech Acquisition Corp.',

    'OPB': 'Opus Bank',

    'BSTG': 'Biostage, Inc.',

    'CYNA': 'Cynapsus Therapeutics Inc.',

    'BK': 'Bank Of New York Mellon Corporation (The)',

    'AMKR': 'Amkor Technology, Inc.',

    'NICK': 'Nicholas Financial, Inc.',

    'FORD': 'Forward Industries, Inc.',

    'SNY': 'Sanofi',

    'CCLP': 'CSI Compressco LP',

    'CNLM': 'CB Pharma Acquisition Corp.',

    'PER': 'SandRidge Permian Trust',

    'V': 'Visa Inc.',

    'EOCA': 'Endesa Americas S.A.',

    'SAFM': 'Sanderson Farms, Inc.',

    'ACST': 'Acasti Pharma, Inc.',

    'ABTL': 'Autobytel Inc.',

    'GLPI': 'Gaming and Leisure Properties, Inc.',

    'ICD': 'Independence Contract Drilling, Inc.',

    'BAC-Z': 'Bank of America Corporation',

    'ELSE': 'Electro-Sensors, Inc.',

    'ORAN': 'Orange',

    'SIFY': 'Sify Technologies Limited',

    'CTB': 'Cooper Tire & Rubber Company',

    'MAYS': 'J. W. Mays, Inc.',

    'KEYS': 'Keysight Technologies Inc.',

    'APEI': 'American Public Education, Inc.',

    'EXFO': 'EXFO Inc',

    'ROKA': 'Roka Bioscience, Inc.',

    'LC': 'LendingClub Corporation',

    'NOG': 'Northern Oil and Gas, Inc.',

    'NBRV': 'Nabriva Therapeutics AG',

    'GRSHW': 'Gores Holdings, Inc.',

    'ENZ': 'Enzo Biochem, Inc.',

    'CMA': 'Comerica Incorporated',

    'PAAC': 'Pacific Special Acquisition Corp.',

    'IRR': 'Voya Natural Resources Equity Income Fund',

    'GLBS': 'Globus Maritime Limited',

    'UBFO': 'United Security Bancshares',

    'FC': 'Franklin Covey Company',

    'FSI': 'Flexible Solutions International Inc.',

    'FCAN': 'First Trust Canada AlphaDEX Fund',

    'EMO': 'ClearBridge Energy MLP Opportunity Fund Inc.',

    'PETS': 'PetMed Express, Inc.',

    'TCRX': 'THL Credit, Inc.',

    'GDV-A': 'Gabelli Dividend',

    'UNF': 'Unifirst Corporation',

    'SSN': 'Samson Oil & Gas Limited',

    'SZC': 'Cushing Renaissance Fund (The)',

    'FONE': 'First Trust NASDAQ Smartphone Index Fund',

    'RMCF': 'Rocky Mountain Chocolate Factory, Inc.',

    'ORBK': 'Orbotech Ltd.',

    'SQM': 'Sociedad Quimica y Minera S.A.',

    'FRC-B': 'FIRST REPUBLIC BANK',

    'TCON': 'TRACON Pharmaceuticals, Inc.',

    'FWRD': 'Forward Air Corporation',

    'CNCE': 'Concert Pharmaceuticals, Inc.',

    'PDI': 'PIMCO Dynamic Income Fund',

    'CVGW': 'Calavo Growers, Inc.',

    'FIX': 'Comfort Systems USA, Inc.',

    'DUC': 'Duff & Phelps Utility & Corporate Bond Trust, Inc.',

    'WPG': 'WP Glimcher Inc.',

    'VUZI': 'Vuzix Corporation',

    'RFIL': 'RF Industries, Ltd.',

    'TDI': 'Telephone and Data Systems, Inc.',

    'MESG': 'Xura, Inc.',

    'OCRX': 'Ocera Therapeutics, Inc.',

    'ZB-A': 'Zions Bancorporation',

    'HUM': 'Humana Inc.',

    'ERB': 'ERBA Diagnostics, Inc.',

    'SRLP': 'Sprague Resources LP',

    'CACB': 'Cascade Bancorp',

    'LTXB': 'LegacyTexas Financial Group, Inc.',

    'CR': 'Crane Company',

    'ROVI': 'Rovi Corporation',

    'NBL': 'Noble Energy Inc.',

    'SHLD': 'Sears Holdings Corporation',

    'ORLY': 'O\'Reilly Automotive, Inc.',

    'HSGX': 'Histogenics Corporation',

    'JWN': 'Nordstrom, Inc.',

    'PDCE': 'PDC Energy, Inc.',

    'EDD': 'Morgan Stanley Emerging Markets Domestic Debt Fund, Inc.',

    'PF': 'Pinnacle Foods, Inc.',

    'EMN': 'Eastman Chemical Company',

    'CVU': 'CPI Aerostructures, Inc.',

    'WRB-D': 'W.R. Berkley Corporation',

    'MXIM': 'Maxim Integrated Products, Inc.',

    'LNN': 'Lindsay Corporation',

    'WRLD': 'World Acceptance Corporation',

    'VCO': 'Vina Concha Y Toro',

    'CTZ': 'Qwest Corporation',

    'CIB': 'BanColombia S.A.',

    'NEON': 'Neonode Inc.',

    'KKR': 'KKR & Co. L.P.',

    'IVR': 'INVESCO MORTGAGE CAPITAL INC',

    'TNK': 'Teekay Tankers Ltd.',

    'ZEUS': 'Olympic Steel, Inc.',

    'HII': 'Huntington Ingalls Industries, Inc.',

    'BANX': 'StoneCastle Financial Corp',

    'ZNH': 'China Southern Airlines Company Limited',

    'CATH': 'Global X S&P 500 Catholic Values ETF',

    'PIR': 'Pier 1 Imports, Inc.',

    'MDIV': 'First Trust Multi-Asset Diversified Income Index Fund',

    'TCP': 'TC PipeLines, LP',

    'CKEC': 'Carmike Cinemas, Inc.',

    'MMI': 'Marcus & Millichap, Inc.',

    'NTLA': 'Intellia Therapeutics, Inc.',

    'BUD': 'Anheuser-Busch Inbev SA',

    'SDPI': 'Superior Drilling Products, Inc.',

    'MED': 'MEDIFAST INC',

    'PEBK': 'Peoples Bancorp of North Carolina, Inc.',

    'WFC-O': 'Wells Fargo & Company',

    'GZT': 'Gazit-Globe Ltd.',

    'FRPH': 'FRP Holdings, Inc.',

    'AC': 'Associated Capital Group, Inc.',

    'GSJ': 'Goldman Sachs Group, Inc. (The)',

    'MNRO': 'Monro Muffler Brake, Inc.',

    'LE': 'Lands\' End, Inc.',

    'AUO': 'AU Optronics Corp',

    'HK': 'Halcon Resources Corporation',

    'IRET-B': 'Investors Real Estate Trust',

    'CHS': 'Chico\'s FAS, Inc.',

    'TCCO': 'Technical Communications Corporation',

    'AG': 'First Majestic Silver Corp.',

    'BPFHW': 'Boston Private Financial Holdings, Inc.',

    'SCHN': 'Schnitzer Steel Industries, Inc.',

    'CYTK': 'Cytokinetics, Incorporated',

    'EDIT': 'Editas Medicine, Inc.',

    'UCBI': 'United Community Banks, Inc.',

    'CNP': 'CenterPoint Energy, Inc.',

    'CCNE': 'CNB Financial Corporation',

    'ILMN': 'Illumina, Inc.',

    'SPA': 'Sparton Corporation',

    'OPTT': 'Ocean Power Technologies, Inc.',

    'MSN': 'Emerson Radio Corporation',

    'PIP': 'PharmAthene, Inc',

    'KAI': 'Kadant Inc',

    'JMEI': 'Jumei International Holding Limited',

    'DISCA': 'Discovery Communications, Inc.',

    'NRCIB': 'National Research Corporation',

    'MSD': 'Morgan Stanley Emerging Markets Debt Fund, Inc.',

    'UBIC': 'UBIC, Inc.',

    'CALA': 'Calithera Biosciences, Inc.',

    'TDC': 'Teradata Corporation',

    'AGN-A': 'Allergan plc.',

    'BCO': 'Brink\'s Company (The)',

    'NXC': 'Nuveen Insured California Select Tax-Free Income Portfolio',

    'CLGX': 'CoreLogic, Inc.',

    'FSNN': 'Fusion Telecommunications International, Inc.',

    'FSLR': 'First Solar, Inc.',

    'HAFC': 'Hanmi Financial Corporation',

    'AHL-C': 'Aspen Insurance Holdings Limited',

    'SAGE': 'Sage Therapeutics, Inc.',

    'ZBIO': 'ProShares UltraPro Short NASDAQ Biotechnology',

    'LRAD': 'LRAD Corporation',

    'IIN': 'IntriCon Corporation',

    'CFNL': 'Cardinal Financial Corporation',

    'NG': 'Novagold Resources Inc.',

    'SSH': 'Sunshine Heart Inc',

    'SCE-E': 'Southern California Edison Company',

    'SSWN': 'Seaspan Corporation',

    'ORIG': 'Ocean Rig UDW Inc.',

    'ATLO': 'Ames National Corporation',

    'TPZ': 'Tortoise Power and Energy Infrastructure Fund, Inc',

    'PLPM': 'Planet Payment, Inc.',

    'SSFN': 'Stewardship Financial Corp',

    'HCACW': 'Hennessy Capital Acquisition Corp. II',

    'BTI': 'British American Tobacco p.l.c.',

    'PGTI': 'PGT, Inc.',

    'TACT': 'TransAct Technologies Incorporated',

    'MUR': 'Murphy Oil Corporation',

    'ENG': 'ENGlobal Corporation',

    'CREG': 'China Recycling Energy Corporation',

    'ANH': 'Anworth Mortgage Asset  Corporation',

    'EVV': 'Eaton Vance Limited Duration Income Fund',

    'SUN': 'Sunoco LP',

    'FPO-A.CL': 'First Potomac Realty Trust',

    'TST': 'TheStreet, Inc.',

    'ANCB': 'Anchor Bancorp',

    'C-N': 'Citigroup Inc.',

    'MVO': 'MV Oil Trust',

    'FMO': 'Fiduciary/Claymore MLP Opportunity Fund',

    'FIS': 'Fidelity National Information Services, Inc.',

    'VYMI': 'Vanguard International High Dividend Yield ETF',

    'EVBS': 'Eastern Virginia Bankshares, Inc.',

    'ASNA': 'Ascena Retail Group, Inc.',

    'ARP': 'Atlas Resource Partners, L.P.',

    'GEQ': 'Guggenheim Equal Weight Enhanced Equity Income Fund',

    'SOHO': 'Sotherly Hotels Inc.',

    'APTO': 'Aptose Biosciences, Inc.',

    'PEBO': 'Peoples Bancorp Inc.',

    'CBFV': 'CB Financial Services, Inc.',

    'HSII': 'Heidrick & Struggles International, Inc.',

    'RHP': 'Ryman Hospitality Properties, Inc.',

    'F': 'Ford Motor Company',

    'IDXX': 'IDEXX Laboratories, Inc.',

    'TPVZ': 'TriplePoint Venture Growth BDC Corp.',

    'DNP': 'Duff & Phelps Utilities Income, Inc.',

    'RCMT': 'RCM Technologies, Inc.',

    'FMBI': 'First Midwest Bancorp, Inc.',

    'FCF': 'First Commonwealth Financial Corporation',

    'BID': 'Sotheby\'s',

    'PPT': 'Putnam Premier Income Trust',

    'AGYS': 'Agilysys, Inc.',

    'GBDC': 'Golub Capital BDC, Inc.',

    'VGZ': 'Vista Gold Corporation',

    'CSLT': 'Castlight Health, inc.',

    'HCN': 'Welltower Inc.',

    'TMUS': 'T-Mobile US, Inc.',

    'CDNS': 'Cadence Design Systems, Inc.',

    'CMTL': 'Comtech Telecommunications Corp.',

    'PSA-W': 'Public Storage',

    'FCE.A': 'Forest City Realty Trust, Inc.',

    'PFIE': 'Profire Energy, Inc.',

    'ZIONW': 'Zions Bancorporation',

    'DD': 'E.I. du Pont de Nemours and Company',

    'WRN': 'Western Copper and Gold Corporation',

    'WYIGW': 'JM Global Holding Company',

    'VCV': 'Invesco California Value Municipal Income Trust',

    'FFWM': 'First Foundation Inc.',

    'VIAV': 'Viavi Solutions Inc.',

    'JNPR': 'Juniper Networks, Inc.',

    'UBND': 'WisdomTree Western Asset Unconstrained Bond Fund',

    'AIT': 'Applied Industrial Technologies, Inc.',

    'GNBC': 'Green Bancorp, Inc.',

    'CRH': 'CRH PLC',

    'HZNP': 'Horizon Pharma plc',

    'RNG': 'Ringcentral, Inc.',

    'STKS': 'The ONE Group Hospitality, Inc.',

    'FNF': 'Fidelity National Financial, Inc.',

    'MEI': 'Methode Electronics, Inc.',

    'TINY': 'Harris & Harris Group, Inc.',

    'MTX': 'Minerals Technologies Inc.',

    'VIRT': 'Virtu Financial, Inc.',

    'WAFDW': 'Washington Federal, Inc.',

    'CETX': 'Cemtrex Inc.',

    'ELOS': 'Syneron Medical Ltd.',

    'IEUS': 'iShares MSCI Europe Small-Cap ETF',

    'PMD': 'Psychemedics Corporation',

    'WASH': 'Washington Trust Bancorp, Inc.',

    'MSCC': 'Microsemi Corporation',

    'EQFN': 'Equitable Financial Corp.',

    'CNTY': 'Century Casinos, Inc.',

    'WIRE': 'Encore Wire Corporation',

    'EVBN': 'Evans Bancorp, Inc.',

    'IRET-': 'Investors Real Estate Trust',

    'MATX': 'Matson, Inc.',

    'REXI': 'Resource America, Inc.',

    'TPVG': 'TriplePoint Venture Growth BDC Corp.',

    'PSMT': 'PriceSmart, Inc.',

    'ENFC': 'Entegra Financial Corp.',

    'CPK': 'Chesapeake Utilities Corporation',

    'CZFC': 'Citizens First Corporation',

    'ISG': 'ING Group, N.V.',

    'KRG': 'Kite Realty Group Trust',

    'WHFBL': 'WhiteHorse Finance, Inc.',

    'TECD': 'Tech Data Corporation',

    'OSIR': 'Osiris Therapeutics, Inc.',

    'PRKR': 'ParkerVision, Inc.',

    'EMCB': 'WisdomTree Emerging Markets Corporate Bond Fund',

    'AHP-B': 'Ashford Hospitality Prime, Inc.',

    'PPG': 'PPG Industries, Inc.',

    'NOM': 'Nuveen Missouri Premium Income Municipal Fund',

    'LILA': 'Liberty Global plc',

    'UUU': 'Universal Security Instruments, Inc.',

    'AVHI': 'A V Homes, Inc.',

    'GJV': 'Synthetic Fixed-Income Securities, Inc.',

    'CATYW': 'Cathay General Bancorp',

    'NH': 'NantHealth, Inc.',

    'DRQ': 'Dril-Quip, Inc.',

    'LDRH': 'LDR Holding Corporation',

    'WAFD': 'Washington Federal, Inc.',

    'MWA': 'MUELLER WATER PRODUCTS',

    'IAE': 'Voya Asia Pacific High Dividend Equity Income Fund',

    'TSN': 'Tyson Foods, Inc.',

    'LDL': 'Lydall, Inc.',

    'CNLMU': 'CB Pharma Acquisition Corp.',

    'AMDA': 'Amedica Corporation',

    'MFIN': 'Medallion Financial Corp.',

    'AGNCB': 'American Capital Agency Corp.',

    'JCTCF': 'Jewett-Cameron Trading Company',

    'EARN': 'Ellington Residential Mortgage REIT',

    'COVS': 'Covisint Corporation',

    'MUC': 'Blackrock MuniHoldings California Quality Fund,  Inc.',

    'PKX': 'POSCO',

    'BOBE': 'Bob Evans Farms, Inc.',

    'VIIZ': 'region',

    'DMB': 'Dreyfus Municipal Bond Infrastructure Fund, Inc.',

    'CRHM': 'CRH Medical Corporation',

    'GM': 'General Motors Company',

    'WEN': 'Wendy\'s Company (The)',

    'CVBF': 'CVB Financial Corporation',

    'FDX': 'FedEx Corporation',

    'AMTD': 'TD Ameritrade Holding Corporation',

    'AFGH': 'American Financial Group, Inc.',

    'CXO': 'Concho Resources Inc.',

    'VIGI': 'Vanguard International Dividend Appreciation ETF',

    'CREE': 'Cree, Inc.',

    'MANT': 'ManTech International Corporation',

    'AGFS': 'AgroFresh Solutions, Inc.',

    'RUTH': 'Ruth\'s Hospitality Group, Inc.',

    'EQCO': 'Equity Commonwealth',

    'CFI': 'Culp, Inc.',

    'HMC': 'Honda Motor Company, Ltd.',

    'WFE-A': 'Wells Fargo & Company',

    'MACK': 'Merrimack Pharmaceuticals, Inc.',

    'H': 'Hyatt Hotels Corporation',

    'VGIT': 'Vanguard Intermediate -Term Government Bond ETF',

    'TUMI': 'Tumi Holdings, Inc.',

    'ABIO': 'ARCA biopharma, Inc.',

    'EXTN': 'Exterran Corporation',

    'OBCI': 'Ocean Bio-Chem, Inc.',

    'CFR': 'Cullen/Frost Bankers, Inc.',

    'GCBC': 'Greene County Bancorp, Inc.',

    'DKL': 'Delek Logistics Partners, L.P.',

    'GLYC': 'GlycoMimetics, Inc.',

    'BYFC': 'Broadway Financial Corporation',

    'CORE': 'Core-Mark Holding Company, Inc.',

    'SHSP': 'SharpSpring, Inc.',

    'PSF': 'Cohen & Steers Select Preferred and Income Fund, Inc.',

    'LALT': 'PowerShares Multi-Strategy Alternative Portfolio',

    'ADTN': 'ADTRAN, Inc.',

    'TSL': 'Trina Solar Limited',

    'CNOB': 'ConnectOne Bancorp, Inc.',

    'BIOC': 'Biocept, Inc.',

    'XRA': 'Exeter Resource Corporation',

    'MSM': 'MSC Industrial Direct Company, Inc.',

    'STRS': 'Stratus Properties, Inc.',

    'CYS-B': 'CYS Investments, Inc.',

    'EEP': 'Enbridge Energy, L.P.',

    'EVA': 'Enviva Partners, LP',

    'ECC           ': 'Eagle Point Credit Company Inc.',

    'TKF': 'Turkish Investment Fund, Inc. (The)',

    'GIII': 'G-III Apparel Group, LTD.',

    'CBIO': 'Catalyst Biosciences, Inc. ',

    'CHN': 'China Fund, Inc. (The)',

    'STOR': 'STORE Capital Corporation',

    'ACBI': 'Atlantic Capital Bancshares, Inc.',

    'TX': 'Ternium S.A.',

    'DMF': 'Dreyfus Municipal Income, Inc.',

    'BMO': 'Bank Of Montreal',

    'KWR': 'Quaker Chemical Corporation',

    'PYDS': 'Payment Data Systems, Inc.',

    'NTZ': 'Natuzzi, S.p.A.',

    'SITE': 'SiteOne Landscape Supply, Inc.',

    'IGLD': 'Internet Gold Golden Lines Ltd.',

    'NSR': 'Neustar, Inc.',

    'SGNL': 'Signal Genetics, Inc.',

    'KTOVW': 'Kitov Pharamceuticals Holdings Ltd.',

    'CW': 'Curtiss-Wright Corporation',

    'SGM': 'Stonegate Mortgage Corporation',

    'EDF': 'Stone Harbor Emerging Markets Income Fund',

    'FOGO': 'Fogo de Chao, Inc.',

    'NBD': 'Nuveen Build America Bond Opportunity Fund',

    'TIPT': 'Tiptree Financial Inc.',

    'ARIA': 'ARIAD Pharmaceuticals, Inc.',

    'BCRX': 'BioCryst Pharmaceuticals, Inc.',

    'GSIT': 'GSI Technology, Inc.',

    'GRO': 'Agria Corporation',

    'MINDP': 'Mitcham Industries, Inc.',

    'JFC': 'JPMorgan China Region Fund, Inc.',

    'EGP': 'EastGroup Properties, Inc.',

    'SB': 'Safe Bulkers, Inc',

    'BHACU': 'Barington/Hilco Acquisition Corp.',

    'AST': 'Asterias Biotherapeutics, Inc.',

    'PCYO': 'Pure Cycle Corporation',

    'QSII': 'Quality Systems, Inc.',

    'ETE': 'Energy Transfer Equity, L.P.',

    'RBS-S': 'Royal Bank Scotland plc (The)',

    'TOF': 'Tofutti Brands Inc.',

    'GTY': 'Getty Realty Corporation',

    'BAX': 'Baxter International Inc.',

    'GLF': 'GulfMark Offshore, Inc.',

    'VALE': 'VALE S.A.',

    'CSRA': 'CSRA Inc.',

    'SALM': 'Salem Media Group, Inc.',

    'KYN': 'Kayne Anderson MLP Investment Company',

    'TCRD': 'THL Credit, Inc.',

    'HRB': 'H&R Block, Inc.',

    'NTI': 'Northern Tier Energy LP',

    'HLF': 'Herbalife LTD.',

    'MER-M': 'Merrill Lynch & Co., Inc.',

    'LBIO': 'Lion Biotechnologies, Inc.',

    'ISTR': 'Investar Holding Corporation',

    'USB-A': 'U.S. Bancorp',

    'REFR': 'Research Frontiers Incorporated',

    'HTLD': 'Heartland Express, Inc.',

    'PSAU': 'PowerShares Global Gold & Precious Metals Portfolio',

    'SLRA': 'Solar Capital Ltd.',

    'WTT': 'Wireless Telecom Group,  Inc.',

    'HIVE': 'Aerohive Networks, Inc.',

    'BPTH': 'Bio-Path Holdings, Inc.',

    'LMHA': 'Legg Mason, Inc.',

    'RARE': 'Ultragenyx Pharmaceutical Inc.',

    'MCHP': 'Microchip Technology Incorporated',

    'SMTX': 'SMTC Corporation',

    'SIF': 'SIFCO Industries, Inc.',

    'GAB-H': 'Gabelli Equity Trust, Inc. (The)',

    'MVIS': 'Microvision, Inc.',

    'KLRE': 'KLR Energy Acquisition Corp.',

    'NMBL': 'Nimble Storage, Inc.',

    'AKAO': 'Achaogen, Inc.',

    'HPT-D': 'Hospitality Properties Trust',

    'AWF': 'Alliance World Dollar Government Fund II',

    'TVC': 'Tennessee Valley Authority',

    'LDOS': 'Leidos Holdings, Inc.',

    'FCLF': 'First Clover Leaf Financial Corp.',

    'BNY': 'BlackRock New York Investment Quality Municipal Trust Inc. (Th',

    'ICLDW': 'InterCloud Systems, Inc',

    'EOS': 'Eaton Vance Enhanced Equity Income Fund II',

    'ESRX': 'Express Scripts Holding Company',

    'VLT': 'Invesco High Income Trust II',

    'GJS': 'STRATS Trust',

    'WD': 'Walker & Dunlop, Inc.',

    'AFG': 'American Financial Group, Inc.',

    'MNGA': 'MagneGas Corporation',

    'QEP': 'QEP Resources, Inc.',

    'BBK': 'Blackrock Municipal Bond Trust',

    'ATHN': 'athenahealth, Inc.',

    'TTI': 'Tetra Technologies, Inc.',

    'GPIAW': 'GP Investments Acquisition Corp.',

    'BBBY': 'Bed Bath & Beyond Inc.',

    'ACC': 'American Campus Communities Inc',

    'JPM-A': 'J P Morgan Chase & Co',

    'RILY': 'B. Riley Financial, Inc.',

    'OMI': 'Owens & Minor, Inc.',

    'PGP': 'Pimco Global Stocksplus & Income Fund',

    'MAN': 'ManpowerGroup',

    'RBCAA': 'Republic Bancorp, Inc.',

    'IHT': 'InnSuites Hospitality Trust',

    'SCE-D': 'Southern California Edison Company',

    'TK': 'Teekay Corporation',

    'TRN': 'Trinity Industries, Inc.',

    'TRT': 'Trio-Tech International',

    'FAF': 'First American Corporation (The)',

    'VVR': 'Invesco Senior Income Trust',

    'MBRG': 'Middleburg Financial Corporation',

    'PKG': 'Packaging Corporation of America',

    'NIE': 'AllianzGI Equity & Convertible Income Fund',

    'MLVF': 'Malvern Bancorp, Inc.',

    'CBL-E': 'CBL & Associates Properties, Inc.',

    'NBN': 'Northeast Bancorp',

    'NL': 'NL Industries, Inc.',

    'TDOC': 'Teladoc, Inc.',

    'APTS': 'Preferred Apartment Communities, Inc.',

    'GTE': 'Gran Tierra Energy Inc.',

    'ITRI': 'Itron, Inc.',

    'POR': 'Portland General Electric Company',

    'ALK': 'Alaska Air Group, Inc.',

    'FEX': 'First Trust Large Cap Core AlphaDEX Fund',

    'TGD': 'Timmons Gold Corp',

    'PCG-E': 'Pacific Gas & Electric Co.',

    'CTU': 'Qwest Corporation',

    'CAAS': 'China Automotive Systems, Inc.',

    'SR': 'Spire Inc.',

    'THGA': 'The Hanover Insurance Group, Inc.',

    'MDP': 'Meredith Corporation',

    'AMGN': 'Amgen Inc.',

    'JKHY': 'Jack Henry & Associates, Inc.',

    'CUI': 'CUI Global, Inc.',

    'MTCH': 'Match Group, Inc.',

    'JPI': 'Nuveen Preferred and Income Term Fund',

    'NGHCO': 'National General Holdings Corp',

    'GTS': 'Triple-S Management Corporation',

    'QUNR': 'Qunar Cayman Islands Limited',

    'PMC': 'Pharmerica Corporation',

    'TTMI': 'TTM Technologies, Inc.',

    'BJZ': 'Blackrock California Municipal 2018 Term Trust',

    'BRT': 'BRT Realty Trust',

    'DHT': 'DHT Holdings, Inc.',

    'AVY': 'Avery Dennison Corporation',

    'VNO': 'Vornado Realty Trust',

    'VTR': 'Ventas, Inc.',

    'CMCO': 'Columbus McKinnon Corporation',

    'ININ': 'Interactive Intelligence Group, Inc.',

    'ACM': 'AECOM',

    'SSRI': 'Silver Standard Resources Inc.',

    'MC': 'Moelis & Company',

    'ITG': 'Investment Technology Group, Inc.',

    'NCT': 'Newcastle Investment Corporation',

    'GMS': 'GMS Inc.',

    'BPK': 'Blackrock Municipal 2018 Term Trust',

    'MAR': 'Marriott International',

    'ALGN': 'Align Technology, Inc.',

    'PLM': 'Polymet Mining Corp.',

    'ED': 'Consolidated Edison Inc',

    'CHFC': 'Chemical Financial Corporation',

    'HEB': 'Hemispherx BioPharma, Inc.',

    'SBNA': 'Scorpio Tankers Inc.',

    'EHI': 'Western Asset Global High Income Fund Inc',

    'TMHC': 'Taylor Morrison Home Corporation',

    'ASA': 'ASA Gold and Precious Metals Limited',

    'IMMY': 'Imprimis Pharmaceuticals, Inc.',

    'INCR': 'INC Research Holdings, Inc.',

    'DYN': 'Dynegy Inc.',

    'SITO': 'SITO Mobile, Ltd.',

    'CMS': 'CMS Energy Corporation',

    'EGT': 'Entertainment Gaming Asia Incorporated',

    'EFX': 'Equifax, Inc.',

    'JW.A': 'John Wiley & Sons, Inc.',

    'ROP': 'Roper Technologies, Inc.',

    'DLTR': 'Dollar Tree, Inc.',

    'LRN': 'K12 Inc',

    'ELECU': 'Electrum Special Acquisition Corporation',

    'AKO.A': 'Embotelladora Andina S.A.',

    'CAPR': 'Capricor Therapeutics, Inc.',

    'CDTI': 'Clean Diesel Technologies, Inc.',

    'VTA': 'Invesco Credit Opportunities Fund',

    'GAB-D': 'Gabelli Equity Trust, Inc. (The)',

    'ASND': 'Ascendis Pharma A/S',

    'GS-K': 'Goldman Sachs Group, Inc. (The)',

    'STKL': 'SunOpta, Inc.',

    'CSCO': 'Cisco Systems, Inc.',

    'BBRG': 'Bravo Brio Restaurant Group, Inc.',

    'CEV': 'Eaton Vance California Municipal Income Trust',

    'DTK': 'Deutsche Bank AG',

    'TVPT': 'Travelport Worldwide Limited',

    'STN': 'Stantec Inc',

    'ISBC': 'Investors Bancorp, Inc.',

    'PBNC': 'Paragon Commercial Corporation',

    'NEPT': 'Neptune Technologies & Bioresources Inc',

    'GERN': 'Geron Corporation',

    'TANN': 'TravelCenters of America LLC',

    'MER-K': 'Merrill Lynch & Co., Inc.',

    'DXLG': 'Destination XL Group, Inc.',

    'GS-N': 'Goldman Sachs Group, Inc. (The)',

    'EXG': 'Eaton Vance Tax-Managed Global Diversified Equity Income Fund',

    'NYCB': 'New York Community Bancorp, Inc.',

    'RP': 'RealPage, Inc.',

    'MTT': 'Western Asset Municipal Defined Opportunity Trust Inc',

    'SIRI': 'Sirius XM Holdings Inc.',

    'CTL': 'CenturyLink, Inc.',

    'EDE': 'Empire District Electric Company (The)',

    'CODI': 'Compass Diversified Holdings',

    'SHPG': 'Shire plc',

    'SQQQ': 'ProShares UltraPro Short QQQ',

    'UCFC': 'United Community Financial Corp.',

    'GI': 'EndoChoice Holdings, Inc.',

    'FRD': 'Friedman Industries Inc.',

    'FMX': 'Fomento Economico Mexicano S.A.B. de C.V.',

    'NTRI': 'NutriSystem Inc',

    'RH': 'Restoration Hardware Holdings Inc.',

    'AMAG': 'AMAG Pharmaceuticals, Inc.',

    'NS': 'Nustar Energy L.P.',

    'VSAR': 'Versartis, Inc.',

    'EVK': 'Ever-Glory International Group, Inc.',

    'THRM': 'Gentherm Inc',

    'RFEM': 'First Trust RiverFront Dynamic Emerging Markets ETF',

    'ENSV': 'ENSERVCO Corporation',

    'BRN': 'Barnwell Industries, Inc.',

    'NJR': 'NewJersey Resources Corporation',

    'LWAY': 'Lifeway Foods, Inc.',

    'BASI': 'Bioanalytical Systems, Inc.',

    'SKY': 'Skyline Corporation',

    'FSFR': 'Fifth Street Senior Floating Rate Corp.',

    'CEE': 'Central Europe, Russia and Turkey Fund, Inc. (The)',

    'EMD': 'Western Asset Emerging Markets Income Fund, Inc',

    'SPP': 'Sanchez Production Partners LP',

    'IP': 'International Paper Company',

    'SSTK': 'Shutterstock, Inc.',

    'PUB': 'People\'s Utah Bancorp',

    'AAP': 'Advance Auto Parts Inc',

    'MARK': 'Remark Media, Inc.',

    'VJET': 'voxeljet AG',

    'FDEF': 'First Defiance Financial Corp.',

    'NEE-G': 'NextEra Energy, Inc.',

    'HIHO': 'Highway Holdings Limited',

    'PBPB': 'Potbelly Corporation',

    'MNTA': 'Momenta Pharmaceuticals, Inc.',

    'OI': 'Owens-Illinois, Inc.',

    'WTFCW': 'Wintrust Financial Corporation',

    'EPIX': 'ESSA Pharma Inc.',

    'SPN': 'Superior Energy Services, Inc.',

    'GSBD': 'Goldman Sachs BDC, Inc.',

    'MCA': 'Blackrock MuniYield California Insured Fund, Inc.',

    'RDUS': 'Radius Health, Inc.',

    'NRZ': 'New Residential Investment Corp.',

    'CUBI-E': 'Customers Bancorp, Inc',

    'BRK.B': 'Berkshire Hathaway Inc.',

    'MCO': 'Moody\'s Corporation',

    'ZB-H': 'Zions Bancorporation',

    'TCRZ': 'THL Credit, Inc.',

    'IO': 'Ion Geophysical Corporation',

    'SUI': 'Sun Communities, Inc.',

    'MANU': 'Manchester United Ltd.',

    'BDX': 'Becton, Dickinson and Company',

    'OFIX': 'Orthofix International N.V.',

    'WDAY': 'Workday, Inc.',

    'VNOM': 'Viper Energy Partners LP',

    'FVC': 'First Trust Dorsey Wright Dynamic Focus 5 ETF',

    'TNP-B': 'Tsakos Energy Navigation Ltd',

    'PAG': 'Penske Automotive Group, Inc.',

    'FBNK': 'First Connecticut Bancorp, Inc.',

    'EMCF': 'Emclaire Financial Corp',

    'SCE-F': 'Southern California Edison Company',

    'UBP-F': 'Urstadt Biddle Properties Inc.',

    'QYLD': 'Recon Capital NASDAQ-100 Covered Call ETF',

    'IEP': 'Icahn Enterprises L.P.',

    'ALXA': 'Alexza Pharmaceuticals, Inc.',

    'RDS.B': 'Royal Dutch Shell PLC',

    'EMF': 'Templeton Emerging Markets Fund',

    'MWO': 'Morgan Stanley',

    'KNL': 'Knoll, Inc.',

    'OSB': 'Norbord Inc.',

    'WFD': 'Westfield Financial, Inc.',

    'SUPN': 'Supernus Pharmaceuticals, Inc.',

    'ACWX': 'iShares MSCI ACWI ex US Index Fund',

    'HCCI': 'Heritage-Crystal Clean, Inc.',

    'OPK': 'Opko Health Inc',

    'SIGI': 'Selective Insurance Group, Inc.',

    'BDN-E': 'Brandywine Realty Tr',

    'TTHI': 'Transition Therapeutics, Inc.',

    'NHS': 'Neuberger Berman High Yield Strategies Fund',

    'SBBX': 'Sussex Bancorp',

    'EHIC': 'eHi Car Services Limited',

    'HTZ': 'Hertz Global Holdings, Inc',

    'BXC': 'BlueLinx Holdings Inc.',

    'SPNE': 'SeaSpine Holdings Corporation',

    'QVCA': 'Liberty Interactive Corporation',

    'TRCB': 'Two River Bancorp',

    'BCH': 'Banco De Chile',

    'XYL': 'Xylem Inc.',

    'SFST': 'Southern First Bancshares, Inc.',

    'WILC': 'G. Willi-Food International,  Ltd.',

    'LH': 'Laboratory Corporation of America Holdings',

    'BANC-E': 'Banc of California, Inc.',

    'EGY': 'Vaalco Energy Inc',

    'STMP': 'Stamps.com Inc.',

    'IDXG': 'Interpace Diagnostics Group, Inc.',

    'ESEA': 'Euroseas Ltd.',

    'NBY': 'NovaBay Pharmaceuticals, Inc.',

    'RY-S': 'Royal Bank Of Canada',

    'VFL': 'Delaware Investments Florida Insured Municipal Income Fund',

    'DRWIW': 'DragonWave Inc',

    'TTP': 'Tortoise Pipeline & Energy Fund, Inc.',

    'ARRS': 'ARRIS International plc',

    'GAB': 'Gabelli Equity Trust, Inc. (The)',

    'CGI': 'Celadon Group, Inc.',

    'FMBH': 'First Mid-Illinois Bancshares, Inc.',

    'ETM': 'Entercom Communications Corporation',

    'BCPC': 'Balchem Corporation',

    'QCRH': 'QCR Holdings, Inc.',

    'UFCS': 'United Fire Group, Inc',

    'IL': 'IntraLinks Holdings, Inc.',

    'FEIM': 'Frequency Electronics, Inc.',

    'STAG-C': 'Stag Industrial, Inc.',

    'HBAN': 'Huntington Bancshares Incorporated',

    'EVGN': 'Evogene Ltd.',

    'FRC': 'FIRST REPUBLIC BANK',

    'BFR': 'BBVA Banco Frances S.A.',

    'MCZ': 'Mad Catz Interactive Inc',

    'DORM': 'Dorman Products, Inc.',

    'AUMA': 'AR Capital Acquisition Corp.',

    'CIVI': 'Civitas Solutions, Inc.',

    'MS-F': 'Morgan Stanley',

    'KELYB': 'Kelly Services, Inc.',

    'JD': 'JD.com, Inc.',

    'USB-O': 'U.S. Bancorp',

    'ISHG': 'iShares S&P/Citigroup 1-3 Year International Treasury Bond Fun',

    'FLKS': 'Flex Pharma, Inc.',

    'BWINB': 'Baldwin & Lyons, Inc.',

    'BYM': 'Blackrock Municipal Income Quality Trust',

    'HDRAW': 'Hydra Industries Acquisition Corp.',

    'AMT-A': 'American Tower Corporation (REIT)',

    'HY': 'Hyster-Yale Materials Handling, Inc.',

    'SN': 'Sanchez Energy Corporation',

    'FRO': 'Frontline Ltd.',

    'TRS': 'TriMas Corporation',

    'WGO': 'Winnebago Industries, Inc.',

    'FEUZ': 'First Trust Eurozone AlphaDEX ETF',

    'TTGT': 'TechTarget, Inc.',

    'ETP': 'ENERGY TRANSFER PARTNERS',

    'UAL': 'United Continental Holdings, Inc.',

    'HHY': 'Brookfield High Income Fund Inc.',

    'TECH': 'Bio-Techne Corp',

    'NSA': 'National Storage Affiliates Trust',

    'MPX': 'Marine Products Corporation',

    'YZC': 'Yanzhou Coal Mining Company Limited',

    'BAC-I': 'Bank of America Corporation',

    'CAPN': 'Capnia, Inc.',

    'MBWM': 'Mercantile Bank Corporation',

    'ESV': 'ENSCO plc',

    'AUMAU': 'AR Capital Acquisition Corp.',

    'MFS': 'Manitowoc Food Service, Inc.',

    'AF-C': 'Astoria Financial Corporation',

    'AIV-A': 'Apartment Investment and Management Company',

    'PAHC': 'Phibro Animal Health Corporation',

    'SCHW-D': 'The Charles Schwab Corporation',

    'ZF': 'Zweig Fund, Inc. (The)',

    'NPK': 'National Presto Industries, Inc.',

    'UG': 'United-Guardian, Inc.',

    'GM.WS.B': 'General Motors Company',

    'BAC-L': 'Bank of America Corporation',

    'EDGE': 'Edge Therapeutics, Inc.',

    'TS': 'Tenaris S.A.',

    'GBIM': 'GlobeImmune, Inc.',

    'NBHC': 'National Bank Holdings Corporation',

    'DLB': 'Dolby Laboratories',

    'HCSG': 'Healthcare Services Group, Inc.',

    'PBMD': 'Prima BioMed Ltd',

    'DHR': 'Danaher Corporation',

    'HAIN': 'The Hain Celestial Group, Inc.',

    'TNAV': 'TeleNav, Inc.',

    'SGYPU': 'Synergy Pharmaceuticals, Inc.',

    'GAB-G': 'Gabelli Equity Trust, Inc. (The)',

    'MICT': 'Micronet Enertec Technologies, Inc.',

    'EROS': 'Eros International PLC',

    'SUM': 'Summit Materials, Inc.',

    'BPT': 'BP Prudhoe Bay Royalty Trust',

    'B': 'Barnes Group, Inc.',

    'EHTH': 'eHealth, Inc.',

    'NMI': 'Nuveen Municipal Income Fund, Inc.',

    'VNTV': 'Vantiv, Inc.',

    'SCE-B': 'Southern California Edison Company',

    'SB-B': 'Safe Bulkers, Inc',

    'EIM': 'Eaton Vance Municipal Bond Fund',

    'RECN': 'Resources Connection, Inc.',

    'HMSY': 'HMS Holdings Corp',

    'VIP': 'VimpelCom Ltd.',

    'FTSL': 'First Trust Senior Loan Fund ETF',

    'IMO': 'Imperial Oil Limited',

    'TACO': 'Del Taco Restaurants, Inc.',

    'NEWTZ': 'Newtek Business Services Corp.',

    'BNCL': 'Beneficial Bancorp, Inc.',

    'COTV': 'Cotiviti Holdings, Inc.',

    'DIAX': 'Nuveen Dow 30SM Dynamic Overwrite Fund',

    'CARZ': 'First Trust NASDAQ Global Auto Index Fund',

    'WSFSL': 'WSFS Financial Corporation',

    'FDP': 'Fresh Del Monte Produce, Inc.',

    'RICE': 'Rice Energy Inc.',

    'KIO': 'KKR Income Opportunities Fund',

    'KITE': 'Kite Pharma, Inc.',

    'HPT': 'Hospitality Properties Trust',

    'SFR': 'Colony Starwood Homes',

    'CRUS': 'Cirrus Logic, Inc.',

    'LSXMA': 'Liberty Media Corporation',

    'NTCT': 'NetScout Systems, Inc.',

    'DFT': 'Dupont Fabros Technology, Inc.',

    'SCSC': 'ScanSource, Inc.',

    'WFC-J': 'Wells Fargo & Company',

    'ASCMA': 'Ascent Capital Group, Inc.',

    'TEF': 'Telefonica SA',

    'UHAL': 'Amerco',

    'CFNB': 'California First National Bancorp',

    'MFD': 'Macquarie/First Trust Global',

    'BELFB': 'Bel Fuse Inc.',

    'IBTX': 'Independent Bank Group, Inc',

    'NSSC': 'NAPCO Security Technologies, Inc.',

    'FUR': 'Winthrop Realty Trust',

    'HEOP': 'Heritage Oaks Bancorp',

    'GTLS': 'Chart Industries, Inc.',

    'FNX': 'First Trust Mid Cap Core AlphaDEX Fund',

    'RELL': 'Richardson Electronics, Ltd.',

    'AGX': 'Argan, Inc.',

    'IHD': 'Voya Emerging Markets High Income Dividend Equity Fund',

    'ATRS': 'Antares Pharma, Inc.',

    'NWHM': 'New Home Company Inc. (The)',

    'VISI': 'Volt Information Sciences, Inc.',

    'MFA-B': 'MFA Financial, Inc.',

    'EGAS': 'Gas Natural Inc.',

    'NAVB': 'Navidea Biopharmaceuticals, Inc.',

    'FEO': 'First Trust/Aberdeen Emerging Opportunity Fund',

    'USEG': 'U.S. Energy Corp.',

    'SGB': 'Southwest Georgia Financial Corporation',

    'HTGM': 'HTG Molecular Diagnostics, Inc.',

    'TGA': 'Transglobe Energy Corp',

    'FLXN': 'Flexion Therapeutics, Inc.',

    'TGEN': 'Tecogen Inc.',

    'EAB': 'Entergy Arkansas, Inc.',

    'RNVA': 'Rennova Health, Inc.',

    'RIO': 'Rio Tinto Plc',

    'MATW': 'Matthews International Corporation',

    'PINC': 'Premier, Inc.',

    'CBB': 'Cincinnati Bell Inc',

    'HYLS': 'First Trust High Yield Long/Short ETF',

    'ISRG': 'Intuitive Surgical, Inc.',

    'FULL': 'Full Circle Capital Corporation',

    'CPL': 'CPFL Energia S.A.',

    'ABR-C': 'Arbor Realty Trust',

    'SMSI': 'Smith Micro Software, Inc.',

    'QURE': 'uniQure N.V.',

    'CNLMR': 'CB Pharma Acquisition Corp.',

    'HCHC': 'HC2 Holdings, Inc.',

    'DXJS': 'WisdomTree Japan Hedged SmallCap Equity Fund',

    'HURC': 'Hurco Companies, Inc.',

    'HCAP': 'Harvest Capital Credit Corporation',

    'ARCB': 'ArcBest Corporation',

    'CFMS': 'ConforMIS, Inc.',

    'PMV': 'PMV Acquisition Corp.',

    'EGAN': 'eGain Corporation',

    'VONV': 'Vanguard Russell 1000 Value ETF',

    'SYMX': 'Synthesis Energy Systems, Inc.',

    'VNO-L': 'Vornado Realty Trust',

    'UAMY': 'United States Antimony Corporation',

    'DB': 'Deutsche Bank AG',

    'MDSO': 'Medidata Solutions, Inc.',

    'BMRC': 'Bank of Marin Bancorp',

    'NVGS': 'Navigator Holdings Ltd.',

    'NXTD': 'NXT-ID Inc.',

    'KLIC': 'Kulicke and Soffa Industries, Inc.',

    'AVG': 'AVG Technologies N.V.',

    'MTB.WS': 'M&T Bank Corporation',

    'FRBK': 'Republic First Bancorp, Inc.',

    'NYNY': 'Empire Resorts, Inc.',

    'AIXG': 'Aixtron SE',

    'IBN': 'ICICI Bank Limited',

    'CVCY': 'Central Valley Community Bancorp',

    'ASRVP': 'AmeriServ Financial Inc.',

    'MDT': 'Medtronic plc',

    'TIER': 'TIER REIT, Inc.',

    'MMC': 'Marsh & McLennan Companies, Inc.',

    'AAOI': 'Applied Optoelectronics, Inc.',

    'YDKN': 'Yadkin Financial Corporation',

    'AQXP': 'Aquinox Pharmaceuticals, Inc.',

    'FSAM': 'Fifth Street Asset Management Inc.',

    'NSIG': 'NeuroSigma, Inc.',

    'BGE-B': 'Baltimore Gas & Electric Company',

    'RMR': 'The RMR Group Inc.',

    'THM': 'International Tower Hill Mines Ltd',

    'RYN': 'Rayonier Inc.',

    'PRGX': 'PRGX Global, Inc.',

    'NZF': 'Nuveen Enhanced Municipal Credit Opportunities Fun',

    'FFNW': 'First Financial Northwest, Inc.',

    'MMT': 'MFS Multimarket Income Trust',

    'TERP': 'TerraForm Power, Inc.',

    'CCU': 'Compania Cervecerias Unidas, S.A.',

    'BBT-H': 'BB&T Corporation',

    'PCO': 'Pendrell Corporation',

    'NAVI': 'Navient Corporation',

    'NXPI': 'NXP Semiconductors N.V.',

    'SORL': 'SORL Auto Parts, Inc.',

    'GVP': 'GSE Systems, Inc.',

    'JASN': 'Jason Industries, Inc.',

    'CAF': 'Morgan Stanley China A Share Fund Inc.',

    'VPG': 'Vishay Precision Group, Inc.',

    'ICAD': 'icad inc.',

    'TE': 'TECO Energy, Inc.',

    'CAPX': 'Elkhorn S&P 500 Capital Expenditures Portfolio',

    'EDUC': 'Educational Development Corporation',

    'CERCW': 'Cerecor Inc.',

    'BSD': 'BlackRock Strategic Municipal Trust Inc. (The)',

    'WATT': 'Energous Corporation',

    'QUIK': 'QuickLogic Corporation',

    'CBAY': 'Cymabay Therapeutics Inc.',

    'XLRN': 'Acceleron Pharma Inc.',

    'NXTDW': 'NXT-ID Inc.',

    'MIC': 'Macquarie Infrastructure Company',

    'TRGP': 'Targa Resources, Inc.',

    'MS-A': 'Morgan Stanley',

    'EPR-F': 'EPR Properties',

    'AMD': 'Advanced Micro Devices, Inc.',

    'RAS-A': 'RAIT Financial Trust',

    'LFC': 'China Life Insurance Company Limited',

    'PHH': 'PHH Corp',

    'IFGL': 'iShares FTSE EPRA/NAREIT Global Real Estate ex-U.S. Index Fund',

    'GPP': 'Green Plains Partners LP',

    'RELV': 'Reliv\' International, Inc.',

    'BETR': 'Amplify Snack Brands, inc.',

    'CTXS': 'Citrix Systems, Inc.',

    'AI': 'Arlington Asset Investment Corp',

    'AHPI': 'Allied Healthcare Products, Inc.',

    'BFY': 'BlackRock New York Municipal Income Trust II',

    'FUEL': 'Rocket Fuel Inc.',

    'GNTX': 'Gentex Corporation',

    'PGNX': 'Progenics Pharmaceuticals Inc.',

    'WSR': 'Whitestone REIT',

    'MNOV': 'MediciNova, Inc.',

    'CHE': 'Chemed Corp.',

    'CVE': 'Cenovus Energy Inc',

    'OIBR': 'Oi S.A.',

    'AMT-B': 'American Tower Corporation (REIT)',

    'WYIG': 'JM Global Holding Company',

    'ALL-B': 'Allstate Corporation (The)',

    'GPRO': 'GoPro, Inc.',

    'ULH': 'Universal Logistics Holdings, Inc.',

    'ENZY          ': 'Enzymotec Ltd.',

    'VIPS': 'Vipshop Holdings Limited',

    'SNPS': 'Synopsys, Inc.',

    'ASTE': 'Astec Industries, Inc.',

    'CPSI': 'Computer Programs and Systems, Inc.',

    'MOC': 'Command Security Corporation',

    'GIFI': 'Gulf Island Fabrication, Inc.',

    'EQC-D': 'Equity Commonwealth',

    'ABCO': 'The Advisory Board Company',

    'REED': 'Reeds, Inc.',

    'FNV': 'Franco-Nevada Corporation',

    'SBNY': 'Signature Bank',

    'LKOR': 'FlexShares Credit-Scored US Long Corporate Bond Index Fund',

    'AXL': 'American Axle & Manufacturing Holdings, Inc.',

    'GDV-D': 'Gabelli Dividend',

    'AMH-D': 'American Homes 4 Rent',

    'PBH': 'Prestige Brand Holdings, Inc.',

    'CLX': 'Clorox Company (The)',

    'GLPG': 'Galapagos NV',

    'AIRM': 'Air Methods Corporation',

    'LXFT': 'Luxoft Holding, Inc.',

    'AMRS': 'Amyris, Inc.',

    'DDBI': 'Legg Mason Developed EX-US Diversified Core ETF',

    'ORRF': 'Orrstown Financial Services Inc',

    'DLNG': 'Dynagas LNG Partners LP',

    'AAPC': 'Atlantic Alliance Partnership Corp.',

    'G': 'Genpact Limited',

    'LMIA': 'LMI Aerospace, Inc.',

    'EW': 'Edwards Lifesciences Corporation',

    'SSL': 'Sasol Ltd.',

    'CANF': 'Can-Fite Biopharma Ltd',

    'NVLS': 'Nivalis Therapeutics, Inc.',

    'CASM': 'CAS Medical Systems, Inc.',

    'PW': 'Power REIT',

    'MGNX': 'MacroGenics, Inc.',

    'PSCF': 'PowerShares S&P SmallCap Financials Portfolio',

    'IPB': 'Merrill Lynch & Co., Inc.',

    'BECN': 'Beacon Roofing Supply, Inc.',

    'UVE': 'UNIVERSAL INSURANCE HOLDINGS INC',

    'GS-J': 'Goldman Sachs Group, Inc. (The)',

    'CRF': 'Cornerstone Strategic Return Fund, Inc. (The)',

    'CCCL': 'China Ceramics Co., Ltd.',

    'PCAR': 'PACCAR Inc.',

    'QLGC': 'QLogic Corporation',

    'CHSCL': 'CHS Inc',

    'TCB': 'TCF Financial Corporation',

    'LSBK': 'Lake Shore Bancorp, Inc.',

    'GHY': 'Prudential Global Short Duration High Yield Fund, Inc.',

    'GPRK': 'Geopark Ltd',

    'LION': 'Fidelity Southern Corporation',

    'FORM': 'FormFactor, Inc.',

    'OFG-B': 'OFG Bancorp',

    'OXFD': 'Oxford Immunotec Global PLC',

    'ACTS': 'Actions Semiconductor Co., Ltd.',

    'CDZI': 'Cadiz, Inc.',

    'RGNX': 'REGENXBIO Inc.',

    'MMU': 'Western Asset Managed Municipals Fund, Inc.',

    'ABIL': 'Ability Inc.',

    'SGEN': 'Seattle Genetics, Inc.',

    'DJCO': 'Daily Journal Corp. (S.C.)',

    'HRZN': 'Horizon Technology Finance Corporation',

    'PSTG': 'Pure Storage, Inc. ',

    'NSS': 'NuStar Logistics, L.P.',

    'CYTXW': 'Cytori Therapeutics Inc',

    'WDR': 'Waddell & Reed Financial, Inc.',

    'ATEN': 'A10 Networks, Inc.',

    'NPV': 'Nuveen Virginia Premium Income Municipal Fund',

    'FXCB': 'Fox Chase Bancorp, Inc.',

    'DTRM': 'Determine, Inc. ',

    'FII': 'Federated Investors, Inc.',

    'CACQ': 'Caesars Acquisition Company',

    'NYCB-U': 'New York Community Bancorp, Inc.',

    'NOA': 'North American Energy Partners, Inc.',

    'LFUS': 'Littelfuse, Inc.',

    'JPC': 'Nuveen Preferred Income Opportunites Fund',

    'ACTG': 'Acacia Research Corporation',

    'A': 'Agilent Technologies, Inc.',

    'MYI': 'Blackrock MuniYield Quality Fund III, Inc.',

    'CM': 'Canadian Imperial Bank of Commerce',

    'DVN': 'Devon Energy Corporation',

    'JSYNW': 'Jensyn Acquistion Corp.',

    'CRK': 'Comstock Resources, Inc.',

    'GJH': 'STRATS Trust',

    'KIM-K': 'Kimco Realty Corporation',

    'VNO-G': 'Vornado Realty Trust',

    'KMI': 'Kinder Morgan, Inc.',

    'KEYW': 'The KEYW Holding Corporation',

    'CYCC': 'Cyclacel Pharmaceuticals, Inc.',

    'FLAT': 'region',

    'RTN': 'Raytheon Company',

    'NTWK': 'NetSol Technologies Inc.',

    'WHR': 'Whirlpool Corporation',

    'PRTO': 'Proteon Therapeutics, Inc.',

    'NVIV': 'InVivo Therapeutics Holdings Corp.',

    'QGEN': 'Qiagen N.V.',

    'CMT': 'Core Molding Technologies Inc',

    'GFED': 'Guaranty Federal Bancshares, Inc.',

    'MX': 'MagnaChip Semiconductor Corporation',

    'LZB': 'La-Z-Boy Incorporated',

    'ZLIG': 'Aperion Biologics, Inc.',

    'MIRN': 'Mirna Therapeutics, Inc.',

    'AGI': 'Alamos Gold Inc.',

    'MINI': 'Mobile Mini, Inc.',

    'PZN': 'Pzena Investment Management Inc',

    'NMR': 'Nomura Holdings Inc ADR',

    'AGO': 'Assured Guaranty Ltd.',

    'BW': 'Babcock',

    'KBSF': 'KBS Fashion Group Limited',

    'UHS': 'Universal Health Services, Inc.',

    'WMAR': 'West Marine, Inc.',

    'SYUT': 'Synutra International, Inc.',

    'QUMU': 'Qumu Corporation',

    'KWEB': 'KraneShares CSI China Internet ETF',

    'UBSH': 'Union Bankshares Corporation',

    'NETE': 'Net Element, Inc.',

    'BF.B': 'Brown Forman Corporation',

    'GTN.A': 'Gray Television, Inc.',

    'TCB.WS': 'TCF Financial Corporation',

    'MSK': 'Morgan Stanley',

    'ZNWAA': 'Zion Oil & Gas Inc',

    'YUM': 'Yum! Brands, Inc.',

    'NFBK': 'Northfield Bancorp, Inc.',

    'WOOD': 'iShares S&P Global Timber & Forestry Index Fund',

    'HYZD': 'WisdomTree BofA Merrill Lynch High Yield Bond Zero Duration Fu',

    'AWI': 'Armstrong World Industries Inc',

    'ECPG': 'Encore Capital Group Inc',

    'HUSI-F.CL': 'HSBC USA, Inc.',

    'TSS': 'Total System Services, Inc.',

    'ADK': 'Adcare Health Systems Inc',

    'KO': 'Coca-Cola Company (The)',

    'CDR': 'Cedar Realty Trust, Inc.',

    'PPP': 'Primero Mining Corp',

    'CCCR': 'China Commercial Credit, Inc.',

    'SMTC': 'Semtech Corporation',

    'GPIA': 'GP Investments Acquisition Corp.',

    'JKS': 'JinkoSolar Holding Company Limited',

    'CONN': 'Conn\'s, Inc.',

    'CLWT': 'Euro Tech Holdings Company Limited',

    'TRIP': 'TripAdvisor, Inc.',

    'FLWS': '1-800 FLOWERS.COM, Inc.',

    'FRC-E': 'FIRST REPUBLIC BANK',

    'SOXX': 'iShares PHLX SOX Semiconductor Sector Index Fund',

    'DDE': 'Dover Downs Gaming & Entertainment Inc',

    'EOI': 'Eaton Vance Enhance Equity Income Fund',

    'NVCR': 'NovoCure Limited',

    'VRTX': 'Vertex Pharmaceuticals Incorporated',

    'GBCI': 'Glacier Bancorp, Inc.',

    'LIOX': 'Lionbridge Technologies, Inc.',

    'HDRAU': 'Hydra Industries Acquisition Corp.',

    'FTRI': 'First Trust Indxx Global Natural Resources Income ETF',

    'PRH': 'Prudential Financial, Inc.',

    'NSC': 'Norfolk Souther Corporation',

    'TYL': 'Tyler Technologies, Inc.',

    'ALR-B': 'Alere Inc.',

    'GURE': 'Gulf Resources, Inc.',

    'MGIC': 'Magic Software Enterprises Ltd.',

    'PARN': 'Parnell Pharmaceuticals Holdings Ltd',

    'BBW': 'Build-A-Bear Workshop, Inc.',

    'RT': 'Ruby Tuesday, Inc.',

    'SIG': 'Signet Jewelers Limited',

    'FNFG': 'First Niagara Financial Group Inc.',

    'WFC': 'Wells Fargo & Company',

    'USB': 'U.S. Bancorp',

    'TSLX': 'TPG Specialty Lending, Inc.',

    'MYCC': 'ClubCorp Holdings, Inc.',

    'CDR-B': 'Cedar Realty Trust, Inc.',

    'RDC': 'Rowan Companies plc',

    'NADL': 'North Atlantic Drilling Ltd.',

    'SFE': 'Safeguard Scientifics, Inc.',

    'DGX': 'Quest Diagnostics Incorporated',

    'ARIS': 'ARI Network Services, Inc.',

    'DUK': 'Duke Energy Corporation',

    'QTWO': 'Q2 Holdings, Inc.',

    'AZN': 'Astrazeneca PLC',

    'WSTL': 'Westell Technologies, Inc.',

    'SPSC': 'SPS Commerce, Inc.',

    'PRA': 'ProAssurance Corporation',

    'SEED': 'Origin Agritech Limited',

    'GRID': 'First Trust NASDAQ Clean Edge Smart Grid Infrastructure Index ',

    'APHB': 'AmpliPhi Biosciences Corporation',

    'AFCO': 'American Farmland Company',

    'ESBK': 'Elmira Savings Bank NY (The)',

    'HE-U': 'Hawaiian Electric Industries, Inc.',

    'ATV': 'Acorn International, Inc.',

    'PSA-Z': 'Public Storage',

    'SMRT': 'Stein Mart, Inc.',

    'PHT': 'Pioneer High Income Trust',

    'CIBR': 'First Trust NASDAQ Cybersecurity ETF',

    'HTF': 'Horizon Technology Finance Corporation',

    'DENN': 'Denny\'s Corporation',

    'TWER': 'Towerstream Corporation',

    'SOR': 'Source Capital, Inc.',

    'ASEI': 'American Science and Engineering, Inc.',

    'SIR': 'Select Income REIT',

    'DRI': 'Darden Restaurants, Inc.',

    'NEE-J': 'NextEra Energy, Inc.',

    'SPWR': 'SunPower Corporation',

    'MDGS': 'Medigus Ltd.',

    'HOTR': 'Chanticleer Holdings, Inc.',

    'MB': 'MINDBODY, Inc.',

    'ADK-A': 'Adcare Health Systems Inc',

    'PFX': 'Phoenix Companies, Inc. (The)',

    'SCHL': 'Scholastic Corporation',

    'BURL': 'Burlington Stores, Inc.',

    'PGLC': 'Pershing Gold Corporation',

    'ATHM': 'Autohome Inc.',

    'RAS': 'RAIT Financial Trust',

    'CCUR': 'Concurrent Computer Corporation',

    'BC': 'Brunswick Corporation',

    'DELT': 'Delta Technology Holdings Limited',

    'LBTYB': 'Liberty Global plc',

    'ZNGA': 'Zynga Inc.',

    'NSAM': 'NorthStar Asset Management Group, Inc.',

    'CBG': 'CBRE Group, Inc.',

    'NRG': 'NRG Energy, Inc.',

    'BGR': 'BlackRock Energy and Resources Trust',

    'FLR': 'Fluor Corporation',

    'HTHT': 'China Lodging Group, Limited',

    'SINO': 'Sino-Global Shipping America, Ltd.',

    'RBIO': 'rEVO Biologics, Inc.',

    'OBAS': 'Optibase Ltd.',

    'SEMI': 'SunEdison Semiconductor Limited',

    'CLRBW': 'Cellectar Biosciences, Inc.',

    'BGH': 'Babson Capital Global Short Duration High Yield Fund',

    'XCOM': 'Xtera Communications, Inc.',

    'ATRO': 'Astronics Corporation',

    'SCTY': 'SolarCity Corporation',

    'PPH': 'VanEck Vectors Pharmaceutical ETF',

    'MCFT': 'MCBC Holdings, Inc.',

    'IPGP': 'IPG Photonics Corporation',

    'LPTN': 'Lpath, Inc.',

    'SLIM': 'The Obesity ETF',

    'BOTJ': 'Bank of the James Financial Group, Inc.',

    'FAV': 'First Trust Dividend and Income Fund',

    'STAR-I': 'iStar Financial Inc.',

    'PBA': 'Pembina Pipeline Corp.',

    'MTW': 'Manitowoc Company, Inc. (The)',

    'VTL': 'Vital Therapies, Inc.',

    'PSDV': 'pSivida Corp.',

    'FIT': 'Fitbit, Inc.',

    'BBT-G': 'BB&T Corporation',

    'EFM': 'Entergy Mississippi, Inc.',

    'KHC': 'The Kraft Heinz Company',

    'CNHI': 'CNH Industrial N.V.',

    'SAEX': 'SAExploration Holdings, Inc.',

    'INB': 'Cohen & Steers Global Income Builder, Inc.',

    'CLNY-B': 'Colony Capital, Inc',

    'AGO-F': 'Assured Guaranty Ltd.',

    'QAT': 'iShares MSCI Qatar Capped ETF',

    'JBSS': 'John B. Sanfilippo & Son, Inc.',

    'AFSD': 'Aflac Incorporated',

    'TPB': 'Turning Point Brands, Inc.',

    'PH': 'Parker-Hannifin Corporation',

    'RDNT': 'RadNet, Inc.',

    'ORCL': 'Oracle Corporation',

    'TPLM': 'Triangle Petroleum Corporation',

    'GOGO': 'Gogo Inc.',

    'TWX': 'Time Warner Inc.',

    'KIQ': 'Kelso Technologies Inc',

    'PCTY': 'Paylocity Holding Corporation',

    'WSBF': 'Waterstone Financial, Inc.',

    'LINDW': 'Lindblad Expeditions Holdings Inc.',

    'PSA-Y': 'Public Storage',

    'XEL': 'Xcel Energy Inc.',

    'THR': 'Thermon Group Holdings, Inc.',

    'WHLRP': 'Wheeler Real Estate Investment Trust, Inc.',

    'FLIC': 'The First of Long Island Corporation',

    'UFPT': 'UFP Technologies, Inc.',

    'GPAC': 'Global Partner Acquisition Corp.',

    'XOXO': 'XO Group, Inc.',

    'SHAK': 'Shake Shack, Inc.',

    'BUFF': 'Blue Buffalo Pet Products, Inc.',

    'MHG': 'Marine Harvest ASA',

    'UBA': 'Urstadt Biddle Properties Inc.',

    'RNR-E': 'RenaissanceRe Holdings Ltd.',

    'KED': 'Kayne Anderson Energy Development Company',

    'GOODN': 'Gladstone Commercial Corporation',

    'PGEM': 'Ply Gem Holdings, Inc.',

    'TXT': 'Textron Inc.',

    'CSC': 'Computer Sciences Corporation',

    'SKLN': 'Skyline Medical Inc.',

    'DTUL': 'region',

    'WBKC': 'Wolverine Bancorp, Inc.',

    'WPG-H': 'WP Glimcher Inc.',

    'FJP': 'First Trust Japan AlphaDEX Fund',

    'FDEU': 'First Trust Dynamic Europe Equity Income Fund',

    'PRCP': 'Perceptron, Inc.',

    'LDP': 'Cohen & Steers Limited Duration Preferred and Income Fund, Inc',

    'NBTB': 'NBT Bancorp Inc.',

    'BRSS': 'Global Brass and Copper Holdings, Inc.',

    'BWINA': 'Baldwin & Lyons, Inc.',

    'TPC': 'Tutor Perini Corporation',

    'GPACU': 'Global Partner Acquisition Corp.',

    'WTR': 'Aqua America, Inc.',

    'RIBT': 'RiceBran Technologies',

    'JHX': 'James Hardie Industries plc.',

    'QDEL': 'Quidel Corporation',

    'UCP': 'UCP, Inc.',

    'C-J': 'Citigroup Inc.',

    'FIBK': 'First Interstate BancSystem, Inc.',

    'HSKA': 'Heska Corporation',

    'WSFS': 'WSFS Financial Corporation',

    'IRET': 'Investors Real Estate Trust',

    'CNS': 'Cohn & Steers Inc',

    'HBHC': 'Hancock Holding Company',

    'THFF': 'First Financial Corporation Indiana',

    'BHBK': 'Blue Hills Bancorp, Inc.',

    'LAQ': 'Latin America Equity Fund, Inc. (The)',

    'LSTR': 'Landstar System, Inc.',

    'NUW': 'Nuveen AMT-Free Municipal Value Fund',

    'CLFD': 'Clearfield, Inc.',

    'LNDC': 'Landec Corporation',

    'OAKS-A': 'Five Oaks Investment Corp.',

    'MFL': 'Blackrock MuniHoldings Investment Quality Fund',

    'OMC': 'Omnicom Group Inc.',

    'SDT': 'SandRidge Mississippian Trust I',

    'TNH': 'Terra Nitrogen Company, L.P.',

    'MARA': 'Marathon Patent Group, Inc.',

    'SJT': 'San Juan Basin Royalty Trust',

    'DSM': 'Dreyfus Strategic Municipal Bond Fund, Inc.',

    'KCC': 'Lehman ABS Corporation',

    'CPXX': 'Celator Pharmaceuticals Inc.',

    'LIQT': 'LiqTech International, Inc.',

    'ESNT': 'Essent Group Ltd.',

    'SEE': 'Sealed Air Corporation',

    'MMYT': 'MakeMyTrip Limited',

    'KONA': 'Kona Grill, Inc.',

    'AF': 'Astoria Financial Corporation',

    'O-F': 'Realty Income Corporation',

    'BORN': 'China New Borun Corporation',

    'VIAB': 'Viacom Inc.',

    'GLRI': 'Glori Energy Inc',

    'SLVO': 'region',

    'VSTO': 'Vista Outdoor Inc.',

    'ING': 'ING Group, N.V.',

    'SZMK': 'Sizmek Inc.',

    'HBP': 'Huttig Building Products, Inc.',

    'EGIF': 'Eagle Growth and Income Opportunities Fund',

    'PJT': 'PJT Partners Inc.',

    'PRAH': 'PRA Health Sciences, Inc.',

    'CNI': 'Canadian National Railway Company',

    'GGZ': 'Gabelli Global Small and Mid Cap Value Trust (The)',

    'HSY': 'Hershey Company (The)',

    'IILG': 'Interval Leisure Group, Inc.',

    'HOTRW': 'Chanticleer Holdings, Inc.',

    'IPI': 'Intrepid Potash, Inc',

    'VIA': 'Viacom Inc.',

    'STAR-F': 'iStar Financial Inc.',

    'SIFI': 'SI Financial Group, Inc.',

    'CPLA': 'Capella Education Company',

    'CIG': 'Comp En De Mn Cemig ADS',

    'C': 'Citigroup Inc.',

    'KURA': 'Kura Oncology, Inc.',

    'MEMP': 'Memorial Production Partners LP',

    'SGMO': 'Sangamo BioSciences, Inc.',

    'RIGL': 'Rigel Pharmaceuticals, Inc.',

    'XENT': 'Intersect ENT, Inc.',

    'DSX-B': 'Diana Shipping inc.',

    'SYRG': 'Synergy Resources Corporation',

    'SWNC': 'Southwestern Energy Company',

    'KEY-G': 'KeyCorp',

    'OIA': 'Invesco Municipal Income Opportunities Trust',

    'PAYX': 'Paychex, Inc.',

    'XNPT': 'XenoPort, Inc.',

    'NLY-D': 'Annaly Capital Management Inc',

    'PML': 'Pimco Municipal Income Fund II',

    'AHL-B': 'Aspen Insurance Holdings Limited',

    'SAM': 'Boston Beer Company, Inc. (The)',

    'SPLS': 'Staples, Inc.',

    'FENX': 'Fenix Parts, Inc.',

    'SBR': 'Sabine Royalty Trust',

    'IGI': 'Western Asset Investment Grade Defined Opportunity Trust Inc.',

    'IVH': 'Ivy High Income Opportunities Fund',

    'HEI': 'Heico Corporation',

    'NWY': 'New York & Company, Inc.',

    'WBK': 'Westpac Banking Corporation',

    'SCCI': 'Shimmick Construction Company, Inc.',

    'CRVP': 'Crystal Rock Holdings, Inc.',

    'STNG': 'Scorpio Tankers Inc.',

    'AB': 'AllianceBernstein Holding L.P.',

    'ASRV': 'AmeriServ Financial Inc.',

    'SCNB': 'Suffolk Bancorp',

    'LAMR': 'Lamar Advertising Company',

    'IAG': 'Iamgold Corporation',

    'CY': 'Cypress Semiconductor Corporation',

    'ISNS': 'Image Sensing Systems, Inc.',

    'TRTL': 'Terrapin 3 Acquisition Corporation',

    'FRC-C': 'FIRST REPUBLIC BANK',

    'BXMX': 'Nuveen S&P 500 Buy-Write Income Fund',

    'CYH': 'Community Health Systems, Inc.',

    'JE': 'Just Energy Group, Inc.',

    'TPHS': 'Trinity Place Holdings Inc.',

    'LXRX': 'Lexicon Pharmaceuticals, Inc.',

    'WEX': 'WEX Inc.',

    'COST': 'Costco Wholesale Corporation',

    'LHO-I': 'LaSalle Hotel Properties',

    'KEQU': 'Kewaunee Scientific Corporation',

    'MHNB': 'Maiden Holdings, Ltd.',

    'PMO': 'Putnam Municipal Opportunities Trust',

    'CLD': 'Cloud Peak Energy Inc',

    'DWCH': 'Datawatch Corporation',

    'EHT': 'Eaton Vance High Income 2021 Target Term Trust',

    'INDY': 'iShares S&P India Nifty 50 Index Fund',

    'ELGX': 'Endologix, Inc.',

    'TNC': 'Tennant Company',

    'KTCC': 'Key Tronic Corporation',

    'WETF': 'WisdomTree Investments, Inc.',

    'ABTX': 'Allegiance Bancshares, Inc.',

    'GNT': 'GAMCO Natural Resources, Gold & Income Tust ',

    'PAACW': 'Pacific Special Acquisition Corp.',

    'MEIP': 'MEI Pharma, Inc.',

    'WING': 'Wingstop Inc.',

    'BCRH': 'Blue Capital Reinsurance Holdings Ltd.',

    'RGR': 'Sturm, Ruger & Company, Inc.',

    'SBUX': 'Starbucks Corporation',

    'TXN': 'Texas Instruments Incorporated',

    'ROL': 'Rollins, Inc.',

    'MDM': 'Mountain Province Diamonds Inc.',

    'PERI': 'Perion Network Ltd',

    'ALL': 'Allstate Corporation (The)',

    'ANDE': 'The Andersons, Inc.',

    'PRQR': 'ProQR Therapeutics N.V.',

    'GS-D': 'Goldman Sachs Group, Inc. (The)',

    'MRO': 'Marathon Oil Corporation',

    'PGR': 'Progressive Corporation (The)',

    'CDW': 'CDW Corporation',

    'AGM-B': 'Federal Agricultural Mortgage Corporation',

    'AXN': 'Aoxing Pharmaceutical Company, Inc.',

    'ERF': 'Enerplus Corporation',

    'SGI': 'Silicon Graphics International Corp',

    'OAK': 'Oaktree Capital Group, LLC',

    'ROIAK': 'Radio One, Inc.',

    'UBP-G': 'Urstadt Biddle Properties Inc.',

    'GDF': 'Western Asset Global Partners Income Fund, Inc.',

    'KRO': 'Kronos Worldwide Inc',

    'SSI': 'Stage Stores, Inc.',

    'CSTM': 'Constellium N.V.',

    'PETX': 'Aratana Therapeutics, Inc.',

    'SHLDW': 'Sears Holdings Corporation',

    'FRP': 'FairPoint Communications, Inc.',

    'TWO': 'Two Harbors Investments Corp',

    'AYR': 'Aircastle Limited',

    'GCO': 'Genesco Inc.',

    'BCR': 'C.R. Bard, Inc.',

    'DNI': 'Dividend and Income Fund',

    'ERN': 'Erin Energy Corp.',

    'VSAT': 'ViaSat, Inc.',

    'DAVE': 'Famous Dave\'s of America, Inc.',

    'TNP-D': 'Tsakos Energy Navigation Ltd',

    'ARTX': 'Arotech Corporation',

    'WHG': 'Westwood Holdings Group Inc',

    'ECF': 'Ellsworth Growth and Income Fund Ltd.',

    'PFBC': 'Preferred Bank',

    'SFBC': 'Sound Financial Bancorp, Inc.',

    'WFM': 'Whole Foods Market, Inc.',

    'NXR': 'Nuveen Select Tax Free Income Portfolio III',

    'VOXX': 'VOXX International Corporation',

    'OKE': 'ONEOK, Inc.',

    'SHOS': 'Sears Hometown and Outlet Stores, Inc.',

    'ECT': 'ECA Marcellus Trust I',

    'SAVE': 'Spirit Airlines, Inc.',

    'CLNY-C': 'Colony Capital, Inc',

    'CEL': 'Cellcom Israel, Ltd.',

    'KFRC': 'Kforce, Inc.',

    'EARS': 'Auris Medical Holding AG',

    'CYRX': 'CryoPort, Inc.',

    'TLF': 'Tandy Leather Factory, Inc.',

    'GXP': 'Great Plains Energy Inc',

    'UMC': 'United Microelectronics Corporation',

    'BBX': 'BBX Capital Corporation',

    'WMGI': 'Wright Medical Group N.V.',

    'BPI': 'Bridgepoint Education, Inc.',

    'GJP': 'Synthetic Fixed-Income Securities, Inc.',

    'RLH': 'Red Lion Hotels Corporation',

    'DCO': 'Ducommun Incorporated',

    'SNV-C': 'Synovus Financial Corp.',

    'PDT': 'John Hancock Premium Dividend Fund',

    'SFM': 'Sprouts Farmers Market, Inc.',

    'NCB': 'Nuveen California Municipal Value Fund 2',

    'TRV': 'The Travelers Companies, Inc.',

    'SGMS': 'Scientific Games Corp',

    'FMN': 'Federated Premier Municipal Income Fund',

    'CLF': 'Cliffs Natural Resources Inc.',

    'BPOP': 'Popular, Inc.',

    'MBII': 'Marrone Bio Innovations, Inc.',

    'PNNT': 'PennantPark Investment Corporation',

    'FITB': 'Fifth Third Bancorp',

    'PARR': 'Par Pacific Holdings, Inc.',

    'DTLA-': 'Brookfield DTLA Inc.',

    'MTBCP': 'Medical Transcription Billing, Corp.',

    'MUI': 'Blackrock Muni Intermediate Duration Fund Inc',

    'FNY': 'First Trust Mid Cap Growth AlphaDEX Fund',

    'QQQ': 'PowerShares QQQ Trust, Series 1',

    'WFC-W': 'Wells Fargo & Company',

    'ENR': 'Energizer Holdings, Inc.',

    'AFSI': 'AmTrust Financial Services, Inc.',

    'SEIC': 'SEI Investments Company',

    'HDRA': 'Hydra Industries Acquisition Corp.',

    'PPL': 'PPL Corporation',

    'JSM': 'SLM Corporation',

    'WSCI': 'WSI Industries Inc.',

    'TRIB': 'Trinity Biotech plc',

    'DEO': 'Diageo plc',

    'WNFM': 'Wayne Farms, Inc.',

    'EDBI': 'Legg Mason Emerging Markets Diversified Core ETF',

    'VNRCP': 'Vanguard Natural Resources LLC',

    'CFC-B': 'Countrywide Financial Corporation',

    'BLDP': 'Ballard Power Systems, Inc.',

    'ISL': 'Aberdeen Israel Fund, Inc.',

    'WLKP': 'Westlake Chemical Partners LP',

    'UNIS': 'Unilife Corporation',

    'MS': 'Morgan Stanley',

    'SLB': 'Schlumberger N.V.',

    'DNKN': 'Dunkin\' Brands Group, Inc.',

    'BTE': 'Baytex Energy Corp',

    'MLM': 'Martin Marietta Materials, Inc.',

    'PCBK': 'Pacific Continental Corporation (Ore)',

    'DLX': 'Deluxe Corporation',

    'PSTB': 'Park Sterling Corporation',

    'BIOD': 'Biodel Inc.',

    'VER-F': 'VEREIT Inc.',

    'AVEO': 'AVEO Pharmaceuticals, Inc.',

    'SSP': 'E.W. Scripps Company (The)',

    'NWPX': 'Northwest Pipe Company',

    'ACXM': 'Acxiom Corporation',

    'VHC': 'VirnetX Holding Corp',

    'PHMD': 'PhotoMedex, Inc.',

    'JOF': 'Japan Smaller Capitalization Fund Inc',

    'EVLV': 'EVINE Live Inc.',

    'SLAB': 'Silicon Laboratories, Inc.',

    'CCI': 'Crown Castle International Corporation',

    'STZ': 'Constellation Brands Inc',

    'CEO': 'CNOOC Limited',

    'JCI': 'Johnson Controls, Inc.',

    'CNAT': 'Conatus Pharmaceuticals Inc.',

    'ATOS': 'Atossa Genetics Inc.',

    'PCG-H': 'Pacific Gas & Electric Co.',

    'BQH': 'Blackrock New York Municipal Bond Trust',

    'AMH-A': 'American Homes 4 Rent',

    'ADRU': 'BLDRS Europe 100 ADR Index Fund',

    'ENLC': 'EnLink Midstream, LLC',

    'HRMNU': 'Harmony Merger Corp.',

    'PAI': 'Pacific American Income Shares, Inc.',

    'WHLRW': 'Wheeler Real Estate Investment Trust, Inc.',

    'TCI': 'Transcontinental Realty Investors, Inc.',

    'TDE': 'Telephone and Data Systems, Inc.',

    'SLCT': 'Select Bancorp, Inc.',

    'JLS': 'Nuveen Mortgage Opportunity Term Fund',

    'RADA': 'Rada Electronics Industries Limited',

    'LUK': 'Leucadia National Corporation',

    'PCG-D': 'Pacific Gas & Electric Co.',

    'RNP': 'Cohen & Steers Reit and Preferred Income Fund Inc',

    'GJO': 'STRATS Trust',

    'OXLC': 'Oxford Lane Capital Corp.',

    'DTJ': 'DTE Energy Company',

    'SXC': 'SunCoke Energy, Inc.',

    'NTN': 'NTN Buzztime, Inc.',

    'WRB-B': 'W.R. Berkley Corporation',

    'YORW': 'The York Water Company',

    'FARM': 'Farmer Brothers Company',

    'RGA': 'Reinsurance Group of America, Incorporated',

    'FGB': 'First Trust Specialty Finance and Financial Opportunities Fund',

    'E': 'ENI S.p.A.',

    'SBS': 'Companhia de saneamento Basico Do Estado De Sao Paulo - Sabesp',

    'HCA': 'HCA Holdings, Inc.',

    'BJRI': 'BJ\'s Restaurants, Inc.',

    'IOT': 'Income Opportunity Realty Investors, Inc.',

    'HNSN': 'Hansen Medical, Inc.',

    'LMBS': 'First Trust Low Duration Opportunities ETF',

    'MUS': 'Blackrock MuniHoldings Quality Fund, Inc.',

    'AXGN': 'AxoGen, Inc.',

    'LUX': 'Luxottica Group, S.p.A.',

    'PTY': 'Pimco Corporate & Income Opportunity Fund',

    'AGM.A': 'Federal Agricultural Mortgage Corporation',

    'NPP': 'Nuveen Performance Plus Municipal Fund, Inc.',

    'CCBG': 'Capital City Bank Group',

    'FHN-A': 'First Horizon National Corporation',

    'CORI': 'Corium International, Inc.',

    'AMRN': 'Amarin Corporation PLC',

    'MS-E': 'Morgan Stanley',

    'SRT': 'StarTek, Inc.',

    'LPTH': 'LightPath Technologies, Inc.',

    'HNRG': 'Hallador Energy Company',

    'GME': 'Gamestop Corporation',

    'TLOG': 'TetraLogic Pharmaceuticals Corporation',

    'FVE': 'Five Star Quality Care, Inc.',

    'ETX           ': 'Eaton Vance Municipal Income 2028 Term Trust',

    'BOFIL': 'BofI Holding, Inc.',

    'MGRC': 'McGrath RentCorp',

    'BWFG': 'Bankwell Financial Group, Inc.',

    'PLD': 'ProLogis, Inc.',

    'OTTR': 'Otter Tail Corporation',

    'QQEW': 'First Trust NASDAQ-100 Equal Weighted Index Fund',

    'MNP': 'Western Asset Municipal Partners Fund, Inc.',

    'OPXAW': 'Opexa Therapeutics, Inc.',

    'LIVN': 'LivaNova PLC',

    'FTV$': 'Fortive Corporation',

    'TCBIP': 'Texas Capital Bancshares, Inc.',

    'CXE': 'Colonial High Income Municipal Trust',

    'SODA': 'SodaStream International Ltd.',

    'CHUY': 'Chuy\'s Holdings, Inc.',

    'AAPL': 'Apple Inc.',

    'PSTI': 'Pluristem Therapeutics, Inc.',

    'HSEA': 'HSBC Holdings plc',

    'SIEB': 'Siebert Financial Corp.',

    'CVX': 'Chevron Corporation',

    'CPSH': 'CPS Technologies Corp.',

    'PRSS': 'CafePress Inc.',

    'BHK': 'Blackrock Core Bond Trust',

    'BOH': 'Bank of Hawaii Corporation',

    'ALOT': 'AstroNova, Inc.',

    'BOSC': 'B.O.S. Better Online Solutions',

    'ISM': 'SLM Corporation',

    'EPD': 'Enterprise Products Partners L.P.',

    'SVBI': 'Severn Bancorp Inc',

    'TROVU': 'TrovaGene, Inc.',

    'BZH': 'Beazer Homes USA, Inc.',

    'SMI': 'Semiconductor  Manufacturing International Corporation',

    'HRC': 'Hill-Rom Holdings Inc',

    'GFA': 'Gafisa SA',

    'CVLY': 'Codorus Valley Bancorp, Inc',

    'SBY': 'Silver Bay Realty Trust Corp.',

    'DF': 'Dean Foods Company',

    'XL': 'XL Group plc',

    'ANCX': 'Access National Corporation',

    'CTLT': 'Catalent, Inc.',

    'STDY': 'SteadyMed Ltd.',

    'ALDX': 'Aldeyra Therapeutics, Inc.',

    'CIL': 'Victory CEMP International Volatility Wtd Index ETF',

    'ORG': 'The Organics ETF',

    'CRAI': 'CRA International,Inc.',

    'PFMT': 'Performant Financial Corporation',

    'GS-C': 'Goldman Sachs Group, Inc. (The)',

    'KEY': 'KeyCorp',

    'EGN': 'Energen Corporation',

    'IPWR': 'Ideal Power Inc.',

    'EQR': 'Equity Residential',

    'ABR-B': 'Arbor Realty Trust',

    'LAYN': 'Layne Christensen Company',

    'CTV': 'Qwest Corporation',

    'BUSE': 'First Busey Corporation',

    'GOVN': 'Government Properties Income Trust',

    'RUSHA': 'Rush Enterprises, Inc.',

    'NPI': 'Nuveen Premium Income Municipal Fund, Inc.',

    'ETR': 'Entergy Corporation',

    'NTES': 'NetEase, Inc.',

    'MVF': 'MuniVest Fund, Inc.',

    'JMBA': 'Jamba, Inc.',

    'HYT': 'Blackrock Corporate High Yield Fund, Inc.',

    'ANTM': 'Anthem, Inc.',

    'CII': 'Blackrock Capital and Income Strategies Fund Inc',

    'RPXC': 'RPX Corporation',

    'NEO': 'NeoGenomics, Inc.',

    'CIA': 'Citizens, Inc.',

    'SXT': 'Sensient Technologies Corporation',

    'NWS': 'News Corporation',

    'RXDX': 'Ignyta, Inc.',

    'FCH': 'FelCor Lodging Trust Incorporated',

    'DWRE': 'DEMANDWARE, INC.',

    'AVID': 'Avid Technology, Inc.',

    'HYF': 'Managed High Yield Plus Fund, Inc.',

    'CBNK': 'Chicopee Bancorp, Inc.',

    'TWIN': 'Twin Disc, Incorporated',

    'ALEX': 'Alexander & Baldwin Holdings, Inc.',

    'OGE': 'OGE Energy Corporation',

    'ESI': 'ITT Educational Services, Inc.',

    'AJG': 'Arthur J. Gallagher & Co.',

    'ALRM': 'Alarm.com Holdings, Inc.',

    'BBU$': 'Brookfield Business Partners L.P.',

    'CPTA': 'Capitala Finance Corp.',

    'SCMP': 'Sucampo Pharmaceuticals, Inc.',

    'CDE': 'Coeur Mining, Inc.',

    'CHGG': 'Chegg, Inc.',

    'NEN': 'New England Realty Associates Limited Partnership',

    'COB': 'CommunityOne Bancorp',

    'MTL-': 'Mechel OAO',

    'BWP': 'Boardwalk Pipeline Partners L.P.',

    'HPP': 'Hudson Pacific Properties, Inc.',

    'MDCA': 'MDC Partners Inc.',

    'ZIOP': 'ZIOPHARM Oncology Inc',

    'URBN': 'Urban Outfitters, Inc.',

    'MIY': 'Blackrock MuniYield Michigan Quality Fund, Inc.',

    'CZZ': 'Cosan Limited',

    'PRTS': 'U.S. Auto Parts Network, Inc.',

    'ORIT': 'Oritani Financial Corp.',

    'DVCR': 'Diversicare Healthcare Services Inc.',

    'TI.A': 'Telecom Italia S.P.A.',

    'FMER-A': 'FirstMerit Corporation',

    'ZUMZ': 'Zumiez Inc.',

    'BCOR': 'Blucora, Inc.',

    'NWN': 'Northwest Natural Gas Company',

    'QPAC': 'Quinpario Acquisition Corp. 2',

    'PTX': 'Pernix Therapeutics Holdings, Inc.',

    'FUL': 'H. B. Fuller Company',

    'AIMT': 'Aimmune Therapeutics, Inc.',

    'TPL': 'Texas Pacific Land Trust',

    'ZFC': 'ZAIS Financial Corp.',

    'SLMAP': 'SLM Corporation',

    'HPS': 'John Hancock Preferred Income Fund III',

    'STAF': 'Staffing 360 Solutions, Inc.',

    'RJF': 'Raymond James Financial, Inc.',

    'RGSE': 'Real Goods Solar, Inc.',

    'RNET': 'RigNet, Inc.',

    'ACHN': 'Achillion Pharmaceuticals, Inc.',

    'MS-G': 'Morgan Stanley',

    'ODP': 'Office Depot, Inc.',

    'ETFC': 'E*TRADE Financial Corporation',

    'MCD': 'McDonald\'s Corporation',

    'UGLD': 'region',

    'HTS-A': 'Hatteras Financial Corp',

    'NWL': 'Newell Brands Inc.',

    'PEG': 'Public Service Enterprise Group Incorporated',

    'GORO': 'Gold Resource Corporation',

    'CIVBP': 'Civista Bancshares, Inc. ',

    'CCXI': 'ChemoCentryx, Inc.',

    'LPLA': 'LPL Financial Holdings Inc.',

    'BSQR': 'BSQUARE Corporation',

    'AON': 'Aon plc',

    'MITT-B': 'AG Mortgage Investment Trust, Inc.',

    'FPA': 'First Trust Asia Pacific Ex-Japan AlphaDEX Fund',

    'MSFT': 'Microsoft Corporation',

    'SAL': 'Salisbury Bancorp, Inc.',

    'CTT': 'CatchMark Timber Trust, Inc.',

    'TCCB': 'Triangle Capital Corporation',

    'WAC': 'Walter Investment Management Corp.',

    'OPXA': 'Opexa Therapeutics, Inc.',

    'ALR': 'Alere Inc.',

    'CALX': 'Calix, Inc',

    'NUVA': 'NuVasive, Inc.',

    'JMM': 'Nuveen Multi-Market Income Fund',

    'SWJ': 'Stanley Black & Decker, Inc.',

    'CIVB': 'Civista Bancshares, Inc. ',

    'BBD': 'Banco Bradesco Sa',

    'AGU': 'Agrium Inc.',

    'NEU': 'NewMarket Corporation',

    'TREC': 'Trecora Resources',

    'CXH': 'Colonial Investment Grade Municipal Trust',

    'NNI': 'Nelnet, Inc.',

    'ANW': 'Aegean Marine Petroleum Network Inc.',

    'ACU': 'Acme United Corporation.',

    'NMZ': 'Nuveen Municipal High Income Opportunity Fund',

    'NMM': 'Navios Maritime Partners LP',

    'ST': 'Sensata Technologies Holding N.V.',

    'BRCD': 'Brocade Communications Systems, Inc.',

    'ONSIZ': 'Oncobiologics, Inc.',

    'INWK': 'InnerWorkings, Inc.',

    'SCVL': 'Shoe Carnival, Inc.',

    'KELYA': 'Kelly Services, Inc.',

    'JHD': 'Nuveen High Income December 2019 Target Term Fund',

    'MDWD': 'MediWound Ltd.',

    'HEES': 'H&E Equipment Services, Inc.',

    'ESMC': 'Escalon Medical Corp.',

    'BOI': 'Brookfield Mortgage Opportunity Income Fund Inc.',

    'CTWS': 'Connecticut Water Service, Inc.',

    'SIX': 'Six Flags Entertainment Corporation New',

    'LARK': 'Landmark Bancorp Inc.',

    'ANH-A': 'Anworth Mortgage Asset  Corporation',

    'KCG': 'KCG Holdings, Inc.',

    'NEWT': 'Newtek Business Services Corp.',

    'GGT-B': 'Gabelli Multi-Media Trust Inc. (The)',

    'WVFC': 'WVS Financial Corp.',

    'CCM': 'Concord Medical Services Holdings Limited',

    'ADP': 'Automatic Data Processing, Inc.',

    'HIFS': 'Hingham Institution for Savings',

    'RWC': 'RELM Wireless Corporation',

    'KCAP': 'KCAP Financial, Inc.',

    'PEI': 'Pennsylvania Real Estate Investment Trust',

    'RACE': 'Ferrari N.V.',

    'MCQ': 'Medley Capital Corporation',

    'NFX': 'Newfield Exploration Company',

    'ARI': 'Apollo Commercial Real Estate Finance',

    'AAL': 'American Airlines Group, Inc.',

    'SMCI': 'Super Micro Computer, Inc.',

    'SDLP': 'Seadrill Partners LLC',

    'IBB': 'iShares Nasdaq Biotechnology Index Fund',

    'MFCB': 'MFC Bancorp Ltd.',

    'GNC': 'GNC Holdings, Inc.',

    'FTR': 'Frontier Communications Corporation',

    'MA': 'Mastercard Incorporated',

    'TNET': 'TriNet Group, Inc.',

    'DNAI': 'ProNAi Therapeutics, Inc.',

    'SEAS': 'SeaWorld Entertainment, Inc.',

    'BAC-Y': 'Bank of America Corporation',

    'PHK': 'Pimco High Income Fund',

    'ZBH': 'Zimmer Biomet Holdings, Inc.',

    'PBR': 'Petroleo Brasileiro S.A.- Petrobras',

    'MSTX': 'Mast Therapeutics, Inc.',

    'VNQI': 'Vanguard Global ex-U.S. Real Estate ETF',

    'EFII': 'Electronics for Imaging, Inc.',

    'CZR': 'Caesars Entertainment Corporation',

    'EAD': 'Wells Fargo Income Opportunities Fund',

    'GNMK': 'GenMark Diagnostics, Inc.',

    'AV': 'Aviva plc',

    'EYEGW': 'Eyegate Pharmaceuticals, Inc.',

    'HOS': 'Hornbeck Offshore Services',

    'BBF': 'BlackRock Municipal Income Investment Trust',

    'GLOP': 'GasLog Partners LP',

    'CIE': 'Cobalt International Energy, Inc.',

    'CHSCP': 'CHS Inc',

    'TUES': 'Tuesday Morning Corp.',

    'TNP': 'Tsakos Energy Navigation Ltd',

    'SMLR': 'Semler Scientific, Inc.',

    'NVX': 'Nuveen California Dividend Advantage Municipal Fund 2',

    'FLC': 'Flaherty & Crumrine Total Return Fund Inc',

    'AAME': 'Atlantic American Corporation',

    'RGCO': 'RGC Resources Inc.',

    'ABB': 'ABB Ltd',

    'VBTX': 'Veritex Holdings, Inc.',

    'PGH': 'Pengrowth Energy Corporation',

    'ENSG': 'The Ensign Group, Inc.',

    'ONDK': 'On Deck Capital, Inc.',

    'DECK': 'Deckers Outdoor Corporation',

    'JCAP': 'Jernigan Capital, Inc.',

    'OUTR': 'Outerwall Inc.',

    'DX-B': 'Dynex Capital, Inc.',

    'GEB': 'General Electric Company',

    'BST': 'BlackRock Science and Technology Trust',

    'HL': 'Hecla Mining Company',

    'NMK-B': 'Niagara Mohawk Holdings, Inc.',

    'AHS': 'AMN Healthcare Services Inc',

    'ARCC': 'Ares Capital Corporation',

    'UZC': 'United States Cellular Corporation',

    'WAYN': 'Wayne Savings Bancshares Inc.',

    'AWH': 'Allied World Assurance Company Holdings, AG',

    'ENTA': 'Enanta Pharmaceuticals, Inc.',

    'PAAS': 'Pan American Silver Corp.',

    'APPS': 'Digital Turbine, Inc.',

    'NWSA': 'News Corporation',

    'CYS-A': 'CYS Investments, Inc.',

    'DTYS': 'region',

    'PRU': 'Prudential Financial, Inc.',

    'CBPO': 'China Biologic Products, Inc.',

    'GSH': 'Guangshen Railway Company Limited',

    'SPNS': 'Sapiens International Corporation N.V.',

    'CAMT': 'Camtek Ltd.',

    'DGAS': 'Delta Natural Gas Company, Inc.',

    'WTFCM': 'Wintrust Financial Corporation',

    'HOVNP': 'Hovnanian Enterprises Inc',

    'LTRX': 'Lantronix, Inc.',

    'JBR': 'Select Asset Inc.',

    'NI': 'NiSource, Inc',

    'MVC': 'MVC Capital, Inc.',

    'AMSGP': 'Amsurg Corp.',

    'SLP': 'Simulations Plus, Inc.',

    'SRI': 'Stoneridge, Inc.',

    'HH': 'Hooper Holmes, Inc.',

    'AMS': 'American Shared Hospital Services',

    'FNBC': 'First NBC Bank Holding Company',

    'INBK': 'First Internet Bancorp',

    'CDK': 'CDK Global, Inc.',

    'LII': 'Lennox International, Inc.',

    'SRTSU': 'Sensus Healthcare, Inc.',

    'SGYP': 'Synergy Pharmaceuticals, Inc.',

    'C.WS.A': 'Citigroup Inc.',

    'DBVT': 'DBV Technologies S.A.',

    'BOX': 'Box, Inc.',

    'ONS': 'Oncobiologics, Inc.',

    'PYN': 'PIMCO New York Municipal Income Fund III',

    'BBVA': 'Banco Bilbao Viscaya Argentaria S.A.',

    'ASX': 'Advanced Semiconductor Engineering, Inc.',

    'CBD': 'Companhia Brasileira de Distribuicao',

    'GGM': 'Guggenheim Credit Allocation Fund',

    'FLY': 'Fly Leasing Limited',

    'HOT': 'Starwood Hotels & Resorts Worldwide, Inc.',

    'LNTH': 'Lantheus Holdings, Inc.',

    'BPMX': 'BioPharmX Corporation',

    'FTC': 'First Trust Large Cap Growth AlphaDEX Fund',

    'SFL': 'Ship Finance International Limited',

    'PRE-I': 'PartnerRe Ltd.',

    'TMH': 'Team Health Holdings, Inc.',

    'GHM': 'Graham Corporation',

    'UFAB': 'Unique Fabricating, Inc.',

    'AIN': 'Albany International Corporation',

    'KBR': 'KBR, Inc.',

    'ELP': 'Companhia Paranaense de Energia (COPEL)',

    'CIO': 'City Office REIT, Inc.',

    'RAND': 'Rand Capital Corporation',

    'KIM': 'Kimco Realty Corporation',

    'KOSS': 'Koss Corporation',

    'TFSCU': '1347 Capital Corp.',

    'NOK': 'Nokia Corporation',

    'TGB': 'Taseko Mines Limited',

    'CAVM': 'Cavium, Inc.',

    'SID': 'National Steel Company',

    'WES': 'Western Gas Partners, LP',

    'HLI': 'Houlihan Lokey, Inc.',

    'MZF': 'Managed Duration Investment Grade Municipal Fund',

    'NRF-C': 'Northstar Realty Finance Corp.',

    'APB': 'Asia Pacific Fund, Inc. (The)',

    'PQ': 'Petroquest Energy Inc',

    'IID': 'Voya International High Dividend Equity Income Fund',

    'NPM': 'Nuveen Premium Income Municipal Fund II, Inc.',

    'PEB-B': 'Pebblebrook Hotel Trust',

    'IMGN': 'ImmunoGen, Inc.',

    'TOO': 'Teekay Offshore Partners L.P.',

    'CHRW': 'C.H. Robinson Worldwide, Inc.',

    'GSVC': 'GSV Capital Corp',

    'CMCM': 'Cheetah Mobile Inc.',

    'SCHW': 'The Charles Schwab Corporation',

    'AIG': 'American International Group, Inc.',

    'WRK': 'Westrock Company',

    'VNCE': 'Vince Holding Corp.',

    'JNP': 'Juniper Pharmaceuticals, Inc.',

    'PHG': 'Koninklijke Philips N.V.',

    'TAT': 'Transatlantic Petroleum Ltd',

    'STFC': 'State Auto Financial Corporation',

    'USB-H': 'U.S. Bancorp',

    'BH': 'Biglari Holdings Inc.',

    'Y': 'Alleghany Corporation',

    'OMF': 'OneMain Holdings, Inc.',

    'UEC': 'Uranium Energy Corp.',

    'JGH': 'Nuveen Global High Income Fund',

    'NANO': 'Nanometrics Incorporated',

    'TCX': 'Tucows Inc.',

    'UFPI': 'Universal Forest Products, Inc.',

    'QIHU': 'Qihoo 360 Technology Co. Ltd.',

    'DATA': 'Tableau Software, Inc.',

    'ESLT': 'Elbit Systems Ltd.',

    'GAINP': 'Gladstone Investment Corporation',

    'YECO': 'Yulong Eco-Materials Limited',

    'PPBI': 'Pacific Premier Bancorp Inc',

    'MET-A': 'MetLife, Inc.',

    'SALE': 'RetailMeNot, Inc.',

    'ECHO': 'Echo Global Logistics, Inc.',

    'CORT': 'Corcept Therapeutics Incorporated',

    'FFBCW': 'First Financial Bancorp.',

    'XIN': 'Xinyuan Real Estate Co Ltd',

    'GSL-B': 'Global Ship Lease, Inc.',

    'OXLCO': 'Oxford Lane Capital Corp.',

    'ARWAU': 'Arowana Inc.',

    'STWD': 'STARWOOD PROPERTY TRUST, INC.',

    'PBYI': 'Puma Biotechnology Inc',

    'HDRAR': 'Hydra Industries Acquisition Corp.',

    'DW': 'Drew Industries Incorporated',

    'NATR': 'Nature\'s Sunshine Products, Inc.',

    'ICUI': 'ICU Medical, Inc.',

    'BOLT': 'BioLight Life Sciences Ltd.',

    'CHSP': 'Chesapeake Lodging Trust',

    'FTGC': 'First Trust Global Tactical Commodity Strategy Fund',

    'TUTI': 'Tuttle Tactical Management Multi-Strategy Income ETF',

    'UE': 'Urban Edge Properties',

    'AVX': 'AVX Corporation',

    'PPC': 'Pilgrim\'s Pride Corporation',

    'ES': 'Eversource Energy',

    'FSCE': 'Fifth Street Finance Corp.',

    'INCY': 'Incyte Corporation',

    'ATRA': 'Atara Biotherapeutics, Inc.',

    'LMCK': 'Liberty Media Corporation',

    'MCRN': 'Milacron Holdings Corp.',

    'ALG': 'Alamo Group, Inc.',

    'SYNA': 'Synaptics Incorporated',

    'DELTW': 'Delta Technology Holdings Limited',

    'GYRO': 'Gyrodyne , LLC',

    'ITW': 'Illinois Tool Works Inc.',

    'LXP-C': 'Lexington Realty Trust',

    'SSD': 'Simpson Manufacturing Company, Inc.',

    'RAD': 'Rite Aid Corporation',

    'CALI': 'China Auto Logistics Inc.',

    'CRWS': 'Crown Crafts, Inc.',

    'JP': 'Jupai Holdings Limited',

    'BML-J': 'Bank of America Corporation',

    'EWBC': 'East West Bancorp, Inc.',

    'CBZ': 'CBIZ, Inc.',

    'SVU': 'SuperValu Inc.',

    'VPV': 'Invesco Pennsylvania Value Municipal Income Trust',

    'BKD': 'Brookdale Senior Living Inc.',

    'RNWK': 'RealNetworks, Inc.',

    'ECOL': 'US Ecology, Inc.',

    'CDC': 'Victory CEMP US EQ Income Enhanced Volatility Wtd Index ETF',

    'MHY': 'Western Asset Managed High Income Fund, Inc.',

    'RTEC': 'Rudolph Technologies, Inc.',

    'MUSA': 'Murphy USA Inc.',

    'MAGS': 'Magal Security Systems Ltd.',

    'YNDX': 'Yandex N.V.',

    'DUKH': 'Duke Energy Corporation',

    'NVRO': 'Nevro Corp.',

    'OFC-L': 'Corporate Office Properties Trust',

    'MTB-C': 'M&T Bank Corporation',

    'CBAN': 'Colony Bankcorp, Inc.',

    'HCAC': 'Hennessy Capital Acquisition Corp. II',

    'FTRPR': 'Frontier Communications Corporation',

    'LHCG': 'LHC Group',

    'AGTC': 'Applied Genetic Technologies Corporation',

    'GOV': 'Government Properties Income Trust',

    'TYG': 'Tortoise Energy Infrastructure Corporation',

    'M': 'Macy\'s Inc',

    'TGNA': 'TEGNA Inc.',

    'GPX': 'GP Strategies Corporation',

    'ENV': 'Envestnet, Inc',

    'VRSK': 'Verisk Analytics, Inc.',

    'DKT': 'Deutsch Bk Contingent Cap Tr V',

    'WPX': 'WPX Energy, Inc.',

    'FLIR': 'FLIR Systems, Inc.',

    'HQH': 'Tekla Healthcare Investors',

    'IBA': 'Industrias Bachoco, S.A. de C.V.',

    'PMX': 'PIMCO Municipal Income Fund III',

    'NTT': 'Nippon Telegraph and Telephone Corporation',

    'HXL': 'Hexcel Corporation',

    'KIM-J': 'Kimco Realty Corporation',

    'SKX': 'Skechers U.S.A., Inc.',

    'ARH-C': 'Arch Capital Group Ltd.',

    'EPE': 'EP Energy Corporation',

    'DHR$': 'Danaher Corporation',

    'TCK': 'Teck Resources Ltd',

    'STI': 'SunTrust Banks, Inc.',

    'EMITF': 'Elbit Imaging Ltd.',

    'ASML': 'ASML Holding N.V.',

    'BMA': 'Macro Bank Inc.',

    'TIL': 'Till Capital Ltd.',

    'COBZ': 'CoBiz Financial Inc.',

    'DLR-G': 'Digital Realty Trust, Inc.',

    'SLG': 'SL Green Realty Corporation',

    'RL': 'Ralph Lauren Corporation',

    'ALTY': 'Global X SuperDividend Alternatives ETF',

    'DSLV': 'region',

    'ATAI': 'ATA Inc.',

    'QINC': 'First Trust RBA Quality Income ETF',

    'BKMU': 'Bank Mutual Corporation',

    'TV': 'Grupo Televisa S.A.',

    'AGR': 'Avangrid, Inc.',

    'PCG-C': 'Pacific Gas & Electric Co.',

    'RFDI': 'First Trust RiverFront Dynamic Developed International ETF',

    'NAT': 'Nordic American Tankers Limited',

    'DWFI': 'SPDR Dorsey Wright Fixed Income Allocation ETF',

    'EQS': 'Equus Total Return, Inc.',

    'MPWR': 'Monolithic Power Systems, Inc.',

    'DLR-I': 'Digital Realty Trust, Inc.',

    'SENEA': 'Seneca Foods Corp.',

    'SMMT': 'Summit Therapeutics plc',

    'USATP': 'USA Technologies, Inc.',

    'ARDX': 'Ardelyx, Inc.',

    'TM': 'Toyota Motor Corp Ltd Ord',

    'PCOM': 'Points International, Ltd.',

    'RXII': 'RXI Pharmaceuticals Corporation',

    'DSS': 'Document Security Systems, Inc.',

    'FLS': 'Flowserve Corporation',

    'UNT': 'Unit Corporation',

    'BIND': 'BIND Therapeutics, Inc.',

    'MITK': 'Mitek Systems, Inc.',

    'CPB': 'Campbell Soup Company',

    'SAQ': 'Saratoga Investment Corp',

    'HLX': 'Helix Energy Solutions Group, Inc.',

    'KODK.WS.A': 'Eastman Kodak Company',

    'NAME': 'Rightside Group, Ltd.',

    'HCN-I': 'Welltower Inc.',

    'PDM': 'Piedmont Office Realty Trust, Inc.',

    'AHT': 'Ashford Hospitality Trust Inc',

    'AFAM': 'Almost Family Inc',

    'BLK': 'BlackRock, Inc.',

    'NWBI': 'Northwest Bancshares, Inc.',

    'GSL': 'Global Ship Lease, Inc.',

    'SPLP': 'Steel Partners Holdings LP',

    'PPR': 'Voya Prime Rate Trust',

    'FCAP': 'First Capital, Inc.',

    'EWZS': 'iShares MSCI Brazil Small-Cap ETF',

    'GBR': 'New Concept Energy, Inc',

    'HTS': 'Hatteras Financial Corp',

    'SQNM': 'Sequenom, Inc.',

    'SUNW': 'Sunworks, Inc.',

    'ITCB': 'Ita? CorpBanca',

    'ULTR': 'Ultrapetrol (Bahamas) Limited',

    'FRA': 'Blackrock Floating Rate Income Strategies Fund Inc',

    'CSPI': 'CSP Inc.',

    'GDL': 'The GDL Fund',

    'TSC': 'TriState Capital Holdings, Inc.',

    'KFI': 'KKR Financial Holdings LLC',

    'MOSY': 'MoSys, Inc.',

    'MDXG': 'MiMedx Group, Inc',

    'VNDA': 'Vanda Pharmaceuticals Inc.',

    'VBFC': 'Village Bank and Trust Financial Corp.',

    'HTBX': 'Heat Biologics, Inc.',

    'IIIN': 'Insteel Industries, Inc.',

    'MIW': 'Eaton Vance Michigan Municipal Bond Fund',

    'ESNC': 'EnSync, Inc.',

    'COSI': 'Cosi, Inc.',

    'KALU': 'Kaiser Aluminum Corporation',

    'XNET': 'Xunlei Limited',

    'DYSL': 'Dynasil Corporation of America',

    'GBLI': 'Global Indemnity plc',

    'HBM': 'HudBay Minerals Inc',

    'COWN': 'Cowen Group, Inc.',

    'NNA': 'Navios Maritime Acquisition Corporation',

    'IMNP          ': 'Immune Pharmaceuticals Inc.',

    'NEE-I': 'NextEra Energy, Inc.',

    'VTTI': 'VTTI Energy Partners LP',

    'MYD': 'Blackrock MuniYield Fund, Inc.',

    'SPE': 'Special Opportunities Fund Inc.',

    'SABR': 'Sabre Corporation',

    'CWEI': 'Clayton Williams Energy, Inc.',

    'IIF': 'Morgan Stanley India Investment Fund, Inc.',

    'LEA': 'Lear Corporation',

    'KZ': 'KongZhong Corporation',

    'ZAIS': 'ZAIS Group Holdings, Inc.',

    'REX': 'REX American Resources Corporation',

    'BANR': 'Banner Corporation',

    'JTA': 'Nuveen Tax-Advantaged Total Return Strategy Fund',

    'EIP': 'Eaton Vance Pennsylvania Municipal Bond Fund',

    'ITT': 'ITT Inc.',

    'IOSP': 'Innospec Inc.',

    'RCL': 'Royal Caribbean Cruises Ltd.',

    'WOR': 'Worthington Industries, Inc.',

    'PACEU': 'Pace Holdings Corp.',

    'ARWA': 'Arowana Inc.',

    'UEIC': 'Universal Electronics Inc.',

    'NORT': 'Nordic Realty Trust, Inc.',

    'KFH': 'KKR Financial Holdings LLC',

    'HRG': 'HRG Group, Inc.',

    'NUROW': 'NeuroMetrix, Inc.',

    'BCBP': 'BCB Bancorp, Inc. (NJ)',

    'TFG': 'Goldman Sachs Group, Inc. (The)',

    'DXKW': 'WisdomTree Korea Hedged Equity Fund',

    'DSKY': 'iDreamSky Technology Limited',

    'ABMD': 'ABIOMED, Inc.',

    'MPET': 'Magellan Petroleum Corporation',

    'NTIP': 'Network-1 Technologies, Inc.',

    'PY': 'Principal Shareholder Yield Index ETF',

    'ARL': 'American Realty Investors, Inc.',

    'FTSM': 'First Trust Enhanced Short Maturity ETF',

    'SWFT': 'Swift Transportation Company',

    'SYN': 'Synthetic Biologics, Inc',

    'BNS': 'Bank of Nova Scotia (The)',

    'NMK-C': 'Niagara Mohawk Holdings, Inc.',

    'IDT': 'IDT Corporation',

    'NXST': 'Nexstar Broadcasting Group, Inc.',

    'TER': 'Teradyne, Inc.',

    'SPXC': 'SPX Corporation',

    'JASO': 'JA Solar Holdings, Co., Ltd.',

    'KB': 'KB Financial Group Inc',

    'OKS': 'ONEOK Partners, L.P.',

    'CERCZ': 'Cerecor Inc.',

    'SCCO': 'Southern Copper Corporation',

    'MIII': 'M III Acquisition Corp.',

    'NOVT': 'Novanta Inc.',

    'IPG': 'Interpublic Group of Companies, Inc. (The)',

    'ABEOW': 'Abeona Therapeutics Inc.',

    'TDF': 'Templeton Dragon Fund, Inc.',

    'ZIXI': 'Zix Corporation',

    'DIOD': 'Diodes Incorporated',

    'KN': 'Knowles Corporation',

    'TMUSP': 'T-Mobile US, Inc.',

    'RWT': 'Redwood Trust, Inc.',

    'AIC': 'Arlington Asset Investment Corp',

    'PVTBP': 'PrivateBancorp, Inc.',

    'IRL': 'New Ireland Fund, Inc. (The)',

    'SBCP': 'Sunshine Bancorp, Inc.',

    'HFWA': 'Heritage Financial Corporation',

    'BF.A': 'Brown Forman Corporation',

    'FB': 'Facebook, Inc.',

    'CONE': 'CyrusOne Inc',

    'FUNC': 'First United Corporation',

    'SNP': 'China Petroleum & Chemical Corporation',

    'FHK': 'First Trust Hong Kong AlphaDEX Fund',

    'SVT': 'Servotronics, Inc.',

    'NDP': 'Tortoise Energy Independence Fund, Inc.',

    'AVIR': 'Aviragen Therapeutics, Inc.',

    'EGBN': 'Eagle Bancorp, Inc.',

    'WLB': 'Westmoreland Coal Company',

    'AXU': 'Alexco Resource Corp',

    'NCIT': 'NCI, Inc.',

    'TRST': 'TrustCo Bank Corp NY',

    'SYNC': 'Synacor, Inc.',

    'REG-F': 'Regency Centers Corporation',

    'FBIO': 'Fortress Biotech, Inc.',

    'VRML': 'Vermillion, Inc.',

    'IDSY': 'I.D. Systems, Inc.',

    'KIM-I': 'Kimco Realty Corporation',

    'EFOI': 'Energy Focus, Inc.',

    'GG': 'Goldcorp Inc.',

    'GGT': 'Gabelli Multi-Media Trust Inc. (The)',

    'FELE': 'Franklin Electric Co., Inc.',

    'NGG': 'National Grid Transco, PLC',

    'CLNY-A': 'Colony Capital, Inc',

    'SAR': 'Saratoga Investment Corp',

    'AMRB': 'American River Bankshares',

    'VSLR': 'Vivint Solar, Inc.',

    'ATW': 'Atwood Oceanics, Inc.',

    'IBM': 'International Business Machines Corporation',

    'BGC': 'General Cable Corporation',

    'MIXT': 'MiX Telematics Limited',

    'DSGX': 'The Descartes Systems Group Inc.',

    'CPT': 'Camden Property Trust',

    'WMC': 'Western Asset Mortgage Capital Corporation',

    'EGO': 'Eldorado Gold Corporation',

    'LTRPA': 'Liberty TripAdvisor Holdings, Inc.',

    'SCL': 'Stepan Company',

    'GMTA': 'GATX Corporation',

    'CATB': 'Catabasis Pharmaceuticals, Inc.',

    'PWR': 'Quanta Services, Inc.',

    'ADRA': 'BLDRS Asia 50 ADR Index Fund',

    'PKD': 'Parker Drilling Company',

    'CPHD': 'CEPHEID',

    'AVV': 'Aviva plc',

    'ALJJ': 'ALJ Regional Holdings, Inc.',

    'ANAC': 'Anacor Pharmaceuticals, Inc.',

    'EVN': 'Eaton Vance Municipal Income Trust',

    'FMNB': 'Farmers National Banc Corp.',

    'MCV': 'Medley Capital Corporation',

    'ARR': 'ARMOUR Residential REIT, Inc.',

    'TKC': 'Turkcell Iletisim Hizmetleri AS',

    'CP': 'Canadian Pacific Railway Limited',

    'K': 'Kellogg Company',

    'CDI': 'CDI Corporation',

    'SUP': 'Superior Industries International, Inc.',

    'TICC': 'TICC Capital Corp.',

    'BAC': 'Bank of America Corporation',

    'CTRP': 'Ctrip.com International, Ltd.',

    'DGSE': 'DGSE Companies, Inc.',

    'ERH': 'Wells Fargo Utilities and High Income Fund',

    'NUTR': 'Nutraceutical International Corporation',

    'ADBE': 'Adobe Systems Incorporated',

    'HEQ': 'John Hancock Hedged Equity & Income Fund',

    'CVCO': 'Cavco Industries, Inc.',

    'TOUR': 'Tuniu Corporation',

    'ALLY': 'Ally Financial Inc.',

    'MIDD': 'The Middleby Corporation',

    'CTRL': 'Control4 Corporation',

    'DXB': 'Deutsche Bank AG',

    'ACNB': 'ACNB Corporation',

    'MHK': 'Mohawk Industries, Inc.',

    'ARU': 'Ares Capital Corporation',

    'ASPS': 'Altisource Portfolio Solutions S.A.',

    'FEM': 'First Trust Emerging Markets AlphaDEX Fund',

    'AVB': 'AvalonBay Communities, Inc.',

    'EPAY': 'Bottomline Technologies, Inc.',

    'EMCG': 'WisdomTree Emerging Markets Consumer Growth Fund',

    'ETY': 'Eaton Vance Tax-Managed Diversified Equity Income Fund',

    'BKE': 'Buckle, Inc. (The)',

    'SMM': 'Salient Midstream & MLP Fund',

    'EXAS': 'EXACT Sciences Corporation',

    'SKYW': 'SkyWest, Inc.',

    'RIBTW': 'RiceBran Technologies',

    'COF-F': 'Capital One Financial Corporation',

    'AHT-E': 'Ashford Hospitality Trust Inc',

    'CSFL': 'CenterState Banks, Inc.',

    'NOC': 'Northrop Grumman Corporation',

    'TGLS': 'Tecnoglass Inc.',

    'JCP': 'J.C. Penney Company, Inc. Holding Company',

    'HUSA': 'Houston American Energy Corporation',

    'AOS': 'Smith (A.O.) Corporation',

    'GOODO': 'Gladstone Commercial Corporation',

    'MGLN': 'Magellan Health, Inc.',

    'MPW': 'Medical Properties Trust, Inc.',

    'WSO.B': 'Watsco, Inc.',

    'ADRO': 'Aduro Biotech, Inc.',

    'FPF': 'First Trust Intermediate Duration Preferred & Income Fund',

    'FTW': 'First Trust Taiwan AlphaDEX Fund',

    'RNST': 'Renasant Corporation',

    'INVN': 'InvenSense, Inc.',

    'HT': 'Hersha Hospitality Trust',

    'BEAT': 'BioTelemetry, Inc.',

    'RJD': 'Raymond James Financial, Inc.',

    'VVUS': 'VIVUS, Inc.',

    'UVSP': 'Univest Corporation of Pennsylvania',

    'EBS': 'Emergent Biosolutions, Inc.',

    'TNXP': 'Tonix Pharmaceuticals Holding Corp.',

    'LCAHU': 'Landcadia Holdings, Inc.',

    'WFC-N': 'Wells Fargo & Company',

    'NPTN': 'NeoPhotonics Corporation',

    'ONVO': 'Organovo Holdings, Inc.',

    'NYLD': 'NRG Yield, Inc.',

    'MMAC': 'MMA Capital Management, LLC',

    'OPHT': 'Ophthotech Corporation',

    'EVM': 'Eaton Vance California Municipal Bond Fund',

    'TCBIW': 'Texas Capital Bancshares, Inc.',

    'NPO': 'Enpro Industries',

    'EEI': 'Ecology and Environment, Inc.',

    'SPI': 'SPI Energy Co., Ltd.',

    'XBKS': 'Xenith Bankshares, Inc.',

    'MSF': 'Morgan Stanley Emerging Markets Fund, Inc.',

    'WNC': 'Wabash National Corporation',

    'FCAU': 'Fiat Chrysler Automobiles N.V.',

    'AKER': 'Akers Biosciences Inc',

    'LBRDK': 'Liberty Broadband Corporation',

    'IPL-D': 'Interstate Power and Light Company',

    'EMCI': 'EMC Insurance Group Inc.',

    'HOFT': 'Hooker Furniture Corporation',

    'TWN': 'Taiwan Fund, Inc. (The)',

    'IQNT': 'Inteliquent, Inc.',

    'VWOB': 'Vanguard Emerging Markets Government Bond ETF',

    'LOCK': 'LifeLock, Inc.',

    'FOX': 'Twenty-First Century Fox, Inc.',

    'LDF': 'Latin American Discovery Fund, Inc. (The)',

    'RTK': 'Rentech, Inc.',

    'ALSK': 'Alaska Communications Systems Group, Inc.',

    'RSAS': 'RESAAS Services Inc.',

    'AMIC': 'American Independence Corp.',

    'BG': 'Bunge Limited',

    'GIL': 'Gildan Activewear, Inc.',

    'RMTI': 'Rockwell Medical, Inc.',

    'CIG.C': 'Comp En De Mn Cemig ADS',

    'SRET': 'Global X SuperDividend REIT ETF',

    'NKA': 'Niska Gas Storage Partners LLC',

    'PXD': 'Pioneer Natural Resources Company',

    'RLYP': 'Relypsa, Inc.',

    'STRZB': 'Starz',

    'WILN': 'Wi-Lan Inc',

    'YRCW': 'YRC Worldwide, Inc.',

    'III': 'Information Services Group, Inc.',

    'PSCM': 'PowerShares S&P SmallCap Materials Portfolio',

    'LLNW': 'Limelight Networks, Inc.',

    'KBH': 'KB Home',

    'ICFI': 'ICF International, Inc.',

    'BOOT': 'Boot Barn Holdings, Inc.',

    'UNP': 'Union Pacific Corporation',

    'GST-A': 'Gastar Exploration Inc.',

    'MN': 'Manning & Napier, Inc.',

    'HDNG': 'Hardinge, Inc.',

    'GMZ': 'Goldman Sachs MLP Income Opportunities Fund',

    'KKD': 'Krispy Kreme Doughnuts, Inc.',

    'WPC': 'W.P. Carey Inc.',

    'PSA-U': 'Public Storage',

    'SMBC': 'Southern Missouri Bancorp, Inc.',

    'SCE-C': 'Southern California Edison Company',

    'GPS': 'Gap, Inc. (The)',

    'CBL-D': 'CBL & Associates Properties, Inc.',

    'LMFAW': 'LM Funding America, Inc.',

    'HPE': 'Hewlett Packard Enterprise Company',

    'ICE': 'Intercontinental Exchange Inc.',

    'BEBE': 'bebe stores, inc.',

    'GNE': 'Genie Energy Ltd.',

    'VKQ': 'Invesco Municipal Trust',

    'EMKR': 'EMCORE Corporation',

    'MATR': 'Mattersight Corporation',

    'CASC': 'Cascadian Therapeutics, Inc.',

    'SRAQU': 'Silver Run Acquisition Corporation',

    'SAUC': 'Diversified Restaurant Holdings, Inc.',

    'FCT': 'First Trust Senior Floating Rate Income Fund II',

    'SRNE': 'Sorrento Therapeutics, Inc.',

    'STRP': 'Straight Path Communications Inc.',

    'CPGX': 'Columbia Pipeline Group, Inc.',

    'TBRA': 'Tobira Therapeutics, Inc.',

    'GPT-A': 'Gramercy Property Trust Inc.',

    'S': 'Sprint Corporation',

    'AVNU': 'Avenue Financial Holdings, Inc.',

    'KMDA': 'Kamada Ltd.',

    'AHH': 'Armada Hoffler Properties, Inc.',

    'VCLT': 'Vanguard Long-Term Corporate Bond ETF',

    'ASGN': 'On Assignment, Inc.',

    'TD': 'Toronto Dominion Bank (The)',

    'RNR': 'RenaissanceRe Holdings Ltd.',

    'CEA': 'China Eastern Airlines Corporation Ltd.',

    'CIZ': 'Victory CEMP Developed Enhanced Volatility Wtd Index ETF',

    'NYMTO': 'New York Mortgage Trust, Inc.',

    'PLAB': 'Photronics, Inc.',

    'FMSA': 'Fairmount Santrol Holdings Inc.',

    'FTLB': 'First Trust Low Beta Income ETF',

    'INTL': 'INTL FCStone Inc.',

    'DYNT': 'Dynatronics Corporation',

    'GGB': 'Gerdau S.A.',

    'ALE': 'Allete, Inc.',

    'BHLB': 'Berkshire Hills Bancorp, Inc.',

    'FBZ': 'First Trust Brazil AlphaDEX Fund',

    'AGFSW': 'AgroFresh Solutions, Inc.',

    'LYV': 'Live Nation Entertainment, Inc.',

    'OREX': 'Orexigen Therapeutics, Inc.',

    'CUBE': 'CubeSmart',

    'RFI': 'Cohen & Steers Total Return Realty Fund, Inc.',

    'HCM': 'Hutchison China MediTech Limited',

    'XRAY': 'DENTSPLY SIRONA Inc.',

    'QTM': 'Quantum Corporation',

    'MCHI': 'iShares MSCI China ETF',

    'ONB': 'Old National Bancorp',

    'HOG': 'Harley-Davidson, Inc.',

    'QADA': 'QAD Inc.',

    'DHXM': 'DHX Media Ltd.',

    'WG': 'Willbros Group, Inc.',

    'AFMD': 'Affimed N.V.',

    'GCV': 'Gabelli Convertible and Income Securities Fund, Inc. (The)',

    'IPHS': 'Innophos Holdings, Inc.',

    'CRESY': 'Cresud S.A.C.I.F. y A.',

    'DAKT': 'Daktronics, Inc.',

    'EXC': 'Exelon Corporation',

    'CYCCP': 'Cyclacel Pharmaceuticals, Inc.',

    'W': 'Wayfair Inc.',

    'BCS-A': 'Barclays PLC',

    'SYRX': 'Sysorex Global',

    'MHNC': 'Maiden Holdings, Ltd.',

    'CUDA': 'Barracuda Networks, Inc.',

    'ADMA': 'ADMA Biologics Inc',

    'LOAN': 'Manhattan Bridge Capital, Inc',

    'SBNB': 'Scorpio Tankers Inc.',

    'ATRI': 'ATRION Corporation',

    'TROX': 'Tronox Limited',

    'DCI': 'Donaldson Company, Inc.',

    'ANTH': 'Anthera Pharmaceuticals, Inc.',

    'AEGN': 'Aegion Corp',

    'FFIN': 'First Financial Bankshares, Inc.',

    'CASI': 'CASI Pharmaceuticals, Inc.',

    'CPST': 'Capstone Turbine Corporation',

    'DNR': 'Denbury Resources Inc.',

    'GRF': 'Eagle Capital Growth Fund, Inc.',

    'GRIF': 'Griffin Industrial Realty, Inc.',

    'KFY': 'Korn/Ferry International',

    'CBR': 'Ciber, Inc.',

    'FMY': 'First Trust',

    'ROLL': 'RBC Bearings Incorporated',

    'IMAX': 'Imax Corporation',

    'BZM': 'BlackRock Maryland Municipal Bond Trust',

    'PATI': 'Patriot Transportation Holding, Inc.',

    'OUT': 'OUTFRONT Media Inc.',

    'AWP': 'Alpine Global Premier Properties Fund',

    'CLR': 'Continental Resources, Inc.',

    'UBNK': 'United Financial Bancorp, Inc.',

    'PATK': 'Patrick Industries, Inc.',

    'RDS.A': 'Royal Dutch Shell PLC',

    'GSOL': 'Global Sources Ltd.',

    'MXL': 'MaxLinear, Inc',

    'BDSI': 'BioDelivery Sciences International, Inc.',

    'NSH': 'Nustar GP Holdings, LLC',

    'WBS': 'Webster Financial Corporation',

    'CTRN': 'Citi Trends, Inc.',

    'HTGY': 'Hercules Capital, Inc.',

    'BFIN': 'BankFinancial Corporation',

    'BKK': 'Blackrock Municipal 2020 Term Trust',

    'VALE.P': 'VALE S.A.',

    'ATO': 'Atmos Energy Corporation',

    'ICL': 'Israel Chemicals Shs',

    'HRT': 'Arrhythmia Research Technology Inc.',

    'TSRI': 'TSR, Inc.',

    'CLDT': 'Chatham Lodging Trust (REIT)',

    'DWSN': 'Dawson Geophysical Company',

    'DEST': 'Destination Maternity Corporation',

    'KEG': 'Key Energy Services, Inc.',

    'BIDU': 'Baidu, Inc.',

    'CTF': 'Nuveen Long/Short Commodity Total Return Fund',

    'IBCP': 'Independent Bank Corporation',

    'BLMN': 'Bloomin\' Brands, Inc.',

    'CUNB': 'CU Bancorp (CA)',

    'TA': 'TravelCenters of America LLC',

    'FORR': 'Forrester Research, Inc.',

    'AVD': 'American Vanguard Corporation',

    'CRAY': 'Cray Inc',

    'CAKE': 'The Cheesecake Factory Incorporated',

    'ATLC': 'Atlanticus Holdings Corporation',

    'NLY': 'Annaly Capital Management Inc',

    'WRE': 'Washington Real Estate Investment Trust',

    'ECCZ': 'Eagle Point Credit Company Inc.',

    'CVC': 'Cablevision Systems Corporation',

    'PNY': 'Piedmont Natural Gas Company, Inc.',

    'FTEK': 'Fuel Tech, Inc.',

    'VRTS': 'Virtus Investment Partners, Inc.',

    'CMI': 'Cummins Inc.',

    'CHK': 'Chesapeake Energy Corporation',

    'STAY': 'Extended Stay America, Inc.',

    'FENG': 'Phoenix New Media Limited',

    'FFIV': 'F5 Networks, Inc.',

    'TCBIL': 'Texas Capital Bancshares, Inc.',

    'FI': 'Frank\'s International N.V.',

    'AFST': 'AmTrust Financial Services, Inc.',

    'YGE': 'Yingli Green Energy Holding Company Limited',

    'STE': 'STERIS plc',

    'AXP': 'American Express Company',

    'THS': 'Treehouse Foods, Inc.',

    'COL': 'Rockwell Collins, Inc.',

    'CUZ': 'Cousins Properties Incorporated',

    'QPACW': 'Quinpario Acquisition Corp. 2',

    'SAN-A': 'Banco Santander, S.A.',

    'KMX': 'CarMax Inc',

    'GOOG': 'Alphabet Inc.',

    'NBB': 'Nuveen Build America Bond Fund',

    'DRIOW': 'LabStyle Innovations Corp.',

    'NAO': 'Nordic American Offshore Ltd',

    'AMBA': 'Ambarella, Inc.',

    'RPT-D': 'Ramco-Gershenson Properties Trust',

    'PL-E': 'Protective Life Corporation',

    'IBKCP': 'IBERIABANK Corporation',

    'WCN': 'Waste Connections, Inc.',

    'MZA': 'MuniYield Arizona Fund, Inc.',

    'SNCR': 'Synchronoss Technologies, Inc.',

    'PVCT.WS': 'Provectus Biopharmaceuticals, Inc.',

    'CCJ': 'Cameco Corporation',

    'CNO': 'CNO Financial Group, Inc.',

    'IBKCO': 'IBERIABANK Corporation',

    'GOGL': 'Golden Ocean Group Limited',

    'DFS-B': 'Discover Financial Services',

    'FBP': 'First BanCorp.',

    'CELG': 'Celgene Corporation',

    'GRP.U': 'Granite Real Estate Inc.',

    'EVGBC': 'Eaton Vance NextShares Trust',

    'OCLR': 'Oclaro, Inc.',

    'SRAQW': 'Silver Run Acquisition Corporation',

    'PCRX': 'Pacira Pharmaceuticals, Inc.',

    'JHA': 'Nuveen High Income 2020 Target Term Fund',

    'ZION': 'Zions Bancorporation',

    'GLADO': 'Gladstone Capital Corporation',

    'AKRX': 'Akorn, Inc.',

    'BLL': 'Ball Corporation',

    'UZB': 'United States Cellular Corporation',

    'AMBR': 'Amber Road, Inc.',

    'DNN': 'Denison Mine Corp',

    'NGL': 'NGL ENERGY PARTNERS LP',

    'DNB': 'Dun & Bradstreet Corporation (The)',

    'MYOK': 'MyoKardia, Inc.',

    'PGZ': 'Principal Real Estate Income Fund',

    'XCRA': 'Xcerra Corporation',

    'CLB': 'Core Laboratories N.V.',

    'TGTX': 'TG Therapeutics, Inc.',

    'ANDAU': 'Andina Acquisition Corp. II',

    'PKE': 'Park Electrochemical Corporation',

    'SYK': 'Stryker Corporation',

    'VKTXW': 'Viking Therapeutics, Inc.',

    'WMK': 'Weis Markets, Inc.',

    'PCM': 'PIMCO Commercial Mortgage Securities Trust, Inc.',

    'NDRO': 'Enduro Royalty Trust',

    'MQT': 'Blackrock MuniYield Quality Fund II, Inc.',

    'KTH': 'Lehman ABS Corporation',

    'HTY': 'John Hancock Tax-Advantaged Global Shareholder Yield Fund',

    'PBI': 'Pitney Bowes Inc.',

    'BCC': 'Boise Cascade, L.L.C.',

    'DDF': 'Delaware Investments Dividend & Income Fund, Inc.',

    'WIBC': 'Wilshire Bancorp, Inc.',

    'PHI': 'Philippine Long Distance Telephone Company',

    'AOD': 'Alpine Total Dynamic Dividend Fund',

    'EDGW': 'Edgewater Technology, Inc.',

    'EMI': 'Eaton Vance Michigan Municipal Income Trust',

    'TBI': 'TrueBlue, Inc.',

    'MUH': 'Blackrock MuniHoldings Fund II, Inc.',

    'GKOS': 'Glaukos Corporation',

    'SGOC': 'SGOCO Group, Ltd',

    'NUO': 'Nuveen Ohio Quality Income Municipal Fund',

    'NKX': 'Nuveen California AMT-Free Municipal Income Fund',

    'RELY': 'Real Industry, Inc. ',

    'BTX.WS': 'BioTime, Inc.',

    'IND': 'ING Group, N.V.',

    'CWT': 'California Water  Service Group Holding',

    'MU': 'Micron Technology, Inc.',

    'CADTR': 'DT Asia Investments Limited',

    'FPI': 'Farmland Partners Inc.',

    'PLCM': 'Polycom, Inc.',

    'TLRD': 'Tailored Brands, Inc.',

    'CHFN': 'Charter Financial Corp.',

    'ANGO': 'AngioDynamics, Inc.',

    'SHO-E': 'Sunstone Hotel Investors, Inc.',

    'SB-C': 'Safe Bulkers, Inc',

    'LLL': 'L-3 Communications Holdings, Inc.',

    'OB': 'OneBeacon Insurance Group, Ltd.',

    'QPACU': 'Quinpario Acquisition Corp. 2',

    'SBFGP': 'SB Financial Group, Inc.',

    'NXQ': 'Nuveen Select Tax Free Income Portfolio II',

    'PPHMP': 'Peregrine Pharmaceuticals Inc.',

    'SGMA': 'SigmaTron International, Inc.',

    'WIA': 'Western Asset/Claymore U.S. Treasury Inflation Prot Secs Fd',

    'ONSIW': 'Oncobiologics, Inc.',

    'POPE': 'Pope Resources',

    'FYT': 'First Trust Small Cap Value AlphaDEX Fund',

    'JEC': 'Jacobs Engineering Group Inc.',

    'FTA': 'First Trust Large Cap Value AlphaDEX Fund',

    'MOV': 'Movado Group Inc.',

    'HCAPL': 'Harvest Capital Credit Corporation',

    'PROV': 'Provident Financial Holdings, Inc.',

    'VC': 'Visteon Corporation',

    'ARWR': 'Arrowhead Pharmaceuticals, Inc.',

    'MH-A': 'Maiden Holdings, Ltd.',

    'JHI': 'John Hancock Investors Trust',

    'BDC': 'Belden Inc',

    'NYV': 'Nuveen New York Municipal Value Fund 2',

    'CH': 'Aberdeen Chile Fund, Inc.',

    'SYF': 'Synchrony Financial',

    'ENX': 'Eaton Vance New York Municipal Bond Fund',

    'HMNY': 'Helios and Matheson Analytics Inc',

    'WMT': 'Wal-Mart Stores, Inc.',

    'LMT': 'Lockheed Martin Corporation',

    'MMSI': 'Merit Medical Systems, Inc.',

    'PSO': 'Pearson, Plc',

    'APO': 'Apollo Global Management, LLC',

    'JMF': 'Nuveen Energy MLP Total Return Fund',

    'PACW': 'PacWest Bancorp',

    'LPI': 'Laredo Petroleum, Inc.',

    'CHMG': 'Chemung Financial Corp',

    'WFC-T': 'Wells Fargo & Company',

    'JSYNR': 'Jensyn Acquistion Corp.',

    'AFSS': 'AmTrust Financial Services, Inc.',

    'OSIS': 'OSI Systems, Inc.',

    'IRDMB': 'Iridium Communications Inc',

    'DRIO': 'LabStyle Innovations Corp.',

    'TGH': 'Textainer Group Holdings Limited',

    'CKX': 'CKX Lands, Inc.',

    'RIC': 'Richmont Mines, Inc.',

    'OCIP': 'OCI Partners LP',

    'PYT': 'PPlus Trust',

    'RLOG': 'Rand Logistics, Inc.',

    'NERV': 'Minerva Neurosciences, Inc',

    'RESI': 'Altisource Residential Corporation',

    'GEK': 'General Electric Capital Corporation',

    'POWL': 'Powell Industries, Inc.',

    'DCUB': 'Dominion Resources, Inc.',

    'JQC': 'Nuveen Credit Strategies Income Fund',

    'LOB': 'Live Oak Bancshares, Inc.',

    'CNR': 'China Metro-Rural Holdings Limited',

    'WLFC': 'Willis Lease Finance Corporation',

    'JSD': 'Nuveen Short Duration Credit Opportunities Fund',

    'MSTR': 'MicroStrategy Incorporated',

    'HUN': 'Huntsman Corporation',

    'DFT-C': 'Dupont Fabros Technology, Inc.',

    'HES-A': 'Hess Corporation',

    'USAT': 'USA Technologies, Inc.',

    'BCS-': 'Barclays PLC',

    'AMTG': 'Apollo Residential Mortgage, Inc.',

    'DVAX': 'Dynavax Technologies Corporation',

    'TRNS': 'Transcat, Inc.',

    'MPG': 'Metaldyne Performance Group Inc.',

    'PRGO': 'Perrigo Company',

    'CFCB': 'Centrue Financial Corporation',

    'AR': 'Antero Resources Corporation',

    'NHA': 'Nuveen Municipal 2021 Target Term Fund',

    'CRDC': 'Cardica, Inc.',

    'TEI': 'Templeton Emerging Markets Income Fund, Inc.',

    'CHL': 'China Mobile (Hong Kong) Ltd.',

    'NGHC': 'National General Holdings Corp',

    'BBT-E': 'BB&T Corporation',

    'GPOR': 'Gulfport Energy Corporation',

    'QLTI': 'QLT Inc.',

    'STT': 'State Street Corporation',

    'DRA': 'Diversified Real Asset Income Fund',

    'GALTU': 'Galectin Therapeutics Inc.',

    'NCV': 'AllianzGI Convertible & Income Fund',

    'AHL-A': 'Aspen Insurance Holdings Limited',

    'NVG': 'Nuveen Dividend Advantage Municipal Income Fund',

    'MGP': 'MGM Growth Properties LLC',

    'EGRX': 'Eagle Pharmaceuticals, Inc.',

    'GSM': 'Ferroglobe PLC',

    'PESI': 'Perma-Fix Environmental Services, Inc.',

    'MCHX': 'Marchex, Inc.',

    'GS': 'Goldman Sachs Group, Inc. (The)',

    'KNOP': 'KNOT Offshore Partners LP',

    'IXUS': 'iShares Core MSCI Total International Stock ETF',

    'ELS': 'Equity Lifestyle Properties, Inc.',

    'BBOX': 'Black Box Corporation',

    'WTM': 'White Mountains Insurance Group, Ltd.',

    'TG': 'Tredegar Corporation',

    'AVAL': 'Grupo Aval Acciones y Valores S.A.',

    'GGAL': 'Grupo Financiero Galicia S.A.',

    'AHP': 'Ashford Hospitality Prime, Inc.',

    'UL': 'Unilever PLC',

    'RUBI': 'The Rubicon Project, Inc.',

    'GLV': 'Clough Global Allocation Fund',

    'AYI': 'Acuity Brands Inc',

    'KEX': 'Kirby Corporation',

    'BAC-D': 'Bank of America Corporation',

    'AXAS': 'Abraxas Petroleum Corporation',

    'CBX': 'CBX (Listing Market NYSE Networks AE',

    'AAC': 'AAC Holdings, Inc.',

    'ANSS': 'ANSYS, Inc.',

    'GEO': 'Geo Group Inc (The)',

    'CMO-E': 'Capstead Mortgage Corporation',

    'MHF': 'Western Asset Municipal High Income Fund, Inc.',

    'HIX': 'Western Asset High Income Fund II Inc.',

    'MANH': 'Manhattan Associates, Inc.',

    'PAACR': 'Pacific Special Acquisition Corp.',

    'KTP': 'Lehman ABS Corporation',

    'HGSH': 'China HGS Real Estate, Inc.',

    'LCI': 'Lannett Co Inc',

    'FSZ': 'First Trust Switzerland AlphaDEX Fund',

    'TEX': 'Terex Corporation',

    'RM': 'Regional Management Corp.',

    'FLOW': 'SPX FLOW, Inc.',

    'VIV': 'Telefonica Brasil S.A.',

    'FSD': 'First Trust High Income Long Short Fund',

    'KAMN': 'Kaman Corporation',

    'FNK': 'First Trust Mid Cap Value AlphaDEX Fund',

    'AFB': 'Alliance National Municipal Income Fund Inc',

    'IHS': 'IHS Inc.',

    'LMNR': 'Limoneira Co',

    'GHL': 'Greenhill & Co., Inc.',

    'TCBK': 'TriCo Bancshares',

    'THLD': 'Threshold Pharmaceuticals, Inc.',

    'RSO-C': 'Resource Capital Corp.',

    'EVOL': 'Evolving Systems, Inc.',

    'SGZA': 'Selective Insurance Group, Inc.',

    'IFN': 'India Fund, Inc. (The)',

    'PULM': 'Pulmatrix, Inc.',

    'JGBB': 'WisdomTree Japan Interest Rate Strategy Fund',

    'LIVE': 'Live Ventures Incorporated',

    'ATR': 'AptarGroup, Inc.',

    'C-P': 'Citigroup Inc.',

    'ACH': 'Aluminum Corporation of China Limited',

    'NVGN': 'Novogen Limited',

    'IT': 'Gartner, Inc.',

    'MMP': 'Magellan Midstream Partners L.P.',

    'DGLD': 'region',

    'MDC': 'M.D.C. Holdings, Inc.',

    'CTRV': 'ContraVir Pharmaceuticals Inc',

    'AIB': 'Apollo Investment Corporation',

    'NCQ': 'NovaCopper Inc.',

    'BVX': 'Bovie Medical Corporation',

    'RTIX': 'RTI Surgical, Inc.',

    'CLACU': 'Capitol Acquisition Corp. III',

    'ACUR': 'Acura Pharmaceuticals, Inc.',

    'PUK-': 'Prudential Public Limited Company',

    'APDNW': 'Applied DNA Sciences Inc',

    'RTTR': 'Ritter Pharmaceuticals, Inc.',

    'OPHC': 'OptimumBank Holdings, Inc.',

    'IESC': 'IES Holdings, Inc.',

    'OAS': 'Oasis Petroleum Inc.',

    'OSBCP': 'Old Second Bancorp, Inc.',

    'EGL': 'Engility Holdings, Inc.',

    'MWG': 'Morgan Stanley',

    'ANH-B': 'Anworth Mortgage Asset  Corporation',

    'RUSHB': 'Rush Enterprises, Inc.',

    'CMS-B': 'CMS Energy Corporation',

    'VRA': 'Vera Bradley, Inc.',

    'WB': 'Weibo Corporation',

    'BANC-D': 'Banc of California, Inc.',

    'CHCO': 'City Holding Company',

    'MOCO': 'MOCON, Inc.',

    'BXMT': 'Capital Trust, Inc.',

    'SHBI': 'Shore Bancshares Inc',

    'STAG-A': 'Stag Industrial, Inc.',

    'ADVM': 'Adverum Biotechnologies, Inc.',

    'DDR-J': 'DDR Corp.',

    'MSGN': 'MSG Networks Inc.',

    'SCI': 'Service Corporation International',

    'EMES': 'Emerge Energy Services LP',

    'ABR': 'Arbor Realty Trust',

    'WBA': 'Walgreens Boots Alliance, Inc.',

    'OA': 'Orbital ATK, Inc.',

    'TYPE': 'Monotype Imaging Holdings Inc.',

    'DISCK': 'Discovery Communications, Inc.',

    'INTLL': 'INTL FCStone Inc.',

    'SHG': 'Shinhan Financial Group Co Ltd',

    'MLI': 'Mueller Industries, Inc.',

    'AIW': 'Arlington Asset Investment Corp',

    'CDXS': 'Codexis, Inc.',

    'CHH': 'Choice Hotels International, Inc.',

    'BPFHP': 'Boston Private Financial Holdings, Inc.',

    'FNFG-B': 'First Niagara Financial Group Inc.',

    'MJN': 'Mead Johnson Nutrition Company',

    'RNR-C': 'RenaissanceRe Holdings Ltd.',

    'INFY': 'Infosys Limited',

    'WBB': 'Westbury Bancorp, Inc.',

    'OLN': 'Olin Corporation',

    'NHTC': 'Natural Health Trends Corp.',

    'DD-B': 'E.I. du Pont de Nemours and Company',

    'DCTH': 'Delcath Systems, Inc.',

    'SLM': 'SLM Corporation',

    'INVT': 'Inventergy Global, Inc.',

    'RFP': 'Resolute Forest Products Inc.',

    'PEO': 'Adams Natural Resources Fund, Inc.',

    'ENOC': 'EnerNOC, Inc.',

    'CAG': 'ConAgra Foods, Inc.',

    'PCG-G': 'Pacific Gas & Electric Co.',

    'TGP': 'Teekay LNG Partners L.P.',

    'JLL': 'Jones Lang LaSalle Incorporated',

    'CBS': 'CBS Corporation',

    'MNR-B': 'Monmouth Real Estate Investment Corporation',

    'AEK': 'Aegon NV',

    'TGS': 'Transportadora De Gas Sa Ord B',

    'ADS': 'Alliance Data Systems Corporation',

    'ERII': 'Energy Recovery, Inc.',

    'IMH': 'Impac Mortgage Holdings, Inc.',

    'TANH': 'Tantech Holdings Ltd.',

    'LBY': 'Libbey, Inc.',

    'LLY': 'Eli Lilly and Company',

    'FBC': 'Flagstar Bancorp, Inc.',

    'QQQC': 'Global X NASDAQ China Technology ETF',

    'USA': 'Liberty All-Star Equity Fund',

    'USM': 'United States Cellular Corporation',

    'BGFV': 'Big 5 Sporting Goods Corporation',

    'PEB-D': 'Pebblebrook Hotel Trust',

    'WYIGU': 'JM Global Holding Company',

    'BRFS': 'BRF S.A.',

    'STRZA': 'Starz',

    'NTK': 'Nortek Inc.',

    'GRR': 'Asia Tigers Fund, Inc. (The)',

    'NOMD': 'Nomad Foods Limited',

    'EACQU': 'Easterly Acquisition Corp.',

    'CYS': 'CYS Investments, Inc.',

    'RPRX': 'Repros Therapeutics Inc.',

    'SPEX': 'Spherix Incorporated',

    'ARTNA': 'Artesian Resources Corporation',

    'COLB': 'Columbia Banking System, Inc.',

    'PLSE': 'Pulse Biosciences, Inc',

    'MHI': 'Pioneer Municipal High Income Trust',

    'DRD': 'DRDGOLD Limited'
}



with open('bats_symbols.csv') as symbols:
    symbolReader = csv.reader(symbols)
    symbols = []
    for row in symbolReader:
        symbols.append(row[0])
        if row[0] in stockDict:
            symbols.append(stockDict[row[0]])

import json

output = open('search_terms.txt', 'w')
json.dump(symbols, output)
output.close()
