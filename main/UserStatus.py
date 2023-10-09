from datetime import datetime, timedelta, timezone

class UserStatus:
    @staticmethod
    def get_status(last_seen_date, phrases):

        offset_aware_datetime = datetime.fromisoformat(last_seen_date).astimezone(timezone.utc)
        
        now = datetime.now().astimezone(timezone.utc)
     
        time_diff = now - offset_aware_datetime
        days_difference = time_diff.days
        hours_difference = time_diff.seconds // 3600
        minutes_difference = time_diff.seconds // 60
        seconds_difference = time_diff.seconds

        if days_difference > 7:
            return phrases[2]
        if days_difference > 1:
            return phrases[3]
        if offset_aware_datetime.day != datetime.now().day and (hours_difference > 2 or days_difference == 1):
            return phrases[4]
        if hours_difference > 2:
            return phrases[5]
        if hours_difference >= 1:
            return phrases[6]
        if minutes_difference > 1:
            return phrases[7]
        if seconds_difference > 30:
            return phrases[8]
        return phrases[9]

# Example usage:
# To call the function:
# status = UserStatus.get_status(last_seen_date, phrases)
