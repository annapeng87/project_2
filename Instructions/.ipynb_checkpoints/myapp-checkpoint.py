import yfinance as yf
import streamlit as st
import pandas as pd
import hvplot.pandas
from bokeh.plotting import figure
import holoviews as hv
hv.extension('bokeh', logo=False)
from PIL import Image

st.set_page_config(layout="wide")

# Load Image
image = Image.open('Pokemon Logo.jpg')
st.sidebar.image(image, use_column_width=True)

# load cardset list csv
cardset_list_df = pd.read_csv('Cardset List.csv')

st.title("Pokemon Cardsets Closing Price Predictor")
st.markdown("This application shows the Real and Predicted Prices for selected Pokemon Cardsets")

#st.sidebar.title("Pokemon Cardsets Closing Price Predictor")

st.sidebar.markdown("Select one or more Cardsets")

cardset_sel = st.sidebar.multiselect('', cardset_list_df['Cardsets'].unique())

url1_md = f"[Cardset Closing Prices Data Set](https://www.pokemonprice.com/TotalSetPrices)"
url2_md = f"[Keras Sequential Model Guide](https://keras.io/getting-started/sequential-model-guide/)"
url3_md = f"[Illustrated Guide to LSTMs](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21)"
url4_md = f"[Stanford's RNN Cheatsheet](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks)"
url5_md = f"[Price Sentiment](https://www.dexerto.com/pokemon/pokemon-analyst-reveals-insane-impact-logan-paul-has-had-on-tcg-prices-1428118/)"
url6_md = f"[Logo](https://aminoapps.com/c/pokemon/page/blog/pikachu-and-the-pokemon-logo/3GhB_uR0wKvx8ago8kqkVqn56zmJ4)"
url7_md = f"[Tools](https://mlpnk72yciwc.i.optimole.com/cqhiHLc.WqA8~2eefa/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2021/01/Screen-Shot-2020-12-16-at-4.28.29-AM-copy-7-1.jpg)"

st.sidebar.title("Resources")
st.sidebar.markdown(url1_md)
st.sidebar.markdown(url2_md)
st.sidebar.markdown(url3_md)
st.sidebar.markdown(url4_md)
st.sidebar.markdown(url5_md)

st.sidebar.title("jpg References")
st.sidebar.markdown(url6_md)
st.sidebar.markdown(url7_md)

column_1, column_2 = st.beta_columns([2,1])

if cardset_sel:
    for file in cardset_sel:
        cardset_md = f"{file}"
#        st.markdown(cardset_md)
        
        path = file + ".csv"
        jpg = file + ".jpg"
        
        pokemon_prices = pd.read_csv(path, index_col="Month", infer_datetime_format=True, parse_dates=True)
        pokemon_prices = pokemon_prices.sort_index()

        cardset_model = file
        cardset_title = f"LSTM Cardset Model {cardset_model}: Real vs Predicted Values"

        # Plot the real vs predicted values as a line chart
        nice_plot = pokemon_prices.hvplot.line(xlabel="Month",
                                   ylabel="Price",
                                   title=cardset_title) 
#                                   frame_width=600)

#        with st.beta_container():
        with column_1:
            st.header(cardset_md)
            st.write(hv.render(nice_plot, backend='bokeh'))
#        with column_2:
#            st.header('Picture')
#            image1 = Image.open(jpg)
#            st.image(image1, use_column_width=True, height=100)            
else:
    st.write("No cardset selected")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
#tickerSymbol = 'GOOGL'

#get data on this ticker
#tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
#tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

#st.line_chart(tickerDf.Close)
#st.line_chart(tickerDf.Volume)

