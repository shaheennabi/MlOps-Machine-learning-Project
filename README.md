# Gemstone Price Prediction

## Project Overview
Gem Stones Co Ltd. is interested in using data-driven insights to optimize its profit margins by accurately predicting the prices of cubic gemstones. This project leverages historical gemstone data to build a predictive model that estimates gemstone prices based on their physical and categorical characteristics. Additionally, the model highlights the top 5 attributes most crucial in determining gemstone price, enabling the company to distinguish between higher- and lower-value gemstones and make strategic pricing decisions.

## Problem Statement
You have been hired by Gem Stones Co Ltd., and are provided with a dataset containing prices and other attributes of nearly 27,000 cubic gemstones. The company’s profits vary across different price brackets, and by accurately predicting gemstone prices, they can better identify profitable stones, improving their profit share. 

The project objectives include:
1. **Predicting gemstone prices** based on the provided dataset attributes.

## Data Dictionary
The dataset includes the following features:

| Feature      | Description                                                                                                                                               |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Carat**    | The carat weight of the gemstone.                                                                                                                         |
| **Cut**      | Quality of the gemstone cut, rated in ascending quality as *Fair*, *Good*, *Very Good*, *Premium*, and *Ideal*.                                           |
| **Color**    | The color grade of the gemstone, with *D* being the highest quality and *J* the lowest.                                                                   |
| **Clarity**  | Refers to the clarity of the gemstone, or the absence of inclusions and blemishes. Graded in descending quality: *FL* (Flawless) to *I3* (Level 3 Inclusions). |
| **Depth**    | The height of the gemstone (measured from the culet to the table) divided by its average girdle diameter, expressed as a percentage.                     |
| **Table**    | The width of the gemstone’s table as a percentage of its average diameter.                                                                                |
| **Price**    | The price of the gemstone in USD (target variable).                                                                                                       |
| **X**        | Length of the gemstone in millimeters.                                                                                                                    |
| **Y**        | Width of the gemstone in millimeters.                                                                                                                     |
| **Z**        | Height of the gemstone in millimeters.                                                                                                                    |

## Project Structure

- **data/**: Directory containing the dataset files.
- **notebooks/**: Jupyter notebooks used for exploratory data analysis (EDA), feature engineering, and model training/testing.
- **src/**: Source code, including data processing, feature selection, and model building scripts.
- **README.md**: Project overview and instructions.



## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shaheennabi/MlOps-Machine-learning-Project

   ```
2. Create conda env
   ```bash
   conda create -n mlops python=3.8 -y
   ```

3. Activate conda mlops
   ```bash
   conda activate mlops
   ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```




## Future Work
Potential future directions include:
- Improving the model by exploring more complex ensemble methods.
- Incorporating domain-specific adjustments to better capture unique gemstone characteristics.
- Integrating the model into an application for real-time pricing analysis.

## License
This project is licensed under the MIT License.
