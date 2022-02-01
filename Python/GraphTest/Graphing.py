import plotly.graph_objects as go

def BarChart():
  fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="Rando Test"
  )
  fig.show()

def Main():
  BarChart()
   
if __name__ == "__main__":
    Main()