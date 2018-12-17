import itertools
import geopandas as gpd
import pandas as pd
from pydash import _
import matplotlib.pyplot as plt
from shapely.geometry import Point

oc_points = []
oil_points = []


def is_none(*items):
    """Cette fonction determine si les items sont de types None
                Parameters
                ----------
                items : args
                    Une liste d'arguments
                Returns
                -------
                bool
                    True si au moins un item est de type None
                """
    i = 0
    for item in items:
        is_instance = isinstance(None, type(item))
        if is_instance:
            i += 1
    return i > 0 and True or False


def item_aply_pfx_oil_or_oc(colt_oc_item: object, colt_oil_item: object, comn_item: object) -> object:
    """Cette fonction compare un prefixe oc et oil avec un nom de commune
        Parameters
        ----------
        colt_oc_item : str
            Le prefixe oc
        colt_oil_item : str
            Le prefixe oil
        comn_item: str
            Le nom de commune
        Returns
        -------
        int
            une valeur compris dans cette intervalle [-1, 1]
        """
    if is_none(colt_oil_item, colt_oc_item):
        return 0
    elif is_none(colt_oc_item):
        return _.starts_with(_.lower_case(comn_item), colt_oil_item) and -1 or 0
    elif is_none(colt_oil_item):
        return _.starts_with(_.lower_case(comn_item), colt_oc_item) and 1 or 0
    else:
        return _.starts_with(_.lower_case(comn_item), colt_oc_item) and 1 or _.starts_with(_.lower_case(comn_item),
                                                                                           colt_oil_item) and -1 or 0


def item_aply_sfx_oil_or_oc(colt_oc_item: object, colt_oil_item: object, comn_item: object) -> object:
    """Cette fonction compare un suffixe oc et oil avec un nom de commune
            Parameters
            ----------
            colt_oc_item : str
                Le suffixe oc
            colt_oil_item : str
                Le suffixe oil
            comn_item: str
                Le nom de commune
            Returns
            -------
            int
                une valeur compris dans cette intervalle [-1, 1]
            """
    if is_none(colt_oil_item, colt_oc_item):
        return 0
    elif is_none(colt_oc_item):
        return _.ends_with(_.lower_case(comn_item), colt_oil_item) and -1 or 0
    elif is_none(colt_oil_item):
        return _.ends_with(_.lower_case(comn_item), colt_oc_item) and 1 or 0
    else:
        return _.ends_with(_.lower_case(comn_item), colt_oc_item) and 1 or _.ends_with(_.lower_case(comn_item),
                                                                                       colt_oil_item) and -1 or 0


def ling_rl_value(oc_clt, oil_clt, comn_name):
    """Cette fonction renvoie la valeur de la variable linguistique
                Parameters
                ----------
                oc_clt : list
                    la collection des règles oc
                oil_clt: list
                    la collection des règles oi
                comn_name: str
                    Le nom de commune à traiter
                Returns
                -------
                int
                    une valeur compris dans cette intervalle [-1, 1]
                """
    vld_rle = 0
    i = 0
    for oc_pfx_item, oc_sfx_item, oil_pfx_item, oil_sfx_item in itertools.zip_longest(oc_clt.prefixe,
                                                                                      oc_clt.suffixe,
                                                                                      oil_clt.prefixe,
                                                                                      oil_clt.suffixe):
        pfx_rle = item_aply_pfx_oil_or_oc(oc_pfx_item, oil_pfx_item, comn_name)
        sfx_rle = item_aply_sfx_oil_or_oc(oc_sfx_item, oil_sfx_item, comn_name)
        ling_rle = pfx_rle != 0 and pfx_rle or sfx_rle != 0 and sfx_rle or 0
        if ling_rle == -1:
            vld_rle = ling_rle
        elif ling_rle == 1:
            vld_rle = ling_rle
        i = i + 1

    return vld_rle


def is_oc(ling_rule):
    """Cette fonction determine par rapport à la valeur de la variable linguistique si une commune est oc ou non
            Parameters
            ----------
            ling_rule: int
                La valeur de la règle linguistique
            Returns
            -------
            bool
                true si oc false sinon
            """
    return ling_rule == 1


def is_oil(ling_rule):
    """Cette fonction determine par rapport à la valeur de la variable linguistique si une commune est oil ou non
             Parameters
             ----------
             ling_rule: int
                 La valeur de la règle linguistique
             Returns
             -------
             bool
                 true si oil false sinon
             """
    return ling_rule == -1


def crt_oc_oil_pts(df_rproj_clt, rules_clt, df_cmnes):
    i = 0
    for nom in df_cmnes:
        ling_var = ling_rl_value(rules_clt.oc, rules_clt.oil, nom)
        if is_oc(ling_var):
            global oc_points
            oc_points.append(df_rproj_clt.ix[i])
        elif is_oil(ling_var):
            global oil_points
            oil_points.append(df_rproj_clt.ix[i])
        i += 1

    global oc_df
    global oil_df
    oc_df = pd.DataFrame.from_records(oc_points, columns=['X', 'Y', 'code', 'nom'])
    oil_df = pd.DataFrame.from_records(oil_points, columns=['X', 'Y', 'code', 'nom'])


def get_dframe(geojsonfile):
    """Cette fonction lit une fichier de format .geojson et retourne un data frame
             Parameters
             ----------
             geojsonfile: str
                 le chemin vers le fichier .geojson
             Returns
             -------
             DataFrame
                 un object de type data frame
             """
    dframe = gpd.read_file(geojsonfile)
    return dframe


def geojson_reprojected(csvpath):
    gdf = pd.read_csv(csvpath)
    return gdf


def draw_fr_map(dframe):
    """Cette fonction dessine une carte en fonction du dataframe fournit
             Parameters
             ----------
             dframe: DataFrame
                 Le data frame en question
             """
    fig, ax = plt.subplots(1, figsize=(30, 30))
    dframe.plot(ax=ax, color='#FDFFFC', alpha=0.5, edgecolor='#0E0F19')
    rules = get_rules('prm2_rules.json')
    crt_oc_oil_pts(geojson_reprojected('communes.csv'), rules, dframe.nom)
    geometry_oc = [Point(xy) for xy in zip(oc_df.X, oc_df.Y)]
    geometry_oil = [Point(xy) for xy in zip(oil_df.X, oil_df.Y)]
    crs = {'init', 'epsg:4326'}
    oc_map = gpd.GeoDataFrame(crs=crs, geometry=geometry_oc)
    oil_map = gpd.GeoDataFrame(crs=crs, geometry=geometry_oil)
    oc_map.plot(ax=ax, color='#ED1C24', marker='o', markersize=92, label="commune oc", legend=True)
    oil_map.plot(ax=ax, color='#235789', marker='o', markersize=92, label="commune oil", legend=True)
    ax.legend(fancybox=True, loc='lower center', scatterpoints=1, framealpha=1, shadow=True, borderpad=1,
              ncol=2, fontsize=40)
    ax.set_title("Cartographie de la France selon le critère de langue oc ou oil",
                 fontsize=55)
    ax.set_axis_off()
    plt.show()


def get_rules(jsonfile):
    """Cette fonction lit un fichier de format .json
             Parameters
             ----------
             jsonfile: str
                 Le chemin vers le fichier json
             Returns
             -------
             object
                 un object json manipulable
             """
    ctrules = pd.read_json(jsonfile)
    return ctrules


df = get_dframe("communes.geojson")
draw_fr_map(df)
# print(df.nom)
# rules = get_rules("prm2_rules.json")
# crt_oc_oil_pts(geojson_reprojected('communes.csv'), rules, df.nom)
# print(df.ix[0].head())
# print(is_oil(ling_rl_value(rules.oc, rules.oil, "Villeneuve")))
# print(ling_rl_value(rules.oc, rules.oil, "Villefort"))
# print(ling_rl_value(rules.oc, rules.oil, "Rougemont"))
# print(ling_rl_value(rules.oc, rules.oil, " Blanc-Mont"))
