import folium
from django.shortcuts import render
import pandas as pd
import json

with open("all_id_new.geojson", "r",  encoding='utf-8') as read_file:  # фиксит проблему с инкодингом русских слов
     encod_geo_data = json.load(read_file) # (десериализует json в обьекты python)

def show_map(request, pk):

    m = folium.Map(location=[55.17, 51.00], tiles="OpenStreetMap", name="Light Map",
                   zoom_start=7.5)

    csv_test_data = pd.read_csv("csv_test_map_1.csv")  # через pandas подгружаем возможность прочесть csv код

    choice = ['Test_1', 'Test_2', 'Test_3', 'Test_4']  # значения выбора

    folium.Choropleth(
        geo_data="all_id_new.geojson",   # можно поменять на encod_geo_data, если нужно будет работать с русским текстом
        name="choropleth",
        data=csv_test_data,
        columns=["id",choice[pk]],
        key_on="feature.properties.id",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=.1,
        # legend_name=choice_selected
    ).add_to(m)

    folium.features.GeoJson(data=encod_geo_data
                            , name="States", popup=folium.features.GeoJsonPopup(fields=["rname", "id"],
                                                                                aliases=["region_name",
                                                                                         "region_id"])).add_to(m)
    m = m._repr_html_()
    context = {'my_map': m}

    return render(request, 'map/map_render.html', context)



