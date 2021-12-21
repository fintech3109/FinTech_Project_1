{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "JTTHt1iV-bpN"
   },
   "source": [
    "# U.S. Mint Catalog List with Metals APIs and Simulations\n",
    "\n",
    "In this Project, project member will develop tools using Jupyter notebook to analyze the relationship between USD coins melt and face value. The Project will also analyze the pro's and con's of Commodity-Backed Monetary Systems.\n",
    "\n",
    "\n",
    ">##### Part 1: Melt Value of U.S. Coins. \n",
    ">The user will be able to use this tool to visualize the relationship between USD notes and coins (or melt value of coin in USD notes). The user can then compare the coins face value, and melt value.  \n",
    ">##### Part 2: Population Calculator. \n",
    "\n",
    "This tool provide the estimated global and U.S. population. To do this, the tool will make an \n",
    "API call via the uscenses.gov & metal-api SDK to get the estimated population. Additional feature of the app will allow users to analyze the distribution of each metal based on the annual production of each metal and global population, as well as economic and price data using Monte Carlo simulations.\n",
    "\n",
    "\n",
    "Project member will use the information from the Monte Carlo simulation to answer questions about prospects of a UBI scheme for Commodity-Backed Monetary Systems.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "id": "1ea8qvBR-bpQ"
   },
   "outputs": [],
   "source": [
    "# Import the required libraries and dependencies\n",
    "import os\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "from dotenv import load_dotenv\n",
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'dataset' (Bunch)\n"
     ]
    }
   ],
   "source": [
    "from sklearn import datasets\n",
    "dataset = datasets.load_iris()\n",
    "%store dataset\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "elxGQkEt9-f2",
    "outputId": "7a870e48-b2ef-4366-e03c-aaf69bbe7c71"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Python-dotenv could not parse statement starting at line 15\n",
      "Python-dotenv could not parse statement starting at line 16\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Load the environment variables from the .env file\n",
    "#by calling the load_dotenv function\n",
    "\n",
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 1: MEASUREMENT VARIABLES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'avdp_ou' (float)\n"
     ]
    }
   ],
   "source": [
    "avdp_ou = 28.34952312 \n",
    "%store avdp_ou"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "troy_ou = 31.1034768"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "metric_tonne = 1000000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "gram = 1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 2: COIN LIST & WEIGHTS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# provide the weight (in grams) for each of the coins listed in the US mint catalog.\n",
    "\n",
    "Penny_wt = 2.5*gram\n",
    "Nickel_wt = 5.0*gram\n",
    "Dime_wt = 2.268*gram \n",
    "Quarter_wt = 5.67*gram\n",
    "Half_Dollar_wt = 11.34*gram \n",
    "dollar_coin_wt = 8.1*gram "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 3: METAL PRICES"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Step 1: Access Metals API for Daily, Monthly, or Yearly Rates for Metals\n",
    "\n",
    " > **To-Do**: Review the endpoint URLs for the API calls to census population calculator and metals live prices API in order to get the current pricing information for metals used in U.S. Coins and global population figure.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The Population Calculator & Metal Prices API Call endpoint URLs \n",
    "\n",
    "Population_url = \"https://api.census.gov/data/2019/pep/population\"\n",
    "\n",
    "Metals_url = \"https://www.metals-api.com/api/latest?access_key=g7t30l1a5xvpn5e3d22fg95dc5zzom6epc728v26y870gu4mp38o7rn0aiv5&base=USD&symbols=XAU,XAG,XCU,NI,ZNC\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Step 2: Using the Python requests library, make an API call to access the current price USD for metals"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "response = requests.get(Metals_url).json()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Step 3: Use the json.dumps function to review the response data from the API call\n",
    " > **To-Do**: Use the indent and sort_keys parameters to make the response object readable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"base\": \"USD\",\n",
      "    \"date\": \"2021-12-21\",\n",
      "    \"rates\": {\n",
      "        \"NI\": 1.646374403514,\n",
      "        \"USD\": 1,\n",
      "        \"XAG\": 0.0449190456,\n",
      "        \"XAU\": 0.00055830132,\n",
      "        \"XCU\": 3.7126901669759,\n",
      "        \"ZNC\": 10.379441282259\n",
      "    },\n",
      "    \"success\": true,\n",
      "    \"timestamp\": 1640064780,\n",
      "    \"unit\": \"per ounce\"\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "print(json.dumps(response, indent=4, sort_keys=True))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Metals - List & Currect Market Price"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.1- Copper Price"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> AVDP OUNCE "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "copper avdp ou $ 0.27\n"
     ]
    }
   ],
   "source": [
    "# Copper Price per Avdp Ounce\n",
    "\n",
    "cu_rates = response['rates']['XCU']\n",
    "USD = response['rates']['USD']\n",
    "\n",
    "cu_avdp_ou  = USD/cu_rates\n",
    "\n",
    "print(f\"copper avdp ou ${cu_avdp_ou: .2f}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> GRAM"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "copper gram = $ 0.00950\n"
     ]
    }
   ],
   "source": [
    "# Copper Price per gram. cu_g is also cu_1000\n",
    "cu_g = cu_avdp_ou / avdp_ou\n",
    "print(f\"copper gram = ${cu_g: .5f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.2- Nickel Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nickel avdp ou $ 0.60740\n",
      "Stored 'USD' (int)\n"
     ]
    }
   ],
   "source": [
    "# Nickel Price per Avdp Ounce\n",
    "ni_rates = response['rates']['NI']\n",
    "USD = response['rates']['USD']\n",
    "\n",
    "ni_troy_ou = USD/ni_rates\n",
    "\n",
    "print(f\"Nickel avdp ou ${ni_troy_ou: .5f}\")\n",
    "\n",
    "%store USD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nickel gram = $ 0.01953\n"
     ]
    }
   ],
   "source": [
    "# Nickel Price per gram\n",
    "ni_g = ni_troy_ou / troy_ou\n",
    "print(f\"Nickel gram = ${ni_g: .5f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.3- Zink Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Zinc avdp ou $ 0.09634\n"
     ]
    }
   ],
   "source": [
    "zn_rates = response['rates']['ZNC']\n",
    "USD = response['rates']['USD']\n",
    "\n",
    "zn_avdp_ou = USD/zn_rates\n",
    "\n",
    "print(f\"Zinc avdp ou ${zn_avdp_ou: .5f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Zinc gram = $ 0.003398\n"
     ]
    }
   ],
   "source": [
    "zn_g = zn_avdp_ou / avdp_ou\n",
    "print(f\"Zinc gram = ${zn_g: .6f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "mn_g = 0.00006\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.4 Silver Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silver troy ou $ 22.26\n"
     ]
    }
   ],
   "source": [
    "ag_rates = response['rates']['XAG']\n",
    "USD = response['rates']['USD']\n",
    "\n",
    "ag_troy_ou = USD/ag_rates\n",
    "\n",
    "print(f\"Silver troy ou ${ag_troy_ou: .2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Silver gram = $ 0.72\n"
     ]
    }
   ],
   "source": [
    "ag_g = ag_troy_ou / troy_ou\n",
    "print(f\"Silver gram = ${ag_g: .2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3.5- Gold Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gold avdp ou $ 1791.15\n"
     ]
    }
   ],
   "source": [
    "au_rates = response['rates']['XAU']\n",
    "USD = response['rates']['USD']\n",
    "\n",
    "au_troy_ou = USD/au_rates\n",
    "\n",
    "print(f\"Gold avdp ou ${au_troy_ou: .2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Gold gram = $ 57.59\n"
     ]
    }
   ],
   "source": [
    "au_g = au_troy_ou / troy_ou\n",
    "print(f\"Gold gram = ${au_g: .2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 4- U.S. COIN METAL COMPOSITION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.1- Dollar Coin"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dollar Coin Metal Composition- Percentage Breakdown"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.0\n",
      "Stored 'DOLLAR' (float)\n"
     ]
    }
   ],
   "source": [
    "# Dollar Coin Metal Composition- Percentage Breakdown\n",
    "\n",
    "cu_100= 0.885\n",
    "ni_100= 0.02\n",
    "zn_100= 0.06\n",
    "mn_100= 0.035\n",
    "\n",
    "dollar_coin= cu_100+ni_100+zn_100+mn_100\n",
    "print(dollar_coin)\n",
    "\n",
    "DOLLAR = dollar_coin\n",
    "%store DOLLAR\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dollar Coin metal composition measured in grams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "dollar_cu = dollar_coin_wt * cu_100\n",
    "dollar_ni = dollar_coin_wt * ni_100\n",
    "dollar_zn = dollar_coin_wt * zn_100\n",
    "dollar_mn = dollar_coin_wt * mn_100"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.2- Quarter Dollar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Quarter-Dollar Coin Metal Composition- Percentage Breakdown\n",
    "\n",
    "cu_25= 11/12\n",
    "ni_25= 1/12"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Quarter-Dollar Coin metal composition measured in grams"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "quarter_dollar_cu = Quarter_wt * cu_25  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "quarter_dollar_ni = Quarter_wt * ni_25 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.3- Dime Coin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dime Coin Metal Composition- Percentage Breakdown\n",
    "\n",
    "cu_10= 11/12\n",
    "ni_10= 1/12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "dime_cu = Dime_wt * cu_10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "dime_ni = Dime_wt * ni_10"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.4- Nickel Coin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Nickel Coin Metal Composition- Percentage Breakdown\n",
    "\n",
    "cu_05= 0.75\n",
    "ni_05= 0.25"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "nickel_cu = Nickel_wt * cu_05"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "nickel_ni = Nickel_wt * ni_05"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4.5- Penny Coin"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Penny Coin Metal Composition- Percentage Breakdown\n",
    "\n",
    "cu_01= 0.025\n",
    "zn_01= 0.975"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "penny_cu = Penny_wt * cu_01"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "penny_zn = Penny_wt * zn_01"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "uIS70bUe-bpU"
   },
   "source": [
    "## PART 5: Develope a Seigneuriage Calculator named Sovereign.Credit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iJeBkWQH-bpU"
   },
   "source": [
    "### Evaluate the Melt Value by Using the Requests Library\n",
    "\n",
    "In this section, you’ll determine the melt value of the coins of the US mint catalog. Project member will collect the current market prices for the metals used in the coins by using the Python Requests library. For the prototype, we will assume that the user holds one of each coin. \n",
    "\n",
    "1. Create a variable named `US_mint_catalog`, and set its face value to `$1.91`.\n",
    "\n",
    "2. Use the Requests library to get the current price (in US dollars) of copper (cu), nickel (ni), zinc (zn), and  manganese (mn) by using the API endpoints. \n",
    "\n",
    "3. Navigate the JSON response object to access the current price of each coin, and store each in a variable.\n",
    "\n",
    "    > **Hint** Note the specific identifier for each metal in the API JSON response. The usd identifier is `1`, and the sovereign.credit identifier is `1187`.\n",
    "\n",
    "4. Calculate the value, in US dollars, of the melt calue of each coin type listed in the U.S. mint catalog.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Step 4: Navigate the JSON response object to access the current price of each of the metals in dollar coin, and store each in a variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ">Navigate the JSON response object to access the current price of each of the metals in U.S. coin, and store each in a variable."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5.1- Dollar Coin: \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Navigate the metals response object to access the current price of metals\n",
    "\n",
    "cu_100_price = dollar_cu*cu_g\n",
    "ni_100_price = dollar_ni*ni_g\n",
    "zn_100_price = dollar_zn*zn_g\n",
    "mn_100_price = dollar_mn*mn_g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.06810732512218429\n"
     ]
    }
   ],
   "source": [
    "print(cu_100_price)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Dollar Melt Value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Melt value of one dollar coin is  0.0729\n"
     ]
    }
   ],
   "source": [
    "dollar_metal_value= dollar_cu*cu_g+dollar_ni*ni_g+dollar_zn*zn_g+dollar_mn*mn_g\n",
    "\n",
    "print(f\"Melt value of one dollar coin is {dollar_metal_value: .4f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "USD is the metal value of the Dollar coin conveyed as a ration. Dollar coin Value is $ 0.07294 USD\n"
     ]
    }
   ],
   "source": [
    "USD = ((dollar_coin+dollar_metal_value)*(dollar_metal_value)- (dollar_metal_value))/dollar_metal_value\n",
    "print(f\"USD is the metal value of the Dollar coin conveyed as a ration. Dollar coin Value is ${USD: .5f} USD\")\n",
    "\n",
    "#dollar_coin is the sum of the ratio of all the metals in the USD one coin -or- 1\n",
    "#dollar_metal_value is the metal value of all the metals in the dollar_coin\n",
    "#USD is the percent difference of 1 + dollar_metal_value multiplied by the dollar_metal_value \n",
    "\n",
    "# dollar_metal_value / 1 + dollar_metal_value = price of copper content in dollar coin (cu_100_price) \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5.2- Quarter Dollar: "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 0.0586\n"
     ]
    }
   ],
   "source": [
    "# Navigate the metals response object to access the current price of metals\n",
    "\n",
    "cu_25_price = quarter_dollar_cu * cu_g\n",
    "ni_25_price = quarter_dollar_ni * ni_g\n",
    "\n",
    "# Quarter-Dollar Melt Value\n",
    "\n",
    "quarter_metal_value = cu_25_price + ni_25_price\n",
    "print(f\"{quarter_metal_value: .4f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5.3- Dime Coin:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 0.0234\n"
     ]
    }
   ],
   "source": [
    "# Navigate the metals response object to access the current price of metals\n",
    "\n",
    "cu_10_price = dime_cu * cu_g\n",
    "ni_10_price = dime_ni * ni_g\n",
    "\n",
    "# Dime Melt Value\n",
    "\n",
    "dime_metal_value = cu_10_price + ni_10_price\n",
    "\n",
    "print(f\"{dime_metal_value: .4f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5.4- Nickel Coin:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 0.0600\n"
     ]
    }
   ],
   "source": [
    "# Navigate the metals response object to access the current price of metals\n",
    "\n",
    "cu_05_price = nickel_cu * cu_g\n",
    "ni_05_price = nickel_ni * ni_g\n",
    "\n",
    "# Nickel Melt Value\n",
    "\n",
    "nickel_metal_value = cu_05_price + ni_05_price\n",
    "\n",
    "print(f\"{nickel_metal_value: .4f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5.5- Penny Coin:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 0.0089\n"
     ]
    }
   ],
   "source": [
    "cu_01_price = penny_cu * cu_g\n",
    "zn_01_price = penny_zn * zn_g\n",
    " \n",
    "    \n",
    "# Penny Melt Value\n",
    "\n",
    "penny_metal_value = cu_01_price + zn_01_price\n",
    "\n",
    "print(f\"{penny_metal_value: .4f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Coin List - Melt Value "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'Dollar' (float)\n",
      "Stored 'Quarter' (float)\n",
      "Stored 'Nickel' (float)\n",
      "Stored 'Dime' (float)\n",
      "Stored 'Penny' (float)\n"
     ]
    }
   ],
   "source": [
    "# provide the weight (in grams) for each of the coins listed in the US mint catalog.\n",
    "\n",
    "Penny = penny_metal_value\n",
    "Nickel = nickel_metal_value\n",
    "Dime = dime_metal_value\n",
    "Quarter = quarter_metal_value\n",
    "Dollar = dollar_metal_value\n",
    "\n",
    "%store Dollar\n",
    "%store Quarter\n",
    "%store Nickel\n",
    "%store Dime\n",
    "%store Penny"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Seigneuriage Calculator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 S.C. = $ 13.7100\n",
      "Stored 'SC' (float)\n"
     ]
    }
   ],
   "source": [
    "Seigneuriage = DOLLAR / USD\n",
    "print(f\"1 S.C. = ${Seigneuriage: .4f}\")\n",
    "\n",
    "SC = Seigneuriage\n",
    "\n",
    "\n",
    "%store SC "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    ">##### PRIME 13 & 53"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 6: WORLD POPULATION"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import requests\n",
    "import json\n",
    "import pandas as pd\n",
    "from dotenv import load_dotenv\n",
    "import csv\n",
    "from pathlib import Path\n",
    "\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "International_Database = pd.read_csv(\n",
    "    Path(\"../census/International_Database.csv\"),\n",
    "    index_col=\"Row\",\n",
    "    parse_dates=True,\n",
    "    infer_datetime_format=True\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "int_data_sliced= International_Database.loc[:,\"Population\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Row\n",
       "1      37466414\n",
       "2       3088385\n",
       "3      43576691\n",
       "4         46366\n",
       "5         85645\n",
       "         ...   \n",
       "224     2949246\n",
       "225      668862\n",
       "226    30399243\n",
       "227    19077816\n",
       "228    14829988\n",
       "Name: Population, Length: 228, dtype: int64"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "int_data_sliced"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "World Population = 7772850805 people\n"
     ]
    }
   ],
   "source": [
    "world_population = int_data_sliced.sum()\n",
    "print(f\"World Population = {world_population} people\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Islamic Cooperative Population"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "df= International_Database.iloc[0:227]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [],
   "source": [
    "rows= [1,2,3,16, 17, 22, 26, 36, 40, 44, 56, 60, 72, 73, 85, 86, 94, 95, 96, 104, 105, 111, 112, 115, 118, 125, 126, 127, 130, 139, 140, 148, 149, 153, 154, 164, 178, 179, 182, 188, 193, 194, 197, 199, 206, 207, 208, 211, 213, 224, 227]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "umm_population= df[\"Population\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "selected_population= umm_population.loc[rows].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1827880190\n"
     ]
    }
   ],
   "source": [
    "print(selected_population)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "ratio= selected_population / world_population"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " 0.24\n"
     ]
    }
   ],
   "source": [
    " \n",
    "print(f\"{ratio: .2f}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### DATA STOREAGE"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$ 0.07\n"
     ]
    }
   ],
   "source": [
    "dollar=(f\"${dollar_metal_value: .2f}\")\n",
    "quarter =(f\"${quarter_metal_value: .2f}\")\n",
    "dime=(f\"${dime_metal_value: .2f}\")\n",
    "nickel=(f\"${nickel_metal_value: .2f}\")\n",
    "penny =(f\"${penny_metal_value: .2f}\")\n",
    "\n",
    "print(dollar)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "dollar = dollar\n",
    "quarter = quarter\n",
    "dime = dime\n",
    "nickel = nickel\n",
    "penny = penny\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Stored 'dollar' (float)\n",
      "Stored 'quarter' (float)\n",
      "Stored 'nickel' (float)\n",
      "Stored 'dime' (float)\n",
      "Stored 'penny' (float)\n"
     ]
    }
   ],
   "source": [
    "%store dollar\n",
    "%store quarter\n",
    "%store nickel\n",
    "%store dime\n",
    "%store penny"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "collapsed_sections": [],
   "name": "Untitled",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
