import plotly
import plotly.graph_objs as go

data = [go.Scatter(
    x = ["1/10","2/10","3/10","4/10","5/10", "6/10", "7/10", "8/10", "9/10", "10/10", "11/10", "12/10", "13/10", "14/10", "15/10", "16/10", "17/10", "18/10", "19/10", "20/10", "21/10", "22/10", "23/10", "24/10", "25/10", "26/10", "27/10"],
    y = [3273, 3324, 3387, 3367, 3312, 3289, 3286, 3220, 3360, 3403, 3237, 3330, 3365, 3261, 3467, 3259, 3381, 3322, 3340, 3301, 3283, 3296, 3372, 3401, 3245, 3371, 3297],
)]
layout = go.Layout(
        xaxis=dict(
            title='days',    
        ),
        yaxis=dict(
            title='Tips',  
        )
    )
fig = go.Figure(data=data, layout=layout)

plotly.offline.plot(fig,filename='tips.html',config={'displayModeBar': False})
