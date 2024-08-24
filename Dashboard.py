{
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#Menyiapkan dashboard"
      ],
      "metadata": {
        "id": "QgyQne0ISimU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XOlH7bH9NFXq",
        "outputId": "8dd44871-d6e3-4196-fd06-75635b688d93"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.37.1)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.1.4)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (14.0.2)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.7.1)\n",
            "Requirement already satisfied: tenacity<9,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.5.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: watchdog<5,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.0.2)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: tzdata>=2022.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.3.0->streamlit) (2024.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.7.4)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.16.1)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.3.0->streamlit) (1.16.0)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile dashboard.py\n",
        "# Import library\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from babel.numbers import format_currency\n",
        "import streamlit as st\n",
        "sns.set(style='white')\n",
        "\n",
        "# read dongsi_data\n",
        "dongsi_df = pd.read_csv(\"https://raw.githubusercontent.com/Myrachel/Proyek-Analisis-Data-Air-Quality-Dataset/main/dongsi_data.csv\")\n",
        "\n",
        "# Pembuaatan data frame\n",
        "# Stasiun Dongsi\n",
        "def create_monthly_rain_df(df):\n",
        "    monthly_rain = df.groupby(by=\"month\").agg({\"RAIN\": \"mean\"})\n",
        "    monthly_rain_df = monthly_rain.reset_index()\n",
        "    monthly_rain_df.rename(columns={\n",
        "        'month': \"Bulan\",\n",
        "        'RAIN': \"Curah Hujan (mm)\"\n",
        "        }, inplace=True)\n",
        "    return monthly_rain_df\n",
        "\n",
        "def create_monthly_temp_df(df):\n",
        "    monthly_temp = df.groupby(by=\"month\").agg({\"TEMP\": \"mean\"})\n",
        "    monthly_temp_df = monthly_temp.reset_index()\n",
        "    monthly_temp_df.rename(columns={\n",
        "        'month': \"Bulan\",\n",
        "        'TEMP': \"Temperatur (°C)\"\n",
        "    }, inplace=True)\n",
        "    return monthly_temp_df\n",
        "\n",
        "def create_monthly_PM25_df(df):\n",
        "    monthly_PM25 = df.groupby(by=\"month\").agg({\"PM2.5\": \"mean\"})\n",
        "    monthly_PM25_df = monthly_PM25.reset_index()\n",
        "    monthly_PM25_df.rename(columns={\n",
        "        'month': \"Bulan\",\n",
        "        'PM2.5': \"Indeks PM2.5\" #salah satu indeks kualitas udara\n",
        "    }, inplace=True)\n",
        "    return monthly_PM25_df\n",
        "\n",
        "monthly_rain_df = create_monthly_rain_df(dongsi_df)\n",
        "monthly_temp_df = create_monthly_temp_df(dongsi_df)\n",
        "monthly_PM25_df = create_monthly_PM25_df(dongsi_df)\n",
        "\n",
        "# Set layout\n",
        "st.set_page_config(\n",
        "    page_title=\"Station Air Quality Dashboard\",\n",
        "    page_icon=\"🚉\"\n",
        ")\n",
        "\n",
        "st.header('Station Air Quality Dashboard :sunglasses:')\n",
        "\n",
        "# Filter di sidebar\n",
        "st.sidebar.title(\"Stasiun\")\n",
        "selected_station = st.sidebar.selectbox(\"Pilih Stasiun\", [\"Dongsi\", \"Stasiun Lain\"])\n",
        "\n",
        "if selected_station == \"Dongsi\":\n",
        "    st.subheader('Curah Hujan per Bulan')\n",
        "    fig, ax = plt.subplots(figsize=(16, 8))\n",
        "    ax.plot(\n",
        "        monthly_rain_df[\"Bulan\"],\n",
        "        monthly_rain_df[\"Curah Hujan (mm)\"],\n",
        "        marker='o',\n",
        "        linewidth=2,\n",
        "        color=\"#90CAF9\"\n",
        "    )\n",
        "    ax.tick_params(axis='y', labelsize=20)\n",
        "    ax.tick_params(axis='x', labelsize=20)\n",
        "    ax.set_ylim(bottom=0)\n",
        "    ax.set_xlabel(\"Bulan\", fontsize=25)\n",
        "    ax.set_ylabel(\"Curah Hujan (mm)\", fontsize=25)\n",
        "    st.pyplot(fig)\n",
        "\n",
        "    st.subheader('Temperatur per Bulan')\n",
        "    fig, ax = plt.subplots(figsize=(16, 8))\n",
        "    ax.plot(\n",
        "        monthly_temp_df[\"Bulan\"],\n",
        "        monthly_temp_df[\"Temperatur (°C)\"],\n",
        "        marker='o',\n",
        "        linewidth=2,\n",
        "        color=\"#90CAF9\"\n",
        "    )\n",
        "    ax.tick_params(axis='y', labelsize=20)\n",
        "    ax.tick_params(axis='x', labelsize=20)\n",
        "    ax.set_ylim(bottom=0)\n",
        "    ax.set_xlabel(\"Bulan\", fontsize=25)\n",
        "    ax.set_ylabel(\"Temperatur (°C)\", fontsize=25)\n",
        "    st.pyplot(fig)\n",
        "\n",
        "    st.subheader('Indeks PM2.5 per Bulan')\n",
        "    fig, ax = plt.subplots(figsize=(16, 8))\n",
        "    ax.plot(\n",
        "        monthly_PM25_df[\"Bulan\"],\n",
        "        monthly_PM25_df[\"Indeks PM2.5\"],\n",
        "        marker='o',\n",
        "        linewidth=2,\n",
        "        color=\"#90CAF9\"\n",
        "    )\n",
        "    ax.tick_params(axis='y', labelsize=20)\n",
        "    ax.tick_params(axis='x', labelsize=20)\n",
        "    ax.set_ylim(bottom=0)\n",
        "    ax.set_xlabel(\"Bulan\", fontsize=25)\n",
        "    ax.set_ylabel(\"Indeks PM2.5\", fontsize=25)\n",
        "    st.pyplot(fig)\n",
        "\n",
        "elif selected_station == \"Stasiun Lain\":\n",
        "    st.write(\"Visualisasi untuk stasiun lain akan ditambahkan di sini.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7itwOilUDvHT",
        "outputId": "02592844-b1b9-4f4a-be21-e480e34c2ff1"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting dashboard.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!streamlit run dashboard.py & npx localtunnel --port 8501"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JYVswDyc6yRM",
        "outputId": "838eb913-bc3d-4b60-f914-e1e2b5464d11"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Local URL: \u001b[0m\u001b[1mhttp://localhost:8501\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://34.125.172.48:8501\u001b[0m\n",
            "\u001b[0m\n",
            "your url is: https://ripe-rats-like.loca.lt\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "^C\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
