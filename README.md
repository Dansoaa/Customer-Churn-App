<a name="Customer-Churn-App"></a>

<div align="center">
  <h1><b>Customer Churn Application</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Customer Churn Application ](#Customer-Churn-Application-)
  - [🛠 Built With ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [Key Features ](#key-features-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
    - [Install](#install)
    - [Usage](#usage)
  - [👥 Authors ](#-authors-)
  - [🔭 Future Features ](#-future-features-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [🙏 Acknowledgments ](#-acknowledgments-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Customer Churn Application <a name="about-project"></a>

**Customer Churn Application** is a data application that allows users to interact with a machine learning model, view data visualizations on the data and see the values of their input saved for future use.

Features

1. **CustomerID**: Unique identifier for each customer
2. **gender**: Whether the customer is a male or a female
3. **SeniorCitizen**: Whether the customer is a senior citizen or not (1, 0)
4. **Partner**: Whether the customer has a partner or not (Yes, No)
5. **Dependent**: Whether the customer has dependents or not (Yes, No)
6. **PhoneService**: Whether the customer has a phone service or not (Yes, No)
7. **MultipeLines**: Whether the customer has multiple lines (Yes, No, No phone service)
8. **InternetService**: Customer’s internet service provider (DSL, Fiber optic, No)
9. **OnlineSecurity**: Whether the customer has online security (Yes, No, No internet service)
10. **OnlineBackup**: Whether the customer has an online backup (Yes, No, No internet service)
11. **DeviceProtection**: Whether the customer has device protection (Yes, No, No internet service)
12. **TechSupport**: Whether the customer has tech support (Yes, No, No internet service)
13. **StreamingTV**: Whether the customer streams TV (Yes, No, No internet service)
14. **StreamingMovies**: Whether the customer streams movies (Yes, No, No internet service)
15. **Contract**: The contract term of the customer (Month-to-month, One year, Two years)
16. **PaperlessBilling**:** Whether the customer does paperless Billing or not (True, False)
17. **PaymentMethod**: The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>GUI</summary>
  <ul>
    <li><a href="">Streamlit</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="">Microsoft SQL Server</a></li>
  </ul>
</details>

<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>

<details>
<summary>Model</summary>
  <ul>
    <li><a href="">Sklearn</a></li>
  </ul>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Features <a name="key-features"></a>

- **A data application that presents visualizations on both the exploratory data and the KPIs**
- **A predicitons page to predict by specifying the model you want to use**
- **View proprietory data loaded in real-time form the remote server**
- **Predictions are save for further analysis in the future and users can view the history of their prediction input values**


<p align="right">(<a href="#readme-top">back to top</a>)</p>

![image](https://github.com/coderacheal/Attrition-Meter/assets/97846040/eb717bf3-d42b-4005-8080-276b69f08167)


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python
- Streamlit

### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/coderacheal/Attrition-Meter.git
```

Change into the cloned repository

```sh
  cd Attrition-Meter
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    virtual_env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:


```sh
    streamlit run 1_🏠_Home.py

```

- A webpage opens up to view the app
- Login to the app with `username=coderacheal` and `password:abc`
- Finally test a prediction by clicking on the predicitons page
- **Note**: Users may not be able to access the View Data page as the secrets file is not checked into git

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Racheal Appiah-kubi**

- GitHub: [GitHub Profile](https://github.com/coderacheal)
- Twitter: [Twitter Handle](https://twitter.com/racheal_kubi)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/racheal-appiah-kubi/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>


- **Add a front end application for users**
  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I would like to thank all the free available resource made available online

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>