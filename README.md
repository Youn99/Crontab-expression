# Crontab Expression: https://crontab.guru/.

This function will allow you to check if the crontab parameters are correct => you can visit the web site.
you need to follow the order of the schedule expression like in the web site: (minute, hour, day_month, month, day_week)

  - day_week: need to be * or 7.

  - month: need to be * or 12.

  - day_month: need to be * or 31.

  - hour: need to be * or 23.

  - minute: need to be * or 59.

  - *: is equal to None.

Parameter:

  - crontab_parameter => need to be a string.

Return:

  - if the parameters are valid or not.
