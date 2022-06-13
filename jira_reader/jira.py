import requests  # trzecia
from bs4 import BeautifulSoup  # trzecia


# TODO: dodać Unittest - w czasie estimated zamiast liczby może być podany ciąg: 'Not specified' -> co wtedy???
def convert_text_time_to_hours(text_time: str) -> float:
    time_list_values = text_time.split()
    days = 0
    hours = 0
    for time in time_list_values:
        if 'd' in time:
            days = float(time[0:time.find('d')])
        if 'h' in time:
            hours = float(time[0:time.find('h')])
    sum_time = days * 8 + hours
    return sum_time


def get_page_content(url: str, username: str, password: str):
    session = requests.Session()
    session.auth = (username, password)

    response = session.get(url, verify=False)
    if not response.ok:
        response.raise_for_status()
    return response.text


def get_information_about_task(content: str) -> tuple[float, float, float]:
    soup = BeautifulSoup(content, features='lxml')
    estimated_text = soup.find(id='tt_single_values_orig').text.strip()
    remaining_text = soup.find(id='tt_single_values_remain').text.strip()
    logged_text = soup.find(id='tt_single_values_spent').text.strip()

    estimated_time = convert_text_time_to_hours(estimated_text)
    remaining_time = convert_text_time_to_hours(remaining_text)
    logged_time = convert_text_time_to_hours(logged_text)

    return estimated_time, remaining_time, logged_time

