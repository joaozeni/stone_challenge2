import plotly
import plotly.graph_objs as go
"1/2009": 66824, 
"2/2009": 66680, 
"3/2009": 73948, 
"4/2009": 71142, 
"5/2009": 74151, 
"6/2009": 71342, 
"1/2010": 66179, 
"1/2011": 55570, 
"1/2012": 80926, 
"10/2009": 74011, 
"10/2010": 73648, 
"10/2011": 78580, 
"10/2012": 72783, 
"11/2009": 71424, 
"11/2010": 70876, 
"11/2011": 63027, 
"12/2009": 21583, 
"12/2010": 25874, 
"2/2010": 66837, 
"2/2011": 70990, 
"2/2012": 78451, 
"3/2010": 73616, 
"3/2011": 78285, 
"3/2012": 83368, 
"4/2010": 71075, 
"4/2011": 76122, 
"4/2012": 81298, 
"5/2010": 73663, 
"5/2011": 78591, 
"5/2012": 83935, 
"6/2010": 70987, 
"6/2011": 75734, 
"6/2012": 80814, 
"7/2009": 74076, 
"7/2010": 73487, 
"7/2011": 78713, 
"7/2012": 84421, 
"8/2009": 74021, 
"8/2010": 73358, 
"8/2011": 78855, 
"8/2012": 83431, 
"9/2009": 71511, 
"9/2010": 71113, 
"9/2011": 76246, 
"9/2012": 81286
  }
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