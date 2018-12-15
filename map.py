import geopandas as gpd
import matplotlib.pyplot as plt


def nme_catgory(dframe):
    for name in dframe.nom:
        print(name)


def get_df_data(geojsonfile):
    dframe = gpd.read_file(geojsonfile)
    return dframe


def draw_fr_map(dframe, color, markersize):
    dframe.plot(color=color, markersize=markersize)
    plt.show()


df = get_df_data("communes.geojson")
draw_fr_map(df, 'blue', 1.5)
