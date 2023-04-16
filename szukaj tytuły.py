import requests, bs4, re, csv, time, datetime, os

v1 = "&time_from=0&time_to=2"
v2 = "&time_from=2&time_to=4"
v3 = "&time_from=4&time_to=6"
v4 = "&time_from=6&time_to=8"
v5 = "&time_from=8&time_to=10"
v6 = "&time_from=10&time_to=12"
v7 = "&time_from=12&time_to=14"
v8 = "&time_from=14&time_to=16"
v9 = "&time_from=16&time_to=18"
v10 = "&time_from=18&time_to=20"
v11 = "&time_from=20&time_to=22"
v12 = "&time_from=22&time_to=0"
allperiods = [v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12]



start_date = datetime.date(2014, 6, 27)
end_date = datetime.date(2023, 3, 31)
delta = datetime.timedelta(days=1)

while start_date <= end_date:

    searchdate = start_date.strftime('%d-%m-%Y')
    start_date += delta

    for x in allperiods:

        #time.sleep(2)
        print(x)
        link = 'https://www.odsluchane.eu/szukaj.php?r=2&date='+str(searchdate)+str(x)
        r = requests.get(link)
        date_pattern = r'\d{2}-\d{2}-\d{4}'
        #print(link)


        r.status_code       #checks connection
        #print(r)            #print status of connection
        date = [re.findall(date_pattern,link)]


        RMF = bs4.BeautifulSoup(r.text, 'html.parser')
        HTML = RMF.find_all("a", class_="title-link")

        #print(HTML)
        pattern = r'>\s*(.*?)\s*</a>'
        titles = re.findall(pattern , str(HTML) )


        #HTML = RMF.find_all("a", class_="line-content")

        #print(HTML)
        hourpattern =r"\d{2}:\d{2}"
        td = RMF.find_all('td')
        hours = re.findall(hourpattern, str(td))
        if '00:00' in hours:
            if '00:00' in hours:
                hours.remove('00:00')
            else: pass
            if '01:00' in hours:
                hours.remove('01:00')
            else: pass
        elif '02:00' in hours:
            if '02:00' in hours:
                hours.remove('02:00')
            else: pass
            if '03:00' in hours:
                hours.remove('03:00')
            else: pass
        elif '04:00' in hours:
            if '04:00' in hours:
                hours.remove('04:00')
            else: pass
            if '05:00' in hours:
                hours.remove('05:00')
            else: pass
        elif '06:00' in hours:
            if '06:00' in hours:
                hours.remove('06:00')
            else: pass
            if '07:00' in hours:
                hours.remove('07:00')
            else: pass
        elif '08:00' in hours:
            if '08:00' in hours:
                hours.remove('08:00')
            else: pass
            if '09:00' in hours:
                hours.remove('09:00')
            else: pass
        elif '10:00' in hours:
            if '10:00' in hours:
                hours.remove('10:00')
            else: pass
            if '11:00' in hours:
                hours.remove('11:00')
            else: pass
        elif '12:00' in hours:
            if '12:00' in hours:
                hours.remove('12:00')
            else: pass
            if '13:00' in hours:
                hours.remove('13:00')
            else: pass
        elif '14:00' in hours:
            if '14:00' in hours:
                hours.remove('14:00')
            else: pass
            if '15:00' in hours:
                hours.remove('15:00')
            else: pass
        elif '16:00' in hours:
            if '16:00' in hours:
                hours.remove('16:00')
            else: pass
            if '17:00' in hours:
                hours.remove('17:00')
            else: pass
        elif '18:00' in hours:
            if '18:00' in hours:
                hours.remove('18:00')
            else: pass
            if '19:00' in hours:
                hours.remove('19:00')
            else:pass
        elif '20:00' in hours:
            if '20:00' in hours:
                hours.remove('20:00')
            else: pass
            if '21:00' in hours:
                hours.remove('21:00')
            else: pass
        elif '22:00' in hours:
            if '22:00' in hours:
                hours.remove('22:00')
            else: pass
            if '23:00' in hours:
                hours.remove('23:00')
            else: pass
        else: pass
        #print(hours)

        titles.remove('Reklama w serwisie')
        titles.remove('Radia')
        titles.remove('Polityka prywatności')
        #print(titles)

        NumberOfTitles = len(titles)
        NumberOfHours = len(hours)
        NumberOfDates = NumberOfTitles * date
        NewLine = '/n'
        NumberOfNewLines = NumberOfTitles * NewLine
        #print('number of titles: ' + str(NumberOfTitles))
        #print('number of timestamps: ' + str(NumberOfHours)) #trzeba wyrzucić 18 i 19 godzine
        #print('number of datestamps: ' + str(len(NumberOfDates)))

        data = zip( NumberOfDates ,hours,titles)



        clearcsv = str(tuple(list(data))).replace(r"), ",")\n")
        clearcsv = clearcsv.replace(r"(", "")
        clearcsv = clearcsv.replace(r")","")
        clearcsv = clearcsv.replace(r"'","")

        print(clearcsv)

        filename = searchdate + ".txt"

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(clearcsv + "\n")
            

