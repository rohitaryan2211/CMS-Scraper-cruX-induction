import requests
from bs4 import BeautifulSoup
import re

index = 1
data = []


def write_csv(items, path):
    # Open the file in write mode
    with open(path, 'w', encoding="utf-8") as f:
        # Return if there's nothing to write
        if len(items) == 0:
            return

        # Write the headers in the first line
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        # Write one item per line
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


for n in range(0, 2):
    response = requests.get(
        f'https://cms.bits-hyderabad.ac.in/course/index.php?categoryid=26&perpage=1000&browse=courses&page={n}')
    soup = BeautifulSoup(response.content, "html.parser")
    # print(soup.prettify())

    courses = soup.find_all("div", {"data-type": "1"})
    # print(courses)

    for course in courses:
        # print(course)

        # course_id = course.get("data-courseid")

        a = course.find_all("a")
        course_name_old = a[0].text
        # course_link = a[0].get("href")

        course_name_new = re.sub(r'[^\w]', ' ', course_name_old)

        f = {
            'Index': index,
            'Course ID': course.get("data-courseid"),
            'Course Name': course_name_new,
            'Course Link': a[0].get("href")
        }

        data.append(f)

        print(f"{index:3}. {course_name_new} link scraped.")

        index += 1

write_csv(data, 'cms_course-links.csv')
