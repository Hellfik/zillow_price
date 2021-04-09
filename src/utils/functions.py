import matplotlib.pyplot as plt

# Functions to display a diagram showing the percent of missing values for each column in a dataframe

def msv1(data, thresh=20, color='black', edgecolor='black', width=30, height=15):
    """
    SOURCE: https://www.kaggle.com/amiiiney/price-prediction-regularization-stacking
    """
    
    plt.figure(figsize=(width,height))
    percentage=(data.isnull().mean())*100
    percentage.sort_values(ascending=False).plot.bar(color=color, edgecolor=edgecolor)
    plt.axhline(y=thresh, color='r', linestyle='-')
    plt.title('Missing values percentage per column', fontsize=20, weight='bold' )
    plt.text(len(data.isnull().sum()/len(data))/1.7, thresh+12.5, 'Columns with more than %s%s missing values' %(thresh, '%'), fontsize=12,weight='bold', color='crimson',
         ha='left' ,va='top')
    plt.text(len(data.isnull().sum()/len(data))/1.7, thresh - 5, 'Columns with less than %s%s missing values' %(thresh, '%'), fontsize=12,weight='bold', color='blue',
         ha='left' ,va='top')
    plt.xlabel('Columns', size=15, weight='bold')
    plt.ylabel('Missing values percentage', weight='bold')
    plt.yticks(weight ='bold')
    
    return plt.show()



"""
    Assign better names to all feature columns of 'properties' table
"""
def rename_columns(prop):
     prop.rename(columns={
          'parcelid': 'parcelid',  # Unique identifier of parcels
          'airconditioningtypeid': 'cooling_id',  # type of cooling system (if any), 1~13
          'architecturalstyletypeid': 'architecture_style_id',  # Architectural style of the home, 1~27
          'basementsqft': 'basement_sqft',  # Size of the basement
          'bathroomcnt': 'bathroom_cnt',  # Number of bathrooms (including fractional bathrooms)
          'bedroomcnt': 'bedroom_cnt',  # Number of bedrooms
          'buildingclasstypeid': 'framing_id',  # The building framing type, 1~5
          'buildingqualitytypeid': 'quality_id',  # building condition from best (lowest) to worst (highest)
          'calculatedbathnbr': 'bathroom_cnt_calc',  # Same meaning as 'bathroom_cnt'?
          'decktypeid': 'deck_id',  # Type of deck (if any)
          'finishedfloor1squarefeet': 'floor1_sqft',  # Size of finished living area on first floor
          'calculatedfinishedsquarefeet': 'finished_area_sqft_calc',  # calculated total finished living area
          'finishedsquarefeet12': 'finished_area_sqft',  # Same meaning as 'finished_area_sqft_calc'?
          'finishedsquarefeet13': 'perimeter_area',  # Perimeter living area
          'finishedsquarefeet15': 'total_area',  # Total area
          'finishedsquarefeet50': 'floor1_sqft_unk',  # Same meaning as 'floor1_sqft'?
          'finishedsquarefeet6': 'base_total_area',  # Base unfinished and finished area
          'fips': 'fips',  # Federal Information Processing Standard code
          'fireplacecnt': 'fireplace_cnt',  # Number of fireplaces in the home (if any)
          'fullbathcnt': 'bathroom_full_cnt',  # Number of full bathrooms
          'garagecarcnt': 'garage_cnt',  # Total number of garages
          'garagetotalsqft': 'garage_sqft',  # Total size of the garages
          'hashottuborspa': 'spa_flag',  # Whether the home has a hot tub or spa
          'heatingorsystemtypeid': 'heating_id',  # type of heating system, 1~25
          'latitude': 'latitude',  # latitude of the middle of the parcel multiplied by 1e6
          'longitude': 'longitude',  # longitude of the middle of the parcel multiplied by 1e6
          'lotsizesquarefeet': 'lot_sqft',  # Area of the lot in sqft
          'poolcnt': 'pool_cnt', # Number of pools in the lot (if any)
          'poolsizesum': 'pool_total_size',  # Total size of the pools
          'pooltypeid10': 'pool_unk_1',
          'pooltypeid2': 'pool_unk_2',
          'pooltypeid7': 'pool_unk_3',
          'propertycountylandusecode': 'county_landuse_code',
          'propertylandusetypeid': 'landuse_type_id' ,  # Type of land use the property is zoned for, 25 categories
          'propertyzoningdesc': 'zoning_description',  # Allowed land uses (zoning) for that property
          'rawcensustractandblock': 'census_1',
          'regionidcity': 'city_id',  # City in which the property is located (if any)
          'regionidcounty': 'county_id',  # County in which the property is located
          'regionidneighborhood': 'neighborhood_id',  # Neighborhood in which the property is located
          'regionidzip': 'region_zip',
          'roomcnt': 'room_cnt',  # Total number of rooms in the principal residence
          'storytypeid': 'story_id',  # Type of floors in a multi-story house, 1~35
          'threequarterbathnbr': 'bathroom_small_cnt',  # Number of 3/4 bathrooms
          'typeconstructiontypeid': 'construction_id',  # Type of construction material, 1~18
          'unitcnt': 'unit_cnt',  # Number of units the structure is built into (2=duplex, 3=triplex, etc)
          'yardbuildingsqft17': 'patio_sqft',  # Patio in yard
          'yardbuildingsqft26': 'storage_sqft',  # Storage shed/building in yard
          'yearbuilt': 'year_built',  # The year the principal residence was built
          'numberofstories': 'story_cnt',  # Number of stories or levels the home has
          'fireplaceflag': 'fireplace_flag',  # Whether the home has a fireplace
          'structuretaxvaluedollarcnt': 'tax_structure',
          'taxvaluedollarcnt': 'tax_parcel',
          'assessmentyear': 'tax_year',  # The year of the property tax assessment (2015 for 2016 data)
          'landtaxvaluedollarcnt': 'tax_land',
          'taxamount': 'tax_property',
          'taxdelinquencyflag': 'tax_overdue_flag',  # Property taxes are past due as of 2015
          'taxdelinquencyyear': 'tax_overdue_year',  # Year for which the unpaid propert taxes were due
          'censustractandblock': 'census_2'
     }, inplace=True)