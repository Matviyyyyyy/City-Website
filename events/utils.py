import calendar
from datetime import date

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def __init__(self, events, year, month):
        super().__init__()
        self.events = events
        self.year = year
        self.month = month

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            current_day = date.today()

            # Дата, яку відображаємо в календарі
            event_date = date(self.year, self.month, day)

            # Знайдемо події на поточний день
            day_events = [event for event in self.events if event.event_date.day == day]

            # Якщо є події, відобразимо їх з id
            if day_events:
                event_info = ', '.join([event.title for event in day_events])
                return f'''<td class="{cssclass} event-day" style="color: black; font-size: 20px;">{day} - {event_info}</td>'''

            # Якщо дата є сьогоднішньою або в майбутньому, додаємо посилання на додавання події
            if event_date >= current_day:
                url = f'add-event/{self.year}/{self.month}/{day}/'
                return f'<td class="{cssclass}"><a style="text-decoration:none; color: black; font-size: 20px;" href="{url}">{day}</a></td>'

            # Якщо дата в минулому, просто відображаємо число без посилання
            return f'<td class="{cssclass}" style="color: black; font-size: 20px;" data-day="{day}">{day}</td>'

        return '<td></td>'
