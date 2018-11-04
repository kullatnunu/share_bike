from bokeh.io import output_file, show
from bokeh.layouts import widgetbox, column
from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show


df_station = pd.read_csv("C:/YenTingPC/Python_project/sf_bike/station.csv")
df_station.head()


#import data----------

import pandas as pd
dc_name = df_station['name'].unique().tolist()
dc_city = df_station['city'].unique().tolist()
dc_id = df_station['id'].unique().tolist()
dc_dcount = df_station['dock_count'].tolist()
source = ColumnDataSource(data=dict(x=dc_id, y=dc_dcount,
                                   San_Jose_x = df_station.id[df_station.city == "San Jose"],
                                   San_Jose_y = df_station.dock_count[df_station.city == "San Jose"],
                                   Redwood_City_x = df_station.id[df_station.city == "Redwood City"],
                                    Redwood_City_y = df_station.dock_count[df_station.city == "Redwood City"],
                                   Mountain_View_x = df_station.id[df_station.city == "Mountain View"],
                                   Mountain_View_y = df_station.dock_count[df_station.city == "Mountain View"],
                                    Palo_Alto_x = df_station.id[df_station.city == "Palo Alto"],
                                    Palo_Alto_y = df_station.dock_count[df_station.city == "Palo Alto"],
                                   San_Francisco_x = df_station.id[df_station.city == "San Francisco"],
                                    San_Francisco_y = df_station.dock_count[df_station.city == "San Francisco"],
                                   ))

#bar plot----------

plot = Figure(plot_width=400, plot_height=400)
#plot.vbar(x=dc_id, width=0.5, bottom=0, top=dc_dcount, color="firebrick")
plot.vbar(x = 'x',top = 'y', source=source, width=0.5, bottom=0, color="firebrick")

#call back ----------
# plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


def callback1(source=source, source2=source2):
    data = source.data
    data2 = source2.data
    f = cb_obj.value
    data.x=data[f+'_x']
    data.y=data[f+'_y']
    source.change.emit()


#import selecter----------

select1 = Select(title="City:", value="San Jose", options=['San_Jose','Redwood_City','Mountain_View','Palo_Alto','San_Francisco'], callback=CustomJS.from_py_func(callback1))
select2 = Select(title="name:", value="All", options=['All'] + dc_name, callback=callback)


#show image----------

layout = column(select1, select2, plot)

show(layout)
