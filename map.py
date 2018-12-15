import geopandas as gpd
import pandas as pd
from pydash import _
import matplotlib.pyplot as plt


def item_aply_pfx_oil_or_oc(colt_oc_item, colt_oil_item, comn_item):
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
    return _.starts_with(_.lower_case(comn_item), colt_oc_item) and 1 or _.starts_with(_.lower_case(comn_item),
                                                                                       colt_oil_item) and -1 or 0


def item_aply_sfx_oil_or_oc(colt_oc_item, colt_oil_item, comn_item):
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
    return _.ends_with(_.lower_case(comn_item), colt_oc_item) and 1 or _.ends_with(_.lower_case(comn_item),
                                                                                   colt_oil_item) and -1 or 0


def is_oc(ling_rule):
    """Cette fonction determine par rapport à la valeur de la variable linguistique si une commune est oc ou non
            Parameters
            ----------
            ling_rule: str
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
             ling_rule: str
                 La valeur de la règle linguistique
             Returns
             -------
             bool
                 true si oil false sinon
             """
    return ling_rule == -1


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


def draw_fr_map(dframe, color, markersize):
    """Cette fonction dessine une carte en fonction du dataframe fournit
             Parameters
             ----------
             dframe: DataFrame
                 Le data frame en question
             color: str
                 La couleur de fond de la carte
             markersize: int
                Le taille des contours par défaut mettre 1.5
             """
    dframe.plot(figsize=(10, 10), color=color, markersize=markersize, alpha=0.5, edgecolor='w')
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


# df = get_dframe("communes.geojson")
# print(df.nom)
rules = get_rules("prm2_rules.json")

# print(df.ix[0].head())
# print(item_aply_sfx_oil_or_oc("ac", "franche", "Plazac"))
# rules = get_rules("prm2_rules.json")
# draw_fr_map(df, 'blue', 1.5)
