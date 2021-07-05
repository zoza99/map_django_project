import folium
from django.shortcuts import render
import pandas as pd
#from map_django_project.map_api.views import new_frame

# choice_box=['Test_1', 'Test_2', 'Test_3', 'Test_4']

def show_map(request, pk):

    m = folium.Map(location=[55.17, 51.00], tiles= "OpenStreetMap", name="Light Map",
                   zoom_start=6)

    # csv_test_map = "csv_test_map_1.csv"  # присваеваем csv файлу имя
    csv_test_data = pd.read_csv("csv_test_map_1.csv")  # через pandas подгружаем возможность прочесть csv код

    choice = ['Test_1', 'Test_2', 'Test_3', 'Test_4']  # значения выбора
    # choice_selected = st.selectbox("Select choice", choice)  # создание бокса выбора

    folium.Choropleth(
        geo_data="all_id_new.geojson",
        name="choropleth",
        data=csv_test_data,
        columns=["id",choice[pk]],
        key_on="feature.properties.id",
        fill_color="YlOrRd",
        fill_opacity=0.7,
        line_opacity=.1,
        # legend_name=choice_selected
    ).add_to(m)

    # geojson1 =(open("all_id.geojson", "r", encoding="utf-8-sig")).read()
    folium.features.GeoJson(data="all_id_new.geojson"
                            , name="States", popup=folium.features.GeoJsonPopup(fields=["rname", "id"],
                                                                                aliases=["region_name",
                                                                                         "region_id"])).add_to(m)
    m = m._repr_html_()
    context = {'my_map': m}

    return render(request, 'map/map_render.html', context)

print(new_frame)
